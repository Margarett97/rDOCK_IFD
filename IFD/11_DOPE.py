import os
from modeller import *
from modeller.automodel import *
from modeller.scripts import complete_pdb
from modeller.optimizers import molecular_dynamics, conjugate_gradients
from modeller.automodel import autosched

from parameters import *

os.chdir(work_dir)

#DOPE
for i in range(0,int(no_poses)):

        env = environ()
        env.io.hetatm = True
        env.libs.topology.read(file='$(LIB)/top_heav.lib')
        env.libs.parameters.read(file='$(LIB)/par.lib')
        env.io.atom_files_directory = work_dir

        md= complete_pdb(env, './'+'model'+str(i)+'_opt.pdb')
	
        sel=selection(md)
        sel1=sel.only_het_residues()
        sel2=sel1.select_sphere(5)
        sel3=sel2.only_std_residues()
        sel4=sel3.by_residue()


       
        sel4.energy()

        md.restraints.unpick_all()
        md.restraints.pick(sel4)
        print("DOPE VALUE")
        atmsel=selection(md)
        atmsel.assess_dope()
        print("DOPE FOR SELECTED RESIDUES")
        sel4.assess_dope()
