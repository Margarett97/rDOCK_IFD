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


kT = 1.0
smallmoves = 3 
shearmoves = 5
backbone_angle_max = 7
cycles = 9
jobs = 1

init()


for i in range(0,10): 

    p = Pose()


    res_set = generate_nonstandard_residue_set(p,['P'+str(i)+'.params'])
    pose = pose_from_file(p, res_set, 'MODEL'+str(i)+'.pdb')

    # create a reference copy of the pose in fullatom

    starting_p = Pose()
    starting_p.assign(p)

    # score

    scorefxn = create_score_function('ref2015')  # or 'standard'

    # fold tree

    ft = FoldTree()
    ft.add_edge(1,71,-1)
    ft.add_edge(71,74,-1)
    ft.add_edge(71,77,1)
    ft.add_edge(77,75,-1)
    ft.add_edge(77,134,-1)
    ft.add_edge(134,137,-1)
    ft.add_edge(134,140,2)
    ft.add_edge(140,138,-1)
    ft.add_edge(140,278,-1)


    print(ft)


    ft.check_fold_tree()
    p.fold_tree(ft)


    # definiowanie petli

    loop1 = Loop(73, 75, 74)
    loop2 = Loop(136, 138,137 )


    loops = Loops()
    loops.add_loop(loop1)
    loops.add_loop(loop2)

    ##create a MoveMap, all backbone torsions free

    movemap = MoveMap()
    movemap.set_bb(True)

    ## create a SmallMover

    smallmover = SmallMover(movemap, kT, smallmoves)
    smallmover.angle_max(backbone_angle_max)

    ## create a ShearMover

    shearmover = ShearMover(movemap, kT, shearmoves)
    shearmover.angle_max(backbone_angle_max)

    ## create a MinMover, for backbone torsion minimization

    minmover = MinMover()
    minmover.movemap(movemap)
    minmover.score_function(scorefxn)

    ##setup a PackRotamersMover
    to_pack = standard_packer_task(starting_p)
    to_pack.restrict_to_repacking()    # prevents design, packing only
    to_pack.or_include_current(True)    # considers the original sidechains
    packmover = PackRotamersMover(scorefxn, to_pack)

    ##setup a RepeatMover on a TrialMover of a SequenceMover

    combined_mover = SequenceMover()
    combined_mover.add_mover(smallmover)
    combined_mover.add_mover(shearmover)
    combined_mover.add_mover(minmover)
    combined_mover.add_mover(packmover)

    mc = MonteCarlo(p, scorefxn, kT)

    trial = TrialMover(combined_mover, mc)

    refinement = RepeatMover(trial, cycles)



    kic_mover = KinematicMover()
    kic_mover.set_pivots(73, 74, 75)
    kic_mover.set_pivots(136, 138, 140) 
    kic_mover.apply(p)


    print("set up job distributor")
    jd = PyJobDistributor("model"+str(i)+"_opt", 1 ,scorefxn)
    jd.native_pose = starting_p

    while (jd.job_complete == False):

        refinement.apply(p)
        loop_refine = LoopMover_Refine_KIC(loops)
        loop_refine.apply(p)

        jd.output_decoy(p)


