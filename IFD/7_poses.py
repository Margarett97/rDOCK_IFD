# save poses to file
from parameters import *
import os, subprocess

os.chdir(work_dir)

subprocess.call(["obabel", "soft_dock.sd", "-O", "soft_dock.pdb"])

num = 0

with open("soft_dock.pdb") as f:
    for line in f:
        with open("pose" + str(num) + ".pdb", "a+") as n:
            n.write(line)
        if line.find("ENDMDL") != -1 :
            num += 1
         
        
               
               
                
              


                
        

       
    
        
 
        
    
