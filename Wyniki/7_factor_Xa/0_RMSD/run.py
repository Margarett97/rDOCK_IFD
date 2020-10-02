import subprocess

from tmp import *


subprocess.run(["python3", "2_prepare.py"])

with open("soft.txt", "w") as out:
    subprocess.run([chimera_dir + "/chimera",  "--nogui", "--script", "18_RMSD.py"], stdout = out)
with open("hard.txt", "w") as out2:
    subprocess.run([chimera_dir + "/chimera",  "--nogui", "--script", "19_RMSD.py"], stdout = out2)
