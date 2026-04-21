class ConstraintField:

    def __init__(self, dim):
        self.C = torch.randn(dim, dim, device="cuda")

    def update(self, entropy_gradient, lr=0.001):
        self.C += lr * entropy_gradient
        self.C = (self.C + self.C.T) / 2
