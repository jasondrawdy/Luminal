# -*- coding: utf-8 -*-
# ########################################################################                          
# Program: Luminal
# Author: Jason Drawdy
# Version: 1.0.0
# Date: 03/16/23
# ########################################################################
# Description: 
# This module manages all thread contexts running within the program.
# ########################################################################
from ..errors.threads import (
    NoThreadsFoundError, 
    ThreadManagerAlreadyRunningError,
    ThreadLimitReachedError, 
    ThreadsAlreadyRunningError
)
from ..tools.utils import TextUtils
from typing import Any
import threading
import _thread
import time
import sys

class TracedThread(threading.Thread): # pragma: no cover
    """
    Custom thread object that can be halted using the :func:`halt()` function.

    This thread type extends the functionality of the standard :class:`threading.Thread` class to allow for the\
    thread execution to be halted using the :func:`halt()` function. Once halted, the thread will immediately stop\
    execution and expose any underlying pipes. This can be useful for debugging or other similar tasks.
    
    Important
    ----------
    This thread type is best utilized for small tasks that can be daemonized or terminated quickly.
    """
    def __init__(self: "TracedThread", *args: tuple, **keywords: dict[str, Any]):
        """
        Initializes a new instance of the :class:`TracedThread` class with optional arguments forwarded to the
        standard :class:`threading.Thread` class.

        Parameters
        ----------
        *args : :class:`tuple`
            Optional arguments that can be passed to the thread.
        **kwargs : Optional[:class:`dict[str, Any]`]
            The keyword arguments of the initialized instance used in :class:`threading.Thread`.
        """
        threading.Thread.__init__(self, *args, **keywords)
        self.halted: bool = False

    def __run(self: "TracedThread") -> None:
        """
        The control function for the :class:`TracedThread` that sets the global trace function and executes the thread's main function.

        Notes
        ----------
        - This method is used to run the code in the thread, but with a global trace function set beforehand.
        - The ``globaltrace`` attribute, set previously by the user, is set as the current trace function at runtime.
        - The previous :func:`__run_backup()` method, i.e. the original hardcoded run method, is called here to execute the\
        thread's main function.
        - The second to last line overwrites the :func:`run()` method with the original method, effectively undoing any trace\
        function set previously.
        
        """
        sys.settrace(self.globaltrace)
        self.__run_backup()
        self.run = self.__run_backup

    def start(self: "TracedThread") -> None:
        """
        Starts the thread execution by invoking the :func:`Thread.start()` method, but not before setting the appropriate run method.

        Notes
        ----------
        - This method overrides the :func:`run()` method and replaces it with the :func:`__run()` method, which sets the global trace\
        function and executes the thread's main function.
        - The original run method is saved into the ``__run_backup`` attribute before it is swapped out.
        - Finally, the :func:`threading.Thread.start()` method is called on the thread object itself to actually start the\
        execution of the code.

        """
        self.__run_backup: object = self.run
        self.run = self.__run     
        threading.Thread.start(self)

    def globaltrace(self: "TracedThread", frame: Any, event: Any, arg: Any) -> Any:
        """
        The global trace function for a ``TracedThread`` that replaces the default function.

        Parameters
        ----------
        frame : :class:`Any`
            The current thread frame.
        event : :class:`Any` 
            The event type (e.g. 'call', 'line', 'return', 'exception').
        arg : :class:`Any` 
            Event-specific arguments.

        Returns
        ----------
        Optional[:class:`self.localtrace`]
            If the event type is ``call``, ``self.localtrace`` is returned, otherwise :class:`None` is returned.

        Notes
        ----------
        - This method serves as the global trace function for the :class:`TracedThread` class.
        - If the event type is ``call``, the trace function switches to ``self.localtrace`` which handles the local\
        tracing inside the thread in a context-specific manner.
        - If another event type is detected, :class:`None` is returned as there's no further action required.

        """
        if event == 'call':
            return self.localtrace
        else:
            return None

    def localtrace(self: "TracedThread", frame, event, arg) -> Any:
        """
        Trace function for the :class:`TracedThread` class.

        Parameters
        ----------
        frame : :class:`types.FrameType`
            The current frame being executed in the thread.
        event : :class:`str`
            The event that occurred in the thread during tracing.
        arg : :class:`Any` 
            Optional argument associated with the event.

        Returns
        ----------
        Optional[:class:`Callable`]: 
            The next trace function to be called or :class:`None` to stop tracing.

        Raises
        ----------
        SystemExit: 
            If the thread is halted and the event is line, the program is forcefully terminated.

        Notes
        ----------
        - This function can be registered as a trace function on a thread using :func:`sys.settrace()`.\
        It is called every time an event is encountered in the traced thread and returns the next\
        trace function to be called. If the thread is halted and the event is line, it raises a\
        ``SystemExit`` exception to stop the thread execution.

        """
        if self.halted:
            if event == 'line':
                raise SystemExit()
        return self.localtrace

    def halt(self: "TracedThread") -> None:
        """
        Halt function for the :class:`TracedThread` class.

        Notes
        ----------
        - This function sets the ``halted`` attribute of the :class:`TracedThread` instance to ``True``, indicating that\
        the thread should be paused for debugging or other purposes. Once halted, the thread will stop\
        executing at the next available opportunity in its trace function.
        - This function is intended to be used in combination with the :func:`localtrace()` and :func:`globaltrace()` methods\
        from the ``sys`` module, where the former is registered as a trace function for a thread to halt the\
        thread at a specific point, and the latter is used to globally manipulate the trace function of\
        all threads in the running Python process.

        """
        self.halted = True

