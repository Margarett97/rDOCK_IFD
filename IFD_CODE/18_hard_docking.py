# soft docking protocole
from parameters import *
import os, subprocess

os.chdir(work_dir)

os.environ["RBT_ROOT"] = dock_dir
os.environ["LD_LIBRARY_PATH"] = dock_dir+ "/lib"
os.environ["PATH"] = dock_dir + "/bin"

subprocess.call(["rbcavity", "-was", "-d", "-r", "cavity.prm"])
subprocess.call(["rbdock", "-i",ligand + ".sd", "-o", "DOCK", "-r", "cavity.prm", "-p", "dock.prm", "-n"+ no_poses])



