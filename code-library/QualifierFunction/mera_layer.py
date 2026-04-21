class MERALayer(torch.nn.Module):

    def __init__(self, dim):
        super().__init__()
        self.U = torch.nn.Linear(dim, dim, bias=False)
        self.C = torch.nn.Linear(dim, dim//2)

    def forward(self, x):
        x = self.U(x)
        x = torch.tanh(x)
        return self.C(x)
