class ZeroPointEmergenceLayer:

    def __init__(self, dim):
        self.zpf = ZPFTensor(dim)

    def forward(self, constraint_matrix):
        self.zpf.apply_constraint(constraint_matrix)
        emergent_signal = self.zpf.energy()
        return emergent_signal
