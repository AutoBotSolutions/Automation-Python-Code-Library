# vacuum_lattice.py

import numpy as np

class VacuumLattice:

    def __init__(self, size=256):
        self.size = size
        self.field = np.random.normal(0, 1, (size, size))

    def energy_density(self):
        return np.mean(self.field**2)

    def apply_plate_boundary(self, gap_width):
        mask = np.ones((self.size, self.size))
        center = self.size // 2
        mask[:, center-gap_width:center+gap_width] = 0
        self.field *= mask

    def renormalize(self):
        self.field -= np.mean(self.field)

    def step(self):
        noise = np.random.normal(0, 0.1, (self.size, self.size))
        self.field += noise
        self.renormalize()
