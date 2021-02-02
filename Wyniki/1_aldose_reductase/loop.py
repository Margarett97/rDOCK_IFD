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

init()


# uwzglednienie ligandu

p = Pose()


res_set = generate_nonstandard_residue_set(p,['P3.params'])
pose = pose_from_file(p, res_set, "model2.pdb")


starting_p = Pose()
starting_p.assign(p)

# score

scorefxn_low = create_score_function('cen_std')
scorefxn_high = create_score_function('ref2015')  


# definiowanie petli

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

movemap.set_chi(True)

print("setting up movers")
#backbone movers
fragset3mer = ConstantLengthFragSet(3, "2acr.frag3")
mover_3mer = ClassicFragmentMover(fragset3mer, movemap)

ccd_closure1 = CCDLoopClosureMover(loop1, movemap)
ccd_closure2 = CCDLoopClosureMover(loop2, movemap)
ccd_closure3 = CCDLoopClosureMover(loop3, movemap)

#centroid/fullatom conversion movers
to_centroid = SwitchResidueTypeSetMover('centroid')
to_fullatom = SwitchResidueTypeSetMover('fa_standard')
recover_sidechains = ReturnSidechainMover(starting_p)

#set up sidechain packer movers
task_pack = TaskFactory.create_packer_task(starting_p)
task_pack.restrict_to_repacking()
task_pack.or_include_current( True )
pack = PackRotamersMover( scorefxn_high, task_pack )

#convert to centroid mode
to_centroid.apply(p)

starting_p_centroid = Pose()
starting_p_centroid.assign(p)

print("set up job distributor")
jd = PyJobDistributor("loop_output", 1 ,scorefxn_high)
jd.native_pose = starting_p

while (jd.job_complete == False):
  p.assign(starting_p_centroid)

  print("randomizing loop")
  for i in range(18, 21+1):
    p.set_phi(i, -180)
    p.set_psi(i, 180)
    
  for i in range(208, 216+1):
    p.set_phi(i, -180)
    p.set_psi(i, 180)
    
  for i in range(260, 262+1):
    p.set_phi(i, -180)
    p.set_psi(i, 180)
    
  for i in range(18, 21+1):
    mover_3mer.apply(p)
    
  for i in range(268, 216+1):
    mover_3mer.apply(p)
    
  for i in range(260, 262+1):
    mover_3mer.apply(p)
    
  print("low res loop modeling")
  outer_cycles = 10
  inner_cycles = 30

  #simulated annealing incrementing kT geometrically from 2.0 to 0.8
  init_temp = 2.0
  final_temp = 0.8
  gamma = math.pow((final_temp/init_temp),(1.0/(outer_cycles*inner_cycles)))
  kT = init_temp

  mc = MonteCarlo(p, scorefxn_low, kT)

  for i in range(1,outer_cycles+1):
    mc.recover_low(p)
    scorefxn_low(p)
    for j in range(1, inner_cycles+1):
      kT = kT * gamma
      mc.set_temperature(kT)
      mover_3mer.apply(p)
      ccd_closure1.apply(p)
      ccd_closure2.apply(p)
      ccd_closure3.apply(p)
      mc.boltzmann(p)
  mc.recover_low(p)

  print("high-res refinement")
  #no fragment insertions in refinement, only small/shear moves and sidechain packing
  to_fullatom.apply(p)
  recover_sidechains.apply(p)
  pack.apply(p)



  my_loops = Loops()
  my_loops.add_loop(loop1)
  my_loops.add_loop(loop2)
  my_loops.add_loop(loop3)  
  add_single_cutpoint_variant(p, loop1)
  add_single_cutpoint_variant(p, loop2)
  add_single_cutpoint_variant(p, loop3)
  loop_refine = LoopMover_Refine_CCD(my_loops)
  loop_refine.apply(p)

  print("outputting decoy...")
  Lrms = loop_rmsd(p, starting_p, my_loops, True)
  jd.additional_decoy_info = " Lrmsd: " + str(Lrms)
  jd.output_decoy(p)