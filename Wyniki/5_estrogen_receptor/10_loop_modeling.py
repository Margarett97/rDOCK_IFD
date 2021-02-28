from pyrosetta import *
from pyrosetta.toolbox import *

from pyrosetta.rosetta.protocols.loops import *
from pyrosetta.rosetta.protocols.jumping import *

from pyrosetta.rosetta.core.fragment import *
from pyrosetta.rosetta.protocols.simple_moves import *
from pyrosetta.rosetta.protocols.loops.loop_closure.ccd import *
from pyrosetta.rosetta.protocols.loops.loop_mover.refine import *
from pyrosetta.rosetta.core.pack.task import *
from pyrosetta.rosetta.protocols.minimization_packing import *
import math

from pyrosetta.rosetta.protocols.loops.loop_closure.kinematic_closure import *

init()


# uwzglednienie ligandu

p = Pose()


res_set = generate_nonstandard_residue_set(p,['P9.params'])
pose = pose_from_file(p, res_set, "MODEL9.pdb")


starting_p = Pose()
starting_p.assign(p)

# score

scorefxn_high = create_score_function('ref2015')  


# fold tree

ft = FoldTree()
ft.add_edge(1,38,-1)
ft.add_edge(38,41,-1)
ft.add_edge(38,46,1)
ft.add_edge(46,42,-1)
ft.add_edge(46,78,-1)
ft.add_edge(78,82,-1)
ft.add_edge(78,86,2)
ft.add_edge(86,83,-1)
ft.add_edge(86,111,-1)
ft.add_edge(111,115,-1)
ft.add_edge(111,120,3)
ft.add_edge(120,116,-1)
ft.add_edge(120,225,-1)

print(ft)


ft.check_fold_tree()
p.fold_tree(ft)


# definiowanie petli

loop1 = Loop(40, 44, 41)
loop2 = Loop(80, 84, 82)
loop3 = Loop(113, 118, 115)


loops = Loops()
loops.add_loop(loop1)
loops.add_loop(loop2)
loops.add_loop(loop3)

kic_mover = KinematicMover()
kic_mover.set_pivots(40,41,44)
kic_mover.set_pivots(80,82,84) 
kic_mover.set_pivots(113,115,118)  
kic_mover.apply(p)


print("set up job distributor")
jd = PyJobDistributor("model9_opt", 1 ,scorefxn_high)
jd.native_pose = starting_p

while (jd.job_complete == False):

  loop_refine = LoopMover_Refine_KIC(loops)
  loop_refine.apply(p)

  jd.output_decoy(p)

