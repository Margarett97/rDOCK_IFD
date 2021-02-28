import os

from parameters import *

path = os.getcwd()
os.chdir(work_dir)


#SCORE

VALUES = []
num = 0
with open("DOCK.sd") as f:
    line = f.readlines()
    with open("SCORE.txt","w") as n:
        for i,lines in enumerate(line):
            if lines.startswith(">  <SCORE.INTER>"):
                n.write(str(num) + "  " + line[i+1])
                VALUES.append(float(line[i+1].strip()))
                num += 1
            
    n.close()        
f.close()



os.chdir(path)
with open("parameters.py","a") as p:
    minimum = VALUES.index(min(VALUES))
    name1 = "best_score2 ='"
    name2 = "best_pose2 ='"
    p.write(name1 + "model" + str(minimum) + "'\n")
    p.write(name2 + "pose" + str(minimum) + "'\n")

