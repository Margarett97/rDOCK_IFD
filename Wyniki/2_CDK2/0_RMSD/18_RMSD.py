#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from chimera import *
from chimera import runCommand as rc
from chimera.tkgui import saveReplyLog as rl

ref = '1dm2'
best_score = 'model0'
best_score2 = 'model7'
ligand = 'HMD'


rc("open #0 " + ref + ".pdb")
rc("open #1 " + best_score2 + ".pdb")
rc("matchmaker #0 #1 ")
RMSD = rc("rmsd #1:LIG #0:" + ligand) 
#rl("soft.txt")
rl("hard.txt")
