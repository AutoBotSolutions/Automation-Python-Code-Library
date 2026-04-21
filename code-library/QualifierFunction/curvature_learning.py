import torch

class CurvatureLearner(torch.nn.Module):

    def __init__(self, dim):
        super().__init__()
        self.theta = torch.nn.Parameter(torch.randn(dim, device="cuda"))

    def loss(self):
        return torch.sum(self.theta**2)

    def fisher_metric(self):
        grad = torch.autograd.grad(self.loss(), self.theta, create_graph=True)[0]
        G = torch.outer(grad, grad) + 1e-3 * torch.eye(len(self.theta), device="cuda")
        return G

    def natural_step(self, lr=0.01):
        L = self.loss()
        grad = torch.autograd.grad(L, self.theta)[0]
        G = self.fisher_metric()
        G_inv = torch.linalg.inv(G)
        update = G_inv @ grad
        self.theta.data -= lr * update
