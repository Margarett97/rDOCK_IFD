#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from chimera import *
from chimera import runCommand as rc
from chimera.tkgui import saveReplyLog as rl

ref = 'S58'
best_score = 'pose8'
best_score2 = 'model2'
ligand = 'S58'


rc("open #0 " + ref + ".pdb")
rc("open #1 " + best_score + ".pdb")
rc("matchmaker #0 #1 ")
RMSD = rc("rmsd #1:LIG #0:" + ligand) 
#rl("soft.txt")
rl("H.txt")