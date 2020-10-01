#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from chimera import *
from chimera import runCommand as rc
from chimera.tkgui import saveReplyLog as rl


os.chdir(chimera_dir)
currentPose=0

rc("open #0 " + ref + ".pdb")
rc("open #1 " + best_score + ".pdb")
rc("matchmaker #0 #1 ")
RMSD = rc("rmsd #1:LIG #0:" + ligand) 
rl("soft.txt")
rc("close session")


rc("open #0 " + ref + ".pdb")
rc("open #1 " + best_score2 + ".pdb")
rc("matchmaker #0 #1 ")
RMSD = rc("rmsd #1:LIG 0:" + ligand) 
rl("hard.txt")
rc("close session")