class ThreadManager: # pragma: no cover
    """
    A class for managing multiple threads in a codebase.

    This class provides functionality for managing and controlling the execution of multiple threads in a
    program. It maintains a list of running and requested threads, a flag to stop all threads gracefully,
    and settings for running threads based on given limits.
    """
    def __init__(self: "ThreadManager") -> None:
        """
        Initializes a new instance of the :class:`ThreadManager` class with default values for all attributes.
        """
        self._manager_uid: str = self._generate_uid()
        self._running_threads: dict = {}
        self._requested_threads: list = []
        self._flag_request: bool = False
        self._currently_watching: bool = False
        self._currently_running: bool = False
        self.thread_limit: int = 10

    def _generate_uid(self: "ThreadManager", delimiter: str = "-") -> str:
        """
        Generates a unique identifier for the instance of the :class:`ThreadManager` class.

        Parameters
        ----------
        delimiter : :class:`str`
            The delimiter to use for concatenating the string chunks. Defaults to the `-` character.

        Returns
        ----------
        :class:`str`: 
            A unique identifier for the :class:`ThreadManager` instance.

        Notes
        ----------
        - This function generates a unique identifier for the :class:`ThreadManager` instance, based on a randomly generated\
        alphanumeric string. However, it splits the string into six equal chunks and concatenates them with the delimiter\
        to create the final UID.
        - This function is primarily intended for internal use by the :class:`ThreadManager` class to generate a unique\
        identifier for each instance. It can be called by other methods within the class to ensure that the\
        identifier is unique and consistent for each instance.
        - Note that the delimiter argument can be customized to fit the specific needs of the program or application,\
        but it is recommended that a standard delimiter such as ``-`` or ``_`` be used to ensure portability and\
        compatibility with other systems.

        """
        cid = TextUtils().generate_cid(length=25)
        chunks, chunk_size = len(cid), int(len(cid)/6)
        chunk_list = [cid[i:i+chunk_size] for i in range(0, chunks, chunk_size)]
        return f'{delimiter}'.join(chunk_list)

    def _clean_threads(self:"ThreadManager") -> None:
        """
        Cleans up the list of running threads in the :class:`ThreadManager` instance.

        This function removes completed threads from the ``_running_threads`` collection of a :class:`ThreadManager` instance. 
        It does so by creating a copy of ``_running_threads``, looping through it to find completed threads and 
        clears them from the original dictionary.

        Notes
        ----------
        - This function is intended for internal use by the :class:`ThreadManager` class to clean up the list of running\
        threads after they have finished executing. It should be called regularly to prevent the running thread\
        list from growing too large and potentially causing memory issues.
        - The function works by creating a shallow copy of the running threads dictionary to ensure that the\
        original dictionary is not modified during iteration, which can cause unexpected behavior. If a thread\
        is found to have finished executing, it is removed from the running threads dictionary to keep the list\
        up to date.
        - Note that this function does not stop or halt any individual threads; it simply removes finished threads\
        from the list of running threads. Any necessary cleanup or stopping of threads should be handled by other\
        methods or functions within the :class:`ThreadManager` class.

        """
        if len(self._running_threads) > 0:
            shallow_running = self._running_threads.copy()
            for thread_cid, thread in shallow_running.items():
                if not thread.is_alive():
                    del self._running_threads[f"{thread_cid}"]

    def _stop_threads(self: "ThreadManager") -> None:
        """
        Stops all running threads in the :class:`ThreadManager` instance.

        This function iterates over the list of running threads in the :class:`ThreadManager` instance and stops each\
        thread using the :func:`halt()` function of the :class:`TracedThread` class. It then waits for each stopped thread to\
        complete using the :func:`join()` function before cleaning up the list of running threads.

        Important
        ----------
        Invoking the :func:`halt()` function on a :class:`TracedThread` instance may cause the thread to stop executing\
        immediately, so it should be used with caution. Additionally, any necessary cleanup or stopping of threads\
        should be handled by other methods or functions within the :class:`ThreadManager` class.

        Notes
        ----------
        - This function is intended for internal use by the :class:`ThreadManager` class to stop all running threads in\
        a program abrubtly. It should be called when the user requests to stop all threads, or when the\
        program is about to exit.
        - The function works by creating a shallow copy of the running threads dictionary to ensure that the\
        original dictionary is not modified during iteration, which can cause unexpected behavior. For each\
        running thread, the function checks if it is still alive, and if so, halts the thread using the :func:`halt()`\
        function of the :class:`TracedThread` class. It then waits for the thread to complete halting using the\
        :func:`join()` function before cleaning up the list of running threads.

        """
        if len(self._running_threads) > 0:
            shallow_running = self._running_threads.copy()
            for thread_cid, thread in shallow_running.items():
                if thread.is_alive():
                    trace: TracedThread = thread
                    trace.halt()
                    trace.join()

    def _start_threads(self: "ThreadManager", watching_threads: bool = False) -> None:
        """
        Starts threads requested in the queue for the :class:`ThreadManager` object. 

        Parameters
        ----------
        watching_threads : Optional[:class:`bool`] 
            When ``True``, the method will check every so often to see if any new threads have been appended to the queue. Defaults to ``False``.

        Raises
        ----------
        NoThreadsFoundError: 
            Raised when there are no threads ready to run in the queue.
        ThreadLimitReachedError: 
            Raised when the maximum number of threads allowed to run in the calling :class:`ThreadManager` instance has been reached.

        Notes
        ----------
        - The ``_requested_threads`` collection is used to keep track of which threads in the queue need to be executed. The method\
        checks to see if any of the requested threads can be run when the thread limit of the :class:`ThreadManager` is not exceeded. Thread limit\
        is determined by the ``thread_limit`` of the calling :class:`ThreadManager` instance. 
        - If there are no threads in the queue, a :class:`NoThreadsFoundError` is raised. If the maximum number of threads allowed to run\
        in the calling instance has been reached, a :class:`ThreadLimitReachedError` is raised. Once a thread has been started, it is added to the\
        ``_running_threads`` attribute so it can be tracked.    
        - If a thread has already been registered as running but is still in the queue, it is removed so that it doesn't get executed twice.

        """
        if len(self._requested_threads) == 0 and not watching_threads:
            raise NoThreadsFoundError("There are no threads ready in the queue that have been appended.")
        shallow_requested = self._requested_threads.copy()
        for thread_cid, thread in shallow_requested:
            if int(len(self._running_threads)) >= int(self.thread_limit):
                message = f"Thread limit of {self.thread_limit} has been reached!"
                message += f"\nRemaining threads left to start — {len(self._requested_threads)}"
                raise ThreadLimitReachedError(f"{message}")
            if self._running_threads.get(thread_cid, None) is None:
                (function, args, kwargs) = thread
                task = TracedThread(group=None, target=function, args=args, kwargs=kwargs)
                task.start()
                self._running_threads[f"{thread_cid}"] = task
                self._requested_threads.remove((thread_cid, thread))
            else: self._requested_threads.remove((thread_cid, thread))

    def append_thread(self: "ThreadManager", function: object, args: tuple = (), kwargs: dict[str, Any] = {}) -> bool:
        """
        Appends a thread to the request queue for the :class:`ThreadManager` object.

        Parameters
        ----------
        function : :class:`object` 
            The callable function to be executed.
        args : Optional[:class:`tuple`] 
            A tuple of positional arguments to be passed into the function when executed. Defaults to `()`.
        kwargs : Optional(:class:`dict[str, Any]`] 
            A dictionary of keyword arguments to be passed into the function when executed. Defaults to `{}`.

        Returns
        ----------
        :class:`bool` 
            `True` if the thread was successfully appended to the queue, `False` otherwise.

        Notes
        ----------
        - The ``_requested_threads`` collection is used to keep track of which threads can be executed when thread execution is started\
        in the :class:`ThreadManager` instance. Each thread is represented as a tuple that contains ``function``, ``args`` and ``kwargs``\
        attributes, respectively. The ``function`` is the callable object that will be executed when the thread is run, while\
        the ``args`` and ``kwargs`` are arguments that will be passed into the ``function`` once executed.
        - The method returns ``True`` if the thread was added to the queue successfully and ``False`` otherwise. An exception catch\
        is implemented in case there is an error in creating the thread. If the :func:`_generate_uid()` method raises an exception,\
        ``False`` is returned as the thread could not be added to the queue.

        """
        try:
            thread_cid = self._generate_uid()
            thread = (function, args, kwargs)
            self._requested_threads.append((thread_cid, thread))
            return True
        except: 
            return False
        
    def stop(self: "ThreadManager") -> None:
        """
        Sets the `_flag_request` attribute to ``True``, a signal that stops all running threads in the :class:`ThreadManager` object.

        Notes
        ----------
        The ``_flag_request`` attribute is a boolean flag that is used to indicate if there is a stop request from the\
        :class:`ThreadManager` object. When ``_flag_request`` is set to ``True``, all running threads are stopped. This method sets the\
        value of this attribute to ``True`` and does not return any value. Once this is done, the :func:`stop_listening()` method\
        is called by the :class:`ThreadManager` object so that all the threads that are currently running can terminate.
        """
        self._flag_request = True

    def halt(self: "ThreadManager") -> None:
        """
        Halts all running threads in the :class:`ThreadManager` object.

        Notes
        ----------
        This method is used to stop (halt) all running threads in the :class:`ThreadManager` object instance. The method achieves this\
        by calling the :func:`_stop_threads()` method of the :class:`ThreadManager` object which terminates all running threads. After this\
        method is called, the ``_running_threads`` collection of the :class:`ThreadManager` is set to an empty dictionary. The method does\
        not return anything.
        """
        self._stop_threads()

    def run(self: "ThreadManager") -> None:
        """
        Starts all threads in the queue for the :class:`ThreadManager` instance.

        Raises
        ----------
        ThreadsAlreadyRunningError
            Raised when new threads have already been started and are currently running.

        Notes
        ----------
        This method is used to start all threads that are in the ``_requested_threads`` collection of the :class:`ThreadManager` object\
        instance. The method calls the :func:`_start_threads()` function of the :class:`ThreadManager` object, and attempts to start all\
        pending threads in the queue. The function raises a :class:`ThreadsAlreadyRunningError` if new threads have already been started and\
        are currently running to avoid starting new threads on top of already running threads.
        """
        if self._currently_running:
            raise ThreadsAlreadyRunningError("The thread manager is already running new threads.")
        self._start_threads()

    def watch(self: "ThreadManager") -> None: # pragma: no cover
        """
        Starts a background thread that continuously starts all threads in the request queue for the :class:`ThreadManager` instance.

        Raises
        ----------
        ThreadManagerAlreadyRunningError
            Raised when a manager has already been spawned and is currently watching for threads to start.

        Notes
        ----------
        This method starts a parent background thread that continuously tries to start child threads that are in the ``_requested_threads``
        collection of the :class:`ThreadManager` object. The method raises a :class:`ThreadManagerAlreadyRunningError` if a manager has already 
        been spawned and is currently watching for threads to start. It avoids starting new threads on top of already running threads too.
        
        - The :func:`_watch()` function tries to start any pending threads by calling :func:`_start_threads(watching_threads=True)`.
        - If the thread limit is reached, a :class:`ThreadLimitReachedError` exception is caught and then the :func:`_clean_threads()` method\
        is called to cleanup/shutdown any inactive threads. If any other exception occurs, it will be raised except if the\
        exception message starts with ``"Thread limit"``. In this case, :func:`_clean_threads()` is called to cleanup inactive threads.
        
        In conclusion, the method adds the new thread that it starts to the ``_running_threads`` attribute of the :class:`ThreadManager` object, 
        as well as to the ``_requested_threads`` collection. The method also sets the ``_currently_watching`` flag to ``True``. This will prevent 
        subsequent calls to this method if ``_currently_watching`` is already ``True``.
        """
        def _watch():
            while not self._flag_request:
                try: self._start_threads(watching_threads=True)
                except ThreadLimitReachedError:
                    self._clean_threads()
                except Exception as error:
                    if str(error).startswith("Thread limit"):
                        self._clean_threads()
                        pass # We'll just keep running threads.
                    else: 
                        raise error
                time.sleep(1)
            self._requested_threads.clear()
            self._running_threads.clear()
        if self._currently_watching:
            raise ThreadManagerAlreadyRunningError("The thread manager is already watching for new threads.")
        _thread.start_new_thread(_watch, (), {})
        self._currently_watching = True