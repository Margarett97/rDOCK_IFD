from pyrosetta import *
from pyrosetta.toolbox import *

from pyrosetta.rosetta.protocols.generalized_kinematic_closure import *
from pyrosetta.rosetta.protocols.loops import *

init()

## LOAD FILES

p = Pose()


res_set = generate_nonstandard_residue_set(p,['P1.params'])
pose = pose_from_file(p, res_set, "MODEL1.pdb")


starting_p = Pose()
starting_p.assign(p)


## SCORE

ref15sfxn = create_score_function('ref2015')  
bb_only = create_score_function('empty')  


## BUILDING LOOP GEOMETRY

loop1 = Loop(18, 21, 19)
loop2 = Loop(208, 216, 212)
loop3 = Loop(260, 262, 261)


loops = Loops()
loops.add_loop(loop1)
loops.add_loop(loop2)
loops.add_loop(loop3)

add_single_cutpoint_variant(p, loop1)
add_single_cutpoint_variant(p, loop2)
add_single_cutpoint_variant(p, loop3)

movemap = MoveMap()
movemap.set_bb_true_range(18, 21)  # set backbone torsions between the residues
movemap.set_bb_true_range(208, 216)
movemap.set_bb_true_range(260, 262)

