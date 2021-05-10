import os, subprocess, shutil



# with open("parameters.py","a") as f:
     # name1 = "soft = '"
     # name2 = "hard = '"
     # f.write(name1 + "soft_docking.prm' \n")
     # f.write(name2 + "hard_docking.prm' \n")

# f.close()

from parameters import *
   

# CREATE NEW FOLDER:

# new_dir = work_dir + "/IFD"
# if not os.path.exists(new_dir):
    # os.makedirs(new_dir)

# ## SOFT DOCKING:


# subprocess.run(["python3", "1_path_change.py"])

# subprocess.run(["python3", "2_prepare.py"])

# subprocess.run(["python3", "3_extension.py"])

# subprocess.run(["python3", "4_cavity_prep.py"])

# subprocess.run(["python3", "5_soft_docking.py"])

# subprocess.run(["python3", "6_chain.py"])

# subprocess.run(["python3", "7_poses.py"])

# subprocess.run(["python3", "8_poses_chain.py"])

# subprocess.run([chimera_dir + "/chimera",  "--nogui", "--script", "9_write_models.py"])

# subprocess.run(["python3", "15_SCORE.py"])

# subprocess.run(["python3", "10a_loop_prepare.py"])

# subprocess.run([chimera_dir + "/chimera",  "--nogui", "--script", "9a_write_models.py"])

#subprocess.run(["python3", "10_MODELLER.py"])

#with open(work_dir + "/dope.log", "w") as out:
#subprocess.run(["python3", "10_loop_modeling.py"], stdout = out)

#with open(work_dir + "/dope.log", "w") as out:
#    subprocess.run(["python3", "11_DOPE.py"], stdout = out)

#subprocess.run(["python3", "12_DISTANCE.py"])


# import parameters
# from six.moves import reload_module
# reload_module(parameters)

# from parameters import *

# ##HARD DOCKING


#subprocess.run([chimera_dir + "/chimera", "--nogui", "--script", "13_prep_sec_docking.py"])

subprocess.run(["python3", "3_extension.py"])

subprocess.run(["python3", "4_cavity_prep.py"])

subprocess.run(["python3", "14_hard_docking.py"])

subprocess.run(["python3", "6_chain.py"])

subprocess.run(["python3", "7_poses.py"])

subprocess.run(["python3", "8_poses_chain.py"])

subprocess.run([chimera_dir + "/chimera", "--nogui", "--script", "9_write_models.py"])

subprocess.run(["python3", "15_SCORE.py"])


# import parameters
# from six.moves import reload_module
# reload_module(parameters)

##from parameters import *
##
##subprocess.run([chimera_dir + "/chimera", "--gui", "--silent", "--script", "16_visualization.py"])

