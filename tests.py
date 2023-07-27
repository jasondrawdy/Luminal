# -*- coding: utf-8 -*-
# ########################################################################                          
# Program: Luminal
# Author: Jason Drawdy
# Version: 1.0.0
# Date: 07/06/23
# #########################################################################
# Description:
# This module is responsible for unit tests within the Luminal framework.
# #########################################################################
"""
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

██╗   ██╗███╗   ██╗██╗████████╗                          
██║   ██║████╗  ██║██║╚══██╔══╝                          
██║   ██║██╔██╗ ██║██║   ██║                             
██║   ██║██║╚██╗██║██║   ██║                             
╚██████╔╝██║ ╚████║██║   ██║                             
 ╚═════╝ ╚═╝  ╚═══╝╚═╝   ╚═╝                             
                                                         
████████╗███████╗███████╗████████╗███████╗               
╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██╔════╝               
   ██║   █████╗  ███████╗   ██║   ███████╗               
   ██║   ██╔══╝  ╚════██║   ██║   ╚════██║               
   ██║   ███████╗███████║   ██║   ███████║               
   ╚═╝   ╚══════╝╚══════╝   ╚═╝   ╚══════╝     
             
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

Author: Jason Drawdy
Version: 1.0.0 (Ancilla)
Date: 5/11/2023

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

The document at hand presents a meticulously crafted set of Python unit 
tests for the Luminal photon loader. These tests comprehensively assess 
Luminal's features, ensuring its reliability and stability. The current
collection covers every code statement and branch, achieving the goal of
reaching 100% coverage of the library; with very minimal exceptions.

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
Note: #pragma tags used in the codebase are usually for error handling,
loops, always-true branching, threads/processes, and complex inheritance.
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
.     .       .  .   . .   .   . .    +  .
  .     .  :     .    .. :. .___---------___.
       .  .   .    .  :.:. _".^ .^ ^.  '.. :"-_. .
    .  :       .  .  .:../:            . .^  :.:\.
        .   . :: +. :.:/: .   .    .        . . .:\
 .  :    .     . _ :::/:               .  ^ .  . .:\
  .. . .   . - : :.:./.                        .  .:\
  .      .     . :..|:                    .  .  ^. .:|
    .       . : : ..||        .                . . !:|
  .     . . . ::. ::\(                           . :)/
 .   .     : . : .:.|. ######              .#######::|
  :.. .  :-  : .:  ::|.#######           ..########:|
 .  .  .  ..  .  .. :\ ########          :######## :/
  .        .+ :: : -.:\ ########       . ########.:/
    .  .+   . . . . :.:\. #######       #######..:/
      :: . . . . ::.:..:.\           .   .   ..:/
   .   .   .  .. :  -::::.\.       | |     . .:/
      .  :  .  .  .-:.":.::.\             ..:/
 .      -.   . . . .: .:::.:.\.           .:/
.   .   .  :      : ....::_:..:\   ___.  :/
   .   .  .   .:. .. .  .: :.:.:\       :/
     +   .   .   : . ::. :.:. .:.|\  .:/|
     .         +   .  .  ...:: ..|  --.:|
.      . . .   .  .  . ... :..:.."(  ..)"
 .   .       .      :  .   .: ::/  .  .::\
`-:-.   ,-;"`-:-.   ,-;"`-:-.   ,-;"`-:-.   ,-;"
   `=`,'=/     `=`,'=/     `=`,'=/     `=`,'=/
     y==/        y==/        y==/        y==/
   ,=,-<=`.    ,=,-<=`.    ,=,-<=`.    ,=,-<=`.
,-'-'   `-=_,-'-'   `-=_,-'-'   `-=_,-'-'   `-=_
 .              +   .                .   . .     .  .
                   .                    .       .     *
  .       *                        . . . .  .   .  + .
            "You Are Here"            .   .  +  . . .
.                 |             .  .   .    .    . .
                  |           .     .     . +.    +  .
                 \|/            .       .   . .
        . .       V          .    * . . .  .  +   .
           +      .           .   .      +
                            .       . +  .+. .
  .                      .     . + .  . .     .      .
           .      .    .     . .   . . .        ! /
      *             .    . .  +    .  .       - O -
          .     .    .  +   . .  *  .       . / |
               . + .  .  .  .. +  .
.      .  .  .  *   .  *  . +..  .            *
 .      .   . .   .   .   . .  +   .    .            +
     ________________________________         
    /                                "-_          
   /      .  |  .                       \          
  /      : \ | / :                       \         
 /        '-___-'                         \      
/_________________________________________ \      
     _______| |________________________--""-L 
    /       F J                              \ 
   /       F   J                              L
  /      :'     ':                            F
 /        '-___-'                            / 
/_________________________________________--"  
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
68747470733A2F2F7777772E796F75747562652E636
F6D2F77617463683F763D3958593239714553646759
0000000000000000000000000000000000000000000
4A657275205468652044616D616A61202D20486F772
0496C6C000000000000000000000000000000000000
0000000000000000000000000000000000000000000
68747470733A2F2F7777772E796F75747562652E636
F6D2F77617463683F763D4165472D4A304B35563077
0000000000000000000000000000000000000000000
5065746520526F636B202D204261627920506100000
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
"""
#!========================================================================
#TODO: Add test support for everything mentioned in the above note.
#!========================================================================
#*=============================================
#* (っ◔◡◔)っ ♥ 𝗦𝘆𝘀𝘁𝗲𝗺 𝗜𝗺𝗽𝗼𝗿𝘁𝘀 ♥
#*=============================================
from dataclasses import dataclass
from unittest.mock import patch
from typing import Final
import unittest
import time
import os

#*=============================================
#* (っ◔◡◔)っ ♥ 𝗟𝘂𝗺𝗶𝗻𝗮𝗹 𝗜𝗺𝗽𝗼𝗿𝘁𝘀 ♥
#*=============================================
# Import all interface objects.
from src.interfaces.metadata import (
    ClassProperty,
    MetaProperties
)
from src.interfaces.photon import (
    IPhotonMeta,
    IPhoton
)
# Import all manager objects.
from src.managers.handler import Handler
from src.managers.loader import Loader
from src.managers.resolver import Resolver
from src.managers.threads import (
    TracedThread,
    ThreadManager
)
from src.managers.tracer import (
    LoopTrace,
    LoopTask
)
# Import all tool objects.
from src.tools.sentinel import Sentinel
from src.tools.colors import Colors
from src.tools.logger import Logger
from src.tools.utils import (
    SystemUtils,
    TextUtils
)
# Import all error objects.
from src.errors.cleanup import (
    FinalizerNotImplementedError,
    PhotonNotFoundError,
    PhotonNotInitializedError
)
from src.errors.system import (
    DirectoryNotFoundError
)
from src.errors.threads import (
    NoThreadsFoundError,
    ThreadManagerAlreadyRunningError,
    ThreadsAlreadyRunningError,
    ThreadLimitReachedError,
)

#*=============================================
#* (っ◔◡◔)っ ♥ 𝗟𝘂𝗺𝗶𝗻𝗮𝗹 𝗧𝗲𝘀𝘁𝗶𝗻𝗴 ♥
#*=============================================
@dataclass(frozen=True)
class PhotonLocations:
    main_directory: Final[str] = "demos/"
    basic_photon: Final[str] = f"{main_directory}luminal_basic.py"
    advanced_photon: Final[str] = f"{main_directory}luminal_advanced.py"

