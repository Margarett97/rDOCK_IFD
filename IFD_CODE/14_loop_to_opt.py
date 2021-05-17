# select residues numbers with distance criterion
import os
from parameters import *

os.chdir(work_dir)

with open("resi5.txt", "r") as f:
    line = f.readlines()
    INDX_ZONE = [] # the last index is a ligand number
    for i, lines in enumerate(line):
        a = lines.split()
        b = a[1].strip("." + act_chain)
        INDX_ZONE.append(int(b))
f.close()

with open("ZONE.txt",'w') as f:
    f.write(str(INDX_ZONE))
f.close()
# select residues numbers   

with open("model0.pdb", "r") as f:
    line = f.readlines()
    tmp = []
    for i, lines in enumerate(line):
        if lines.startswith("ATOM"):
            a = lines.split()
            tmp.append(int(a[5]))
            unique = list(set(tmp))
            INDX_REC = sorted(unique,key = int)         
            INDX_REC.append(INDX_ZONE[-1])
f.close()


# select second structure line  

with open("INFO.txt", "r") as f:
    line = f.readlines()
    for i, lines in enumerate(line):
        if lines.startswith("protocols.DsspMover: "):
            a = lines.split()
            LINE = list(a[1])
            LINE.append('LIG')
f.close()

# assigning a secondary structure to residue number

zip_it = zip(INDX_REC,LINE)
SEC_STRUCT = dict(zip_it)

with open("SEC_STRUCT.txt",'w') as f:
    f.write(str(SEC_STRUCT))
f.close()

# select loops

with open("LOOPS.txt","w") as f:
    for i in range(0,len(INDX_ZONE)):
        if SEC_STRUCT[INDX_ZONE[i]] == "L":
            f.write(str(INDX_ZONE[i])+ "\n")
f.close()