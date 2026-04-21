import torch
import torch.fft as fft

N = 128
dt = 0.01
alpha = 0.5
beta = 1.0
gamma = 0.3

# Initialize complex field
psi = torch.randn(N, N, dtype=torch.cfloat, device="cuda") * 0.01

def laplacian(field):
    return (
        torch.roll(field, 1, 0) +
        torch.roll(field, -1, 0) +
        torch.roll(field, 1, 1) +
        torch.roll(field, -1, 1) -
        4 * field
    )

def pump_field(x0, y0, amplitude=1.0, sigma=5):
    x = torch.arange(N, device="cuda")
    y = torch.arange(N, device="cuda")
    X, Y = torch.meshgrid(x, y, indexing="ij")
    return amplitude * torch.exp(-((X-x0)**2 + (Y-y0)**2)/sigma**2)

for step in range(10000):
    lap = laplacian(psi)
    nonlinear = beta * torch.abs(psi)**2 * psi
    pump = pump_field(N//2, N//2, amplitude=0.8)

    dpsi = alpha * lap + nonlinear + (pump - gamma) * psi
    psi = psi + dt * dpsi
