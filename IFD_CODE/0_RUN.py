import os, subprocess, shutil



# with open("parameters.py","a") as f:
     # name1 = "soft = '"
     # f.write(name1 + "soft_docking.prm' \n")

# f.close()

# from parameters import *
   

# ## CREATE NEW FOLDER:

# new_dir = work_dir + "/HARD_DOCKING"
# if not os.path.exists(new_dir):
    # os.makedirs(new_dir)

# ## SOFT DOCKING:


# subprocess.run(["python3", "1_path_change.py"])

# subprocess.run(["python3", "2_prepare.py"])

# subprocess.run(["python3", "3_extension.py"])

# subprocess.run(["python3", "4_cavity_prep.py"])

# subprocess.run(["python3", "5_soft_docking.py"])

# subprocess.run(["python3", "6_poses.py"])

# subprocess.run(["python3", "7_poses_chain.py"])

# subprocess.run([chimera_dir + "/chimera",  "--nogui", "--script", "8_write_models.py"])

# subprocess.run(["python3", "9_SCORE.py"])  

# subprocess.run(["python3", "10_loop_prepare.py"])

# subprocess.run([chimera_dir + "/chimera",  "--nogui", "--script", "11_write_pyR_mdl.py"])

# ## SELECT LOOP STRUCTURE

# subprocess.run([chimera_dir + "/chimera",  "--nogui", "--script", "12_select_residues.py"])   

# with open(work_dir +"/INFO.txt", "w") as out:
    # subprocess.run(["python3", "13_find_loops.py"], stdout = out)  
# out.close()

# subprocess.run(["python3", "14_loop_to_opt.py"])

# subprocess.run(["python3", "15_loop_modeling.py"])

# subprocess.run(["python3", "16_opt_score.py"])


import parameters
from six.moves import reload_module
reload_module(parameters)

from parameters import *

# ##HARD DOCKING


subprocess.run([chimera_dir + "/chimera", "--nogui", "--script", "17_prep_sec_docking.py"])

subprocess.run(["python3", "2_prepare.py"])

subprocess.run(["python3", "3_extension.py"])

subprocess.run(["python3", "4_cavity_prep.py"])

subprocess.run(["python3", "18_hard_docking.py"])

subprocess.run(["python3", "6_poses.py"])

subprocess.run(["python3", "7_poses_chain.py"])

subprocess.run([chimera_dir + "/chimera", "--nogui", "--script", "8_write_models.py"])

subprocess.run(["python3", "19_SCORE.py"])


import parameters
from six.moves import reload_module
reload_module(parameters)

from parameters import *

subprocess.run([chimera_dir + "/chimera", "--gui", "--silent", "--script", "20_visualization.py"])

