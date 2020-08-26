# change files extensions

from parameters import *
import os
import subprocess 

os.chdir(direct)

subprocess.run(["obabel", receptor + "_prep.pdb", "-O ", receptor + "_prep.mol2", "-h"])

subprocess.run(["obabel", rec_ligand + ".pdb", "-O ", rec_ligand + ".sd", "-h"])

subprocess.run(["obabel", ligand + ".pdb", "-O ", ligand + ".sd", "-h"])
