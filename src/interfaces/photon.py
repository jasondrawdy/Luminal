# -*- coding: utf-8 -*-
# ########################################################################                          
# Program: Luminal
# Author: Jason Drawdy
# Version: 1.0.0
# Date: 07/07/23
# #########################################################################
# Description:
# This module contains all metadata about a given photon and also provides
# a simple, clean, and easy to understand interface for creating photons.
# #########################################################################
from ..errors.cleanup import FinalizerNotImplementedError
from ..interfaces.metadata import MetaProperties, ClassProperty
from typing import TextIO, Any
from abc import ABCMeta
import inspect
import sys

class IPhotonMeta(ABCMeta, MetaProperties):
    """
    The metaclass for the abstract base class :class:`IPhoton` that enables\
    the specification of authorship, version, tags, and a description\
    for the derived classes.

    This metaclass is used to define several class attributes for any\
    class that derives from the base class :class:`IPhoton`. The attributes are\
    used to provide metadata about the derived class. The metaclass is\
    created by inheriting from :class:`ABCMeta` and :class:`MetaProperties` and includes\
    multiple attributes.

    Usage
    ----------
    - This metaclass is typically used by inheriting it from an :class:`IPhoton` base class.
    - To specify values for the metadata attributes in a derived class, simply\
    define the corresponding attributes inside the class definition with\
    appropriate values.

    Examples
    ----------
    >>> class MyPhotonInterface(metaclass=IPhotonMeta):
    >>> ...

    Here, a new class named ``MyPhotonInterface`` is created with the photon-specific metadata.
    """
    __photon_name__: str
    __photon_author__: str
    __photon_version__: str
    __photon_description__: str
    __photon_tags__: list[str]

    def __new__(cls, *args: Any, **kwargs: Any) -> "IPhotonMeta":
        """
        Creates a new class object with the added photon metadata.

        Parameters
        ----------
        cls : :class:`Type[Self@IPhotonMeta]`
            The base metaclass instance.
        args : :class:`Any`
            The positional arguments of the new metaclass instance.
        kwargs : :class:`Any`
            The keyword arguments, including:
                name : :class:`str`
                    The name of the photon.
                author : :class:`str`
                    The name of the photon author.
                version : :class:`str`
                    The version of the photon.
                description : :class:`str`
                    A description of the photon.
                tags : :class:`list[str]`
                    A list of tags associated with the photon.

        Returns
        ----------
        :class:`IPhotonMeta`
            A new class object with the added photon metadata.

        Raises
        ----------
        KeyError
            When `name` is not provided as a keyword argument.
        """
        name, bases, attrs = args
        try:
            photon_name = kwargs.pop('name')
        except KeyError:
            photon_name = name
        attrs['__photon_name__'] = photon_name
        attrs['__photon_author__'] = kwargs.pop('author', "Unknown")
        attrs['__photon_version__'] = kwargs.pop('version', "0.0.0")
        description = kwargs.pop('description', None)
        if description is None: # pragma: no branch
            description = inspect.cleandoc(attrs.get('__doc__', ''))
        attrs['__photon_description__'] = description
        attrs['__photon_tags__'] = kwargs.pop('tags', ['luminal', 'photon'])
        new_cls = super().__new__(cls, name, bases, attrs, **kwargs)
        return new_cls

    def __init__(self, *args: tuple, **kwargs: dict[str, Any]) -> None:
        super().__init__(*args, **kwargs)

