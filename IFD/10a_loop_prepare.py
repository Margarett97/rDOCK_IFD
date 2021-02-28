import os, subprocess

from parameters import *

os.chdir(work_dir)

for i in range(0, int(no_poses)):
    subprocess.call(["obabel",  "pose" + str(i)  + ".pdb", "-O ", "pose" + str(i) + ".mol2", "-h"])
for i in range(0, int(no_poses)):   
    subprocess.run(["python", "molfile_to_params.py", "pose" + str(i) + ".mol2", "-n", "P" + str(i)]) ## create .param file