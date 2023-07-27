# -*- coding: utf-8 -*-
# ########################################################################                          
# Program: Luminal
# Author: Jason Drawdy
# Version: 1.0.0
# Date: 07/07/23
# #########################################################################
# Description:
# These are a collection of custom threading based exception errors.
# #########################################################################
class NoThreadsFoundError(Exception):
    """
    Error raised when no threads are available to run.

    Examples
    ----------
    >>> raise NoThreadsFoundError("No threads available to run.")
    """
    def __init__(self, *args: object) -> None:
        """
        Initializes the :class:`NoThreadsFoundError` instance.

        Parameters
        ----------
        *args : :class:`object`
            The error message arguments.
        """
        super().__init__(*args)

class ThreadManagerAlreadyRunningError(Exception):
    """
    Error raised when a thread manager is already running.

    Examples
    ----------
    >>> raise ThreadManagerAlreadyRunningError("Thread manager already running!")
    """
    def __init__(self, *args: object) -> None:
        """
        Initializes the :class:`ThreadManagerAlreadyRunningError` instance.

        Parameters
        ----------
        *args : :class:`object` 
            The error message arguments.
        """
        super().__init__(*args)

class ThreadsAlreadyRunningError(Exception):
    """
    Error raised when threads are already running.

    Examples:
    ----------
    >>> raise ThreadsAlreadyRunningError("Threads are already running!")
    """
    def __init__(self, *args: object) -> None:
        """
        Initializes the :class:`ThreadsAlreadyRunningError` instance.

        Parameters
        ----------
        *args : :class:`object`
            The error message arguments.
        """
        super().__init__(*args)

class ThreadLimitReachedError(Exception):
    """
    Error raised when the maximum number of threads has been reached.

    Examples
    ----------
    >>> raise ThreadLimitReachedError("Thread limit has been reached!")
    """
    def __init__(self, *args: object) -> None:
        """
        Initializes the :class:`ThreadLimitReachedError` instance.

        Parameters
        ----------
        *args : :class:`object`
            The error message arguments.
        """
        super().__init__(*args)