from pyrosetta import *
from pyrosetta.toolbox import *

init()

pose = pose_from_rcsb("2acr")

dssp = pyrosetta.rosetta.protocols.moves.DsspMover()    
dssp.apply(pose)
 