import os

from parameters import *
os.chdir(work_dir)


#SCORE

VALUES = []
num = 0
with open("DOCK.sd") as f:
    line = f.readlines()
    with open("HARD_SCORE.txt","w") as n:
        for i,lines in enumerate(line):
            if lines.startswith(">  <SCORE.INTER>"):
                n.write(str(num) + "  " + line[i+1])
                VALUES.append(line[i+1])
                num += 1
            
    n.close()        
f.close()


with open("parameters.py","a") as p:
    minimum = VALUES.index(min(VALUES))
    name = "best_score2 ='"
    p.write(name + "model" + str(minimum) + "'\n")

