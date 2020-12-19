import os, re
from parameters import *

os.chdir(work_dir)

# select all DOPE values from log file
num = 1
with open("dope.log","r") as f:
    line = f.readlines()
    with open("all_DOPE.txt","w") as n:
        for i, lines in enumerate(line):
            for j in range(0,10):
                if lines.startswith("model" + str(j)):
                    n.write(lines)
    n.close()
f.close()

# select DOPE for model
with open("all_DOPE.txt",'r') as f:
    line = f.readlines()
    for i in range(0,int(no_poses)):
        with open('model' + str(i) + "_DOPE.txt","w") as n:
            for j, lines in enumerate(line):
                if lines.startswith("model" + str(i)):
                    n.write(lines)
        n.close()
f.close()                

# Find best loop model for each pose
valu = []

for i in range(0,int(no_poses)):
    with open("DOPE.txt", "a") as f:
        with open("NAME.txt","a") as m:
            with open("model" + str(i) + "_DOPE.txt",'r') as n:
                line = n.readlines()
                for j, lines in enumerate(line):
                    a = lines.split()
                    valu.append(float(a[2]))
                    minim = min(valu)
                    indx = valu.index(minim)
                    val = line[indx].split()
    
            m.write(val[0] + "\n")
        f.write(str(i) + "  " + val[2] + "\n")
    valu.clear()
    n.close()
    m.close()
    f.close()


# remove files        
for i in range(0,int(no_poses)):
    os.remove("model" + str(i) + "_DOPE.txt")
        
                   


      
                    
          
 
                
           
