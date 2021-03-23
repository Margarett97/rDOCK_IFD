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
ft.add_edge(1,177,-1)
ft.add_edge(177,180,-1)
ft.add_edge(177,183,1)
ft.add_edge(183,181,-1)
ft.add_edge(183,186,-1)
ft.add_edge(186,189,-1)
ft.add_edge(186,193,2)
ft.add_edge(193,190,-1)
ft.add_edge(193,232,-1)
ft.add_edge(232,235,-1)
ft.add_edge(232,239,3)
ft.add_edge(239,236,-1)
ft.add_edge(239,543,-1)

print(ft)


ft.check_fold_tree()
p.fold_tree(ft)


# definiowanie petli

loop1 = Loop(179, 181, 180)
loop2 = Loop(188, 191, 189)
loop3 = Loop(234, 237, 235)


loops = Loops()
loops.add_loop(loop1)
loops.add_loop(loop2)
loops.add_loop(loop3)

kic_mover = KinematicMover()
kic_mover.set_pivots(179,190,181)
kic_mover.set_pivots(188,189,191) 
kic_mover.set_pivots(234,235,237)  
kic_mover.apply(p)


print("set up job distributor")
jd = PyJobDistributor("model0_opt", 1 ,scorefxn_high)
jd.native_pose = starting_p

while (jd.job_complete == False):

  loop_refine = LoopMover_Refine_KIC(loops)
  loop_refine.apply(p)

  jd.output_decoy(p)

