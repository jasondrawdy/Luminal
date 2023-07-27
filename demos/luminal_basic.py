# -*- coding: utf-8 -*-
# ########################################################################                          
# Program: Luminal
# Author: Jason Drawdy
# Version: 1.0.0
# Date: 07/07/23
# #########################################################################
# Description:
# Basic photon which shows the creation structure with no input or output.
# #########################################################################
from src.interfaces.photon import IPhoton

# φ #
class Photon(IPhoton): # pragma: no cover
    """A photon developed for unit testing and contains a finalizer, but no output."""
    def __init__(self: "Photon"): pass
    async def finalize(self: "Photon") -> bool: pass