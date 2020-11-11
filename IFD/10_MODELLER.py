# models optimization
import os
from modeller import *
from modeller.automodel import *
from modeller.scripts import complete_pdb
from modeller.optimizers import molecular_dynamics, conjugate_gradients
from modeller.automodel import autosched

from parameters import *

os.chdir(work_dir)


#PARAMETRY:

model_name = 'model'

# CONJUGATE GRADIENTS MINIMIZATION                                                                                 

def optimize(atmsel, sched):                                                                                                   

     for step in sched:
         step.optimize(atmsel, max_iterations=200, min_atom_shift=0.001)
    
     refine(atmsel)  # MD SUMULATION
     cg = conjugate_gradients()
     cg.optimize(atmsel, max_iterations=200, min_atom_shift=0.001) # CG SIMULATION


# MOLECULAR DYNAMICS WITH SIMULATED ANNEALING

def refine(atmsel):
     
     md = molecular_dynamics(cap_atom_shift=0.39, md_time_step=4.0,
                             md_return='FINAL')
     init_vel = True
     for (its, equil, temps) in ((200, 20, (150.0, 250.0, 400.0, 700.0, 1000.0)),
                                 (200, 600,
                                  (1000.0, 800.0, 600.0, 500.0, 400.0, 300.0))):
         for temp in temps:
             md.optimize(atmsel, init_velocities=init_vel, temperature=temp,
                         max_iterations=its, equilibrate=equil)
             init_vel = False
 

# DIHEDRAL ANGLE RESTRAINTS - to increase level of accuracy                       
def make_restraints(mdl1, aln):
     rsr = mdl1.restraints
     rsr.clear()
     s = selection(mdl1)
     for typ in ('stereo', 'phi-psi_binormal'):
        rsr.make(s, restraint_type=typ, aln=aln, spline_on_site=True)
     for typ in ('omega', 'chi1', 'chi2', 'chi3', 'chi4'):
        rsr.make(s, restraint_type=typ+'_dihedral', spline_range=4.0,
                 spline_dx=0.3, spline_min_points = 5, aln=aln,
                 spline_on_site=True)
 


#PREPARE ALIGNMENT FILE:                                                                              


env = environ()
env.io.atom_files_directory = [work_dir]

#Create a new empty alignment and model 
aln = alignment(env)
mdl = model(env)

#Read receptor file and add the model sequence to the alignment
mdl.read(file=receptor, model_segment=('FIRST:@', 'END:'))
aln.append_model(mdl, align_codes=receptor, atom_files=receptor)

#Read model file and add the model sequence to the alignment
mdl.read(file=model_name+'0', model_segment=('FIRST:@', 'END:'))
aln.append_model(mdl, align_codes=model_name+'0', atom_files=model_name+'0')

# Align them by sequence
aln.malign(gap_penalties_1d=(-500, -300))
aln.write(file='alignment.ali')

# Align them by structure
aln.malign3d(gap_penalties_3d=(0.0, 2.0))

# check the alignment for its suitability for modeling
aln.check()
aln.write(file='myAlignment.ali')

alig='myAlignment.ali'


# LOOP:

### Comparative modeling by the automodel class
##from modeller import *
##from modeller.automodel import *    # Load the automodel class
##
##log.verbose()
##env = environ()
##
### directories for input atom files
##env.io.atom_files_directory = ['.', '../atom_files']
##
##a = loopmodel(env,
##              alnfile  = alig,     # alignment filename
##              knowns   = receptor,              # codes of the templates
##              sequence = model+str(i))              # code of the target
##a.starting_model= 1                 # index of the first model
##a.ending_model  = 1                 # index of the last model
##                                    # (determines how many models to calculate)
##a.md_level = None                   # No refinement of model
##
##a.loop.starting_model = 1           # First loop model
##a.loop.ending_model   = 4           # Last loop model
##a.loop.md_level       = refine.fast # Loop model refinement level
##
##a.make()   




# OPTIMIZATION:


for i in range(0,int(no_poses)):
	env = environ(rand_seed=-49837)
	env.io.hetatm = True

        ## NON-BONDED ENERGY TERMS  
	
	#soft sphere potential
	env.edat.dynamic_sphere=False #turn off the soft-sphere 
	#lennard-jones potential (more accurate)
	env.edat.dynamic_lennard=True
	env.edat.contact_shell = 4.0
	env.edat.update_dynamic = 0.39

	env.io.atom_files_directory = work_dir

	env.libs.parameters.read(file='$(LIB)/par.lib')
	env.libs.topology.read(file='$(LIB)/top_heav.lib')

	mdl1= complete_pdb(env, './' + model_name + str(i) +'.pdb')
	mdl=complete_pdb(env, './' + receptor + '.pdb')
	print(mdl1.residues[0])

	## DIHEDRAL ANGLES PREDICTED BY USE OF KNOWN TEMPLATE STRUCTURE (PREPARE ALIGNMENT FILE) 
	ali = alignment(env)
	ali.append(file = alig,align_codes = 'all')
	modelname = model_name + '.pdb'
	ali.append_model(mdl1, atom_files = modelname, align_codes = modelname)


        ## DIHEDRAL ANGLE RESTRAINTS (USE HOMOLOGS AND DIHEDRAL LIBRARY)  
	mdl1.env.edat.nonbonded_sel_atoms = 1  # selected region "feels" the rest of system through the non-bonded terms
	sched = autosched.loop.make_for_model(mdl1)
	make_restraints(mdl1, ali) #model
	sel = selection(mdl) #receptor
	mdl.restraints.make(sel, restraint_type='LJ14', spline_on_site=False)

        ## RESIDUES TO OPTIMIZE
	select=selection(mdl1)
	select1=select.only_het_residues()  # selection of ligand
	select2=select1.select_sphere(5)    # selection of all atoms within 5A of ligand
	select3=select2.only_std_residues() # select only standard residues (ATOM)
	select4=select3.by_residue()        # select etire residue
	mdl1.restraints.unpick_all()
	mdl1.restraints.pick(select4) # pick restraints for selected atoms

	select4.energy()
	select4.randomize_xyz(deviation = 4.0) # randomize selected coordinates

	mdl1.env.edat.nonbonded_sel_atoms = 2  # optimized atoms will not "feel" the rest of system through the non-bonded terms  
	optimize(select4, sched) 

	mdl1.env.edat.nonbonded_sel_atoms=1   # selected region "feels" the rest of system through the non-bonded terms
	optimize(select4, sched)

	select4.energy()

	atmsel2=selection(mdl1) 
	score2=atmsel2.assess_dope() # calculate DOPE
	
	mdl1.write(file=model_name+str(i)+'_opt.pdb')



	





	

	

	
	
     
 
