# -*- coding: utf-8 -*-
# ########################################################################                          
# Program: Luminal
# Author: Jason Drawdy
# Version: 1.0.0
# Date: 07/07/23
# #########################################################################
# Description:
# This module is responsible for resolving system paths for the current
# operating system, e.g. Windows, Linux, and macOS.
# #########################################################################
from ..tools.utils import SystemUtils
import sys
import os

class Resolver():
    """This class provides a way to resolve module and package paths for the current operating system."""
    def __init__(self: "Resolver") -> None:
        """
        Initializes an instance of the :class:`Resolver` class and sets attributes specific to the current operating system.

        Attributes
        ----------
        _system : :class:`str`
            A string representing the current operating system. This attribute is determined using the :func:`get_system()` method of the :class:`SystemUtils` class.
        _delimiter : :class:`str` 
            A string representing the folder delimiter for the current operating system. It is set to ``\\`` if the current operating system is ``Windows``, otherwise it is set to ``/``.
        _modified_paths : :class:`str`
            A dictionary that keeps track of modified paths and their timestamps. It is used to monitor changes in module paths.
        """
        self._system = SystemUtils.get_system()
        self._delimiter = "\\" if self._system == SystemUtils.windows else "/"
        self._modified_paths: dict[str, int] = {}

    def _add_path(self: "Resolver", path: str) -> None:
        """
        Append a path to the ``PYTHONPATH`` variable to allow relative imports of an imported 
        module, and save the updated path information in the ``_modified_paths`` dictionary.

        Important
        ----------
        This method should not be called outside of the current :class:`Resolver` instance.

        Parameters
        ----------
        path : :class:`str`
            The path to be added to the ``_modified_paths`` dictionary.
            
        Notes
        ----------
        - This method appends the specified path to the ``PYTHONPATH`` variable and updates the\
        ``_modified_paths`` dictionary with the ``path`` as the key and the index of the ``path``\
        in the ``sys.path`` list as the value. It is used to facilitate relative imports of modules \
        from a given path, and to keep track of any changes in the module paths.
        - This method does not return anything and always adds the new path to the end of the ``sys.path``\
        list. If the specified path is already present in the ``sys.path`` list, it will not be added again\
        and the method will simply update the ``_modified_paths`` dictionary with the new information.
        
        """
        if path not in sys.path:
            self._modified_paths[path] = len(sys.path)
            sys.path.insert(self._modified_paths[path], path)

    def _remove_path(self: "Resolver", path: str) -> None:
        """
        Remove the specified path from the system path ``sys.path``
        and clears its index in the ``_modified_paths`` dictionary.

        Important
        ----------
        This method should not be called outside of the current :class:`Resolver` instance.

        Parameters
        ----------
        path : :class:`str`
            A string representing the path to be removed from the system path.

        Notes
        ----------
        - Helper method for :class:`Resolver` objects that removes a given path from\
        the system path. If the provided path is in ``_modified_paths`` dictionary,\
        this method clears its saved index by deleting the corresponding key-value\
        pair. Then it checks if the saved index is still valid. If it is valid,\
        then it removes the path from the system path using the :func:`pop()` method\
        with the saved index as the argument. If the saved index is not valid,\
        then it removes the last occurrence of the path from the system path by\
        iterating the ``sys.path`` in reverse order.
        - This method does not return anything and modifies ``sys.path`` and the local\
        ``_modified_paths`` dictionary directly.

        """
        if path in self._modified_paths:
            # If PYTHONPATH was modified by an imported module 
            # check if the saved index is still valid.
            if sys.path[self._modified_paths[path]] == path:
                sys.path.pop(self._modified_paths[path])
            else: # Remove the last occurence of the path.
                for i in range(len(sys.path) - 1, 0, -1):
                    if sys.path[i] == path: # pragma: no cover
                        sys.path.pop(i)
    
    def normalize_paths(self: "Resolver", path: str) -> None:
        """
        Converts and adds the input path as an absolute and normalized path to ``sys.path``.

        Important
        ----------
        This method should not be called outside of the current :class:`Resolver` instance.

        Parameters
        ----------
        path : :class:`str`
            The path to be normalized.

        Notes
        ----------
        - This method is a helper function used by the :class:`Resolver` class to\
        ensure consistency in the format of the input path. The :func:`os.path.abspath()` and\
        :func:`os.path.normpath()` functions are used to convert the input ``path`` to an\
        absolute and normalized path. The normalized path is then added to the system\
        path via the :func:`_add_path()` method. The method does not return anything and\
        modifies the current system path.

        """
        path = os.path.abspath(os.path.normpath(path))
        self._add_path(path)

    def reset_paths(self: "Resolver", path: str) -> None:
        """
        Removes the specified path from ``sys.path`` and the internal ``_modified_paths`` dictionary.

        Important
        ----------
        This method should not be called outside of the current :class:`Resolver` instance.

        Parameters
        ----------
        path : :class:`str`
            The path to be removed from the system path

        Notes
        ----------
        - This method is a helper function used by the :class:`Resolver` class to remove a\
        specified path from the system path. The method calls :func:`_remove_path()`\
        with the given path to remove the path from ``sys.path``. The method\
        does not return anything and modifies the system path.

        """
        self._remove_path(path)

    def resolve_path(self: "Resolver", path: str) -> tuple:
        """
        Extracts the module name and its full path from the provided relative path.

        Important
        ----------
        This method should not be called outside of the current :class:`Resolver` instance.

        Parameters
        ----------
        path : :class:`str`
            The relative path to the desired Python module.

        Returns
        ----------
        :class:`tuple`
            A tuple containing the name and resolved path of the
            Python module corresponding to the provided relative path.
        """
        split = path.split(self._delimiter)
        resolved_name = split[-1][0:-3]
        resolved_path = path.replace(f"{resolved_name}.py", "").replace(f"{self._delimiter}", ".")
        return (resolved_name, resolved_path)