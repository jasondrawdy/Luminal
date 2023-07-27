# -*- coding: utf-8 -*-
# ########################################################################                          
# Program: Luminal
# Author: Jason Drawdy
# Version: 1.0.0
# Date: 07/07/23
# #########################################################################
# Description:
# These are a collection of custom operating system based exception errors.
# #########################################################################
class DirectoryNotFoundError(Exception):
    """
    Error raised when a directory is not found.

    Examples
    ----------
    >>> raise DirectoryNotFoundError("Directory not found!")
    """
    def __init__(self, *args: object) -> None:
        """
        Initializes the :class:`DirectoryNotFoundError` instance.

        Parameters
        ----------
        *args : :class:`object` 
            The error message arguments.
        """
        super().__init__(*args)