def detect_vortices(psi):
    phase = torch.angle(psi)
    vortices = torch.zeros_like(phase)

    N = psi.shape[0]
    for i in range(N-1):
        for j in range(N-1):
            loop = [phase[i,j], phase[i+1,j], phase[i+1,j+1], phase[i,j+1], phase[i,j]]
            total = sum(torch.atan2(torch.sin(loop[k+1]-loop[k]), torch.cos(loop[k+1]-loop[k])) for k in range(4))
            if torch.abs(total) > 5.5:  # ~2π
                vortices[i,j] = 1
    return vortices
