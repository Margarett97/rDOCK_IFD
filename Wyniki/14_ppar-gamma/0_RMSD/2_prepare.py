import os
from pdbtools import *
from tmp import *

os.system("pdb_selchain -D " + ref + ".pdb > " + ref + ".log")
pre, ext = os.path.splitext(ref + ".pdb")
os.rename(ref + ".log", pre + ".pdb")
os.system("pdb_delelem -H " + ref + ".pdb  > " + ref + ".log")
pre, ext = os.path.splitext(ref + ".pdb")
os.rename(ref + ".log", pre + ".pdb")
