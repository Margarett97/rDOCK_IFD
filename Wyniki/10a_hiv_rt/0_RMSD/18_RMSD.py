#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from chimera import *
from chimera import runCommand as rc
from chimera.tkgui import saveReplyLog as rl

ref = 'U05'
best_score = 'pose0'
ligand = 'U05'

rc("open #0 " + ref + ".pdb")
rc("open #1 " + best_score + ".pdb")
#rc("matchmaker #0 #1 ")
rc('match #0 #1')
RMSD = rc("rmsd #1:LIG #0:" + ligand) 

