# vacuum_modes.py

import numpy as np

hbar = 1.054e-34
c = 3e8

def casimir_energy(a, n_max=500):
    energy = 0.0
    for n in range(1, n_max):
        k_n = n * np.pi / a
        energy += 0.5 * hbar * c * k_n
    return energy

if __name__ == "__main__":
    a = 1e-7
    print(casimir_energy(a))
