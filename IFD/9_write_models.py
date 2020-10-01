#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from chimera import *
from chimera import runCommand as rc

from parameters import *


os.chdir(work_dir)


for i in range(0,int(no_poses)):
    rc("open #0 " + receptor + ".pdb")
    rc("delete H")
    rc("open #1 pose" + str(i) + ".pdb")
    rc("delete H")
    rc("resrenumber 999 #1")
    rc("combine #0,1 newchainids false")
    rc("changechains A," + rec_chain + " " + rec_chain + "," + rec_chain)
    rc("resrenumber 1 #2")
    rc("write #2 model" +str(i) + ".pdb")
    rc("close all")
