from pyrosetta import *
from pyrosetta.toolbox import *
from pyrosetta.rosetta.protocols.loops import *
init()

##  WCZYTANIE PLIKU PDB  ##
pose = pose_from_pdb("2acr.pdb")  ## z bazy pdb 

# dssp = pyrosetta.rosetta.protocols.moves.DsspMover()
# dssp.apply(pose)
# ss = pose.secstruct()
# print(ss.number(18))
res = pose.residue()
print(res)
a = select_loop_residues(res)
print(a)