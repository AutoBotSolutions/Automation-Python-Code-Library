# zpf_engine.py

import numpy as np

class ZPFEngine:

    def __init__(self, dim):
        self.state = np.random.normal(0, 1, dim)

    def apply_constraint(self, constraint_matrix):
        self.state = constraint_matrix @ self.state

    def energy(self):
        return np.dot(self.state, self.state)

    def gradient(self):
        return 2 * self.state

    def renormalize(self):
        self.state -= np.mean(self.state)
