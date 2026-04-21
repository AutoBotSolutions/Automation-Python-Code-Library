# dynamic_metric.py

import numpy as np

class DynamicMetricVacuum:

    def __init__(self, size=32, dt=0.01):
        self.size = size
        self.dt = dt

        self.phi = np.random.normal(0, 1, (size, size, size))
        self.phi_dot = np.zeros_like(self.phi)

        # simplified scalar curvature proxy
        self.metric = np.ones((size, size, size))

    def laplacian(self, field):
        return (
            np.roll(field,1,0) + np.roll(field,-1,0) +
            np.roll(field,1,1) + np.roll(field,-1,1) +
            np.roll(field,1,2) + np.roll(field,-1,2)
            - 6*field
        )

    def stress_energy(self):
        grad = self.laplacian(self.phi)
        return grad**2

    def update_metric(self):
        T = self.stress_energy()
        self.metric += self.dt * T
        self.metric -= np.mean(self.metric)

    def step(self):
        self.phi_dot += self.dt * self.metric * self.laplacian(self.phi)
        self.phi += self.dt * self.phi_dot
        self.phi -= np.mean(self.phi)
        self.update_metric()

    def total_energy(self):
        return np.mean(self.phi**2 + self.phi_dot**2)
