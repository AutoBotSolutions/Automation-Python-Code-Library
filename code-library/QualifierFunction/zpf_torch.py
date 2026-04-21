# zpf_torch.py

import torch

class ZPFTensor(torch.nn.Module):

    def __init__(self, dim):
        super().__init__()
        self.state = torch.randn(dim, device="cuda")

    def apply_constraint(self, C):
        self.state = C @ self.state

    def energy(self):
        return torch.sum(self.state**2)

    def renormalize(self):
        self.state -= torch.mean(self.state)

    def step(self):
        noise = torch.randn_like(self.state)
        self.state += 0.01 * noise
        self.renormalize()
