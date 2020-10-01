#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from chimera import *
from chimera import runCommand as rc

from parameters import *

os.chdir(work_dir)

# best model - hard docking

rc("open #0 " + receptor + ".pdb")
rc("open #1 " + best_score2 +".pdb")
rc("delete H")
rc("resrenumber 999 #1")
rc("combine #0,1 newchainids false")
rc("changechains A," + rec_chain + "," + rec_chain) 
rc("resrenumber 1 #2")
rc("write #2 model.pdb")
rc("close all")



rc("open #0 " + apo + ".pdb")
rc("open #1 " + model + ".pdb")
rc("color plum #0")
rc("color cyan #1")
rc("color gold :/isHet")
rc("focus #1 ")
rc("rlabel #1:/isHet zr<5")
rc("color byhet")
rc("transparency 98,r")

rc("2dlabels create 1 text LIGAND color gold xpos 0 ypos 0.1")
rc("2dlabels create 2 text 'RECEPTOR BEFORE DOCKING' color plum xpos 0 ypos 0.07")
rc("2dlabels create 3 text 'RECEPTOR AFTER DOCKING' color cyan xpos 0 ypos 0.04")