class IPhoton(metaclass=IPhotonMeta):
    """
    Base class for all Luminal photons.

    Important
    ----------
    This class provides several other utility functions and properties that can be used by Luminal photons.
    """
    __photon_name__: str
    __photon_author__: str
    __photon_version__: str
    __photon_description__: str
    __photon_tags__: list[str]

    def __new__(cls, *args: tuple, **kwargs: dict[str, Any]) -> "IPhoton":
        """
        Creates a new instance of the :class:`IPhoton` class.

        This method is called before initializing the instance.

        Parameters
        ----------
        cls : :class:`Type[Self@IPhoton]`
            The base class itself.
        *args : :class:`Any`
            The positional arguments of the new :class:`IPhoton` instance.
        **kwargs : :class:`Any`
            The keyword arguments of the :class:`IPhoton` instance.

        Returns
        ----------
        :class:`IPhoton`
            The new instance of the :class:`IPhoton` class.
        """
        self = super().__new__(cls)
        return self

    def __init__(self, *args: tuple, **kwargs: dict[str, Any]) -> None:
        """
        Initializes the :class:`IPhoton` instance.

        This method is called after creating the instance.

        Parameters
        ----------
        *args : :class:`Any`
            The positional arguments of the :class:`IPhoton` instance.
        **kwargs : :class:`Any`
            The keyword arguments of the :class:`IPhoton` instance.
        """
        super().__init__()
        
    def _print(self: "IPhoton", message: str, print_output: bool = True, file: TextIO=sys.stdout, **kwargs: dict[str, Any]) -> None:
        """
        Prints the given message to the console or a file.

        Parameters
        ----------
        message : :class:`str`
            The message to print to the console.
        file : Optional[:class:`TextIO`]
            The IO stream that should be written to.
        **kwargs : Optional[:class:`dict[str, Any]`]
            The keyword arguments of the :func:`print()` call.
        """
        if print_output: # pragma: no cover
            print(f"[{self.photon_name}]: {message}", file=file, **kwargs)
        
    def print(self: "IPhoton", message: str, print_output: bool = True, file: TextIO=sys.stdout, **kwargs: dict[str, Any]) -> None:
        """
        Prints the given message to the console or a file.

        Parameters
        ----------
        message : :class:`str`
            The message to print to the console.
        file : Optional[:class:`TextIO`]
            The IO stream that should be written to.
        **kwargs : Optional[:class:`dict[str, Any]`]
            The keyword arguments of the :func:`print()` call.
        """
        if print_output: # pragma: no cover
            self._print(message=message, file=file, **kwargs)

    def eprint(self: "IPhoton", message: str, print_output: bool = True, file: TextIO=sys.stderr, **kwargs: dict[str, Any]) -> None:
        """
        Prints the given error message to the console or a file.

        Parameters
        ----------
        message : :class:`str`
            The error message to print to the console.
        file : Optional[:class:`TextIO`]
            The IO stream that should be written to.
        **kwargs : Optional[:class:`dict[str, Any]`]
            The keyword arguments of the :func:`print()` call.
        """
        if print_output: # pragma: no cover
            self._print(message=message, file=file, **kwargs)

    async def finalize(self: "IPhoton") -> bool:
        """
        A method that can, and should, be overridden to perform finalization tasks when the photon is unloaded.

        Returns
        ----------
        :class:`bool`
            A flag which returns ``True`` if the finalization method completed successfully, else ``False``.

        Raises
        ----------
        FinalizerNotImplementedError
            If this method is not implemented by the subclass.
        """
        raise FinalizerNotImplementedError("The finalizer has not been implemented for this photon.")
    
    @ClassProperty
    def photon_name(cls) -> str:
        """
        Returns the name of the :class:`IPhoton`.

        Parameters
        ----------
        cls : :class:`Type[Self@IPhoton]`
            The base class itself.

        Returns
        ----------
        :class:`str`
            The name of the photon.
        """
        return cls.__name__
    
    @ClassProperty
    def photon_author(cls) -> str:
        """
        Returns the author of the :class:`IPhoton`.

        Parameters
        ----------
        cls : :class:`Type[Self@IPhoton]`
            The base class itself.

        Returns
        ----------
        :class:`str` 
            The author of the photon, as a string.
        """
        return getattr(cls, "__photon_author__", None)
    
    @ClassProperty
    def photon_version(cls) -> str:
        """
        Returns the version of the :class:`IPhoton`.

        Parameters
        ----------
        cls : :class:`Type[Self@IPhoton]`
            The base class itself.

        Returns
        ----------
        :class:`str`
            The version of the photon, as a string.
        """
        return getattr(cls, "__photon_version__", None)
    
    @ClassProperty
    def photon_description(cls) -> str:
        """
        Returns the description of the :class:`IPhoton`.

        Parameters
        ----------
        cls : :class:`Type[Self@IPhoton]`
            The base class itself.

        Returns
        ----------
        :class:`str` 
            The description of the photon, as a string.
        """
        return getattr(cls, "__photon_description__", None)
    
    @ClassProperty
    def photon_tags(cls) -> list[str]:
        """
        Returns the list of tags associated with the :class:`IPhoton`.

        Parameters
        ----------
        cls : :class:`Type[Self@IPhoton]`
            The base class itself.

        Returns
        ----------
        :class:`list`
            The list of tags associated with the photon, as a list of strings.
        """
        return getattr(cls, "__photon_tags__", None)