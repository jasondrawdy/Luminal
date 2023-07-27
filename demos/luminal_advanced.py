# -*- coding: utf-8 -*-
# ########################################################################                          
# Program: Luminal
# Author: Jason Drawdy
# Version: 1.0.0
# Date: 07/07/23
# #########################################################################
# Description:
# More advanced photons which show the creation structure with no input.
# #########################################################################
from src.interfaces.photon import IPhoton
from src.tools.logger import Logger

# α #
class Alpha(IPhoton): # pragma: no cover
    """A photon developed for unit testing and contains a finalizer, but no output."""
    def __init__(self: "Alpha"): pass
    async def finalize(self: "Alpha") -> bool: pass

# Ω # 
class Omega(IPhoton): # pragma: no cover
    """A photon developed for unit testing and contains a finalizer, but no output."""
    def __init__(self: "Omega"): pass
    async def finalize(self: "Omega") -> bool: pass

# Σ #
class Sigma(IPhoton): # pragma: no cover
    """A photon developed for unit testing and contains no finalizer, and no output."""
    def __init__(self: "Sigma"): pass

# γ #
class Gamma(IPhoton): # pragma: no cover
    """A photon developed for unit testing and contains no finalizer, and no output."""
    def __init__(self: "Gamma"): pass

# Δ #
class Delta: # pragma: no cover
    """A regular Python class for loading during unit tests."""
    def __init__(self) -> None:
        _logger = Logger(__name__)
        _logger.private("This IS advanced!", print_output=False)

# λ #
class Lambda: # pragma: no cover
    """Another common class for unit testing."""
    def __init__(self) -> None:
        _logger = Logger(__name__)
        _logger.private("¡Esto ES avanzado!",  print_output=False)