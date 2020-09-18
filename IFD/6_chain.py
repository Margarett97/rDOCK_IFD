# select receptor chain ID
from parameters import *
import os

path = os.getcwd()

os.chdir(work_dir)

with open(receptor + "_prep.pdb") as f:
    line = f.readlines()
    for i,lines in enumerate(line):
        indx = lines.split()
        rec_chain = indx[4]
f.close()


os.chdir(path)
with open("parameters.py","a") as p:
    name = "rec_chain = '"
    p.write(name + rec_chain + "'\n")
p.close()
