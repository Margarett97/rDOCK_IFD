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

shutil.copy(work_dir + "/" + "model" + str(min_score) + "_opt_0.pdb" , work_dir + "/HARD_DOCKING/" + "model" + str(min_score) + "_opt_0.pdb" )     

os.chdir(path)
with open("parameters.py", "a") as p:
    name = "work_dir='"
    name2 ="receptor ='" 
    name3 ="best_opt ='"
    
    p.write(name3 + "model" + str(min_score) + "_opt_0" + "'\n")
    p.write(name + work_dir + "HARD_DOCKING/" +"'\n")
    p.write(name2 + "ligand_remove" + "'\n")
    
    
    
    
