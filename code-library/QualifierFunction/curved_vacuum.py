# curved_vacuum.py

import numpy as np

class CurvedVacuum:

    def __init__(self, size=256):
        self.size = size
        self.field = np.random.normal(0, 1, (size, size))
        self.curvature = np.zeros((size, size))

    def inject_mass(self, x, y, strength=10):
        for i in range(self.size):
            for j in range(self.size):
                r = np.sqrt((i-x)**2 + (j-y)**2)
                self.curvature[i, j] += strength / (1 + r)

    def update(self):
        noise = np.random.normal(0, 1, (self.size, self.size))
        self.field += noise * (1 + self.curvature)
        self.field -= np.mean(self.field)

    def energy_density(self):
        return np.mean(self.field**2)
