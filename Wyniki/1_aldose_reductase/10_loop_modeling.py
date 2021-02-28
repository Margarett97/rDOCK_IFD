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
ft.add_edge(1,16,-1)
ft.add_edge(16,19,-1)
ft.add_edge(16,23,1)
ft.add_edge(23,20,-1)
ft.add_edge(23,206,-1)
ft.add_edge(206,211,-1)
ft.add_edge(206,218,2)
ft.add_edge(218,212,-1)
ft.add_edge(218,258,-1)
ft.add_edge(258,261,-1)
ft.add_edge(258,264,3)
ft.add_edge(264,262,-1)
ft.add_edge(264,316,-1)

print(ft)


ft.check_fold_tree()
p.fold_tree(ft)


# definiowanie petli

loop1 = Loop(18, 21, 19)
loop2 = Loop(208, 216, 212)
loop3 = Loop(260, 262, 261)


loops = Loops()
loops.add_loop(loop1)
loops.add_loop(loop2)
loops.add_loop(loop3)

kic_mover = KinematicMover()
kic_mover.set_pivots(18,19,21)
kic_mover.set_pivots(208,212,216) 
kic_mover.set_pivots(260,261,262)  
kic_mover.apply(p)


print("set up job distributor")
jd = PyJobDistributor("model9_opt", 1 ,scorefxn_high)
jd.native_pose = starting_p

while (jd.job_complete == False):

  loop_refine = LoopMover_Refine_KIC(loops)
  loop_refine.apply(p)

  jd.output_decoy(p)