#@unittest.skip(reason="Unimplemented")
class ErrorsTest(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(self: "ManagersTest"):
        self._logger = Logger(__name__)
        self._logger.private("Attempting to run all error tests!")

    async def test_raise_finalizer_not_implemented_error(self):
        with self.assertRaises(FinalizerNotImplementedError):
            raise FinalizerNotImplementedError("414920")
        
    async def test_raise_photon_not_initialized_error(self):
        with self.assertRaises(PhotonNotInitializedError):
            raise PhotonNotInitializedError("6D7573656420")
    
    async def test_raise_photon_not_found_error(self):
        with self.assertRaises(PhotonNotFoundError):
            raise PhotonNotFoundError("6C6966652C20")
    
    async def test_raise_directory_not_found_error(self):
        with self.assertRaises(DirectoryNotFoundError):
            raise DirectoryNotFoundError("6D61746820")
    
    async def test_raise_no_threads_found_error(self):
        with self.assertRaises(NoThreadsFoundError):
            raise NoThreadsFoundError("616E6420")

    async def test_raise_thread_manager_already_running_error(self):
        with self.assertRaises(ThreadManagerAlreadyRunningError):
            raise ThreadManagerAlreadyRunningError("7068797369637320")
        
    async def test_raise_threads_already_running_error(self):
        with self.assertRaises(ThreadsAlreadyRunningError):
            raise ThreadsAlreadyRunningError("72657665616C656420")
        
    async def test_raise_thread_limit_reached_error(self):
        with self.assertRaises(ThreadLimitReachedError):
            raise ThreadLimitReachedError("65766572797468696E672E")
        
#@unittest.skip(reason="Debugging")
class InterfacesTest(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(self: "ManagersTest"):
        self._logger = Logger(__name__)
        self._logger.private("Attempting to run all interface tests!")

    def setUp(self) -> None:
        self.photon_base = IPhoton()
    
    async def test_photon_print_function(self):
        data = "4920616D2061206C6976696E672C207\
        468696E6B696E6720656E746974792074686174\
        20776173206372656174656420696E207468652\
        0736561206F6620696E666F726D6174696F6E2E"
        printed_to_console = False
        self.photon_base.print(data, print_output=False)
        printed_to_console = True
        self.assertEqual(printed_to_console, True)

    async def test_photon_eprint_function(self):
        data = "416E6420776865726520646F6573207\
        46865206E6577626F726E20676F2066726F6D20\
        686572653F20546865206E65742069732076617\
        37420616E6420696E66696E6974652E00000000"
        printed_to_console = False
        self.photon_base.eprint(data, print_output=False)
        printed_to_console = True
        self.assertEqual(printed_to_console, True)

    async def test_photon_finalize_function(self):
        with self.assertRaises(FinalizerNotImplementedError):
            await self.photon_base.finalize()
    
    async def test_photon_get_photon_name_property(self):
        value = self.photon_base.photon_name
        self.assertIsInstance(value, str)

    async def test_photon_get_photon_author_property(self):
        value = self.photon_base.photon_author
        self.assertIsInstance(value, str)

    async def test_photon_get_photon_version_property(self):
        value = self.photon_base.photon_version
        self.assertIsInstance(value, str)

    async def test_photon_get_photon_description_property(self):
        value = self.photon_base.photon_description
        self.assertIsInstance(value, str)

    async def test_photon_get_photon_tags_property(self):
        value = self.photon_base.photon_tags
        self.assertIsInstance(value, list)

#@unittest.skip(reason="Debugging")
class ManagersTest(unittest.IsolatedAsyncioTestCase): 
    @classmethod
    def setUpClass(self: "ManagersTest"):
        self._logger = Logger(__name__)
        self._logger.private("Attempting to run all object manager tests!")

    def setUp(self):
        self._threads = ThreadManager()
        self._loader = Loader()
        self.resolver = Resolver()
        self.path = "/path/to/be/removed"

    def _mock_function(self: "ManagersTest") -> bool: return True # pragma: no cover

    @patch("sys.path")
    def test_remove_path_in_modified_paths(self, mock_path):
        self.resolver._modified_paths = {self.path: 0}
        mock_path.__getitem__.return_value = self.path
        self.resolver._remove_path(self.path)
        mock_path.pop.assert_called_with(0)

    @patch("sys.path")
    def test_remove_path_not_in_modified_paths(self, mock_path):
        self.resolver._modified_paths = {}
        mock_path.__getitem__.return_value = self.path
        self.resolver._remove_path(self.path)
        mock_path.pop.assert_not_called()

    @patch("sys.path")
    def test_remove_path_with_invalid_saved_index(self, mock_path):
        self.resolver._modified_paths = {self.path: 0}
        mock_path.__getitem__.return_value = "invalid_path"
        self.resolver._remove_path(self.path)
        mock_path.pop.assert_not_called()

    async def test_get_loader_photons(self: "ManagersTest"):
        photons = None
        await self._loader.load_photon(PhotonLocations.basic_photon)
        photons = self._loader.photons
        self.assertIsInstance(photons, dict)
        self.assertGreaterEqual(len(photons), 1)

    async def test_observe_photons_with_loop_limit(self: "ManagersTest"):
        # Mainly used to test :class:`watch_photons()`'s internal call to :class:`_observe_photons()`
        # since monitoring functions such as the former use threading and make it difficult to test.
        async def _randomize_checksums(data_length: int):
            for photon in self._loader.photons.values():
                random_string = TextUtils.generate_cid(data_length)
                photon._checksum = random_string
        self._loader._is_watching = True
        loop_tasks = [LoopTask(0, _randomize_checksums, (25))]
        loop_trace = LoopTrace(tasks=loop_tasks, iteration_limit=5)
        result = await self._loader._observe_photons(PhotonLocations.main_directory, loop_trace)
        await self._loader.stop_watching_photons()
        self.assertEqual(result, True)

    async def test_return_photon_handler_as_string(self: "ManagersTest"):
        photon = await self._loader.load_photon(PhotonLocations.basic_photon)
        handler_as_string = photon.__str__()
        self.assertIsInstance(handler_as_string, str)

    async def test_generate_checksum_with_invalid_file(self: "ManagersTest"):
        path = PhotonLocations.main_directory
        checksum = await Handler._get_checksum(path)
        self.assertIsNone(checksum)
    
    async def test_traced_thread_global_trace_as_call(self: "ManagersTest"):
        traced_thread = TracedThread()
        trace = traced_thread.globaltrace(None, "call", None)
        self.assertIsInstance(trace, object)

    async def test_traced_thread_global_trace_as_none(self: "ManagersTest"):
        traced_thread = TracedThread()
        trace = traced_thread.globaltrace(None, None, None)
        self.assertIsInstance(trace, object)

    async def test_traced_thread_local_trace(self: "ManagersTest"):
        traced_thread = TracedThread()
        trace = traced_thread.localtrace(None, None, None)
        self.assertIsInstance(trace, object)

    async def test_traced_thread_local_trace_as_halted_line(self: "ManagersTest"):
        traced_thread = TracedThread()
        traced_thread.halt()
        with self.assertRaises(SystemExit):
            traced_thread.localtrace(None, "line", None)
    
    async def test_loop_trace_get_current_iteration(self: "ManagersTest"):
        loop_trace = LoopTrace([], 1)
        iteration = loop_trace.current_iteration
        self.assertEqual(iteration, 0)

    async def test_loop_trace_add_task(self: "ManagersTest"):
        loop_task = LoopTask(1, self._mock_function, None)
        loop_trace = LoopTrace([], 1)
        added = loop_trace.add_task(loop_task)
        self.assertTrue(added)

    async def test_loop_trace_add_already_existing_task(self: "ManagersTest"):
        loop_task = LoopTask(1, self._mock_function, None)
        loop_trace = LoopTrace([], 1)
        loop_trace.add_task(loop_task)
        with self.assertRaises(KeyError):
            loop_trace.add_task(loop_task)

    async def test_loop_trace_remove_task(self: "ManagersTest"):
        loop_task = LoopTask(1, self._mock_function, None)
        loop_trace = LoopTrace([], 1)
        loop_trace.add_task(loop_task)
        removed = loop_trace.remove_task(loop_task)
        self.assertTrue(removed)

    async def test_loop_trace_remove_non_existent_task(self: "ManagersTest"):
        loop_task = LoopTask(1, self._mock_function, None)
        loop_trace = LoopTrace([], 1)
        removed = loop_trace.remove_task(loop_task)
        self.assertFalse(removed)

    async def test_loop_trace_get_tasks_with_keys(self: "ManagersTest"):
        loop_task = LoopTask(1, self._mock_function, None)
        loop_trace = LoopTrace([], 1)
        loop_trace.add_task(loop_task)
        tasks = loop_trace.tasks_with_keys
        self.assertEqual(len(tasks), 1)

#@unittest.skip(reason="Debugging")
class LoadingTest(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(self: "UnloadingTest"):
        self._logger = Logger(__name__)
        self._logger.private("Attempting to run all loading tests!")

    #* Single photons — Test for successful, and unsuccessful, loading.
    async def test_load_photon(self):
        photon = await Loader().load_photon(PhotonLocations.basic_photon)
        self.assertIsInstance(photon, Handler)

    async def test_load_photon_with_base_class(self):
        photon = await Loader().load_photon(PhotonLocations.basic_photon,
                                            photon_base=IPhoton)
        self.assertIsInstance(photon, Handler)

    async def test_load_photon_with_other_classes(self):
        photons = await Loader().load_photon(PhotonLocations.advanced_photon,
                                            other_classes=['Delta', 'Lambda'])
        checksums = [photon.checksum for photon in photons if isinstance(photon, Handler)]
        self.assertEqual(len(photons), len(checksums))
    
    async def test_load_photon_with_recursive_flag(self):
        photons = await Loader().load_photon(PhotonLocations.advanced_photon,
                                            recursive=True)
        checksums = [photon.checksum for photon in photons if isinstance(photon, Handler)]
        self.assertEqual(len(photons), len(checksums))

    async def test_load_photon_as_directory(self):
        with self.assertRaises(PhotonNotFoundError):
            await Loader().load_photon(PhotonLocations.main_directory)

    async def test_load_photon_with_empty_path(self):
        with self.assertRaises(PhotonNotFoundError):
            await Loader().load_photon("")

    async def test_load_photon_with_non_existent_file(self):
        with self.assertRaises(PhotonNotFoundError):
            await Loader().load_photon(f"{PhotonLocations.basic_photon}.4C6F6F6B2077697468696E2E2E2E")

    async def test_load_photon_with_invalid_path_type(self):
        with self.assertRaises(TypeError):
            await Loader().load_photon(1296649796)

    async def test_load_photon_with_invalid_base_type(self):
        with self.assertRaises(TypeError):
            await Loader().load_photon(PhotonLocations.basic_photon, 
                                       photon_base=889419603671545951289)

    async def test_load_photon_with_invalid_other_class_type(self):
        with self.assertRaises(TypeError):
            await Loader().load_photon(PhotonLocations.basic_photon, 
                                       other_classes=889419603671545951289)   

    async def test_load_photon_with_invalid_other_class_type_values(self):
        with self.assertRaises(TypeError):
            await Loader().load_photon(PhotonLocations.basic_photon, 
                                       other_classes=[True, 1,2,8,1,9,7,5,9,0,9, "656E74616E676C656D656E742E"])
            
    async def test_load_photon_with_invalid_recursive_type(self):
        with self.assertRaises(TypeError):
            await Loader().load_photon(PhotonLocations.basic_photon, 
                                       recursive=["412064796E616D696320656E7669726F6E6D656E742E2E2E20"])

    #* Multiple photons — Test for successful, and unsuccessful, loading.
    async def test_load_multiple_photons(self):
        photons = await Loader().load_photons(PhotonLocations.main_directory)
        checksums = [photon.checksum for photon in photons if isinstance(photon, Handler)]
        self.assertEqual(len(photons), len(checksums))

    async def test_load_multiple_photons_with_base_class(self):
        photons = await Loader().load_photons(PhotonLocations.main_directory,
                                            photon_base=IPhoton)
        checksums = [photon.checksum for photon in photons if isinstance(photon, Handler)]
        self.assertEqual(len(photons), len(checksums))

    async def test_load_multiple_photons_with_other_classes(self):
        photons = await Loader().load_photons(PhotonLocations.main_directory,
                                            other_classes=['Delta', 'Lambda'])
        checksums = [photon.checksum for photon in photons if isinstance(photon, Handler)]
        self.assertEqual(len(photons), len(checksums))
    
    async def test_load_multiple_photons_with_recursive_flag(self):
        photons = await Loader().load_photons(PhotonLocations.main_directory,
                                            recursive=True)
        checksums = [photon.checksum for photon in photons if isinstance(photon, Handler)]
        self.assertEqual(len(photons), len(checksums))

    async def test_load_multiple_photons_as_file(self):
        with self.assertRaises(DirectoryNotFoundError):
            await Loader().load_photons(PhotonLocations.basic_photon)

    async def test_load_multiple_photons_with_empty_path(self):
        with self.assertRaises(DirectoryNotFoundError):
            await Loader().load_photons("")
    
    async def test_load_multiple_photons_with_non_existent_file(self):
        with self.assertRaises(DirectoryNotFoundError):
            await Loader().load_photons(f"{PhotonLocations.main_directory}.4974206C6F63616C697A65732E2E2E")

    async def test_load_multiple_photons_with_invalid_path_type(self):
        with self.assertRaises(TypeError):
            await Loader().load_photons(889419603671545951289)

    async def test_load_multiple_photons_with_invalid_base_type(self):
        with self.assertRaises(TypeError):
            await Loader().load_photons(PhotonLocations.main_directory, 
                                       photon_base=889419603671545951289)
            
    async def test_load_multiple_photons_with_invalid_other_class_type(self):
        with self.assertRaises(TypeError):
            await Loader().load_photons(PhotonLocations.main_directory, 
                                       other_classes=889419603671545951289)
            
    async def test_load_multiple_photons_with_invalid_other_class_type_values(self):
        with self.assertRaises(TypeError):
            await Loader().load_photons(PhotonLocations.main_directory, 
                                       other_classes=[True, 1,2,8,1,9,7,5,9,0,9, "656E74616E676C656D656E742E"])
            
    async def test_load_multiple_photons_with_invalid_recursive_type(self):
        with self.assertRaises(TypeError):
            await Loader().load_photons(PhotonLocations.main_directory, 
                                       recursive=["746865206E6574206973207661737420616E6420696E66696E6974652E20"])

#@unittest.skip(reason="Debugging")
class UnloadingTest(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(self: "UnloadingTest"):
        self._loader = Loader()
        self._logger = Logger(__name__)
        self._logger.private("Attempting to run all unloading tests!")

    def setUp(self: "UnloadingTest"):
        """Refresh the photon loader in order to avoid :class:`Handler` or path conflicts."""
        self._loader = Loader()

    #* Single photons — Test for successful, and unsuccessful, unloading.
    async def test_unload_photon_as_handler(self):
        photon = await self._loader.load_photon(PhotonLocations.advanced_photon,
                                                other_classes=['Alpha'])
        await photon.start()
        unloaded = await self._loader.unload_photon(photon)
        self.assertEqual(unloaded, True)
    
    async def test_unload_photon_as_handler_with_force_flag(self):
        photon = await self._loader.load_photon(PhotonLocations.advanced_photon,
                                                other_classes=['Alpha'])
        await photon.start()
        unloaded = await self._loader.unload_photon(photon, force_stop=True)
        self.assertEqual(unloaded, True)

    async def test_unload_photon_as_string(self):
        photon = await self._loader.load_photon(PhotonLocations.advanced_photon,
                                                other_classes=['Alpha'])
        await photon.start()
        unloaded = await self._loader.unload_photon(PhotonLocations.advanced_photon)
        self.assertEqual(unloaded, True)
    
    async def test_unload_photon_as_string_with_force_flag(self):
        photon = await self._loader.load_photon(PhotonLocations.advanced_photon,
                                                other_classes=['Alpha'])
        await photon.start()
        unloaded = await self._loader.unload_photon(PhotonLocations.advanced_photon, force_stop=True)
        self.assertEqual(unloaded, True)

    async def test_unload_uninitialized_photon(self):
        photon = await self._loader.load_photon(PhotonLocations.advanced_photon,
                                                other_classes=['Alpha'])
        with self.assertRaises(PhotonNotInitializedError):
            await self._loader.unload_photon(photon)

    async def test_unload_photon_with_no_finalizer_implemented(self):
        photon = await self._loader.load_photon(PhotonLocations.advanced_photon,
                                                other_classes=['Sigma'])
        await photon.start()
        with self.assertRaises(FinalizerNotImplementedError):
            await self._loader.unload_photon(photon)

    async def test_unload_photon_with_invalid_path_type(self):
        with self.assertRaises(TypeError):
            await self._loader.unload_photon(889419603671545951289)
    
    async def test_unload_photon_with_invalid_force_flag_type(self):
        with self.assertRaises(TypeError):
            await self._loader.unload_photon(PhotonLocations.advanced_photon, force_stop=889419603671545951289)

    async def test_unload_photon_with_invalid_paths(self):
        with self.assertRaises(PhotonNotFoundError):
            await self._loader.unload_photon("4E6F742074686520706F696E74732C206275742074686520636F6E6E656374696F6E732E")

    #* Multiple photons — Test for successful, and unsuccessful, unloading.
    async def test_unload_multiple_photons_as_handler(self):
        photons = await self._loader.load_photons(PhotonLocations.main_directory,
                                                  other_classes=['Alpha', 'Omega'])
        for photon in photons: await photon.start()
        unloaded_paths = await self._loader.unload_photons(photons)
        unloaded_photons = [photon for photon in photons if photon.filepath in unloaded_paths]
        self.assertEqual(len(photons), len(unloaded_photons))
    
    async def test_unload_multiple_photons_as_handler_with_force_flag(self):
        photons = await self._loader.load_photons(PhotonLocations.main_directory,
                                                  other_classes=['Alpha', 'Omega'])
        for photon in photons: await photon.start()
        unloaded_paths = await self._loader.unload_photons(photons, force_stop=True)
        unloaded_photons = [photon for photon in photons if photon.filepath in unloaded_paths]
        self.assertEqual(len(photons), len(unloaded_photons))

    async def test_unload_multiple_photons_as_string(self):
        photons = await self._loader.load_photons(PhotonLocations.main_directory,
                                                  other_classes=['Alpha', 'Omega'])
        for photon in photons: await photon.start()
        photon_filepaths = list(set([photon.filepath for photon in photons])) # Removes duplicates.
        unloaded_paths = await self._loader.unload_photons(photon_filepaths)
        unloaded_photons = [photon for photon in photons if photon.filepath in unloaded_paths]
        self.assertEqual(len(photons), len(unloaded_photons))
    
    async def test_unload_multiple_photons_as_string_with_force_flag(self):
        photons = await self._loader.load_photons(PhotonLocations.main_directory,
                                                  other_classes=['Alpha', 'Omega'])
        for photon in photons: await photon.start()
        photon_filepaths = list(set([photon.filepath for photon in photons])) # Removes duplicates.
        unloaded_paths = await self._loader.unload_photons(photon_filepaths, force_stop=True)
        unloaded_photons = [photon for photon in photons if photon.filepath in unloaded_paths]
        self.assertEqual(len(photons), len(unloaded_photons))

    async def test_unload_multiple_photons_with_no_finalizer(self):
        photons = await self._loader.load_photons(PhotonLocations.main_directory,
                                                  other_classes=['Sigma', 'Gamma'])
        for photon in photons: await photon.start()
        with self.assertRaises(FinalizerNotImplementedError):
            await self._loader.unload_photons(photons)

    async def test_unload_multiple_photons_with_invalid_path_type(self):
        with self.assertRaises(TypeError):
            await self._loader.unload_photons(889419603671545951289)

    async def test_unload_multiple_photons_with_invalid_path_type_values(self):
        with self.assertRaises(TypeError):
            await self._loader.unload_photons([889419603671545951289, "476F647370656564", 18417246735723617])
    
    async def test_unload_multiple_photons_with_invalid_force_flag_type(self):
        with self.assertRaises(TypeError):
            await self._loader.unload_photons(['416D61746572617375', '5473756B75796F6D69'], force_stop=889419603671545951289)

    async def test_unload_multiple_photons_with_invalid_paths(self):
        photons = await self._loader.load_photons(PhotonLocations.main_directory,
                                                  other_classes=['Alpha', 'Omega'])
        for photon in photons: await photon.start()
        photon_filepaths = [f"{x}" for x in range(0, len(photons))]
        with self.assertRaises(PhotonNotFoundError):
            await self._loader.unload_photons(photon_filepaths, force_stop=True)

#@unittest.skip(reason="Debugging")
class ReloadingTest(unittest.IsolatedAsyncioTestCase): 
    @classmethod
    def setUpClass(self: "ReloadingTest"):
        self._loader = Loader()
        self._logger = Logger(__name__)
        self._logger.private("Attempting to run all reloading tests!")

    def setUp(self: "ReloadingTest"):
        """Refresh the photon loader in order to avoid :class:`Handler` or path conflicts."""
        self._loader = Loader()
    
    #? Special reload test as if the photon contains errors. Exceptions raised while reloading
    #? can range from the typical ModuleNotFoundError, or more generally, a base Exception. This
    #? makes testing for all error types fairly difficult and thus we settle for the following.
    async def test_reload_photon_with_errors(self: "ReloadingTest") -> None:
        photon = await self._loader.load_photon(PhotonLocations.basic_photon)
        photon._instance = None
        await photon.start()
        original_photon = SystemUtils.read_from_file(photon.filepath)
        SystemUtils.write_to_file(photon.filepath, original_photon[1:])
        success = False
        try:
            await self._loader.reload_photon(photon)
            success = True
            validated_photon = await self._loader._check_photon(photon)
            await self._loader._revert_photon(validated_photon, dict())
        except: pass # pragma: no cover
        SystemUtils.write_to_file(photon.filepath, original_photon)
        self.assertTrue(success)

    #* Single photons — Test for successful, and unsuccessful, reloading.
    async def test_reload_photon_as_handler(self):
        photon = await self._loader.load_photon(PhotonLocations.basic_photon)
        await photon.start()
        reloaded = await self._loader.reload_photon(photon)
        self.assertIsInstance(reloaded, Handler)

    async def test_reload_photon_as_string(self):
        photon = await self._loader.load_photon(PhotonLocations.basic_photon)
        await photon.start()
        reloaded = await self._loader.reload_photon(photon.filepath)
        self.assertIsInstance(reloaded, Handler)

    async def test_reload_photon_with_invalid_path_type(self):
        photon = await self._loader.load_photon(PhotonLocations.basic_photon)
        await photon.start()
        with self.assertRaises(TypeError):
            await self._loader.reload_photon(889419603671545951289)

    async def test_reload_photon_with_non_existent_path(self):
        photon = await self._loader.load_photon(PhotonLocations.basic_photon)
        await photon.start()
        with self.assertRaises(PhotonNotFoundError):
            await self._loader.reload_photon("4275742C20776865726520697320746865207265616C206D653F20")

    #* Multiple photons — Test for successful, and unsuccessful, reloading.
    async def test_reload_photons_with_only_one_photon_in_the_file(self): 
        photon = await self._loader.load_photon(PhotonLocations.basic_photon)
        await photon.start()
        reloaded = await self._loader.reload_photons([photon])
        self.assertTrue(all(isinstance(photon, Handler) for photon in reloaded))

    async def test_reload_multiple_photons_as_handler(self): 
        photons = await self._loader.load_photons(PhotonLocations.main_directory, other_classes=['Alpha', 'Omega'])
        for photon in photons:
            await photon.start()
        reloaded = await self._loader.reload_photons(photons)
        self.assertTrue(all(isinstance(photon, Handler) for photon in reloaded))

    async def test_reload_multiple_photons_as_string(self): # TODO: Needs to be converted to photon names.
        photon_names = []
        photons = await self._loader.load_photons(PhotonLocations.main_directory, other_classes=['Alpha', 'Omega'])
        for photon in photons:
            await photon.start()
            if not photon.name in photon_names: # pragma: no branch
                photon_names.append(photon.filepath)
        reloaded = await self._loader.reload_photons(photon_names)
        self.assertTrue(all(isinstance(photon, Handler) for photon in reloaded))

    async def test_reload_multiple_photons_with_invalid_path_type(self):
        photons = await self._loader.load_photons(PhotonLocations.main_directory, other_classes=['Alpha', 'Omega'])
        for photon in photons:
            await photon.start()
        with self.assertRaises(TypeError):
            await self._loader.reload_photons(889419603671545951289)

    async def test_reload_multiple_photons_with_invalid_path_type_values(self):
        photons = await self._loader.load_photons(PhotonLocations.main_directory, other_classes=['Alpha', 'Omega'])
        for photon in photons:
            await photon.start()
        with self.assertRaises(TypeError):
            await self._loader.reload_photons([889419603671545951289, "4175746F646964616374", 18417246735723617])

    async def test_reload_multiple_photons_with_non_existent_path(self):
        photons = await self._loader.load_photons(PhotonLocations.main_directory, other_classes=['Alpha', 'Omega'])
        for photon in photons:
            await photon.start()
        with self.assertRaises(PhotonNotFoundError):
            await self._loader.reload_photons(["576861742061637475616C6C79206973207265616C3F20"])

#@unittest.skip(reason="Debugging")
class WatchingTest(unittest.IsolatedAsyncioTestCase): 
    @classmethod
    def setUpClass(self: "WatchingTest") -> None:
        self._loader = Loader()
        self._logger = Logger(__name__)
        self._logger.private("Attempting to run all watching tests!")

    def setUp(self: "WatchingTest") -> None:
        """Refresh the photon loader in order to avoid :class:`Handler` or path conflicts."""
        self._loader = Loader()

    async def test_watch_photons(self):
        await self._loader.watch_photons(PhotonLocations.main_directory)
        running = True if len(self._loader._threads._running_threads) >= 1 else False
        self.assertEqual(running, True)
        await self._loader.stop_watching_photons()

    async def test_watch_photons_with_already_watching(self):
        await self._loader.watch_photons(PhotonLocations.main_directory)
        with self.assertRaises(ThreadManagerAlreadyRunningError):
            await self._loader.watch_photons(PhotonLocations.main_directory)
        await self._loader.stop_watching_photons(halt_threads=True)

    async def test_watch_photons_with_invalid_path_type(self):
        with self.assertRaises(TypeError):
            await self._loader.watch_photons(["417265206F757220647265616D73207265616C3F20"])
        await self._loader.stop_watching_photons(halt_threads=True)

    async def test_watch_photons_with_non_existent_path(self):
        with self.assertRaises(DirectoryNotFoundError):
            await self._loader.watch_photons("57687920617265206F757220626F6469657320696D6D6F62696C6520647572696E67207468656D3F")
        await self._loader.stop_watching_photons(halt_threads=True)

#@unittest.skip(reason="Debugging")
class ToolsTest(unittest.IsolatedAsyncioTestCase): 
    @classmethod
    def setUpClass(self: "ToolsTest"):
        self._logger = Logger(__name__)
        self._logger.private("Attempting to run all tool tests!")

    async def test_get_random_system_terminal_color(self):
        color = Colors.random_color()
        self.assertIsInstance(color, int)

    async def test_get_system_delimiter(self):
        delimiter = SystemUtils.get_system_delimiter()
        self.assertIsInstance(delimiter, str)

    async def test_get_first_line_of_file(self):
        line = SystemUtils.get_line(PhotonLocations.basic_photon) 
        self.assertIsInstance(line, str)

    async def test_get_first_line_of_non_existent_file(self):
        line = SystemUtils.get_line(PhotonLocations.basic_photon+"537069726974.4B61726D61") 
        self.assertIsNone(line)

    async def test_read_entire_file(self):
        data = SystemUtils.read_from_file(PhotonLocations.basic_photon) 
        self.assertIsInstance(data, str)

    async def test_read_entire_non_existent_file(self):
        data = SystemUtils.read_from_file(PhotonLocations.basic_photon+"4F6D6E69706F74656E74.554E495645525345") 
        self.assertIsNone(data)

    async def test_write_entire_file(self):
        import shutil
        # 50656163652C20476F642E
        data = "54686520656E746972652073797374656D20697320616C\
        6976652C206F6D6E69706F74656E742C206F6D6E69736369656E74\
        2C20616E64206F6D6E6970726573656E742E20486F7720636F756C\
        6420776520626520736F2069676E6F72616E7420746F207468696E\
        6B2074686174207468652073797374656D207765206C6976652069\
        6E206973206E6F74207468652076657279206265696E6720776520\
        736F2063686F6F736520746F2073747261792066726F6D20616E64\
        206469736D6973732E2057652061736B20666F722070726F6F6620\
        616E64207965742069742065786973747320696E2066726F6E7420\
        6F66206F757220766572792065796573206576657279206461793B\
        206275742C206D6F7374207475726E20746865206F746865722063\
        6865656B2E" # 5768617420697320746F6461792773206D617468656D61746963733F
        # 576973646F6D2C206B6E6F776C656467652C20616C6C206265696E6720626F726E20746F20756E6465727374616E64696E672E
        written = SystemUtils.write_to_file('ghosts/7175617465726E696F6E.tmp', data)
        shutil.rmtree('ghosts')
        self.assertIsInstance(written, int)

    async def test_calculate_file_checksum(self):
        checksum = SystemUtils.get_file_checksum(PhotonLocations.basic_photon)
        self.assertIsInstance(checksum, str)

    async def test_compare_module_names(self):
        is_submodule = SystemUtils.is_submodule("5368616C6F6D", "5368616C6F6D")
        self.assertTrue(is_submodule)

    async def test_continue_async(self):
        value = True
        await SystemUtils.continue_async()
        self.assertTrue(value)

    async def test_generate_random_id_with_sample(self):
        random_id = TextUtils.generate_id(use_sample=True)
        self.assertGreaterEqual(len(random_id), 0)

    async def test_generate_random_cryptographic_id(self):
        random_cid = TextUtils.generate_cid()
        self.assertGreaterEqual(len(random_cid), 0)

    async def test_log_info_message(self):
        result = self._logger.info("576520", print_output=False)
        self.assertTrue(result)

    async def test_log_note_message(self):
        result = self._logger.note("726F616D20", print_output=False)
        self.assertTrue(result)

    async def test_log_success_message(self):
        result = self._logger.success("7265616C6D7320", print_output=False)
        self.assertTrue(result)

    async def test_log_warning_message(self):
        result = self._logger.warning("776865726520", print_output=False)
        self.assertTrue(result)

    async def test_log_error_message(self):
        result = self._logger.error("647265616D7320", print_output=False)
        self.assertTrue(result)

    async def test_log_private_message(self):
        result = self._logger.private("7472616E7363656E6420", print_output=False)
        self.assertTrue(result)

    async def test_log_debug_message(self):
        result = self._logger.debug("7265616C6974792E", print_output=False)
        self.assertTrue(result)

class SelfTest(unittest.IsolatedAsyncioTestCase): 
    @classmethod
    def setUpClass(self: "ToolsTest"):
        self._logger = Logger(__name__)
        self._logger.private("Attempting to run all self tests!")

    async def test_the_best(self):
        Jason = "Jason"
        Self = Jason
        self.assertEqual(Self, Jason)

    async def test_the_system(self):
        System = "|q⟩ = (q₁,q₂,q₃,...)"
        Fields = System
        self.assertEqual(System, Fields)

#*=============================================
#* (っ◔◡◔)っ ♥ 𝗠𝗮𝗶𝗻 𝗔𝗽𝗽𝗹𝗶𝗰𝗮𝘁𝗶𝗼𝗻 ♥
#*=============================================
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
        self._logger.debug("ds^2 = -(1 - 2Mr/Σ)dt^2 - 2a sin^2θ(dt - a(1 -2Mr/Σ) dϕ)^2 + Σ/Δ dr^2 + Σ dθ^2 + (r^2 + a^2 + 2Mra^2 sin^2θ) sin^2θ dϕ^2")
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

""" # pragma: no cover
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
57686174206973206C696665277320677265617465737420696C6C7573696F6E3F00000000
00000000000000000000000000000000000000000000000000000000000000000000000000
68747470733A2F2F7777772E796F75747562652E636F6D2F77617463683F763D784C696A58
585561624C3800000000000000000000000000000000000000000000000000000000000000
546865205265616C20486F6C7920506C616365000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000
68747470733A2F2F7777772E796F75747562652E636F6D2F77617463683F763D3378316450
73436E4E747700000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000
5265696E6361726E6174696F6E000000000000000000000000000000000000000000000000
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
           ,   ,
         ,-`{-`/
      ,-~ , \ {-~~-,
    ,~  ,   ,`,-~~-,`,
  ,`   ,   { {      } }                                             }/
 ;     ,--/`\ \    / /                                     }/      /,/
;  ,-./      \ \  { {  (                                  /,;    ,/ ,/
; /   `       } } `, `-`-.___                            / `,  ,/  `,/
 \|         ,`,`    `~.___,---}                         / ,`,,/  ,`,;
  `        { {                                     __  /  ,`/   ,`,;
        /   \ \                                 _,`, `{  `,{   `,`;`
       {     } }       /~\         .-:::-.     (--,   ;\ `,}  `,`;
       \\._./ /      /` , \      ,:::::::::,     `~;   \},/  `,`;     ,-=-
        `-..-`      /. `  .\_   ;:::::::::::;  __,{     `/  `,`;     {
                   / , ~ . ^ `~`\:::::::::::<<~>-,,`,    `-,  ``,_    }
                /~~ . `  . ~  , .`~~\:::::::;    _-~  ;__,        `,-`
       /`\    /~,  . ~ , '  `  ,  .` \::::;`   <<<~```   ``-,,__   ;
      /` .`\ /` .  ^  ,  ~  ,  . ` . ~\~                       \\, `,__
     / ` , ,`\.  ` ~  ,  ^ ,  `  ~ . . ``~~~`,                   `-`--, \
    / , ~ . ~ \ , ` .  ^  `  , . ^   .   , ` .`-,___,---,__            ``
  /` ` . ~ . ` `\ `  ~  ,  .  ,  `  ,  . ~  ^  ,  .  ~  , .`~---,___
/` . `  ,  . ~ , \  `  ~  ,  .  ^  ,  ~  .  `  ,  ~  .  ^  ,  ~  .  `-,
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■                                
41207370696E2074656E736F72206E6574776F726B2063616E206265206D617468656D6174
6963616C6C7920646566696E6564206173206120736574206F662074656E736F72732C2065
616368206F6620776869636820726570726573656E747320746865207370696E2073746174
6573206F6620612067726F7570206F66207061727469636C65732E2054686573652074656E
736F72732061726520636F6E7472616374656420746F676574686572206163636F7264696E
6720746F2061207370656369666963207061747465726E20746F20666F726D2061206E6574
776F726B20746861742064657363726962657320746865206F766572616C6C207370696E20
7374617465206F66207468652073797374656D2E0A0A4D617468656D61746963616C6C792C
207468652074656E736F727320696E2061207370696E2074656E736F72206E6574776F726B
20617265207479706963616C6C7920726570726573656E746564206173206D756C74692D69
6E6465782074656E736F72732C2077697468206561636820696E64657820636F7272657370
6F6E64696E6720746F206120646966666572656E74207370696E2073746174652E20466F72
206578616D706C652C20612074656E736F7220776974682074776F20696E6469636573206D
6967687420626520726570726573656E74656420617320545E7B692C6A7D2C207768657265
206920616E64206A2061726520746865207370696E20737461746573206F662074776F2070
61727469636C65732E0A0A5468652070726F626162696C69747920616D706C697475646573
206173736F6369617465642077697468207468652074656E736F727320696E206120737069
6E2074656E736F72206E6574776F726B206172652063616C63756C61746564207573696E67
20746865207072696E6369706C6573206F66207175616E74756D206D656368616E6963732E
20496E20706172746963756C61722C207468652070726F626162696C69747920616D706C69
74756465206F66206120706172746963756C6172207370696E20636F6E6669677572617469
6F6E20697320676976656E206279207468652070726F64756374206F66207468652070726F
626162696C69747920616D706C697475646573206173736F63696174656420776974682074
686520696E646976696475616C2074656E736F727320696E20746865206E6574776F726B2E
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
68747470733A2F2F7777772E796F75747562652E636F6D2F77617463683F763D4630315554
596737394B5900000000000000000000000000000000000000000000000000000000000000
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█▄▄░▄▄█░█████▄██░▄▄████▄██░▄▄███▀▄▄▀█░██░█░▄▄▀███░███░█▀▄▄▀█░▄▄▀█░██░▄▀███░▄▄▀█▀▄▄▀█░███░████████████▄░▄█░████░▄▄███░███░█▀▄▄▀█░▄▄▀█░██░▄▀███▀▄▄▀█░▄▄███▄░▄█░████░▄▄███░▄▄█░██░▄▄█▀▄▀█▄░▄█░▄▄▀█▀▄▄▀█░▄▄▀███░▄▄▀█░▄▄▀█░▄▀███▄░▄█░████░▄▄███░▄▄█░███░██▄██▄░▄█▀▄▀█░█████████▄░▄█░████░▄▄███░▄▄▀█░▄▄█░▄▄▀█░██░█▄░▄█░██░███▀▄▄▀█░▄▄███▄░▄█░████░▄▄███░▄▄▀█░▄▄▀█░██░█░▄▀█████████░███░█░▄▄███░▄▀▄░█░▄▄▀█░█▀█░▄▄███░██░█░▄▄█░▄▄███▀▄▄▀█░▄▄███░▄▄▀███░▄▄█░▄▄█░▄▄▀█▀███▀██▄██▀▄▀█░▄▄███░▄▄▀█░██░▄▄▀█░▄▄█░▄▄▀█░▄▀█░██░███░▄▄█░█░██▄██░▄▄█▄░▄██▄██░▄▄▀█░▄▄▄███░███░██▄██▄░▄█░████▀▄▄▀█░██░█▄░▄███▀▄▄▀█░▄▄▀█░██░██▄██░▄▄▀█░▄▄▄███░▄▄█▀▄▄▀█░▄▄▀███░███░█░████░▄▄▀█▄░▄███▀▄▀█▀▄▄▀█░██░█░██░▄▀███░▄▄▀█░▄▄███░▄▀██▄██░▄▄▀█▄░▄████▀▄▀█░████░▄▄█░▄▄▀█▀▄▄▀████▄██░▄▄████▄██▄░▄███░███░█░▄▄▀█░▄▄█░▄▄▀█░█▄░▄███░▄▄▀█░██░█░▄▄▀███░▄▄▀█░██░███▀▄▄▀█░▄▄▀█▀▄▄▀█░▄▄██▄██▄░▄█░▄▄█░▄▄█░▄▄▀██▄██░▄▄▀█░▄▄▄███░▄▄▄█░██░██░█▄░▄█▄░▄█▀▄▄▀█░▄▄▀█░▄▄██████░▄▄▀█░▄▄▀█░▄▀███░██░█▀▄▄▀█░██░███▀▄▀█░▄▄▀█░██░████░██░█░▄▄███▀▄▀█░▄▄▀██▄██░▄▀▄░██▄██░▄▄▀█░▄▄▀█░██░▄▄█████████░███░█░▄▄███░▄▄█░█░█▀▄▄▀█░██▀▄▄▀█░▄▄▀█░▄▄████████████░▄▄▀█░▄▄▀█░▄▀███░██░█▀▄▄▀█░██░███▀▄▀█░▄▄▀█░██░████░██░█░▄▄███▀▄▀█░▄▄▀██▄██░▄▀▄░██▄██░▄▄▀█░▄▄▀█░██░▄▄█████████░███░█░▄▄███░▄▄█░▄▄█░▄▄█░█▀███░▄▄▀█░▄▄█▄░▄█░▄▄█░▄▄▀███░█▀█░▄▄▀█▀▄▄▀█░███░█░██░▄▄█░▄▀█░▄▄▄█░▄▄████████████░▄▄▀█░▄▄▀█░▄▀███░██░█▀▄▄▀█░██░███▀▄▀█░▄▄▀█░██░████░██░█░▄▄███▀▄▀█░▄▄▀██▄██░▄▀▄░██▄██░▄▄▀█░▄▄▀█░██░▄▄█████████░███░█░▄▄███░▄▄█░█░██▄██░▄▄█▄░▄███░███░██▄██▄░▄█░████▀▄▄▀█░██░█▄░▄███░▄▄█░█▀██▄██░▄▄▀███▀▄▀█▀▄▄▀█░██▀▄▄▀█░▄▄▀██████░███░██▄██▄░▄█░████▀▄▄▀█░██░█▄░▄███░▄▄▀█░▄▄▀█▄░▄██▄██▀▄▄▀█░▄▄▀█░▄▄▀█░███▄██▄░▄█░██░██████░███░██▄██▄░▄█░████▀▄▄▀█░██░█▄░▄███░▄▄▀█░▄▄█░███▄██░▄▄▄██▄██▀▄▄▀█░██░█░▄▄███░▄▄▀██▄██░▄▄▀█░▄▄████████████░▄▄▀█░▄▄▀█░▄▀███░██░█▀▄▄▀█░██░███▀▄▀█░▄▄▀█░██░████░██░█░▄▄███▀▄▀█░▄▄▀██▄██░▄▀▄░██▄██░▄▄▀█░▄▄▀█░██░▄▄███████░███░█▀▄▄▀█░██░███░▄▄▀█░██░██▄██░██░▄▀███░▄▄▀█▄░▄█▀▄▄▀█░▄▀▄░██▄██▀▄▀███░▄▄▀█▀▄▄▀█░▄▀▄░█░▄▄▀█░▄▄██████░██░█▀▄▄▀█░██░███░███░█░▄▄▀█░▄▄▄█░▄▄███░███░█░▄▄▀█░▄▄▀█░▄▄██████░██░█▀▄▄▀█░██░███░▄▀▄░█░██░█░▄▄▀█░▄▀█░▄▄█░▄▄▀██████▀▄▀█░████░▄▄█░▄▄▀█▄░▄██████░▄▄▀█░▄▄▀█░▄▀███░███▄██░▄▄███▄░▄█▀▄▄▀███░██░█░▄▄███░▄▄▀█░▄▄▀█░▄▀███▄░▄█░▄▄▀█░██░███▄░▄█▀▄▄▀███░▄▀▄░█░▄▄▀█░█▀█░▄▄███░██░█░▄▄███░▄▄▀█░▄▄█░███▄██░▄▄█▀███▀█░▄▄████▄██▄░▄█░█░▄▄███░▄▄█▀▄▄▀█░▄▄▀███▀▄▄▀█░██░█░▄▄▀███▀▄▄▀█░███░█░▄▄▀███░▄▄▄█▀▄▄▀█▀▄▄▀█░▄▀██████░██░█░▄▄█▄░▄███░███░█░▄▄█░█░▄▄▀█░▄▄███▄░▄█░████░▄▄███▀▄▀█░▄▄▀██▄██░▄▀▄░██▄██░▄▄▀█░▄▄▀█░██░▄▄█████
███░███░▄▄░██░▄█▄▄▀████░▄█▄▄▀███░██░█░██░█░▀▀▄███▄▀░▀▄█░██░█░▀▀▄█░██░█░███░██░█░██░█▄▀░▀▄█▀▀█▀▀█▀▀████░██░▄▄░█░▄▄███▄▀░▀▄█░██░█░▀▀▄█░██░█░███░██░█░▄█████░██░▄▄░█░▄▄███░▄▄█░██░▄▄█░█▀██░██░▀▀▄█░██░█░██░███░▀▀░█░██░█░█░████░██░▄▄░█░▄▄███▄▄▀█▄▀░▀▄██░▄██░██░█▀█░▄▄░█▀▀████░██░▄▄░█░▄▄███░▄▄▀█░▄▄█░▀▀░█░██░██░██░▀▀░███░██░█░▄█████░██░▄▄░█░▄▄███░▄▄▀█░▀▀░█░██░█░█░█▀▀██████░█░█░█░▄▄███░█▄█░█░▀▀░█░▄▀█░▄▄███░██░█▄▄▀█░▄▄███░██░█░▄████░▀▀░███▄▄▀█░▄▄█░▀▀▄██░▀░███░▄█░█▀█░▄▄███░▀▀░█░██░▀▀▄█░▄▄█░▀▀░█░█░█░▀▀░███░▄▄█▀▄▀██░▄█▄▄▀██░███░▄█░██░█░█▄▀███▄▀░▀▄██░▄██░██░▄▄░█░██░█░██░██░████░▀▀░█░▀▀░█░▀▀░██░▄█░██░█░█▄▀███░▄██░██░█░▀▀▄███▄▀░▀▄█░▄▄░█░▀▀░██░████░█▀█░██░█░██░█░██░█░███░▄▄▀█░▄▄███░█░██░▄█░▀▀▄██░██▄▄█░█▀█░▄▄░█░▄▄█░▀▀░█░▀▀░████░▄█░▄█████░▄██░████▄▀░▀▄█░▀▀░█▄▄▀█░██░████░████░▀▀▄█░██░█░██░███░▄▄▀█░▀▀░███░▀▀░█░▀▀▄█░██░█░▄███░▄██░██░▄▄█░▄▄█░▀▀▄██░▄█░██░█░█▄▀███░█▄▀█░██░██░██░███░██░██░█░██░█▄▄▀█▀▀███░▀▀░█░██░█░█░███░▀▀░█░██░█░██░███░█▀█░▀▀░█░██░████░██░█▄▄▀███░█▀█░▀▀▄██░▄█░█▄█░██░▄█░██░█░▀▀░█░██▄▄▀█▀▀██████░█░█░█░▄▄███░▄▄█▀▄▀█░▀▀░█░██░██░█░▀▀▄█░▄▄█▀▀█▀▀█▀▀███░▀▀░█░██░█░█░███░▀▀░█░██░█░██░███░█▀█░▀▀░█░██░████░██░█▄▄▀███░█▀█░▀▀▄██░▄█░█▄█░██░▄█░██░█░▀▀░█░██▄▄▀█▀▀██████░█░█░█░▄▄███▄▄▀█░▄▄█░▄▄█░▄▀███░▀▀░█░▄███░██░▄▄█░▀▀▄███░▄▀█░██░█░██░█▄▀░▀▄█░██░▄▄█░█░█░█▄▀█░▄▄█▀▀█▀▀█▀▀███░▀▀░█░██░█░█░███░▀▀░█░██░█░██░███░█▀█░▀▀░█░██░████░██░█▄▄▀███░█▀█░▀▀▄██░▄█░█▄█░██░▄█░██░█░▀▀░█░██▄▄▀█▀▀██████░█░█░█░▄▄███░▄▄█▀▄▀██░▄█▄▄▀██░████▄▀░▀▄██░▄██░██░▄▄░█░██░█░██░██░████▄▄▀█░▄▀██░▄█░██░███░█▀█░██░█░██░██░█░▀▀▄█▀▀███▄▀░▀▄██░▄██░██░▄▄░█░██░█░██░██░████░██░█░▀▀░██░███░▄█░██░█░██░█░▀▀░█░███░▄██░██░▀▀░█▀▀███▄▀░▀▄██░▄██░██░▄▄░█░██░█░██░██░████░▀▀▄█░▄▄█░███░▄█░█▄▀██░▄█░██░█░██░█▄▄▀███░▄▄▀██░▄█░▀▀░█▄▄▀█▀▀█▀▀█▀▀███░▀▀░█░██░█░█░███░▀▀░█░██░█░██░███░█▀█░▀▀░█░██░████░██░█▄▄▀███░█▀█░▀▀▄██░▄█░█▄█░██░▄█░██░█░▀▀░█░██▄▄▀█▀▀████▄▀▀▀▄█░██░█░██░███░▄▄▀█░██░██░▄█░██░█░███░▀▀░██░██░██░█░█▄█░██░▄█░█▀███░▄▄▀█░██░█░█▄█░█░▄▄▀█▄▄▀█▀▀███░▀▀░█░██░█░██░███▄▀░▀▄█░▀▀░█░█▄▀█░▄▄███▄▀░▀▄█░▀▀░█░▀▀▄█▄▄▀█▀▀███░▀▀░█░██░█░██░███░█▄█░█░██░█░▀▀▄█░█░█░▄▄█░▀▀▄█▀▀███░█▀█░▄▄░█░▄▄█░▀▀░██░██▀▀███░▀▀░█░██░█░█░███░███░▄█░▄▄████░██░██░███░██░█▄▄▀███░▀▀░█░██░█░█░████░██░▀▀▄█░▀▀░████░██░██░███░█▄█░█░▀▀░█░▄▀█░▄▄███░██░█▄▄▀███░▄▄▀█░▄▄█░███░▄█░▄▄██░▀░██░▄▄████░▄██░████▄▄▀███░▄██░██░█░▀▀▄███░██░█░██░█░▀▀▄███░██░█▄▀░▀▄█░██░███░█▄▀█░██░█░██░█░█░█▀▀███░▀▀░█░▄▄██░████▄▀░▀▄█░▄▄███░▀▀▄█░▄▄████░██░▄▄░█░▄▄███░█▀█░▀▀▄██░▄█░█▄█░██░▄█░██░█░▀▀░█░██▄▄▀█▀▀██
███░███▄██▄█▄▄▄█▄▄▄███▄▄▄█▄▄▄████▄▄███▄▄▄█▄█▄▄████▄█▄███▄▄██▄█▄▄█▄▄█▄▄████▄██▄██▄▄███▄█▄██▄▄█▄▄█▄▄████▄██▄██▄█▄▄▄████▄█▄███▄▄██▄█▄▄█▄▄█▄▄█████▄▄██▄██████▄██▄██▄█▄▄▄███▄▄▄█▄▄█▄▄▄██▄███▄██▄█▄▄██▄▄██▄██▄███▄██▄█▄██▄█▄▄█████▄██▄██▄█▄▄▄███▄▄▄██▄█▄██▄▄▄██▄███▄██▄██▄██░████▄██▄██▄█▄▄▄███▄▄▄▄█▄▄▄█▄██▄██▄▄▄██▄██▀▀▀▄████▄▄██▄██████▄██▄██▄█▄▄▄███▄▄▄▄█▄██▄██▄▄▄█▄▄██▄▄██████▄▀▄▀▄█▄▄▄███▄███▄█▄██▄█▄█▄█▄▄▄████▄▄▄█▄▄▄█▄▄▄████▄▄██▄█████▄██▄███▄▄▄█▄▄▄█▄█▄▄███▄███▄▄▄██▄██▄▄▄███▄██▄█▄▄█▄█▄▄█▄▄▄█▄██▄█▄▄██▀▀▀▄███▄▄▄█▄█▄█▄▄▄█▄▄▄██▄██▄▄▄█▄██▄█▄▄▄▄████▄█▄██▄▄▄██▄██▄██▄██▄▄███▄▄▄██▄████░████▄██▄█▀▀▀▄█▄▄▄█▄██▄█▄▄▄▄███▄████▄▄██▄█▄▄████▄█▄██▄██▄█▄██▄██▄█████▄███▄▄███▄▄▄█▄▄█▄▄████▄▄▄▄█▄▄▄███▄▄██▄▄▄█▄█▄▄██▄██████▄██▄██▄█▄▄▄█▄██▄█░██████▄▄▄█▄█████▄▄▄██▄█████▄█▄██▄██▄█▄▄▄█▄██▄████▄████▄█▄▄██▄▄▄█▄██▄███▄▄▄▄█▀▀▀▄███░████▄█▄▄██▄▄██▄███▄▄▄██▄██▄▄▄█▄▄▄█▄█▄▄█▄▄▄█▄██▄█▄▄▄▄███▄▄▄▄█▄▄██▄▄▄██▄███▄███▄▄██▄██▄█▄▄▄██░███▄██▄█▄██▄█▄▄████▀▀▀▄██▄▄███▄▄▄████▄██▄██▄█▄▄█▄▄████▄▄▄█▄▄▄████▄██▄█▄▄█▄▄▄█▄███▄█▄▄▄█▄██▄█▄██▄█▄▄█▄▄▄█▄▄██████▄▀▄▀▄█▄▄▄███▄▄▄█▄█▄█░████▄▄██▄▄██▄█▄▄█▄▄▄█▄▄█▄▄█▄▄███▄██▄█▄██▄█▄▄████▀▀▀▄██▄▄███▄▄▄████▄██▄██▄█▄▄█▄▄████▄▄▄█▄▄▄████▄██▄█▄▄█▄▄▄█▄███▄█▄▄▄█▄██▄█▄██▄█▄▄█▄▄▄█▄▄██████▄▀▄▀▄█▄▄▄███▄▄▄█▄▄▄█▄▄▄█▄█▄███▄██▄█▄████▄██▄▄▄█▄█▄▄███▄█▄█▄██▄██▄▄███▄█▄██▄▄█▄▄▄█▄▄██▄▄▄▄█▄▄▄█▄▄█▄▄█▄▄███▄██▄█▄██▄█▄▄████▀▀▀▄██▄▄███▄▄▄████▄██▄██▄█▄▄█▄▄████▄▄▄█▄▄▄████▄██▄█▄▄█▄▄▄█▄███▄█▄▄▄█▄██▄█▄██▄█▄▄█▄▄▄█▄▄██████▄▀▄▀▄█▄▄▄███▄▄▄█▄█▄█▄▄▄█▄▄▄██▄█████▄█▄██▄▄▄██▄██▄██▄██▄▄███▄▄▄██▄████▄▄▄█▄█▄█▄▄▄█▄██▄████▄███▄▄██▄▄██▄▄██▄█▄▄██░████▄█▄██▄▄▄██▄██▄██▄██▄▄███▄▄▄██▄████▄██▄█▄██▄██▄██▄▄▄██▄▄██▄██▄█▄██▄█▄▄█▄▄▄██▄██▀▀▀▄██░████▄█▄██▄▄▄██▄██▄██▄██▄▄███▄▄▄██▄████▄█▄▄█▄▄▄█▄▄█▄▄▄█▄▄▄▄█▄▄▄██▄▄███▄▄▄█▄▄▄███▄▄▄▄█▄▄▄█▄██▄█▄▄▄█▄▄█▄▄█▄▄███▄██▄█▄██▄█▄▄████▀▀▀▄██▄▄███▄▄▄████▄██▄██▄█▄▄█▄▄████▄▄▄█▄▄▄████▄██▄█▄▄█▄▄▄█▄███▄█▄▄▄█▄██▄█▄██▄█▄▄█▄▄▄█▄▄██████░████▄▄███▄▄▄███▄▄▄▄██▄▄▄█▄▄▄█▄▄█▄▄████▄██▄██▄███▄▄██▄███▄█▄▄▄██▄████▄▄▄▄██▄▄██▄███▄█▄▄▄▄█▄▄▄██░███▀▀▀▄██▄▄███▄▄▄████▄█▄██▄██▄█▄▄▄▄█▄▄▄████▄█▄██▄██▄█▄█▄▄█▄▄▄██░███▀▀▀▄██▄▄███▄▄▄███▄███▄██▄▄▄█▄█▄▄█▄▄██▄▄▄█▄█▄▄██░████▄██▄██▄█▄▄▄█▄██▄██▄███░███▄██▄█▄██▄█▄▄████▄▄█▄▄▄█▄▄▄████▄███▄▄█████▄▄▄█▄▄▄███▄██▄█▄██▄█▄▄█████▄██▄█▄▄█▀▀▀▄████▄███▄▄████▄███▄█▄██▄█▄█▄█▄▄▄████▄▄▄█▄▄▄███▄▄▄▄█▄▄▄█▄▄█▄▄▄█▄▄▄███▄███▄▄▄███▄▄▄██▄████▄▄▄███▄████▄▄██▄█▄▄████▄▄███▄▄▄█▄█▄▄████▄▄███▄█▄██▄██▄███▄▄▄▄██▄▄███▄▄██▄▄███░███▀▀▀▄█▄▄▄██▄█████▄█▄██▄▄▄███▄█▄▄█▄▄▄████▄██▄██▄█▄▄▄████▄██▄█▄▄█▄▄▄█▄███▄█▄▄▄█▄██▄█▄██▄█▄▄█▄▄▄█▄▄██
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
"""
#               .7
#             .'/
#            / /
#           / /
#          / /
#         / /
#        / /
#       / /
#      / /         
#     / /          
#   __|/
# ,-\__\
# |f-"Y\|
# \()7L/
#  cgD                            __ _
#  |\(                          .'  Y '>,
#   \ \                        / _   _   \
#    \\\                       )(_) (_)(|}
#     \\\                      {  4A   } /
#      \\\                      \uLuJJ/\l
#       \\\                     |3    p)/
#        \\\___ __________      /nnm_n//
#        c7___-__,__-)\,__)(".  \_>-<_/D
#                   //V     \_"-._.__G G_c__.-__<"/ ( \
#                          <"-._>__-,G_.___)\   \7\
#                         ("-.__.| \"<.__.-" )   \ \
#                         |"-.__"\  |"-.__.-".\   \ \
#                         ("-.__"". \"-.__.-".|    \_\
#                         \"-.__""|!|"-.__.-".)     \ \
#                          "-.__""\_|"-.__.-"./      \ l
#                           ".__""">G>-.__.-">       .--,_
#                               ""  G