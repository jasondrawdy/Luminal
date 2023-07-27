.. 
   ===============================================================================
   Luminal documentation master file, created by
   sphinx-quickstart on Sun Jul 16 06:19:07 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
   ===============================================================================
   .. # ########################################################################                          
   .. # Program: Luminal
   .. # Author: Jason Drawdy
   .. # Version: 1.0.0
   .. # Date: 07/26/23
   .. # #########################################################################
   ===============================================================================
     -----                                                               -----
   1 | H |                                                               |He |
   |---+----                                       --------------------+---|
   2 |Li |Be |                                       | B | C | N | O | F |Ne |
   |---+---|                                       |---+---+---+---+---+---|
   3 |Na |Mg |3B  4B  5B  6B  7B |    8B     |1B  2B |Al |Si | P | S |Cl |Ar |
   |---+---+---------------------------------------+---+---+---+---+---+---|
   4 | K |Ca |Sc |Ti | V |Cr |Mn |Fe |Co |Ni |Cu |Zn |Ga |Ge |As |Se |Br |Kr |
   |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|
   5 |Rb |Sr | Y |Zr |Nb |Mo |Tc |Ru |Rh |Pd |Ag |Cd |In |Sn |Sb |Te | I |Xe |
   |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|
   6 |Cs |Ba |LAN|Hf |Ta | W |Re |Os |Ir |Pt |Au |Hg |Tl |Pb |Bi |Po |At |Rn |
   |---+---+---+------------------------------------------------------------
   7 |Fr |Ra |ACT|
   -------------
               -------------------------------------------------------------
      Lanthanide |La |Ce |Pr |Nd |Pm |Sm |Eu |Gd |Tb |Dy |Ho |Er |Tm |Yb |Lu |
               |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|
      Actinide   |Ac |Th |Pa | U |Np |Pu |Am |Cm |Bk |Cf |Es |Fm |Md |No |Lw |
               ------------------------------------------------------------- 
   ===============================================================================
   Everyone who lives and believes in me will never "die". Do you believe that?
   ===============================================================================

💡 Welcome!
==================
.. toctree::
   :maxdepth: 1
   :caption: Table of Contents
   :titlesonly:
   
   autoapi/index
   Library Index <../genindex>

.. toctree::
   :maxdepth: 2
   :caption: Interfaces
   :titlesonly:

   metadata <autoapi/src/interfaces/metadata/index>
   photon <autoapi/src/interfaces/photon/index>
   
.. toctree::
   :maxdepth: 2
   :caption: Managers
   :titlesonly:

   handler <autoapi/src/managers/handler/index>
   loader <autoapi/src/managers/loader/index>
   resolver <autoapi/src/managers/resolver/index>
   threads <autoapi/src/managers/threads/index>
   tracer <autoapi/src/managers/tracer/index>
   
.. toctree::
   :maxdepth: 2
   :caption: Errors
   :titlesonly:

   cleanup <autoapi/src/errors/cleanup/index>
   system <autoapi/src/errors/system/index>
   threads <autoapi/src/errors/threads/index>
   
.. toctree::
   :maxdepth: 2
   :caption: Tools
   :titlesonly:
   
   colors <autoapi/src/tools/colors/index>
   logger <autoapi/src/tools/logger/index>
   utils <autoapi/src/tools/utils/index>
   sentinel <autoapi/src/tools/sentinel/index>


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
