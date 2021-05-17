# save poses to file
from parameters import *
import os, subprocess

os.chdir(work_dir)

subprocess.call(["obabel", "DOCK.sd", "-O", "DOCK.pdb"])

num = 0

with open("DOCK.pdb") as f:
    for line in f:
        with open("pose" + str(num) + ".pdb", "a+") as n:
            n.write(line)
        if line.find("ENDMDL") != -1 :
            num += 1
        n.close()
f.close()