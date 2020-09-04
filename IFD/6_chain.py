from parameters import *
import os

os.chdir(work_dir)

with open(receptor + "_prep.pdb") as f:
    line = f.readlines()
    for i,lines in enumerate(line):
        indx = lines.split()
        rec_chain = indx[4]
f.close()



with open("soft_dock.pdb", "a+") as n:
    line = n.readlines()
    for i,lines in enumerate(line):
        if lines.startswith("HETATM"):
            a = lines.split()
            a.insert(4,rec_chain)
            
            
            
n.close()
        
