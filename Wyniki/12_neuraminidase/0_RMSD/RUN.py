import subprocess

chimera_dir ='/home/malgorzata/chimera/bin'

subprocess.run([chimera_dir + "/chimera",  "--nogui", "--script", "18_RMSD.py"])
