# move docking files in rDOCK path

from parameters import * 
import os, shutil

path = os.getcwd()

shutil.copy(path + "/docking_files/" + soft, dock_dir + "/data/scripts/" + soft)
#shutil.copy(path + "/docking_files/" + hard, dock_dir + "/data/scripts/" + hard)

    
shutil.copy(path + "/docking_files/cavity.prm", work_dir + "/cavity.prm")

shutil.copy(path + "/docking_files/cavity.prm", work_dir + "/IFD/cavity.prm")
