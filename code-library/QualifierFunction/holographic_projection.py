import torch

class HolographicProjection:

    def __init__(self, bulk_dim, boundary_dim):
        self.P = torch.randn(boundary_dim, bulk_dim, device="cuda")

    def project(self, bulk_state):
        return self.P @ bulk_state
