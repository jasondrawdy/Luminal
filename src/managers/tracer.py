# -*- coding: utf-8 -*-
# ########################################################################                          
# Program: Luminal
# Author: Jason Drawdy
# Version: 1.0.0
# Date: 07/07/23
# #########################################################################
# Description:
# This module is responsible for providing functionality that allows the
# tracing of a loop or even just a task containing a coroutine.
# #########################################################################
from typing import Awaitable

class LoopTask:
    """
    A wrapper for a coroutine and its arguments which will be started at
    a specific iteration within an infinite loop, or any loop in general.

    Examples
    ----------
    >>> async def do_task(some_arg):
    ...     await asyncio.sleep(1)
    ...     print(some_arg)
    ... 
    >>> task = LoopTask(at_iteration=5, coroutine=do_task, some_arg='hello')
    >>> # Run a loop and start the coroutine when on the 5th iteration.
    >>> for i in range(10):
    ...     if i == task._at_iteration:
    ...         await task.coroutine(*task.args)

    """
    def __init__(self: "LoopTask", at_iteration: int, coroutine: Awaitable, *args: tuple) -> None:
        """
        Initializes a new :class:`LoopTask` instance.
        
        Parameters
        ----------
        at_iteration : :class:`int`
            The iteration number at which the coroutine must be executed.
        coroutine : :class:`Awaitable`
            A coroutine to be executed when the :class:`LoopTask` is run.
        *args : :class:`tuple`
            Optional arguments that can be passed to the coroutine when it is executed.
        """
        self._at_iteration: int = at_iteration
        self.coroutine: Awaitable = coroutine
        self.args: tuple = args

class LoopTrace:
    """
    The :class:`LoopTrace` class serves as a versatile tool for testing loops of
    any type, including infinite loops. It can be effortlessly placed within
    any codebase and seamlessly integrated with all loops that call its
    :func:`evaluate_tasks()` method.

    Examples
    ----------
    >>> async def do_task(some_arg):
    ...     print(some_arg)
    ... 
    >>> task = LoopTask(at_iteration=5, coroutine=do_task, some_arg='hello')
    >>> trace = LoopTrace(tasks=[task], iteration_limit=10)
    >>> # Create an infinite loop and start the coroutine when on the 5th iteration. 
    >>> while True:
    ...     try:
    ...         await trace.evaluate_tasks()
    ...     except StopIteration:
    ...         break 
    """
    def __init__(self: "LoopTrace", tasks: list[LoopTask], iteration_limit: int = 0) -> None:
        """
        Initializes a new :class:`LoopTrace` instance.
        
        Parameters
        ----------
        tasks : :class:`List[LoopTask]`
            A list of tasks that will be evaluated on their specific iteration.
        iteration_limit : Optional[:class:`int`]
            The maximum number of iterations after which all evaluations will stop, 
            by default it is ``0`` which indicates an infinite number of iterations.
        """
        self._tasks: list[LoopTask] = tasks
        self._tasks_with_keys: dict = {task._at_iteration: task for task in self.tasks}
        self._iteration_limit: int = iteration_limit
        self._current_iteration: int = 0
    
    @property
    def tasks(self: "LoopTrace") -> list[LoopTask]:
        """
        Returns a list of all available tasks to run.

        Returns
        ----------
        :class:`List[LoopTask]` 
            The list of all tasks added to the :class:`LoopTrace`."""
        return self._tasks
    
    @property
    def tasks_with_keys(self: "LoopTrace") -> dict[int, LoopTask]:
        """
        Returns a list of all available tasks to run and their respective iteration\
        as a :class:`dict[int, LoopTask]`.

        Returns
        ----------
        :class:`dict[int, LoopTask]`
            A dictionary of tasks along with their specific iteration number.
        """
        return {task._at_iteration: task for task in self.tasks}
    
    @property
    def iteration_limit(self: "LoopTrace") -> int:
        """
        Returns the maximum limit of iterations for the current :class:`LoopTrace` instance.

        Returns
        ----------
        :class:`int`
            The maximum number of iterations after which the evaluation will stop.
        """
        return self._iteration_limit
    
    @property
    def current_iteration(self: "LoopTrace") -> int:
        """
        Returns the current loop iteration of the :class:`LoopTrace` instance.

        Returns
        ----------
        :class:`int`
            The current iteration that is being evaluated.
        """
        return self._current_iteration
    
    def add_task(self: "LoopTrace", task: LoopTask) -> bool:
        """
        Adds a new task to the already existing tasks list.

        Parameters
        ----------
        task : :class:`LoopTask`
            A task instance that needs to be added to the tasks list.

        Returns
        ----------
        :class:`bool`
            Returns ``True`` if the task was added, ``False`` otherwise.

        Raises
        ----------
        KeyError
            If the task is already present in the tasks list. 

        Examples
        ----------
        >>> def do_task(args): 
        ...    print(args)
        >>> task = LoopTask(at_iteration=5, coroutine=do_task, some_arg='hello')
        >>> trace = LoopTrace(tasks=[task])
        >>> trace.add_task(task) # Raises KeyError as the task is already present in the tasks list.
        """
        if task in self._tasks:
            raise KeyError("The provided task already exists!")
        self._tasks.append(task)
        return True
    
    def remove_task(self: "LoopTrace", task: LoopTask) -> bool:
        """
        Removes a task from the already existing tasks list.

        Parameters
        ----------
        task : :class:`LoopTask`
            The task instance that needs to be removed from the tasks list.

        Returns
        ----------
        :class:`bool`
            Returns ``True`` if the task was removed, ``False`` otherwise.

        Examples
        ----------
        >>> def do_task(args): 
        ...    print(args)
        >>> task = LoopTask(at_iteration=5, coroutine=do_task, some_arg='hello')
        >>> trace = LoopTrace(tasks=[task])
        >>> trace.remove_task(task) # Returns True as the task was removed from the tasks list.
        """
        if task in self._tasks:
            self._tasks.remove(task)
            return True
        return False
    
    async def evalutate_tasks(self: "LoopTrace") -> None:
        """
        Evaluates and executes the tasks that are supposed to be started at
        the current iteration.

        Raises
        ----------
        StopIteration
            If the iteration limit has been reached.

        Example
        ----------
        >>> def do_task(args): 
        ...    print(args)
        >>> task = LoopTask(at_iteration=5, coroutine=do_task, some_arg='hello')
        >>> trace = LoopTrace(tasks=[task], iteration_limit=10)
        >>> # Create an infinite loop and start the coroutine when on the 5th iteration.
        >>> while True:
        ...     try:
        ...         await lt.evaluate_tasks()
        ...     except StopIteration:
        ...         break 
        """
        if self._current_iteration == self.iteration_limit:
            raise StopIteration("The iteration limit has been reached!")
        task: LoopTask = self.tasks_with_keys.get(self._current_iteration, None)
        if task: await task.coroutine(*task.args)
        self._current_iteration += 1