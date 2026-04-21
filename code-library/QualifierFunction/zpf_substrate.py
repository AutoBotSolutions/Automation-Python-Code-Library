# zpf_substrate.py

import numpy as np

class ZeroPointField:

    def __init__(self, grid_size):
        self.grid = np.random.normal(0, 1, (grid_size, grid_size))

    def apply_boundary(self, mask):
        self.grid *= mask

    def energy_density(self):
        return np.mean(self.grid**2)

    def renormalize(self):
        self.grid -= np.mean(self.grid)
