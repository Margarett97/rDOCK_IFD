from parameters import *
import os

os.chdir(work_dir)

with open(receptor + ".pdb", "r") as f:        # ligand selection from receptor file
    line = f.readlines()
    with open(rec_ligand + ".pdb" , "w") as n:
        for i, lines in enumerate(line):
            if lines.startswith("HETATM"):
                a = lines.split()
                if a[3] == rec_ligand:
                    n.write(lines)
n.close()

with open(receptor + ".pdb", "r") as f:        # receptor selection
    line = f.readlines()              
    with open(receptor+ "_prep.pdb" , "w") as n:
        for i, lines in enumerate(line):
            if lines.startswith("ATOM"):
                n.write(lines)
n.close()
                
