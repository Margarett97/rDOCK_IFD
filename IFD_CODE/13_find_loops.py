from pyrosetta import *
from pyrosetta.toolbox import *
import os

from parameters import *
os.chdir(work_dir)
init()

pose = pose_from_pdb("model1.pdb")

dssp = pyrosetta.rosetta.protocols.moves.DsspMover()    
dssp.apply(pose)