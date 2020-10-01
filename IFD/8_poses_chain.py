# add ligand chain id  
from parameters import *
import os, subprocess
from pdbtools import *

os.chdir(work_dir)

for i in range(0,int(no_poses)):
    os.system("pdb_chain -A pose" + str(i) + ".pdb > pose" + str(i) + ".log")
    pre, ext = os.path.splitext("pose" + str(i) + ".pdb")
    os.rename("pose" + str(i) + ".log", pre + ".pdb")
    os.system("pdb_uniqname pose" + str(i) + ".pdb > pose" + str(i) + ".log")
    pre, ext = os.path.splitext("pose" + str(i) + ".pdb")
    os.rename("pose" + str(i) + ".log", pre + ".pdb")

