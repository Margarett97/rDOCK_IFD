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
ft.add_edge(1,74,-1)
ft.add_edge(74,80,-1)
ft.add_edge(74,86,1)
ft.add_edge(86,81,-1)
ft.add_edge(86,273,-1)



print(ft)


ft.check_fold_tree()
p.fold_tree(ft)


# definiowanie petli

loop1 = Loop(76, 84, 80)




loops = Loops()
loops.add_loop(loop1)



kic_mover = KinematicMover()
kic_mover.set_pivots(76, 80, 84)
kic_mover.apply(p)


print("set up job distributor")
jd = PyJobDistributor("model0_opt", 1 ,scorefxn_high)
jd.native_pose = starting_p

while (jd.job_complete == False):

  loop_refine = LoopMover_Refine_KIC(loops)
  loop_refine.apply(p)

  jd.output_decoy(p)
