# Field update step for N x N complex tensor
def evolve_step(psi_list, alpha_list, beta_list, gamma_list, pump_list, kappa=0.05, dt=0.01):
    N = psi_list[0].shape[0]
    dpsi_list = []

    # Laplacian via roll (discrete diffusion)
    def laplacian(f):
        return torch.roll(f, 1, 0) + torch.roll(f, -1, 0) + \
               torch.roll(f, 1, 1) + torch.roll(f, -1, 1) - 4*f

    # Multi-field evolution
    for idx, psi in enumerate(psi_list):
        lap = alpha_list[idx] * laplacian(psi)
        nonlinear = beta_list[idx] * torch.abs(psi)**2 * psi
        pump = pump_list[idx]
        dpsi = lap + nonlinear + (pump - gamma_list[idx]) * psi
        dpsi_list.append(dpsi)

    # Cross-field coupling
    for i, psi in enumerate(psi_list):
        for j, psi_other in enumerate(psi_list):
            if i != j:
                dpsi_list[i] += kappa * psi * psi_other

    # Euler integration
    for i in range(len(psi_list)):
        psi_list[i] = psi_list[i] + dt * dpsi_list[i]

    return psi_list
