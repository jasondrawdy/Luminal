# -*- coding: utf-8 -*-
# ########################################################################                          
# Program: Luminal
# Author: Jason Drawdy
# Version: 1.0.0
# Date: 07/07/23
# #########################################################################
# Description:
# The main module within Luminal which is responsible for managing photons
# as well as providing functionality such as loading, reloading, and more.
# #########################################################################
from ..errors.threads import ThreadManagerAlreadyRunningError
from ..errors.system import DirectoryNotFoundError
from ..errors.cleanup import PhotonNotFoundError
from ..managers.threads import ThreadManager
from ..managers.tracer import LoopTrace
from ..managers.resolver import Resolver
from ..managers.handler import Handler
from ..interfaces.photon import IPhoton
from ..tools.utils import SystemUtils
from ..tools.logger import Logger
from typing import Optional, Type
from types import ModuleType
import importlib.util as util
import asyncio
import inspect
import sys
import os

class Loader():
    """Allows management of photons and how they are loaded, unloaded, reloaded, and monitored."""
    def __init__(self: "Loader", logging: bool = False, suppress_errors: bool = False) -> None:
        """
        Initializes a new :class:`Loader` instance.

        Parameters
        ----------
        logging : Optional[:class:`bool`]
            If ``True``, enables logging for the :class:`Loader` instance. Defaults to ``False``.
        suppress_errors : Optional[:class:`bool`]
            If ``True``, suppresses errors that occur during loading and unloading of photons.
            Defaults to ``False``, which will raise errors if they occur.

        Raises
        ----------
        TypeError
            If types of the input arguments are not as expected.
        """
        self.logging = logging
        self.suppress_errors = suppress_errors
        self._logger: Logger = Logger(__name__)
        self._resolver: Resolver = Resolver()
        self._threads: ThreadManager = ThreadManager()
        self._photons: dict[str, Handler] = dict()
        self._is_watching: bool = False

    @property
    def photons(self: "Loader") -> dict[str, "Handler"]:
        """
        Returns a dictionary of photon names and corresponding :class:`Handler` objects.

        Returns
        ----------
        :class:`Dict[str, Handler]`
            A dictionary containing photon names as keys and their corresponding :class:`Handler` objects as values.

        Notes
        ----------
        - This is a read-only property, meaning that it can only be accessed and not modified.
        - The photon name is the name assigned to the photon instance in its definition.
        - The :class:`Handler` objects contain information about the photon, including its name, file path,\
        and the :class:`IPhoton` based class itself.

        """
        return self._photons

    async def _validate_module(self: "Loader",
                                imported_module: ModuleType,
                                photon_path: str,
                                photon_base: type,
                                other_classes: list[str] = []) -> Type[list|bool]:
        """``|coro|``

        Checks for all photon instances, specified classes and creates handlers objects for them.

        Parameters
        ----------
        imported_module : :class:`ModuleType` 
            The imported module to be validated.
        photon_path : :class:`str`
            The absolute path of the photon module.
        photon_base : :class:`type`
            The base class that all photons of the system will inherit from.
        other_classes : Optional[:class:`list[str]`] 
            A list of additional classes to check for in the imported module.
            Defaults to ``[]``.

        Returns
        ----------
        :class:`Union[List[Handler], bool]` 
            If the module is a valid photon module, a list of :class:`Handler` objects that correspond
            to the photon instances and specified classes in the module is returned. If it is not a valid photon module,
            returns ``False``.

        Notes
        ----------
        - Even if the module is not a valid photon module and it returns ``False``, the ``imported_module`` will still be\
        deleted from the system.
        """
        photon_found: bool = False
        photon_attributes: list[Handler] = []
        for entry in dir(imported_module): # Check if the module is subclassed as a Photon.
            attribute: type = getattr(imported_module, entry)
            if inspect.isclass(attribute):
                if other_classes and attribute.__name__ in other_classes or \
                    (not other_classes and issubclass(attribute, photon_base) and \
                     attribute != photon_base):
                    if issubclass(attribute, IPhoton):
                        name = attribute.photon_name
                    else:
                        name = attribute.__name__
                    checksum = await Handler._get_checksum(photon_path)
                    handler = Handler(self.logging, name, photon_path, checksum, attribute)
                    self._photons[name] = handler
                    photon_attributes.append(handler)
                    photon_found = True
        if not photon_found: # Check if the module is an actual Photon.
            del imported_module
            return False
        return photon_attributes

    async def _import_module(self: "Loader", module_path: str) -> ModuleType:
        """``|coro|``

        Resolves, executes, and returns a Python module based on the provided module path.

        Parameters
        ----------
        module_path : :class:`str` 
            The absolute path of the module to be imported.

        Returns
        ----------
        :class:`ModuleType`
            The imported module object.

        Raises
        ----------
        ModuleNotFoundError
            If the module cannot be found (either due to an incorrect path or it not existing), or
            if a loader or spec cannot be found for the module.

        Notes
        ----------
        - The imported module is added to the ``sys.modules`` dictionary for future reference, and is also returned.
        - If an error occurs while importing the module and the logging property is set, the error will be logged.
        - If ``suppress_errors`` is set, the error will be skipped.

        """
        module_name: Optional[str] = inspect.getmodulename(module_path)
        if not module_name: # The module name is already checked above.
            module_name = "" # However, spec_from_file needs a string path.
        try:
            module_spec = util.spec_from_file_location(module_name, module_path)
            if module_spec:
                imported_module = util.module_from_spec(module_spec)
                if module_spec.loader:
                    resolved_name = self._resolver.resolve_path(module_path)[0]
                    sys.modules[resolved_name] = imported_module
                    module_spec.loader.exec_module(imported_module)
                    return imported_module
                else: # pragma: no cover
                    raise ModuleNotFoundError(f"No loader found for module '{module_name}'")
            else: # pragma: no cover
                raise ModuleNotFoundError(f"No spec found for module '{module_name}'")
        except ModuleNotFoundError as error: # pragma: no cover
            try: del sys.modules[resolved_name]
            except: await SystemUtils.continue_async() # The module probably doesn't exist in the dictionary.
            if self.logging:
                if not self.suppress_errors:
                    self._logger.error(f"Can't import module for '{module_path}'! ({error}) -> Skipping it.")
        except Exception as error: # pragma: no cover
            try: del sys.modules[resolved_name]
            except: await SystemUtils.continue_async() # The module probably doesn't exist in the dictionary.
            if self.logging:
                if not self.suppress_errors:
                    self._logger.error(f"Syntax error for '{module_path}'! ({error}) -> Skipping it.")
            raise error

    async def _scan_module(self: "Loader", path: str) -> tuple[str, bool, bool]:
        """``|coro|``

        Determines if the provided path is a package or module.

        Parameters
        ----------
        path : :class:`str`
            Absolute path of the file or directory to be checked.

        Returns
        ----------
        :class:`Tuple[str, bool, bool]`
            A tuple containing the absolute path of the module, a flag indicating whether the 
            path is a package, and a flag indicating if there are only packages in the directory.

        Raises
        ----------
        ModuleNotFoundError
            If the file path provided does not exist, is not accessible or is not a valid photon.

        Notes
        ----------
        - The first element, ``path`` in the tuple returned represents the absolute path of the individual module.
        - The second element, ``is_dir`` in the tuple returned is a boolean value that indicates whether the module\
        is in fact a package.
        - The third element of the returned tuple, ``packages_only`` is a boolean value that indicates whether there\
        are only packages in the directory.

        """
        is_dir, packages_only = False, True
        if os.path.isdir(path):
            is_dir = True
            return(path, is_dir, packages_only)
        elif os.path.isfile(path): # pragma: no branch
            if path.endswith(".py"):
                module_name: Optional[str] = inspect.getmodulename(path)
                if module_name and module_name != "__init__": # pragma: no branch
                    packages_only = False # More than just directories.
                    return(path, is_dir, packages_only)
        await SystemUtils.continue_async()
        raise ModuleNotFoundError(f"'{path}' does not exist or is not a valid photon.")

    async def _find_modules(self: "Loader", path: str) -> tuple[list[tuple[str, bool]], bool]:
        """``|coro|``

        Creates a collection of module paths and determines if they're packages.

        Parameters
        ----------
        path : :class:`str`
            The path of the directory containing the modules.

        Returns
        ----------
        :class:`Tuple[List[Tuple[str, bool]], bool]`
            A tuple containing a list of tuples representing available modules 
            and if they're Python packages, and a boolean representing if there are only packages.

        Notes
        ----------
        - If ``path`` is not a valid directory or cannot be accessed, an empty list will be returned.
        - The first element, ``module_path`` in the tuple returned represents the absolute path of the individual module.
        - The second element, ``is_dir`` in the tuple returned is a boolean value that indicates whether the module\
        is in fact a package.
        - The second element of the returned tuple, ``packages_only`` is a boolean value that indicates whether there\
        are only packages in the directory.

        """
        packages_only: bool = True
        modules: list[tuple[str, bool]] = []
        try: paths: list[str] = os.listdir(path)
        except OSError: # pragma: no cover
            paths = [] # Ignore unreadable directories.
        for entry in paths:
            entry = os.path.join(path, entry)
            module_path, is_dir, packages_only = await self._scan_module(entry)
            modules.append((module_path, is_dir))
        return (modules, packages_only)

    async def _check_photon(self: "Loader", photon: str|Handler) -> Handler | list[Handler]:
        """``|coro|``

        Check if the photon belongs to the available photon registry and return the corresponding handler(s).

        Parameters
        ----------
        photon : :class:`str|Handler`
            Name of the photon or :class:`Handler` object.

        Returns
        ----------
        :class:`Union[Handler, List[Handler], None]` 
            If photon exists in the available photons, return the corresponding handler(s).
        
        Raises
        ----------
        PhotonNotFoundError: 
            If photon is not a valid file path or if it does not exist in the available photons.

        Notes
        ----------
        - If photon is a :class:`Handler` object, return it as is. If photon does not exist in the\
        available photons, return ``None``.
        """
        if isinstance(photon, str):
            if not os.path.exists(photon) or not os.path.isfile(photon):
                raise PhotonNotFoundError(f"{photon}")
            handlers = [h for h in self._photons.values() if photon in h.filepath]
            return handlers
        if isinstance(photon, Handler):
            return photon
    
    async def _emit_photon(self: "Loader", 
                            photon_path: str|tuple[str, bool, bool],
                            photon_base: type=IPhoton,
                            other_classes: list[str]=[],
                            recursive: bool=False) -> Handler|list[Handler]|None:
        """``|coro|``
        
        Loads and returns a photon from a given path. 

        Parameters
        ----------
        photon_path : :class:`str | tuple[str, bool, bool]`
            A string representing the file path of the photon or a tuple representing the photon path along with boolean values indicating if the photon is a module or a package.
        photon_base : Optional[:class:`type`]
            Base class for photons. Default is :class:`IPhoton`.
        other_classes : Optional[:class:`list[str]`]
            List of classes that the photon should inherit from. Default is ``[]``.
        recursive : Optional[:class:`bool`]
            A flag indicating whether to look for photons recursively in subdirectories under the ``photons_directory``. Default is ``False``.

        Returns
        ----------
        :class:`Handler | list[Handler] | None`
            The handler object of the photon that was emitted, a list of handler objects of photons that were emitted, or ``None``.

        Raises
        ----------
        ModuleNotFoundError
            When the photon's module is not found.
        Exception
            Generally when a photon author has syntax errors or other issues with their photon source.
            
        Notes
        ----------
        - The :func:`_emit_photon()` function first initializes an empty list called photons. It then checks whether the given path is a module\
        file or a package directory by checking if the type of ``photon_path`` is a tuple. If so, it retrieves the information about the path's\
        readiness, the module path, and whether the specified path contains only packages. If the photon is a package and the recursive flag\
        is ``True`` or the ``package_only`` flag is ``True``, the function reads photons from other levels down in the package.
        - It then checks if the photon has already been loaded by resolving the module path and accessing the ``_photons`` attribute of the instance\
        of :class:`Loader`. If the photon is already loaded, a warning message is logged, and ``None`` is returned.
        - If the photon is not loaded, then the function imports the photon's module path using the :func:`_import_module()` method, and validates the\
        module with the given photon base class and a list of other classes the photon should inherit from using the :func:`_validate_module()` method. 
        - It returns a list of photons that were validated. If the list of photons is empty, a warning message is logged, and ``None`` is returned.\
        Otherwise, a success message is logged for loading the photon, and the photons are added to the list.
        - Finally, the function returns a list of handler objects for the loaded photons.

        Examples
        ----------
        >>> loader = Loader()
        >>> photon = await loader._emit_photon('photons/hello_world.py', IPhoton, ["Other_class1", "Other_class2"])
        """
        try:
            photons: list[Handler] = []
            module_ready = isinstance(photon_path, tuple)
            module_path, is_dir, packages_only = photon_path if module_ready else await self._scan_module(photon_path)
            if is_dir: # Try to find Photon modules n-levels down.
                if recursive or packages_only: # pragma: no branch
                    photons.extend(await self.load_photons(module_path,
                                                            photon_base,
                                                            other_classes,
                                                            recursive))
            resolved_name = self._resolver.resolve_path(module_path)
            photon = self._photons.get(resolved_name, None)
            if not photon is None:
                if self.logging: # pragma: no cover
                    self._logger.warning(f"Photon '{module_path}' is already loaded!")
                    return None
            else:
                photon_module = await self._import_module(module_path)
                validated = await self._validate_module(photon_module, module_path,
                                                        photon_base, other_classes)
                if isinstance(validated, list):
                    if len(validated) > 0:
                        if self.logging: # pragma: no cover
                            self._logger.success(f"Successfully loaded photon — '{module_path}'!")
                        if len(validated) == 1:
                            return validated[-1]
                        photons.extend(validated)
                    else:
                        if self.logging: # pragma: no cover
                            self._logger.warning(f"The photon located at '{module_path}' was not loaded!")
                            return None
            return photons
        except ModuleNotFoundError as error: # pragma: no cover
            if self.logging: 
                self._logger.error(f"{error}")
        except SyntaxError as error:# pragma: no cover
            if self.logging:
                self._logger.note("Requested photon couldn't be reloaded. -> Reverting state!")
            validated_photon, validated_modules = await self._check_photon(photon), dict()
            await self._revert_photon(validated_photon, validated_modules)
        except Exception as error: pass # pragma: no cover
        
    async def _emit_photons(self: "Loader",
                            photons_directory: str,
                            photon_base: type=IPhoton,
                            other_classes: list[str]=[],
                            recursive: bool=False) -> list[Handler]:
        """``|coro|``
        
        Retrieves photon handlers from a specified directory.

        Parameters
        ----------
        photons_directory : :class:`str`
            A string representing the directory where the photons are located.
        photon_base : Optional[:class:`type`]
            An optional argument representing the base class for the photons. Default is `IPhoton`.
        other_classes : Optional[:class:`list[str]`]
            List of strings representing other classes that the photons should inherit from. Default is :class:`[]`.
        recursive : Optional[:class:`bool`]
            A boolean indicating whether to look for photons recursively in subdirectories under `photons_directory`. Default is `False`.

        Returns
        ----------
        :class:`list[Handler]`
            A list of photons representing the handlers stored in the given directory and its subdirectories.

        Raises
        ----------
        Any exceptions raised by the called :func:`_emit_photon()` method.

        See Also
        ----------
        :func:`_emit_photon()`
            Loads and returns a photon from a given path. 

        Examples
        ----------
        >>> loader = Loader()
        >>> photons = await loader._emit_photons("photons_directory", IPhoton, ["Other_class1", "Other_class2"])
        """
        photons: list[Handler] = []
        modules, packages_only = await self._find_modules(photons_directory)
        for module_path, is_dir in modules:
            photon_path = (module_path, is_dir, packages_only)
            emission = await self._emit_photon(photon_path=photon_path,
                                                photon_base=photon_base,
                                                other_classes=other_classes,
                                                recursive=recursive)
            if not emission is None:
                if isinstance(emission, list):
                    photons.extend(emission)
                else:
                    photons.append(emission)
        self._photons.update({photon.name: photon for photon in photons})
        return photons
    
    async def _absorb_photon(self: "Loader", photon: Handler|str, force_stop: bool = False, suppress_finalizer_log: bool = False) -> bool:
        """``|coro|``

        Stops the specified photon and removes it from the loader's photon registry.
        If the given photon is a string, it is looked up in the registry by filepath.
        If the photon is not found, this method returns ``False``.
        
        Parameters
        ----------
        photon : :class:`Handler|str`
            Either a :class:`Handler` object that represents a running photon, or a :class:`str` name of a photon in the photon registry.
        force_stop : :class:`bool`
            A flag that specifies whether to force-stop the photon if it does not stop within a reasonable time or \
            does not implement a finalizer.
        
        Returns
        ----------
        `bool`
            Indicating whether the photon was successfully stopped and removed.
        """
        async def _halt_photon(_photon: Handler):
            try:
                await _photon._stop(force_stop=force_stop)
            except Exception as error:
                if not suppress_finalizer_log:
                    raise error
            self._photons.pop(_photon.name, None)
        result = await self._check_photon(photon)
        if not result is None:
            if result == photon:
                await _halt_photon(photon)
                return True
            if isinstance(result, list): # pragma: no branch
                for _photon in result: 
                    await _halt_photon(_photon)
                return True
        return False

    async def _absorb_photons(self: "Loader", photons: list[Handler|str], force_stop: bool = False) -> list[str]:
        """``|coro|``

        Stops and removes a list of photons from the loader's registry.
        If a given photon is a string, it is looked up in the registry by filepath.
        The method returns a list of successful photon filepaths that were stopped and absorbed.
        
        Parameters
        ----------
        photons : :class:`list[Handler|str]`
            A list of :class:`Handler` objects representing photons, or a list of :class:`str` \
            names of the photons in the photon registry.
        
        Returns
        ----------
        :class:`list[str]`
            A list of successful photon filepaths that were stopped and absorbed.
        """
        def _update_absorption_list(photon_list: list[str], filepath: str):
            if not filepath in photon_list: photon_list.append(filepath)
            return photon_list
        absorbed_photons = []
        for photon in photons:
            if await self._absorb_photon(photon, force_stop): # pragma: no branch
                if isinstance(photon, Handler):
                    _update_absorption_list(absorbed_photons, photon.filepath)
                else: _update_absorption_list(absorbed_photons, photon)
        return absorbed_photons
    
    async def _revert_photon(self: "Loader", 
                             validated_photon: Handler|list[Handler], 
                             validated_modules: dict[str, ModuleType]) -> None:
        """``|coro|``

        Rolls back a photon to a working state if an atomic reload fails.
        
        Parameters
        -----------
        validated_photon : :class:`Union[Handler, List[Handler]]`
            A single :class:`Handler` object or a list of :class:`Handler` objects which are validated successfully
            during the atomic reload.
        validated_modules : :class:`Dict[str, ModuleType]`
            A dictionary containing the validated modules for the given photon.
            These modules are updated in the ``sys.modules`` after the photon has been rolled back.
        
        Raises
        -----------
        Any exception that may occur during the :func:`validated_photon.start()` call.
        
        Notes
        -----------
        This function is responsible for rolling back a photon to a working state if an atomic reload fails.\
        It takes two parameters: a validated photon and validated modules dictionary. If the validation passes \
        successfully, then the :func:`_revert_photon()` function starts the validated photon by calling the\
        :func:`validated_photon.start()` function. Afterward, the ``_photons`` collection is updated to hold the \
        working photon, and updated modules are passed to the ``sys.modules`` by the :func:`sys.modules.update()` call.
        
        This function expects the provided ``validated_photon`` to be a single :class:`Handler` object or a list of such objects.\
        It is also expected that the provided ``validated_photon`` has passed the validation check without any errors.
        
        - Please note that any exception that is raised during the await :func:`validated_photon.start()` function call\
        is propagated back to the caller. The exceptions could arise due to coding bugs, configuration issues, or other\
        environmental reasons.

        """
        try: # pragma: no cover
            if validated_photon == None or validated_photon._instance == None:
                raise PhotonNotFoundError("The photon does not exist.")
            await validated_photon.start()
            self._photons[validated_photon.name] = validated_photon
            sys.modules.update(validated_modules)
            if self.logging: # pragma: no cover
                self._logger.success("Photon successfully reverted to it original state!")
        except PhotonNotFoundError:
            if self.logging: # pragma: no cover
                self._logger.warning("The photon was perturbed and may not function correctly, if at all.")

    async def _reload_photon(self: "Loader", photon: Handler|str) -> Handler|list[Handler]:
        """``|coro|``
        
        Reloads a photon handler or an entire photon atomically and returns the updated :class:`Handler` object(s).
        
        Parameters
        ----------
        photon : :class:`Union[Handler, str]`
            A single handler object or the string name for the photon which needs to be reloaded.
            
        Returns
        ----------
        :class:`Union[Handler, List[Handler]]`
            - If a single photon is provided, it returns the updated :class:`Handler` object.
            - If multiple photons are provided or the photon to be reloaded has multiple handlers,
            - it returns a list of the updated :class:`Handler` objects.
        
        Raises
        ----------
        Any exception that may occur during:
            - :func:`self._check_photon()`
            - :func:`_absorb_photon(validated_photon)`
            - :func:`_emit_photon(photon)`
            - :func:`_revert_photon(validated_photon, validated_modules)`
        
        Notes
        ----------
        This function reloads a photon handler or an entire photon atomically and returns the updated :class:`Handler` object(s).\
        The function starts by validating the provided photon by calling the :func:`_check_photon(photon)` function.\
        Once the validation is complete, this function collects all the validated modules for the photon across the system.
        
        Depending on the number of validated photons i.e., whether a single :class:`Handler` object or a list of them is provided,\
        the function iterates through each of them and collects all validated modules for each.\
        It then calls the :func:`_absorb_photon(validated_photon)` function to atomically update the photon(s).\
        After an atomic update of the photon(s), it returns the updated :class:`Handler` object(s) by calling the \
        :func:`_emit_photon(photon)` function.

        In case any exception occurs during the atomic update,\
        this function calls the :func:`_revert_photon(validated_photon, validated_modules)`\
        function to fall back to the previous working state.

        - Please note that any exception that is raised during any defined calls in this function is propagated back to the caller.\
        The exceptions may arise due to coding bugs, configuration issues, or other environmental reasons.

        """
        def _get_validated_modules(photon_name: str) -> dict:
            modules = {
                name: module
                for name, module in sys.modules.items()
                if SystemUtils.is_submodule(photon_name, name)
            }
            return modules
        validated_photon, validated_modules = await self._check_photon(photon), dict()
        if isinstance(validated_photon, list):
            for _photon in validated_photon:
                cluster = _get_validated_modules(_photon.name)
                validated_modules.update(cluster)
        else:
            cluster = _get_validated_modules(validated_photon.name)
            validated_modules.update(cluster)
        photon = photon.filepath if isinstance(photon, Handler) else photon
        await self._absorb_photon(validated_photon, suppress_finalizer_log=True)
        return await self._emit_photon(photon)
        
    async def _reload_photons(self: "Loader", photons: list[Handler|str]) -> list[Handler]:
        """``|coro|``

        Reloads a list of photon handlers or entire photons atomically and returns the updated :class:`Handler` objects.
        
        Parameters
        ----------
        photons : :class:`List[Union[Handler, str]]`
            A list of :class:`Handler` objects or the string names for the photons that need to be reloaded.
            
        Returns
        ----------
        :class:`List[Handler]`
            A list of updated :class:`Handler` objects after the atomic reload process.
        
        Raises
        ----------
        Any exception that may occur during the :func:`_reload_photon(photon)` call.
        
        Notes
        ----------
        This function reloads a list of photon handlers or entire photons atomically and returns the updated :class:`Handler` \
        objects. The function loops through all provided handlers, atomically updates each of them using the previously defined \
        :func:`_reload_photon(photon)` function, and collects the updated :class:`Handler` objects in a list. If the result of the \
        :func:`_reload_photon(photon)` function call returns a :class:`list` of :class:`Handler` objects, this function concatenates\
        them onto the handlers list. If the result of the :func:`_reload_photon(photon)` function call returns a single :class:`Handler`\
        object, this function appends the single :class:`Handler` object onto the handlers list.
        
        - Please note that any exception that is raised during the :func:`_reload_photon(photon)` function call is immediately propagated\
        back to the caller. The exceptions may arise due to coding bugs, configuration issues, or other environmental reasons.

        """
        handlers = []
        for photon in photons:
            result = await self._reload_photon(photon)
            if isinstance(result, list):
                handlers.extend(result)
            if isinstance(result, Handler):
                handlers.append(result)
        return handlers

    async def _observe_photons(self: "Loader", photons_directory: str, loop_trace: LoopTrace = None) -> bool:
        """``|coro|``

        Observes photons for changes by continuously calculating their checksum and reloading when a change is detected.
        
        Parameters
        ----------
        photons_directory : :class:`str`
            The path to the photons directory which needs to be monitored.
        loop_trace : :class:`LoopTrace`
            An optional trace object to keep track of loop iterations and allow testing of infinite loops, defaults to ``None``.
            
        Returns
        ----------
        :class:`bool`
            The function returns ``True`` when the observer loop has been terminated.
            
        Raises
        ----------
        Any exception that may occur during:
            - :func:`self.load_photons(photons_directory)`
            - :func:`self.reload_photons(photons_to_reload)`
            - :func:`loop_trace.evalutate_tasks()`
            - :func:`SystemUtils.continue_async(1)`
        
        Notes
        ----------
        This function observes photons for changes by consistently calculating their checksum and reloading when a change is detected.\
        The function loops indefinitely until the ``_is_watching`` flag is set to ``False``. The observation process starts by calling\
        the :func:`load_photons(photons_directory)` function to collect all the available photons. The function then makes a copy of all\
        the ``_photons``, and then loops through this copy and calculates the current checksum of each photon.
        
        - If the current photon's checksum is different from the previous checksum value, the photon's filepath is appended to the\
        ``photons_to_reload`` list.
        - Once all the photons have been observed, the function checks whether ``photons_to_reload`` has any new entries.\
        If new entries exist, the function calls the :func:`reload_photons(photons_to_reload)` function to atomically update\
        the observed photons.
        - The function then pauses for one second by calling the :func:`SystemUtils.continue_async(1)` function before resuming with the\
        next cycle. In case the ``loop_trace`` parameter is provided, this function evaluates the provided loop tasks by calling the\
        :func:`loop_trace.evalutate_tasks()` function.
        - Please note that any exception that is raised during any defined calls in this function is propagated back to the caller.\
        The exceptions may arise due to coding bugs, configuration issues, or other environmental reasons.

        """
        def _get_loaded_photon_paths() -> list[str]:
            return list(set([photon.filepath for photon in self.photons.values()]))
        def _get_unloaded_photon_paths(z: list[str]) -> list[str]:
            filepaths = [f"{r}{y}{f}" for r, d, ff in os.walk(x) for f in ff if f.endswith(".py")]
            return [filepath for filepath in filepaths if not filepath in z]
        async def _start_inactive_photons() -> None:
            for photon in self.photons.values(): await photon.start()
        async def _load_photons_by_string(filepaths: list[str]) -> Handler:
            return [await self._emit_photon(filepath) for filepath in filepaths]
        async def _reload_changed_photons() -> None:
            _logger = Logger(__name__)
            _photons_to_reload = []
            _photons = self.photons.copy()
            for photon in _photons.values():
                checksum = SystemUtils.get_file_checksum(photon.filepath)
                if checksum != photon.checksum:
                    _photons_to_reload.append(photon)
            reloaded = await self._reload_photons(_photons_to_reload)
            for entry in reloaded:
                if self.logging: # pragma: no cover
                    _logger.private(f"Successfully reloaded '{entry.filepath}'!")
        x = photons_directory
        y = SystemUtils.get_system_delimiter()
        while self._is_watching: # pragma: no branch
            z = _get_loaded_photon_paths()
            a = _get_unloaded_photon_paths(z)
            await _load_photons_by_string(a)
            await _reload_changed_photons()
            await _start_inactive_photons()
            #* This is mostly for unit testing...
            if loop_trace: # pragma: no branch
                try: await loop_trace.evalutate_tasks()
                except RuntimeError: break # More than likely from unit tests.
            await SystemUtils.continue_async(1)
        return True

    async def load_photon(self: "Loader", 
                            photon_path: str, 
                            photon_base: type=IPhoton, 
                            other_classes: list[str] = [],
                            recursive: bool = False) -> Handler|list[Handler]:
        """``|coro|``

        Loads a photon module from a given path, and initializes a corresponding :class:`Handler` object.\
        The provided path must be an existing file path to a photon module, and not a directory.\
        This function takes an optional base class for the photon module, and a list of other class names to be loaded.\
        If the recursive flag is set to ``True``, this method loads all photon modules recursively from the path.\
        The method raises a :class:`PhotonNotFoundError` error if the provided path is not found, or if it is a directory.
        
        Parameters
        ----------
        photon_path : :class:`str`
            A string representing the path to the photon module file to be loaded.
        photon_base : :class:`type`
            An optional base class type for photon modules to be loaded. Defaults to :class:`IPhoton`.
        other_classes : :class:`list[str]`
            An optional list of string names of other classes to load from the photon module. Defaults to ``[]``.
        recursive : :class:`bool`
            A `bool` flag that indicates whether to search for photon modules recursively under the provided path. Defaults to ``False``.
        
        Returns
        ----------
        :class:`bool`
            A list of :class:`Handler` objects representing the loaded photons, or an empty list if no photons are loaded successfully.
        
        Raises
        ----------
        PhotonNotFoundError
            An error if the provided photon path doesn't exist or is a directory.

        Examples
        ----------
        >>> photon = await load_photon("photons/my_photon.py")
        ... # A photon will then be emitted and ready to start.
        """
        if not isinstance(photon_path, str):
            raise TypeError("The photon path must be a string!")
        if not isinstance(photon_base, type):
            raise TypeError("The photon base must be a valid class type!")
        if not isinstance(other_classes, list):
            raise TypeError("Other classes must be defined as a list!")
        else:
            if any(not isinstance(element, str) for element in other_classes):
                raise TypeError("All classes must be defined as a list of strings!")
        if not isinstance(recursive, bool):
            raise TypeError("The recursive flag must be a boolean!")
        if not os.path.exists(photon_path):
            raise PhotonNotFoundError("The provided photon doesn't exist!")
        if os.path.isdir(photon_path):
            raise PhotonNotFoundError("The provided path is a directory and not a photon file!")
        self._resolver.normalize_paths(os.path.dirname(photon_path))
        photons = await self._emit_photon(photon_path,
                                            photon_base,
                                            other_classes,
                                            recursive)
        self._resolver.reset_paths(os.path.dirname(photon_path))
        return photons
    
    async def load_photons(self: "Loader", 
                            photons_directory: str,
                            photon_base: type=IPhoton,
                            other_classes: list[str] = [],
                            recursive: bool = False) -> list[Handler]:
        """``|coro|``

        Loads a directory of photon modules, each module being represented by a corresponding :class:`Handler` object, and \
        returns a list of :class:`Handler` objects. The provided path must be an existing directory path, and not a file.\
        This function takes an optional base class for photon modules, and a list of other class names to be loaded.\
        If the ``recursive`` flag is set to ``True``, all photon modules will be loaded recursively from the directory.
        
        Parameters
        ----------
        photons_directory : :class:`str`
            Represents the path to the directory containing the photon modules to be loaded.
        photon_base : Optional[:class:`type`]
            An optional base class type for photon modules to be loaded. Defaults to :class:`IPhoton`.
        other_classes : Optional[:class:`list[str]`]
            An optional list of string names of other classes to load from the photon. Defaults to ``[]``.
        recursive : Optional[:class:`bool`]
            A flag that indicates whether to search for photon modules recursively under the provided directory path. Defaults to ``False``.
        
        Returns
        ----------
        :class:`list[Handler]`
            A collection of objects representing the loaded photons, or an empty list if no photons were loaded successfully.

        Raises
        ----------
        DirectoryNotFoundError
            If the provided photon path doesn't exist, or is a file.

        Examples
        ----------
        >>> photons = await load_photons("photons/")
        ... # A list of photons will then be emitted and ready to start.
        """
        if not isinstance(photons_directory, str):
            raise TypeError("The photons directory must be a string!")
        if not isinstance(photon_base, type):
            raise TypeError("The photon base must be a valid class type!")
        if not isinstance(other_classes, list):
            raise TypeError("Other classes must be defined as a list!")
        else:
            if any(not isinstance(element, str) for element in other_classes):
                raise TypeError("All classes must be defined as a list of strings!")
        if not isinstance(recursive, bool):
            raise TypeError("The recursive flag must be a boolean!")
        if not os.path.exists(photons_directory):
            raise DirectoryNotFoundError("The provided photon directory doesn't exist!")
        if os.path.isfile(photons_directory):
            raise DirectoryNotFoundError("The provided path is a file and not a photon directory!")
        self._resolver.normalize_paths(photons_directory)
        photons: list[Handler] = await self._emit_photons(photons_directory,
                                                            photon_base,
                                                            other_classes,
                                                            recursive)
        self._resolver.reset_paths(photons_directory)
        return photons
    
    async def unload_photon(self: "Loader", photon: Handler|str, force_stop: bool = False) -> bool:
        """``|coro|``

        Stops and unloads a specified photon from the loader's photon registry by calling its finalizer, if any,\
        and disposing unused resources. If the given photon is a string, it is looked up in the registry by filepath.\
        The method returns a boolean value indicating whether the photon was successfully stopped and unloaded.
        
        Important
        ----------
        Unloading a single photon unloads the entire file from which that photon originated. So, that means all\
        other photons that may be found within the file as well.

        Parameters
        ----------
        photon : :class:`Handler | str`
            The photon handler object or filepath which represents a running photon to be unloaded.
        force_stop : :class:`bool`
            A flag which allows a photon to be immediately halted and collected without calling its finalizer.

        Returns
        ----------
        :class:`bool`
            A flag indicating if the provided photon was unloaded.

        Examples
        ----------
        >>> await unload_photon(handler)
        True
        >>> await unload_photon('photons/a.py', force_stop=True)
        True
        """
        if not isinstance(photon, Handler) and not isinstance(photon, str):
            raise TypeError("The photon must be a Handler object or a filepath string!")
        if not isinstance(force_stop, bool):
            raise TypeError("The force stop flag must be a boolean value!")
        return await self._absorb_photon(photon, force_stop)

    async def unload_photons(self: "Loader", photons: list[Handler|str], force_stop: bool = False) -> list[str]:
        """``|coro|``
        
        Stops and unloads a collection of photons from the loader's photon registry by calling their finalizers, if any, \
        and disposing unused resources. If a given photon is a string, it is looked up in the registry by filepath.\
        The function returns a list of filepaths indicating whether the photons were successfully stopped and unloaded.
        
        Important
        ----------
        Unloading any photon unloads the entire file from which that photon originated. So, that means all\
        other photons that may be found within the file as well.

        Parameters
        ----------
        photons : :class:`list[Handler|str]` 
            A list of photon handler objects or filepaths to be unloaded.
        force_stop : :class:`bool`
            A flag which allows a photon to be immediately halted and collected without calling its finalizer.

        Returns
        ----------
        :class:`list[str]`
            A list containing the filepaths of all unloaded photons.

        Examples
        ----------
        >>> await unload_photons([handler1, handler2])
        ['photons/a.py', 'photons/a.py']
        >>> await unload_photons(['photons/a.py', 'photons/b.py'], force_stop=True)
        ['photons/a.py', 'photons/b.py']
        """
        if not isinstance(photons, list):
            raise TypeError("Photons must be defined as a list of photon Handler objects or strings!")
        else:
            if any(not isinstance(photon, str) and not isinstance(photon, Handler) for photon in photons):
                raise TypeError("Photons must be defined as a list of photon Handler objects or strings!")
        if not isinstance(force_stop, bool):
            raise TypeError("The force stop flag must be a boolean value!")
        return await self._absorb_photons(photons, force_stop)

    async def reload_photon(self: "Loader", photon: Handler|str) -> Handler|list[Handler]:
        """``|coro|``

        Atomically reloads the specified photon and provides a fresh handler.

        Parameters
        ----------
        photon : :class:`Handler|str`
            The photon handler or filepath of a photon that is to be reloaded.

        Returns
        ----------
        :class:`Handler|list[Handler]`
            A handler or list of handler objects representing the newly updated photon.

        Notes
        ----------
        This function makes a copy of both the loader's ``self._photons``, 
        and the related ``sys.modules``. After which the provided photon will 
        be unloaded, loaded again, and then returned as a freshly updated photon 
        :class:`Handler` object. If any errors, in either unloading or loading,
        all photons will revert to their original states.

        Examples
        ----------
        >>> reloaded_handler = await reload_photon(my_photon_handler)
        ... # A new handler will be created and returned from the original handler object. 
        >>> reloaded_handler = await reload_photon('photons/my_photon.py')
        ... # A new handler will be created and returned from the provided handler file path.
        """
        if not isinstance(photon, Handler) and not isinstance(photon, str):
            raise TypeError("The photon must be a Handler object or a filepath string!")
        return await self._reload_photon(photon)

    async def reload_photons(self: "Loader", photons: list[Handler|str]) -> list[Handler]:
        """``|coro|``

        Atomically reloads the specified photons and provides a list of fresh handlers.

        Returns
        ----------
        :class:`list[Handler]`
            A list of handler objects representing the newly updated photons.

        Notes
        ----------
        This function makes a copy of both the loader's ``self._photons``, 
        and the related ``sys.modules``. After which the provided photons will 
        be unloaded, loaded again, and then returned as freshly updated photon 
        :class:`Handler` objects. If any errors, in either unloading or loading,
        all photons will revert to their original states.
        
        Examples
        ----------
        >>> reloaded_handlers = await reload_photons([my_photon_handler, second_photon_handler])
        ... # New handlers will be created and returned from the original handler objects. 
        >>> reloaded_handlers = await reload_photons('photons/my_photon.py', 'photons/second_photon.py')
        ... # New handlers will be created and returned from the provided handler file path.
        """
        if not isinstance(photons, list):
            raise TypeError("Photons must be defined as a list of photon Handler objects or strings!")
        else:
            if any(not isinstance(photon, str) and not isinstance(photon, Handler) for photon in photons):
                raise TypeError("Photons must be defined as a list of photon Handler objects or strings!")
        return await self._reload_photons(photons)

    async def watch_photons(self: "Loader", photons_directory: str) -> None:
        """``|coro|``

        Creates a thread manager and spawns a new thread to monitor photons in a given directory\
        for changes and reloads them atomically.
        
        Parameters
        ----------
        photons_directory : :class:`str`
            The directory path to the photons folder which needs to be monitored.
            
        Raises
        ----------
        TypeError
            If the ``photons_directory`` argument is not a string.
        DirectoryNotFoundError
            If the ``photons_directory`` argument is not a valid directory.
        ThreadManagerAlreadyRunning
            If the loader is already monitoring photons.
        
        Notes
        ----------
        - This asynchronous function spawns a thread manager and a new thread to monitor photons in a given directory.
        - The function starts by validating whether the `photons_directory` argument is a valid directory and of type :class:`str`.
        - If the `_is_watching` flag is ``True``, the function raises a warning by raising `ThreadManagerAlreadyRunningError`.
        - Then the function sets the ``_is_watching`` flag to ``True`` and sets the number of allowed threads to one.\
        The function appends a new thread to the thread manager through the :func:`_start_watching()` callback function.\
        The thread is then started and runs indefinitely until the ``_is_watching`` flag is set to ``False``.\
        The wait time between cycles is set to one second by calling the :func:`SystemUtils.continue_async(1)` function.
        - Please note that this function starts the thread manager and a new thread to monitor photons. \
        Hence, the thread manager must be stopped by calling the :func:`stop_watching_photons()` function\
        of the photon :class:`Loader` instance.

        """
        def _start_watching(directory: str) -> None: # pragma: no cover
            asyncio.run(self._observe_photons(directory)) 
        if not isinstance(photons_directory, str):
            raise TypeError("The photons directory must be a string!")
        if not os.path.exists(photons_directory) or os.path.isfile(photons_directory):
            raise DirectoryNotFoundError("The photons directory should be a real directory!")
        if self._is_watching:
            raise ThreadManagerAlreadyRunningError("The loader is currently already monitoring photons.")
        self._is_watching = True
        self._threads.thread_limit = 1
        self._threads.append_thread(_start_watching, (photons_directory,))
        self._threads.run()
        await SystemUtils.continue_async(1) # Necessary for unit testing.

    async def stop_watching_photons(self: "Loader", halt_threads: bool = False) -> None:
        """``|coro|``

        Stops all threads from watching changes in photons and gracefully stops the thread manager.
        
        Parameters
        ----------
        halt_threads : Optional[:class:`bool`]
            An optional boolean flag to halt all running threads immediately without a flag,
            instead of gracefully stopping the thread manager, defaults to ``False``.
            
        Notes
        ----------
        This asynchronous function stops all threads and gracefully shuts down the thread manager from watching changes in photons.
        
        - The function starts by setting the ``_is_watching`` flag to ``False``. If ``halt_threads`` is ``True``,\
        the function calls the :func:`halt()` function of the thread manager instance to stop all running threads immediately.\
        If ``halt_threads`` is ``False``, the function calls the :func:`stop()` function to gracefully stop all threads.
        - To prevent memory leaks and other issues, it is recommended to stop any running threads gracefully\
        instead of abruptly halting or killing them. In most cases, setting ``halt_threads`` to ``False`` is preferred to ensure\
        a graceful shutdown of all threads.
        
        """
        self._is_watching = False
        if halt_threads:
            self._threads.halt() # Stops threads immediately without a flag.
        self._threads.stop() # Stop threads gracefully with a flag.