import torch

class TensorSpacetime(torch.nn.Module):

    def __init__(self, nodes):
        super().__init__()
        self.state = torch.randn(nodes, device="cuda")
        self.adj = torch.randn(nodes, nodes, device="cuda")
        self.adj = (self.adj + self.adj.T) / 2  # symmetric

    def entanglement_matrix(self):
        return torch.outer(self.state, self.state)

    def graph_laplacian(self):
        D = torch.diag(torch.sum(self.adj, dim=1))
        return D - self.adj

    def geometric_spectrum(self):
        L = self.graph_laplacian()
        eigvals = torch.linalg.eigvalsh(L)
        return eigvals

    def step(self):
        noise = torch.randn_like(self.state)
        self.state += 0.01 * noise
        self.state -= torch.mean(self.state)
