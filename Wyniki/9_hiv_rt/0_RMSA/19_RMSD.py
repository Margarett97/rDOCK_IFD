#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from chimera import *
from chimera import runCommand as rc
from chimera.tkgui import saveReplyLog as rl

from tmp import *

rc("open #0 " + ref + ".pdb")
rc("open #1 " + best_score2 + ".pdb")
rc("matchmaker #0 #1 ")
rc("rmsd #1:LIG #0:" + ligand) 
rc("close all")
