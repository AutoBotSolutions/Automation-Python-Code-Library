import numpy as np

def spectral_curvature(adj):
    D = np.diag(np.sum(adj, axis=1))
    L = D - adj
    eigvals = np.linalg.eigvalsh(L)
    return np.var(eigvals)
