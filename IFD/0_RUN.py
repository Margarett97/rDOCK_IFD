import os, subprocess, shutil



with open("parameters.py","a") as f:
    name1 = "soft = '"
    name2 = "hard = '"
    name3 = "work_dir = '/home/malgorzata/Desktop/rDOCK_IFD/Wyniki/1_aldose_rductase'" ##DO USUNIĘCIA
    name4 = "dock_dir = '/home/malgorzata/Desktop/rDock_2013.1_src'" ## DO USUNIĘCIA
    name5 = "receptor = '2acr'" ## DO USUNIĘCIA
    name6 = "ligand = 'TOL'" ## DO USUNIĘCIA
    name7 = ("rec_ligand = 'NAP'")## DO USUNIĘCIA
    f.write(name1 + "soft_docking.prm' \n")
    f.write(name2 + "hard_docking.prm' \n")
    f.write(name3 + "\n")## DO USUNIĘCIA
    f.write(name4 + "\n")## DO USUNIĘCIA
    f.write(name5 + "\n")## DO USUNIĘCIA
    f.write(name6 + "\n")## DO USUNIĘCIA
    f.write(name7 + "\n")## DO USUNIĘCIA
f.close()

from parameters import *

chimera_dir = "/home/malgorzata/.local/UCSF-Chimera64-1.13.1/bin/chimera"  ##DO USUNIĘCIA
    

## CREATE NEW FOLDER:

new_dir = work_dir + "/IFD"
if not os.path.exists(new_dir):
    os.makedirs(new_dir)

## SOFT DOCKING:

os.system("alias python=python3")

subprocess.run(["python", "1_path_change.py"])

subprocess.run(["python", "2_prepare.py"])

subprocess.run(["python", "3_extension.py"])

subprocess.run(["python", "4_cavity_prep.py"])

subprocess.run(["python", "5_soft_docking.py"])

subprocess.run(["python", "6_chain.py"])

subprocess.run(["python", "7_poses.py"])

subprocess.run(["python", "8_poses_chain.py"])

subprocess.run([chimera_dir, "--nogui", "--script", "9_write_models.py"])

with open(work_dir + "/dope.log", "w") as out:
    subprocess.run(["python", "10_MODELLER.py"], stdout = out)

subprocess.run(["python", "11_DISTANCE.py"])
