from parameters import *
import os, subprocess

os.chdir(work_dir)

#subprocess.run(["obabel", "soft_dock.sd", "-O", "soft_dock.pdb"])



with open("soft_dock.pdb", "r") as f:
    line = f.readlines()
    for i in range(0,10):
        with open("pose" + str(i) + ".pdb", "w") as n:
            for j, lines in enumerate(line):
               if lines.startswith("MODEL        " + str(i+1)):
                   n.write(lines)
               
               
                     
                   
                    
                    
              
                   
        n.close()
f.close()
                
                
        

       
    
        
 
        
    
