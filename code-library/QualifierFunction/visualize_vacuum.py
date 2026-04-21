# visualize_vacuum.py

import matplotlib.pyplot as plt
from vacuum_lattice import VacuumLattice

vac = VacuumLattice(256)

plt.imshow(vac.field, cmap="inferno")
plt.colorbar()
plt.title("Zero-Point Field Snapshot")
plt.show()
