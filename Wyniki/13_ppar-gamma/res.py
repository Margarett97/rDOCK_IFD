# run in Chimera
#set proper directory
#set proper name of files
import os
from chimera import *
from chimera import runCommand as rc

# change to folder with data files
#os.chdir("C:/Users/.../")

# gather the names of .pdb files in the folder
name="model1"

#replyobj.status("Processing " + name+str(f)+"merged.pdb")  # show what file we're working on
rc("open " + name+".pdb")
rc("select #"+":LIG zr<5")  # put ligand in front of remainder of molecule
rc("writesel " + "resi5.txt")
rc("close all")
rc("stop now")