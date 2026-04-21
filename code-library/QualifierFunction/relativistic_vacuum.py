# relativistic_vacuum.py

import numpy as np

class RelativisticVacuum3D:

    def __init__(self, size=64, dt=0.01):
        self.size = size
        self.dt = dt

        self.field = np.random.normal(0, 1, (size, size, size))
        self.velocity = np.zeros_like(self.field)

        # simple metric tensor (flat Minkowski baseline)
        self.metric = np.ones((size, size, size))

    def inject_mass(self, x, y, z, strength=10):
        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    r = np.sqrt((i-x)**2 + (j-y)**2 + (k-z)**2)
                    self.metric[i,j,k] += strength/(1+r)

    def laplacian(self):
        return (
            np.roll(self.field,1,0) + np.roll(self.field,-1,0) +
            np.roll(self.field,1,1) + np.roll(self.field,-1,1) +
            np.roll(self.field,1,2) + np.roll(self.field,-1,2)
            - 6*self.field
        )

    def step(self):
        curvature_weighted = self.metric * self.laplacian()
        self.velocity += self.dt * curvature_weighted
        self.field += self.dt * self.velocity
        self.field -= np.mean(self.field)

    def energy_density(self):
        return np.mean(self.field**2 + self.velocity**2)
