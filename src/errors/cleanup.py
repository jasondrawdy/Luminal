# -*- coding: utf-8 -*-
# ########################################################################                          
# Program: Luminal
# Author: Jason Drawdy
# Version: 1.0.0
# Date: 07/07/23
# #########################################################################
# Description:
# These are a collection of photon based exception errors.
# #########################################################################
class FinalizerNotImplementedError(Exception):
    """
    Error raised when a photon does not implement the `finalize()` method.

    Examples
    ----------
    >>> raise FinalizerNotImplementedError("Finalize method not implemented in photon!")
    """
    def __init__(self, *args: object) -> None:
        """
        Initializes the `FinalizerNotImplementedError` instance.

        Parameters
        ----------
        *args : :class:`object` 
            The error message arguments.
        """
        super().__init__(*args)

class PhotonNotInitializedError(Exception):
    """
    Error raised when a photon is not initialized before usage.

    Examples
    ----------
    >>> raise PhotonNotInitializedError("Photon has not been initialized!")
    """
    def __init__(self, *args: object) -> None:
        """
        Initializes the `PhotonNotInitializedError` instance.

        Parameters
        ----------
        *args : :class:`object` 
            The error message arguments.
        """
        super().__init__(*args)

class PhotonNotFoundError(Exception):
    """
    Error raised when a photon cannot be found.

    Examples
    ----------
    >>> raise PhotonNotFoundError("Photon could not be found!")
    """
    def __init__(self, *args: object) -> None:
        """
        Initializes the `PhotonNotFoundError` instance.

        Parameters
        ----------
        *args : :class:`object` 
            The error message arguments.
        """
        super().__init__(*args)