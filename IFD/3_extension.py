# change files extensions

from parameters import *
import os
import subprocess 

os.chdir(work_dir)

subprocess.call(["obabel", receptor + ".pdb", "-O ", receptor + ".mol2", "-h"])

subprocess.call(["obabel", rec_ligand + ".pdb", "-O ", rec_ligand + ".sd", "-h"])

subprocess.call(["obabel", ligand + ".pdb", "-O ", ligand + ".sd", "-h"])

