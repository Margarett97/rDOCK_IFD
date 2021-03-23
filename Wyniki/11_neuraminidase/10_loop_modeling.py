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


res_set = generate_nonstandard_residue_set(p,['P0.params'])
pose = pose_from_file(p, res_set, "MODEL0.pdb")


starting_p = Pose()
starting_p.assign(p)

# score

scorefxn_high = create_score_function('ref2015')  


# fold tree

ft = FoldTree()
ft.add_edge(1,70,-1)
ft.add_edge(70,73,-1)
ft.add_edge(70,76,1)
ft.add_edge(76,74,-1)
ft.add_edge(76,142,-1)
ft.add_edge(142,145,-1)
ft.add_edge(142,149,2)
ft.add_edge(149,146,-1)
ft.add_edge(149,165,-1)
ft.add_edge(165,168,-1)
ft.add_edge(165,171,3)
ft.add_edge(171,169,-1)
ft.add_edge(171,391,-1)

print(ft)


ft.check_fold_tree()
p.fold_tree(ft)


# definiowanie petli

loop1 = Loop(70, 74, 73)
loop2 = Loop(144, 147, 145)
loop3 = Loop(167, 169, 168)


loops = Loops()
loops.add_loop(loop1)
loops.add_loop(loop2)
loops.add_loop(loop3)

kic_mover = KinematicMover()
kic_mover.set_pivots(70, 73, 74)
kic_mover.set_pivots(144, 145, 147) 
kic_mover.set_pivots(167, 168, 169)  
kic_mover.apply(p)


print("set up job distributor")
jd = PyJobDistributor("model0_opt", 1 ,scorefxn_high)
jd.native_pose = starting_p

while (jd.job_complete == False):

  loop_refine = LoopMover_Refine_KIC(loops)
  loop_refine.apply(p)

  jd.output_decoy(p)

