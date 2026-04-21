import numpy as np

class EntanglementEngine:

    def __init__(self, field):
        self.field = field

    def covariance(self):
        flat = self.field.reshape(-1)
        return np.outer(flat, flat)

    def entropy(self):
        cov = self.covariance()
        eigvals = np.linalg.eigvalsh(cov + 1e-8*np.eye(cov.shape[0]))
        eigvals = eigvals[eigvals > 0]
        return -np.sum(eigvals * np.log(eigvals))
