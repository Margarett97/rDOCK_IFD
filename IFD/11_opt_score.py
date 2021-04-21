import os, shutil 
from parameters import *

path = os.getcwd()
os.chdir(work_dir)

values = []
for i in range(0,10):
    with open("model" + str(i) + "_opt.fasc", 'r') as f:
        with open("OPT_SCORE_ALL.txt", "a") as n:
            lines = f.readlines()
            for j,line in enumerate(lines):
                n.write(str(i) +"   " + line + "\n")
                a = line.split()
                values.append(a[45]) 
        n.close()
    f.close()
    
    

min_score = values.index(min(values))
os.chdir(work_dir)

shutil.copy(work_dir + "/" + "model" + str(min_score) + "_opt_0.pdb" , work_dir + "/IFD/" + "model" + str(min_score) + "_opt_0.pdb" )     

with open("parameters.py", "a") as p:
    name ='best_opt ='
    p.write(name + "model" + str(min_score) + "_opt" + "\n")
    
