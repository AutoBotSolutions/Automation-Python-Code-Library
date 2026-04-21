def detect_vortices(psi):
    phase = torch.angle(psi)
    vortices = torch.zeros_like(phase)

    for i in range(N-1):
        for j in range(N-1):
            loop = [
                phase[i,j],
                phase[i+1,j],
                phase[i+1,j+1],
                phase[i,j+1],
                phase[i,j]
            ]
            total = 0
            for k in range(4):
                diff = torch.atan2(torch.sin(loop[k+1]-loop[k]),
                                   torch.cos(loop[k+1]-loop[k]))
                total += diff
            if torch.abs(total) > 5.5:  # ~2π threshold
                vortices[i,j] = 1

    return vortices
