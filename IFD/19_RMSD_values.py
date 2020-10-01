import os

os.chdir(rmsd_dir)

num = 0
with open(ligand + ".pdb", "r") as f:
    line = f.readlines()
    for i,lines in enumerate(line):
        if lines.startswith("HETATM"):
            num += 1


start = ("RMSD between" + str(num))



with open("RMSD.txt", "a") as f:
    with open("soft.txt", "r") as s:
        a = s.read()
        if a.startswith(start):
            name1 = "SOFT: "
            f.write(name1 + a + "\n")
    s.close()
    with open("hard.txt", "r") as h:
         b = h.read()
        if b.startswith(start):
            name2 = "HARD: "
            f.write(name2 + b + "\n")
    h.close()       
f.close()   
            


