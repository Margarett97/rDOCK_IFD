import os

from parameters import *
os.chdir(work_dir)


#SCORE

num = 0
with open("DOCK.sd") as f:
    line = f.readlines()
    with open("HARD_SCORE.txt","w") as n:
        for i,lines in enumerate(line):
            if lines.startswith(">  <SCORE.INTER>"):
                n.write(str(num) + "  " + line[i+1])
                num += 1
            
    n.close()        
f.close()
