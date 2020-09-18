# put file names in cavity.prm
from parameters import *
import os, re

os.chdir(work_dir)

with open("cavity.prm", "r+") as f:
    file = f.read()
    file = re.sub("%", receptor + "_prep.mol2", file)
    file = re.sub("&", rec_ligand + ".sd", file)
    f.seek(0)
    f.write(file)
    f.truncate()
f.close()


