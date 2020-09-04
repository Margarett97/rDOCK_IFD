# save score to file
from parameters import *
import os

os.chdir(work_dir)

num = 0
values = []
with open("soft_dock.sd") as f:
    line = f.readlines()
    with open("SOFT_SCORE.txt","w") as n:
        for i,lines in enumerate(line):
            if lines.startswith(">  <SCORE.INTER>"):
                n.write("pose" + str(num) + ":" + line[i+1])
                values.append(float(line[i+1]))
                num += 1
        minimum = min(values)
        n.write("MINIMUM VALUE: pose" + str(values.index(minimum)) + ": " + str(minimum))
            
    n.close()        
f.close()



            
           
            
                
