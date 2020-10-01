import os, shutil

from parameters import *

os.chdir(work_dir)

## CREATE NEW FOLDER:

new_dir = work_dir + "/0_RMSD"
if not os.path.exists(new_dir):
    os.makedirs(new_dir)


shutil.copy(work_dir + "/" + ref + ".pdb", new_dir + ref + ".pdb")
shutil.copy(work_dir + "/" + best_score + ".pdb", new_dir + best_score + ".pdb")
shutil.copy(work_dir + "/" + ligand + ".pdb", new_dir + ligand + ".pdb")
shutil.copy(work_dir + "/IFD/" + best_score2 + ".pdb", new_dir + best_score2 + ".pdb")

with open("parameters.py", "a") as p:
    name = "rmsd_dir = '"
    p.write(name + new_dir + "'\n")
