from parameters import *
import os, subprocess

#os.chdir(work_dir)



subprocess.run(["export", "RBT_ROOT=" + dock_dir ], shell = True)
subprocess.run(["export", "LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$RBT_ROOT/lib"], shell = True)
subprocess.run(["export", "PATH=$PATH:$RBT_ROOT/bin"], shell = True)

subprocess.run(["rbcavity", "-was", "-d", "-r", "cavity.prm"], cwd = work_dir, shell = True)

subprocess.run(["rbdock", "-i", ligand + ".sd", "-o", "DOCK.sd", "-r", "cavity.prm", "-p", "soft_docking.prm", "-n", "10"], cwd = work_dir, shell = True)
