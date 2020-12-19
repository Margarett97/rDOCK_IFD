import os
from parameters import *

os.chdir(work_dir)

names = []

with open("NAME.txt",'r') as f:
    line = f.readlines()
    for j, lines in enumerate(line):
        a = lines.split()
        names.append(a[0])
f.close()


for i in range(0,int(no_poses)):    
    os.rename(names[i],"model" + str(i) + "_opt.pdb")
