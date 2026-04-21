class SubstrateCore:

    def __init__(self, dim):
        self.zpf = ZPFTensor(dim)
        self.metric = torch.ones(dim, device="cuda")

    def apply_constraint(self, C):
        self.zpf.apply_constraint(C)

    def update_metric(self):
        energy = self.zpf.energy()
        self.metric += 0.001 * energy

    def entropy_proxy(self):
        state = self.zpf.state
        cov = torch.outer(state, state)
        eigvals = torch.linalg.eigvalsh(cov + 1e-6*torch.eye(len(state), device="cuda"))
        eigvals = eigvals[eigvals > 0]
        return -torch.sum(eigvals * torch.log(eigvals))

    def forward(self, C):
        self.apply_constraint(C)
        self.update_metric()
        return self.entropy_proxy()
