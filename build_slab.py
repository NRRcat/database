from ase.lattice.surface import *
from ase.constraints import FixAtoms
from ase.io import write

a=3.6149
slab = fcc111('Cu', size=(4,4,4), a=a, vacuum=6.0, orthogonal=True)
c = FixAtoms(mask=[x >2   for x in slab.get_tags()])
slab.set_constraint(c)
write('POSCAR',slab,format='vasp',direct=True)
