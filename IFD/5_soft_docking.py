# soft docking protocole
from parameters import *
import os, subprocess

os.chdir(work_dir)

os.environ["RBT_ROOT"] = dock_dir
os.environ["LD_LIBRARY_PATH"] = dock_dir+ "/lib"
os.environ["PATH"] = dock_dir + "/bin"

subprocess.run(["rbcavity", "-was", "-d", "-r", "cavity.prm"])
subprocess.run(["rbdock", "-i",ligand + ".sd", "-o", "soft_dock", "-r", "cavity.prm", "-p", "soft_docking.prm", "-n", "10"])



