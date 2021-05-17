# select receptor chain

from parameters import *
import os

path = os.getcwd()
os.chdir(work_dir)

with open(receptor + ".pdb", "r") as f:        # receptor selection
    line = f.readlines()              
    with open(receptor+ ".pdb" , "w") as n:
        for i, lines in enumerate(line):
            if lines.startswith("ATOM"):
                a = lines.split()
                if a[4] == act_chain:
                    n.write(lines)
    n.close()
f.close()               
