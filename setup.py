# -*- coding: utf-8 -*-
# ########################################################################                          
# Program: Luminal
# Author: Jason Drawdy
# Version: 1.0.0
# Date: 07/20/23
# #########################################################################
# Description:
# Contains all classes and functions for creating a complete pip package.
# #########################################################################
from setuptools import setup, find_packages
import datetime
import codecs
import os

class Egg:
    """A encapsulation object containing all necessary components for creating a pip package."""
    def __init__(self: "Egg") -> None:
        self.package = "luminal"
        self.author = "Jason Drawdy"
        self.email = "luminalcodebase@protonmail.com"
        self.website = "https://github.com/jasondrawdy/luminal"
        self.references = {
            "Documentation": "https://luminal.readthedocs.io/en/latest/",
            "Issue Tracker": "https://github.com/jasondrawdy/luminal/issues"
        }
        self.version = '1.0.0'
        self.description = 'A lightweight, modular, and atomic photon, a.k.a plugin, loader.'
        self.long_description = self._get_project_readme()

    def _get_project_readme(self: "Egg"):
        """Returns the current README documentation or a default description."""
        default_data = 'Luminal offers developers the perfect solution to\
            streamline and optimize their projects effortlessly by creating\
            dynamic and modular plugins, a.k.a Photons.'
        current_path = os.path.abspath(os.path.dirname(__file__))
        readme_file = os.path.join(current_path, "README.md")
        if os.path.exists(readme_file):
            with codecs.open(readme_file, encoding="utf-8") as file:
                return file.read()
        return default_data 

    def prepare_for_archiving(self: "Egg"):
        """Temporarily modifies the current project structure for more accurate packaging."""
        os.rename('src', self.package)

    def restore_original_structure(self: "Egg"):
        """Creates the original file and directory structure before the creation of any packages."""
        os.rename(self.package, 'src')
    
    def create_project_package(self: "Egg"):
        """Performs the actual package creation process using all provided `setup()` function information."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d @ %H:%M:%S")
        self.long_description += f"\n\nBuilt with Autumn (Jason's AI) — {timestamp}"
        try:
            setup(
                name=self.package,
                version=self.version,
                author=self.author,
                author_email=self.email,
                description=self.description,
                long_description_content_type="text/markdown",
                long_description=self.long_description,
                url=self.website,
                project_urls=self.references,
                packages=find_packages(),
                extras_require={'dev': ['coverage', 'twine', 'sphinx', 'sphinx-rtd-theme', 'sphinx-autoapi']},
                keywords=['actions', 'advanced logging', 'asynchronous', 'atomic', 'atomic reloading', 'branch', 'branch coverage', 'checksum', 'checksum algorithms', 'code', 'code statement coverage', 'comprehensive documentation', 'core features', 'couple', 'couple plugins', 'coupling plugins', 'coverage', 'customization', 'debugging', 'debugging methods', 'decouple', 'decouple plugins', 'decoupling plugins', 'dependencies', 'design', 'development', 'development time', 'documentation', 'dynamic', 'dynamic and modular design', 'dynamic framework', 'efficiency', 'efficient', 'efficient resource usage', 'error', 'error handling', 'existing project', 'extensibility', 'extensible', 'extensible architecture', 'features', 'flexibility', 'footprint', 'functions', 'github actions', 'integrated', 'integration', 'integration tests', 'interoperability', 'loader', 'logging', 'luminal', 'manager', 'metaclasses', 'methods', 'minimal', 'minimal #pragma tags', 'modifications', 'modular', 'modular dynamism', 'modularity', 'monitoring', 'multi-threaded', 'multi-threaded library', 'object', 'object caches', 'optimizations', 'optimizing', 'optimizing resources', 'photons', 'plugin development standards', 'plugins', 'portable', 'prioritizing', 'prioritizing security', 'private methods', 'project', 'public-facing functions', 'python', 'quick modifications', 'readability', 'reliability', 'resources', 'safety', 'scale', 'scale projects', 'seamlessly integrated', 'small', 'small footprint', 'software flexibility', 'statement', 'streamlining', 'streamlining projects', 'structured', 'structured and organized code', 'syntax', 'tags', 'tailoring', 'tailoring functionality', 'testing', 'tools', 'transparency', 'unit', 'unit testing', 'unit tests', 'up-to-date python syntax', 'utilities', 'utils'],
                classifiers=[
                    "Development Status :: 3 - Alpha",
                    "Intended Audience :: Developers",
                    "License :: OSI Approved :: MIT License",
                    "Programming Language :: Python :: 3",
                    "Programming Language :: Python :: 3.6",
                    "Programming Language :: Python :: 3.7",
                    "Programming Language :: Python :: 3.8",
                    "Programming Language :: Python :: 3.9",
                    "Programming Language :: Python :: 3.10",
                    "Programming Language :: Python :: 3.11",
                    "Operating System :: OS Independent",
                ]
            )
        except: pass # Cleanup will be called after setup.

package = Egg()
package.prepare_for_archiving()
package.create_project_package()
package.restore_original_structure()