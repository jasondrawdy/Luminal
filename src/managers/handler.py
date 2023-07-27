# -*- coding: utf-8 -*-
# ########################################################################                          
# Program: Luminal
# Author: Jason Drawdy
# Version: 1.0.0
# Date: 07/07/23
# #########################################################################
# Description:
# This module is responsible for providing an encapsulation for photons
# and their type instances. Also provides extensive information such as
# the name, path, checksum, and more of the photon being encapsulated. 
# #########################################################################
from ..errors.cleanup import (
    FinalizerNotImplementedError, 
    PhotonNotInitializedError
)
from ..managers.resolver import Resolver
from ..interfaces.photon import IPhoton
from ..tools.utils import SystemUtils
from ..tools.logger import Logger
import threading
import hashlib
import asyncio
import psutil
import sys
import os

class Handler():
    """Wraps an :class:`IPhoton` or another inherited photon base class and provides access to local instance information."""
    def __init__(self: "Handler", logging: bool, name: str, filepath: str, checksum: str, instance: IPhoton|object) -> None:
        """
        Initializes a new instance of the :class:`Handler` class.

        Parameters
        ----------
        logging : :class:`bool` 
            Flag to initialize logging or not.
        name : :class:`str`
            The name of the :class:`Handler`.
        filepath : :class:`str` 
            File path where the :class:`Handler` instance is located.
        instance : :class:`IPhoton|object` 
            Either an instance of :Class:`IPhoton` or an instance of another type :class:`object`.

        Notes
        ----------
        - This code initializes logging for the :class:`Handler` instance if the logging attribute is ``True``.\
        It also resolves paths using the ``_resolver`` instance, sets appropriate path delimiters with the ``_delimiter``\
        attribute, and stores the system and location information in the ``_system`` and ``_filepath`` attributes, respectively.
        - The ``_instance`` attribute can hold either an :class:`IPhoton` instance or an :class:`object`.

        """
        self.logging: bool = logging
        self._logger: Logger = Logger(__name__)
        self._resolver: Resolver = Resolver()
        self._system: str = SystemUtils.get_system()
        self._delimiter: str = "\\" if self._system == SystemUtils.windows else "/"
        self._name: str = name
        self._filepath: str = filepath
        self._checksum: str = checksum
        self._instance: IPhoton|object = instance

    def __str__(self) -> str:
        """
        Returns the current :class:`Handler` instance as its string representation.
        
        Returns
        ----------
        :class:`str`
            A string representation of the :class:`Handler` object created by the
            :func:`__dict__()` dunder method.
        """
        return str(self.__dict__)
    
    @property
    def name(self: "Handler") -> str:
        """
        Returns the name of the current :class:`Handler` instance.
        
        Returns
        ----------
        :class:`str`
            The name of the current :class:`Handler` instance.
        """
        return self._name
    
    @property
    def filepath(self: "Handler") -> str:
        """
        Returns the file path of the current :class:`Handler` instance.
        
        Returns
        ----------
        :class:`str`
            The file path of the current :class:`Handler` instance.
        """
        return self._filepath
    
    @property
    def checksum(self: "Handler") -> str:
        """
        Returns the checksum of the original photon file.
        
        Returns
        ----------
        :class:`str`
            The checksum of the original file containing the photon.
        """
        return self._checksum
    
    @staticmethod
    async def _get_checksum(filename: str, block: int = 2**20) -> str|None:
        """``|coro|``

        Generates a calculated ``SHA512`` hash for a given file.

        Parameters
        ----------
        filename : :class:`str`
            The name of the file to generate the checksum for.
        block : Optional[:class:`int`]
            Chunk size to read and hash the file in bytes. Default is ``2^20``.

        Returns
        ----------
        Optional[:class:`str`]
            The calculated ``SHA512`` hash of the file, or ``None`` if there was an error generating the checksum.

        Notes
        ----------
        - This function generates a ``SHA512`` hash for a given file by reading the file in blocks and hashing each block.\
        The generated hash is a digest checksum (a unique fixed-sized representation of the file content).\
        The file is treated as a binary file (read in 'rb' mode) for proper handling of all types of files.
        - The reason ``SHA512`` was chosen is purely for the lack of collisions at runtime when performing dynamic checks.
        - If the specified file cannot be found or if there are any errors while generating the checksum, returns ``None``.
        
        """
        if not os.path.isfile(filename):
            return None
        try:
            checksum = hashlib.sha512()
            with open(filename, 'rb') as file:
                loop = asyncio.get_running_loop()
                while True:
                    data = await loop.run_in_executor(None, file.read, block)
                    if not data: break
                    checksum.update(data)
            return checksum.hexdigest()
        except IOError as error: # pragma: no cover
            raise IOError(f"Checksum generation error: {error}")
    
    async def _clear_module_references(self: "Handler") -> bool:
        """``|coro|``

        Clears all references for the current handler module and its submodules in `sys.modules`.

        Returns
        ----------
        :class:`bool`
            A flag value indicating whether references were cleared successfully.

        Notes
        ----------
        - This function clears all references to the current module and any of its submodules in ``sys.modules``.\
        It is used to ensure that a module can be safely deleted from memory without any leftover references.\
        The function returns ``True`` if the operation to clear references succeeds. Default is ``False``.
        """
        try:
            await SystemUtils.continue_async()
            self._instance = None
            resolved_name = self._resolver.resolve_path(self._filepath)[0]
            sys.modules.pop(resolved_name, None)
            for module in list(sys.modules.keys()):
                if SystemUtils.is_submodule(self._name, module):
                    del sys.modules[module] # pragma: no cover
            return True
        except: return False # pragma: no cover

    async def _stop_photon_threads(self: "Handler") -> bool:
        """``|coro|``

        This function stops all of the running threads that belong to the current photon's thread group. It is typically 
        called during a photon unload to ensure that no threads are left running that could cause errors or conflicts 
        with a new, reloaded photon.

        Returns
        ----------
        :class:`bool`
            A flag indicating whether all photon threads were successfully stopped. This returns ``True`` if 
            all photon threads are successfully stopped. Default is ``False``.
        """
        try:
            await SystemUtils.continue_async()
            for thread in threading.enumerate():
                if thread.name == self._name:
                    thread.stop() # pragma: no cover
            return True
        except: return False # pragma: no cover

    async def _stop_photon_processes(self: "Handler") -> bool: # pragma: no cover
        """``|coro|``

        This function is responsible for stopping and terminating all of the child processes spawned by the handler.

        Returns
        ----------
        :class:`bool`
            A flag indicating whether any child process for the handler were stopped. Default is ``False``.
        """
        await SystemUtils.continue_async()
        current_pid = os.getpid()
        parent_processes = {current_pid: IPhoton}
        parent_class = None
        for parent in psutil.Process(current_pid).parents():
            filename = self._filepath.split(self._delimiter)[-1]
            if parent.pid in parent_processes:
                parent_class = parent_processes[parent.pid]
            elif filename in parent.cmdline():
                parent_processes[parent.pid] = IPhoton
                parent_class = IPhoton
        if parent_class == IPhoton:
            [child.terminate() for child in psutil.Process(os.getpid()).children()]
            psutil.wait_procs(psutil.Process(os.getpid()).children())
            return True
        return False
    
    async def _force_stop(self: "Handler") -> None:
        """``|coro|``

        This function is responsible for forcefully stopping and halting all the running threads and processes of the handler.
        It calls the :func:`_stop_photon_threads()` and :func:`_stop_photon_processes()` methods to perform these tasks.
        """
        if not await self._stop_photon_threads():
            if self.logging: # pragma: no cover
                self._logger.error("Photon child threads could not be halted!")
        if not await self._stop_photon_processes():
            if self.logging:# pragma: no cover
                self._logger.error("Photon child processes could not be terminated!")

    async def _stop(self: "Handler", force_stop: bool = False) -> None:
        """``|coro|``

        This function stops the running :class:`IPhoton` instance, halting all the child threads and processes of the instance 
        if any exist. If ``force_stop`` is ``True``, this function calls the :func:`_force_stop()` method to stop the instance. 
        Otherwise, it first calls the :func:`finalize()` method if present in the current instance. If the :func:`finalize()` method 
        does not exist or raises an error, then the :func:`_force_stop()` method is called.

        Parameters
        ----------
        force_stop : Optional[:class:`bool`] 
            A boolean flag indicating whether to forcefully stop the photon instance. Default is ``False``.

        Raises
        ----------
        PhotonNotInitializedError
            If the photon has not been initialized.
        """
        if isinstance(self._instance, tuple):
            current_instance = self._instance[0]
            if force_stop: await self._force_stop()
            else:
                if hasattr(current_instance, "finalize"): # pragma: no branch
                    finalizer = getattr(current_instance, "finalize")
                    if callable(finalizer): # pragma: no branch
                        try: 
                            await finalizer()
                        except FinalizerNotImplementedError as error:
                            raise error
                        except Exception as error: # pragma: no cover
                            raise error
            await self._clear_module_references()
        else: raise PhotonNotInitializedError("The photon has not been initialized.")
    
    async def start(self: "Handler") -> None:
        """``|coro|``

        This function starts running the ``IPhoton`` instance by creating it if it does not exist already.
        
        Notes
        ----------
        - If already started, it checks if it's a :class:`tuple`. If the instance is not a :class:`tuple`, it\
        initializes the ``IPhoton`` instance and stores it as a tuple with a second value set to ``True``.
        """
        await SystemUtils.continue_async()
        if not self._instance is None:
            if type(self._instance) is not tuple: # pragma: no branch
                try:
                    instance_type = self._instance
                    instance = self._instance()
                    self._instance = (instance, instance_type)
                except Exception as error: # pragma: no cover
                    if self.logging:
                        self._logger.error(f"Photon started in partial-mode due to the following: {error}")
                        self._instance = (None, None)