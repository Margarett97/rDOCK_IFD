#!/usr/bin/env python
# -*- coding: UTF-8 -*-

## PYROSETTA MODELS


import os
from chimera import *
from chimera import runCommand as rc

from parameters import *


os.chdir(work_dir)


for i in range(0,int(no_poses)):
    rc("open #0 " + receptor + ".pdb")
    rc("open #1 P" + str(i) + "_0001.pdb")
    rc("resrenumber 999 #1")
    rc("combine #0,1 newchainids false")
    rc("changechains A," + rec_chain + " " + rec_chain + "," + rec_chain)
    rc("resrenumber 1 #2")
    rc("write #2 MODEL" +str(i) + ".pdb")
    rc("close all")
