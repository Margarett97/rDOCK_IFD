import os, subprocess, shutil

from parameters import *


os.system("alias python=python3")

subprocess.run(["python", "11_DISTANCE.py"],shell=True)
