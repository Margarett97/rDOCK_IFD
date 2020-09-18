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
with open("dope.log") as f:
    line = f.readlines()
    with open("DOPE.txt", "w") as n:
        for i,lines in enumerate(line):
            if lines.startswith("DOPE score               :"):
                value = lines.split(":")[1]
                n.write(str(num) + "   " + value)
    n.close()
f.close()

    

#SCORE

num = 0
with open("soft_dock.sd") as f:
    line = f.readlines()
    with open("SOFT_SCORE.txt","w") as n:
        for i,lines in enumerate(line):
            if lines.startswith(">  <SCORE.INTER>"):
                n.write(str(num) + "  " + line[i+1])
                num += 1
            
    n.close()        
f.close()




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

data = pd.DataFrame(
    {
    "POSES" : ['pose0','pose1','pose2','pose3','pose4','pose5','pose6','pose7','pose8','pose9'],   
    "col1" : [0,1,2,3,4,5,6,7,8,9],
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






