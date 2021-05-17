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

from parameters import *
import os 

os.chdir(work_dir)


## PARAMETERS:

kT = 1.0
smallmoves = 3 
shearmoves = 5
backbone_angle_max = 7
cycles = 9
jobs = 1


## LOOP PREPARE

with open("LOOPS.txt","r") as f:
    line = f.readlines()
    tmp = []
    with open("SEC_STRUCT.txt","r") as n:
        for i, res in enumerate(line):
            tmp.append(int(res))
    n.close()
f.close()

LOOP = []
for j in range(len(tmp)-1):

    if tmp[j] == tmp[j+1] - 1:
        LOOP.append(tmp[j])
        LOOP.append(tmp[j+1])
        LOOP = list(set(LOOP))
        LOOP = sorted(LOOP, key = int)
    elif len(LOOP) == 0:
        LOOP.append(tmp[j])     
        
edge = []  # len(edge) +1 -> number of loops
for j in range(len(LOOP)-1):
    if LOOP[j] != LOOP[j+1] -1:
        edge.append(LOOP.index(LOOP[j+1]))
no_loops = len(edge)  + 1

with open("ZONE.txt","r") as f:
    line = f.readlines()
    X = [] # final loops
    CP = [] # cut points
    for i, val in enumerate(line):
        zone = list(map(int, val.strip("][").split(",")))

    for i in range(no_loops):
        if i == 0:
            if no_loops == 1:
                X.append(LOOP[:])
            else:
                X.append(LOOP[0:edge[i]])
        else:
            if i == no_loops-1:
                X.append(LOOP[edge[i-1]:])
            else:
                X.append(LOOP[edge[i-1]:edge[i]])
    
        if len(X[i]) == 2 :

            if X[i][0]-1 in zone:
                a = X[i][0]-1
                X[i].append(a)
                X[i] = sorted(X[i], key = int)
                
            elif  X[i][1]+1 in zone:
                a = X[i][1]+1
                X[i].append(a)
            else:
                a = X[i][1]+1
                X[i].append(a)
                
        elif len(X[i]) < 2:
            a = X[i][0]+1
            b =  X[i][0]-1   
            X[i].append(a)
            X[i].append(b)
            X[i] = sorted(X[i], key = int)
           
        
        if len(X[i]) % 2 == 0:
            b = X[i][int(len(X[i])/2)]
            CP.append(b-1)
        else:    
            b = X[i][int(len(X[i])/2)]
            CP.append(b)
                   
f.close()


## LOOP OPTIMIZATION:

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


    # create loops

    ft = FoldTree()
    loops = Loops()
    for j in range(len(X)):
        loopX = Loop(X[j][0],X[j][-1], CP[j])
        loops.add_loop(loopX)

    fold_tree_from_loops(p, loops, ft)
    
      
    print(ft)

    ft.check_fold_tree()
    p.fold_tree(ft)   


    #create a MoveMap, all backbone torsions free

    movemap = MoveMap()
    movemap.set_bb(False)

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
    for j in range(len(X)):
        kic_mover.set_pivots(X[j][0],CP[j], X[j][-1])
    
    kic_mover.apply(p)
      
    print("set up job distributor")
    jd = PyJobDistributor("model"+str(i)+"_opt", 1 ,scorefxn)
    jd.native_pose = starting_p

    while (jd.job_complete == False):
        
        refinement.apply(p)
        loop_refine = LoopMover_Refine_KIC(loops)
        loop_refine.apply(p)

        jd.output_decoy(p)

