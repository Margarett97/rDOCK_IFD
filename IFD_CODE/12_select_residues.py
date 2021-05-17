# run in Chimera
#set proper directory
#set proper name of files
import os
from chimera import *
from chimera import runCommand as rc

from parameters import *
os.chdir(work_dir)

# gather the names of .pdb files in the folder
name="model0"

rc("open " + name+".pdb")
rc("select #"+":LIG zr<5")  # put ligand in front of remainder of molecule
rc("writesel resi5.txt namingStyle simple")
rc("close all")
rc("stop now")