#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from chimera import *
from chimera import runCommand as rc

from parameters import *


os.chdir(work_dir)
rc("open "+ best_opt+".pdb")
rc("select :/isHet " ) 
rc("delete selected")
rc("write #0 ligand_remove.pdb")
rc("close all")
