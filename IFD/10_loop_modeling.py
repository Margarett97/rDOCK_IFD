# Loop refinement of an existing model
from modeller import *
from modeller.automodel import *
#from modeller import soap_loop
import os
from parameters import *

os.chdir(work_dir)

log.verbose()
env = environ()
env.io.hetatm = True

# directories for input atom files
env.io.atom_files_directory = work_dir

# Create a new class based on 'loopmodel' so that we can redefine
# select_loop_atoms (necessary)
class MyLoop(loopmodel):
    # This routine picks the residues to be refined by loop modeling
    def select_loop_atoms(self):
        select=selection(m)
        select1=select.only_het_residues()  # selection of ligand
        select2=select1.select_sphere(5)    # selection of all atoms within 5A of ligand
        select3=select2.only_std_residues() 
        select4=select3.by_residue()
        
        return select4

for i in range(0,int(no_poses)):    
    m = MyLoop(env,
           inimodel='model' + str(i) + '.pdb',   # initial model of the target
           sequence= 'model' + str(i),      # MODEL NAME : model1.BL000X000Y.pdf X- model number, Y -(starting_model:ending_model)
           loop_assess_methods=assess.DOPE) 


    m.loop.starting_model= 1           # index of the first loop model
    m.loop.ending_model  = 1           # index of the last loop model
    m.loop.md_level = refine.fast  # loop refinement method

    m.make()
    m.write(file = 'model' + str(i) + '_opt.pdb')


