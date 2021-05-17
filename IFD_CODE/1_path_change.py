# move docking files in rDOCK path

from parameters import * 
import os, shutil

path = os.getcwd()

shutil.copy(path + "/docking_files/" + soft, dock_dir + "/data/scripts/" + soft)
    
shutil.copy(path + "/docking_files/cavity.prm", work_dir + "/cavity.prm")

shutil.copy(path + "/docking_files/cavity.prm", work_dir + "/HARD_DOCKING/cavity.prm")

shutil.copy(work_dir + "/" + ligand + ".pdb", work_dir + "/HARD_DOCKING/" + ligand + ".pdb")

shutil.copy(work_dir + "/" + rec_ligand + ".pdb", work_dir + "/HARD_DOCKING/" + rec_ligand + ".pdb")

shutil.copy(work_dir + "/" + receptor + ".pdb", work_dir + "/HARD_DOCKING/" + receptor + ".pdb")