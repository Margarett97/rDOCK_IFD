import os

from parameters import *

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



