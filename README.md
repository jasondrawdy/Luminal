![converted_img](https://github.com/jasondrawdy/Demos/assets/40871836/3b0f3f7e-70fa-4f31-933a-d1228eec1213)
# Description

Luminal offers developers the perfect solution to streamline and optimize their projects effortlessly by creating dynamic and modular plugins, a.k.a *Photons*. The library has been meticulously created based on best practices and offers a rich set of features and capabilities. 

The library is composed of 100% pure Python code with no dependencies while also using common developer libraries for tests and documentation. This means Luminal can be seamlessly integrated into *any* existing project, reduce development time, and save valuable resources. Furthermore, the library boasts 100% code statement and branch coverage with minimal `#pragma` tags. This feature ensures clean and efficient code, reducing even more development time. Not only that, but the library also includes comprehensive documentation of core features, covering private methods, metaclasses, utilities, and public-facing functions. It is the perfect solution for streamlining your projects and optimizing resources effortlessly, offering reliability, efficiency, and instant modular dynamism.

Luminal has been engineered as a dynamic and modular framework, making it portable, and easier to couple and decouple plugins, a.k.a. *Photons*. This feature expands the functionality of the library, giving developers a way to customize their solutions, improve software flexibility, and optimize required resources to scale their projects. The extensible architecture of the library allows developers to make modifications to the code quickly and easily, enabling them to tailor the library's functionality to their specific needs. Furthermore, Luminal prioritizes security, utilizing modern checksum algorithms and object caches for instance tracking, providing transparency and reliable safety.

> **_NOTE:_**
The code in this repository was written completely by a human being. 🎃

> **_IMPORTANT:_**
This repository uses up-to-date `Python` syntax (version `3.11.1`). Furthermore, the code is structured and organized to maintain good readability and clear modularity. The repository offers comprehensive unit and integration tests using coverage, which run on every push on GitHub Actions. Thank you for being amazing! 😄

## 📖 Features
- 100% pure Python code with no depenencies of *any* kind
- 100% code statement and branch coverage with minimal `#pragma` tags
- Asynchronous & multi-threaded libary allowing for efficient usage of resources
- Atomic reloading & monitoring by using the `watch_photons(path)` method
- Small footprint with optimizations for supporting various project types and sizes
- Dynamic and modular design which allows easy coupling and decoupling of plugins
- Advanced logging of operations and debugging methods to help quickly resolve issues
- Advanced error handling that gracefully provides useful information for debugging code
- Extensible at its core for developers to easily modify and alter portions of code as they see fit
- Security oriented by using modern checksum algorithms and object caches for instance tracking
- Completely documented library covering private methods, metaclasses, utils, and public facing functions
- Luminal follows established standards for plugin development to ensure interoperability with other libraries

## 🧃 Coming *Soon*
```
- Photon encapsulation using serialization
- Photon protection scanning using machine learning
- Advanced performance metrics for project optimization
- Built-in analytics and reporting capabilities to monitor usage and performance
- Improved security measures such as two-factor authentication, encryption, and hashing
```

## ⚙️ Installation
### Overview
The installation process for the Luminal libary is a straightforward process akin to most Python packages. There are also multiple way of installation offered for the libary in order to allow easier installs. Follow the steps below to get started:

#### *Packaging*
The application uses `pip` as a package manager, and all dependencies are explicitly listed in the `requirements.txt` file.

#### *Manual Install*
To install the library manually you should follow these steps:

1. Clone this repository to your local machine: `git clone https://github.com/jasondrawdy/luminal.git`
2. Create a virtual environment: `virtualenv venv && source venv/bin/activate`
3. Install the dependencies: `pip install -r requirements.txt`

Once you have the library installed you can start creating photons of any type!

#### *Automatic Install*
To install via `pip` run the following command:  
`pip install luminal` or `pip3 install luminal`

### Git branching and workflows
This repository has a main branch, which represents the the stable version of the project, and a development branch where all new features are tested before they are merged into the main branch. Pull requests should be used for any suggested changes before being merged.

## 📜 Documentation
Please visit the following webpage for this repository below in order to view comprehensive documentation on the project. A number of code examples are also available in this project repository in order to better understand how to use the library correctly.

https://luminal.readthedocs.io/en/latest/

## 🧰 Library Usage
### Unit Tests
The repository contains a multitude of test cases in `tests.py` — here's what the main code looks like:

```py
class Program: # pragma: no cover
    def __init__(self) -> None:
        self._logger = Logger(__name__)
        self._stopwatch = None

    def _spawn_sentinel(self: "Program"):
        self._logger.note("Spawning a sentinel...")
        sentinel = Sentinel()
        sentinel.authorized = True
        sentinel.start()
        time.sleep(1)
    
    def _start_tests(self: "Program"):
        if not os.path.exists(PhotonLocations.main_directory):
            raise DirectoryNotFoundError("Please make sure to create the 'demos' directory!")
        if not os.path.exists(PhotonLocations.basic_photon):
            raise FileNotFoundError("Please make sure to create a 'luminal_basic.py' file in the" +
                                    "'demos' directory which inherits from the 'IPhoton' class.")
        if not os.path.exists(PhotonLocations.advanced_photon):
            raise FileNotFoundError("Please make sure to create a 'luminal_advanced.py' file in the" +
                                    "'demos' directory which inherits from the 'IPhoton' class, " +
                                    "has another IPhoton class with relative imports n-directories down, " +
                                    "and also a normal class which is as advanced or basic to your liking.")
        unittest.main(verbosity=2)

if __name__ == "__main__": # pragma: no branch
    program = Program()
    program._spawn_sentinel()
    program._start_tests()
```
This code has quite a few elements, however, they are necessary in order to run all tests in a clean and efficient manner. A main `Program` class is constructed in order to encapsulate all of the specific operations we'll be performing during our testing sessions too. We define a `Logger(__name__)` so that way we can get feedback from any tests that call the logger's functions. Before starting any tests we spawn a `Sentinel()` in order to remove (*cleanup*) unwanted files such as cached and compiled artifacts. Finally, we start running our tests granted that the provided folders and files are available.

To run all tests there are actually a few different methods:
- Run `python tests.py`  
    - Performs all tests defined within the script, but with no coverage results other than the console output.
- Alternatively, run `coverage --branch tests.py`
    - Performs all tests and creates a report of code and branch coverage.
    - Running *`coverage html`* after the tests will generate a nice results page for user viewing.

### Photons
In the context of the Luminal framework, a photon represents a modular and extensible component that developers can use to enhance their projects. It is a specialized class that follows certain conventions and inherits from the `IPhoton` base class or its derivatives.

A photon encapsulates a specific functionality, behavior, or feature within a project. It can interact with other photons and the Luminal framework to achieve complex operations or provide additional capabilities. By adhering to the defined metadata attributes, such as `photon_name`, `photon_author`, `photon_version`, `photon_description`, and `photon_tags`, photons provide valuable information about their purpose, usage, and compatibility.

Here are some ways developers can benefit from using photons:

1. **Modularity and Reusability**
    - Photons offer a modular approach to development by encapsulating specific functionalities. Developers can easily plug in or remove photons as needed, promoting code reusability and maintaining clean project structure. With dynamic hotswapping, caching, and cryptographic verification, developers can develop more in-depth scripts and projects which can be updated on-the-fly whenever, and wherever, they want.

2. **Enhanced Functionality**
    - Photons extend the capabilities of the Luminal framework and projects by providing additional features, services, or behaviors. They can handle diverse tasks such as image processing, data manipulation, authentication, logging, and more.

3. **Framework Integration**
    - Photons seamlessly integrate into any project and make use of its features and components. This integration ensures compatibility and simplifies the usage of common functionalities, such as logging, plugin management, and event handling. Photons can also call the framework in a nested complex way.

4. **Customization and Extensibility**
    - Developers can create their own photons, tailor-made to address project-specific requirements, or extend existing photons to modify or enhance their functionality. This customization allows for a flexible and scalable approach to project development.

5. **Standardization and Consistency**
    - As photons follow a predefined set of conventions and standards, they promote consistency across projects. This standardization ensures that developers can easily understand and work with different photons within the Luminal ecosystem.

6. **Collaboration and Shared Development**
     - Leveraging photons encourages collaboration among developers working on Luminal-based projects. They can share and contribute to a growing collection of photons, benefiting from each other's expertise and leveraging existing functionality.

Overall, photons provide an organized and extensible approach to project development within the Luminal framework. They enable developers to enhance project functionality, promote modularity and code reuse, and benefit from collaboration and shared development efforts. By utilizing photons, developers can streamline their projects, focus on specific requirements, and maintain a structured and extensible codebase.

#### Creating a Photon
The following example `Photon` class is a concrete implementation of the `IPhoton` abstract base class from the Luminal framework. It represents a simple new program that greets the world when initialized. The photon defines an `__init__()` method, which is called when a new instance of Photon is created. Inside this method, the program greets the world by printing the greeting message to the console.

The photon also defines an async method named `finalize()`. This method overrides the optional finalize method from the `IPhoton` base class. The finalize method is intended to be used for cleaning up resources when the plugin or program utilizing the `Photon` object is unloaded. In this implementation, the finalize method simply prints a message indicating that the photon was absorbed, or unloaded, gracefully.

```py
from luminal.interfaces import IPhoton

class Photon(IPhoton):
    def __init__(self: "Photon"):
        """Create a simple new program to greet the world."""
        print("Hello, World!")

    async def finalize(self: "Photon") -> bool: 
        """Override the optional program finalizer to cleanup resources."""
        print("The photon was absorbed gracefully.")
```
This code demonstrates the fundamental usage of the `IPhoton` base class and the custom implementation of the `Photon` class. Notably, the `Photon` class doesn't introduce any new attributes or methods beyond what is defined in the `IPhoton` base class. Overall, this code showcases the basic implementation of a Luminal photon with a simple greeting functionality. It demonstrates the ability to define custom behavior and cleanup tasks, providing a foundation for building more complex and feature-rich Luminal photons.

#### Loading, Reloading, & Unloading a Photon
The following code demonstrates the loading, reloading, and unloading of a photon within a `Program` class. It utilizes the `Loader` class from the Luminal framework and relies on asynchronous programming using the `asyncio` module. 

##### Program Class Attributes
The `Program` class encapsulates the photon and its related operations. It has the following *attributes*:

|Attribute        |Type     |Scope    |Description |
|:----------------|:-------:|:-------:|:-----------|
|`photon`         |`str`    |Public   |*A string representing the path to the photon file to be loaded.*|
|`loader`         |`Loader` |Public   |*Responsible for managing photons which includes functionality such as loading, reloading, and unloading.*|

##### Program Class Methods
The class also defines the following *methods*:

|Method           |Scope    |Description |
|:----------------|:-------:|:-----------|
|`load`           |Public   |*An asynchronous method that loads a photon by calling the `load_photon()` method of the `Loader` instance. It then starts the photon instance by calling its start method.*|
|`reload`         |Public   |*An asynchronous method that reloads a specified photon instance. It calls the `reload_photon()` method of the `Loader` instance and then starts the photon instance again.*|
|`unload`         |Public   |*An asynchronous method that stops and unloads a specified photon. It calls the `unload_photon()` method of the `Loader` instance and prints the file's full path.*|

```py
from luminal.managers import Loader
import asyncio

class Program:
    def __init__(self: "Program") -> None:
        """Create a new program to hold a photon path and photon manager."""
        self.photon = "photon_path.py"
        self.loader = Loader(logging=True)
        
    async def load(self: "Program"):
        """Loads a photon and starts its instance."""
        photon = await self.loader.load_photon(self.photon)
        await photon.start()
    
    async def reload(self: "Program"):
        """Reloads a specified photon instance or rolls it back if unable."""
        photon = await self.loader.reload_photon(self.photon)
        await photon.start()

    async def unload(self: "Program"):
        """Stops and unloads a specified photon."""
        unloaded = await self.loader.unload_photon(self.photon)
        print(unloaded) # Prints the file's full path, a.k.a 'self.photon'.

if __name__ == "__main__":
    program = Program()
    asyncio.run(program.load())
    asyncio.run(program.reload())
    asyncio.run(program.unload())
```
In summary, this code demonstrates the basic usage of the `Loader` class to `load`, `reload`, and `unload` a Luminal photon. It initializes the `Program` class with the photon file path and a `Loader` instance. It then asynchronously loads the photon, reloads it, and finally unloads it while printing the file's full path.

#### Loading a Specific Class
In the following example, the `load_photon()` function is being called with several arguments:

- `photon_path`
    - This is the path to the photon module file that will be loaded.
- `photon_base`
    - This is an optional argument that specifies the base class for the photon modules to be loaded. In this code, the base class is *`MyClass`*.
- `other_classes`
    - This is an optional argument that specifies a list of other class names to be loaded from the photon module. In this code, *`ClassA`* and *`ClassB`* will be loaded.
- `recursive`
    - This is a boolean flag that indicates whether to search for photon modules recursively under the provided path. In this code, it is set to True, so the function will search for photon modules recursively.

Also, the `load_photon()` function returns a `list` of `Handler` objects representing the loaded photons, or an empty list if no photons are successfully loaded.

```py
photon = self.loader.load_photon(photon_path: str, 
                                 photon_base: type=MyClass,
                                 other_classes: list[str] = ['ClassA', 'ClassB'],
                                 recursive: bool = True)
```

Lastly, it's worth noting that the `load_photon()` function raises a `PhotonNotFoundError` error if the provided photon path doesn't exist or is a directory.

#### Watching & Atomic Reloading Photons
The following code demonstrates how to watch photons for changes using the `Loader` class. It initializes the `Program` class with the directory path where the photons are located and a `Loader` instance. It then asynchronously begins watching the photons and continuously checks for changes to reload them. The program can be stopped by user input, and upon stopping, all photons are unloaded.

```py
from luminal.managers import Loader
import asyncio

class Program:
    def __init__(self: "Program") -> None:
        """Create a new program to hold a photon manager and photon paths."""
        self.photons = "photons_directory"
        self.loader = Loader(logging=True)

    async def watch(self):
        """Spawns a sentinel, loads photons, and watches for changes to reload."""
        await self.loader.watch_photons(self.photons)

    async def stop(self):
        """Stops the spawned sentinel and begin unloading all photons."""
        await self.loader.stop_watching_photons(halt_threads=True)

if __name__ == "__main__":
    program = Program()
    asyncio.run(program.watch())
    while input("Press any key to exit!") != "": 
        pass
    asyncio.run(program.stop())
```
The code begins by importing the necessary modules: `Loader` from `luminal.managers.loader` and `asyncio` from standard Python. Next, a class named `Program` is defined. This class represents a program that manages watching photons and handling their reloading. The `__init__()` method initializes the program by setting the photons attribute to the directory path where the photons are located and creating an instance of the `Loader` class with logging enabled. The watch method is an asynchronous method that spawns a sentinel, loads photons using the `watch_photons()` method of the `Loader` instance, and continuously watches for changes to reload the photons.

The stop method is an asynchronous method that stops the spawned sentinel and begins unloading all photons using the `stop_watching_photons()` method of the `Loader` instance with `halt_threads=True` to ensure all threads are halted during unloading. The program then creates an instance of the `Program` class named program. The watch method of the program object is called using `asyncio.run()` to asynchronously start watching the photons.

A while loop is used to wait for user input for the program to exit; and will continue until any key is pressed. Finally, the stop method of the program object is called using `asyncio.run()` to asynchronously stop the sentinel and unload all photons.

### Other Tools & Features
#### Tracing Loops
The provided code consists of three parts. The first part includes two classes: `LoopTrace` and `LoopTask`. They are used to create a versatile tool for testing and tracing loops. The second part showcases the usage of these classes in an example. The third part defines additional tools and features used in the code.

```py
from luminal.managers import LoopTask, LoopTrace

async def do_task(some_arg):
    """A random function defined as an example."""
    print(some_arg)

def create_loop():
    """Creates an infinite loop with a trace attached to it for logging."""
    task = LoopTask(at_iteration=5, coroutine=do_task, some_arg='hello')
    trace = LoopTrace(tasks=[task], iteration_limit=10) # 0 is infinite iterations.
    while True:
        try:
            await trace.evaluate_tasks()
        except StopIteration: # Corresponds to the iteration_limit set above.
            break

create_loop()
```

##### LoopTrace:
The `LoopTrace` class serves as a tool for testing loops, including infinite loops. It can be seamlessly integrated into any codebase. The provided example demonstrates how to create a `LoopTrace` instance and evaluate tasks within an infinite loop until the iteration limit is reached. 

|Attribute            |Type     |Scope    |Description |
|:--------------------|:-------:|:-------:|:-----------|
|`tasks`              |`list`   |Public   |*A list of tasks to be evaluated at specific iterations.*|
|`tasks_with_keys`    |`dict`   |Public   |*A dictionary mapping tasks to their iterations.*|
|`iteration_limit`    |`int`    |Public   |*The maximum number of iterations.*|
|`current_iteration`  |`int`    |Public   |*The current iteration being evaluated. Raises `KeyError` if a task that already exists is added, and `StopIteration` if the maximum iteration limit is reached.*|

##### LoopTask:
This class wraps a coroutine and its arguments to be executed at a specific iteration within a loop.

|Attribute            |Type     |Scope    |Description |
|:--------------------|:-------:|:-------:|:-----------|
|`_at_iteration`      |`int`    |Internal  |*The iteration at which to raise a `StopIteration` exception to break.*|

#### Traced Thread Management
The `ThreadManager` class is designed to manage and control the execution of multiple threads in a program. It maintains a list of running and requested threads, a flag to stop all threads gracefully, and settings for running threads based on given limits.

##### ThreadManager Attributes
The `ThreadManager` has the following attributes:

|Attribute            |Type     |Scope    |Description |
|:--------------------|:-------:|:-------:|:-----------|
|`_manager_uid`       |`str`    |Internal |*A unique identifier for each instance of the `ThreadManager` class.*|
|`_running_threads`   |`dict`   |Internal |*A dictionary of currently running threads in the program, with each key representing a thread ID and each value being its respective `TracedThread` object.*|
|`_requested_threads` |`list`   |Internal |*A list of all threads waiting to be executed, represented as `TracedThread` objects.*|
|`_flag_request`      |`bool`   |Internal |*A flag used to indicate the user's request to stop all threads in the program.*|
|`_currently_watching`|`bool`   |Internal |*A flag used to indicate if the program should continuously watch and execute all threads based on the given thread limit.*|
|`_currently_running` |`bool`   |Internal |*A flag used to indicate if the program should run all threads based on the given thread limit only once.*|
|`thread_limit`       |`int`    |Public   |*The maximum number of threads that can be simultaneously running in the program.*|

##### ThreadManager Methods
The `ThreadManager` class also provides methods to manage threads, such as:

|Method           |Scope    |Description |
|:----------------|:-------:|:-----------|
|`append_thread`  |Public   |*Appends a new thread to the list of requested threads.*|
|`run`            |Public   |*Starts executing the requested threads, taking into account the given thread limit.*|
|`stop`           |Public   |*Stops all currently running or requested threads gracefully.*|

Additionally, the code provided in this example includes a function calculate, which is an example of a truly random function with no intrinsic value. This function uses a loop and sleeps for `1` second in each iteration. It continuously performs calculations on the given values of `x` and `y` and prints the updated values.

```py
from luminal.managers import TracedThread, ThreadManager
import time

def calculate(x, y):
    """A truly random function with no intrinsic value."""
    while True:
        x = x*y/2
        y = x*y/3
        time.sleep(1)
        print(f"{x}, {y}")
        return calculate(x,y)
    
def start_traced_manager():
    """Create a thread manager, append a task, and begin a traced cycle."""
    manager = ThreadManager()
    manager.append_thread(function=calculate, args=(10, 20), kwargs={})
    manager.run()
    manager.stop()

def start_traced_thread():
    """Starts an infinite loop function using a traced thread."""
    task = TracedThread(target=calculate, args=(10, 20), kwargs={})
    task.start()

start_traced_manager()
start_traced_thread()
```
The functions `start_traced_manager()` and `start_traced_thread()` demonstrate different approaches to using the `ThreadManager` class. The `start_traced_manager()` function creates an instance of `ThreadManager`, appends a task (using the `calculate(x,y)` function with `x=10` and `y=20`), and then runs the manager. The manager will start executing the task while managing the given thread limit. Finally, the manager is stopped gracefully.

On the other hand, `start_traced_thread()` directly starts an infinite loop function (*calculate*) using a `TracedThread`. This demonstrates the use of a traced thread without the involvement of the `ThreadManager` class.

Overall, this code provides flexibility for managing and controlling the execution of multiple threads in a program, allowing for efficient utilization of system resources and handling of thread limits. 

#### Sentinel & Utils
The given code is a Python program that creates and spawns a `Sentinel` object. The `Sentinel` class is a system watching mechanism used for monitoring files or collecting and cleaning garbage.

```py
from luminal.tools import Sentinel
import time

class Program:
    def __init__(self) -> None:
        """Create a new program with a logger and spawning functions."""
        self._logger = Logger(__name__)

    def spawn_sentinel(self: "Program"):
        """Create a sentinel and allow it to clean the system."""
        self._logger.note("Spawning a sentinel...")
        sentinel = Sentinel()
        sentinel.authorized = True
        sentinel.start()
        time.sleep(1) # Sleep the thread for cache cleanup.
        # Note: If whatever application you're runnning stays active
        # for more than 1 second, then the sleep call is optional.

if __name__ == "__main__":
    program = Program()
    program.spawn_sentinel()
```
The `Program` class in this code has an `__init__()` method that initializes a `Logger`; and the `spawn_sentinel()` method is responsible for creating and starting a `Sentinel` object. 

In the `spawn_sentinel()` method, a logger message is printed to indicate that a sentinel is being spawned. An instance of `Sentinel` is created and assigned to the variable sentinel. The authorized attribute of the sentinel object is set to `True` to allow the sentinel to actually monitor the system, otherwise, it would standby idle. Next, the start method of the sentinel object is called to initialize its monitoring process. 

A `time.sleep()` call is made with a duration of `1` second, which delays the program execution for cache cleanup. This is an optional step and is only necessary if the application being run remains active *for less than `1` second*. Finally, in the `if __name__ == "__main__":` block, an instance of the `Program` class is created and assigned to the variable program. The `spawn_sentinel()` method of the program object is then invoked to start the sentinel and have it monitor the system.

## 💡 Conclusion:
In today's fast-paced software development landscape, it's becoming increasingly important for developers to streamline and optimize their projects to keep up with the growing demands of users. Luminal offers developers the perfect solution to achieve this effortlessly by creating dynamic and modular plugins, a.k.a *Photons*. 

This library has been meticulously created based on best practices and is composed of 100% pure Python code with no dependencies, except for the unit testing package named *coverage*. The library's asynchronous and multi-threaded capabilities offer efficient utilization of system resources, while atomic reloading and monitoring capabilities allow hot reloading of code to improve performance, eliminate downtime, and debug errors faster. Furthermore, Luminal's small footprint technology makes it ideal for various project types and sizes. Luminal offers reliability and efficiency, with comprehensive documentation covering private methods, metaclasses, utilities, and public-facing functions, making it the perfect solution for streamlining your projects and optimizing resources.

The importance of this library cannot be understated, as it provides developers with a way to customize their solutions, improve software flexibility, and optimize required resources to scale their projects more efficiently and securely.

## 🧠 License:
Copyright © 2023 Jason Drawdy

All rights reserved.

The MIT License (MIT)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Except as contained in this notice, the name of the above copyright holder shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization.