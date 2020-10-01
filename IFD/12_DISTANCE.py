import os, shutil 
import numpy as np
from collections import OrderedDict
import pandas as pd
from plotnine import *

from parameters import *

path = os.getcwd()
os.chdir(work_dir)

#DOPE

num = 0
dope_valu = []
with open("dope.log") as f:
    line = f.readlines()
    for i,lines in enumerate(line):
        if lines.startswith("DOPE score               :"):
            value = lines.split(":")[1] 
            dope_valu.append(value)
f.close()

with open("DOPE.txt", "w") as n:
    for i in range(0,len(dope_valu)):
        if i % 2 == 1:
            n.write(str(num) + "   " + dope_valu[i])
            num += 1
n.close()


    

#SCORE

num = 0
VALUES = []
with open("DOCK.sd") as f:
    line = f.readlines()
    with open("SOFT_SCORE.txt","w") as n:
        for i,lines in enumerate(line):
            if lines.startswith(">  <SCORE.INTER>"):
                n.write(str(num) + "  " + line[i+1])
                VALUES.append(line[i+1])
                num += 1
            
    n.close()        
f.close()

minimum = VALUES.index(min(VALUES))


#DISTANCE

DOPE = open(work_dir + '/' + 'DOPE.txt', 'r')
SCORE = open(work_dir + '/' + 'SOFT_SCORE.txt', 'r')


dope = np.loadtxt(DOPE)
dope = dope[:,1]

score = np.loadtxt(SCORE)
score = score[:,1]


dope_norm = abs(dope)/max(abs(dope))
score_norm = abs(score)/max(abs(score))


DISTANCE = np.sqrt((pow(score_norm,2) + pow(dope_norm,2)))
    
## Wykres



POSES = []
NUM = []

for i in range(0,int(no_poses)):
    poses = "pose" + str(i)
    POSES.append(poses)
    num = i
    NUM.append(num)


data = pd.DataFrame(
    {
    "POSES" : POSES,   
    "col1" : NUM,
    "col2" : DISTANCE
    }
    )

gg = ggplot(data , aes(x = 'POSES', y = 'DISTANCE', size='2', color='POSES')) +\
    geom_point() +\
    ggtitle('Optimized distance: ' + receptor)

ggsave(plot = gg, filename ='DISTANCE')

#choose max value:

pose_num = data["col2"].idxmax()

pose = ("model" + str(pose_num) + "_opt")

os.chdir(path)
with open("parameters.py", "a") as p:
    name = "best_pose= '"
    p.write(name + pose + "'\n")
p.close()


shutil.copy(work_dir + "/" + pose + ".pdb", work_dir + "/IFD/" + pose + ".pdb") 
shutil.copy(work_dir + "/" + ligand + ".pdb", work_dir + "/IFD/" + ligand + ".pdb")
shutil.copy(work_dir + "/" + rec_ligand + ".pdb", work_dir + "/IFD/" + rec_ligand + ".pdb") 
shutil.copy(work_dir + "/" + apo + ".pdb", work_dir + "/IFD/" + apo + ".pdb")

with open("parameters.py", "a") as p:
    name1 = "work_dir='"
    name2 = "receptor ='ligand_remove'\n" 
    name3 = "best_score ='"
    p.write(name1 + work_dir+ "/IFD'\n")
    p.write(name2)
    p.write(name + "model" + str(minimum) + "'\n")








