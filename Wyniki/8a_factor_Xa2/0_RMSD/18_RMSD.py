#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from chimera import *
from chimera import runCommand as rc
from chimera.tkgui import saveReplyLog as rl

ref = '1ksn'
best_score = 'pose3'
lig = 'FXV'


rc("open #0 " + lig + ".pdb")
rc("open #1 " + best_score + ".pdb")
#rc("matchmaker #0 #1 ")
RMSD = rc("rmsd #1:LIG #0:" + lig) 

