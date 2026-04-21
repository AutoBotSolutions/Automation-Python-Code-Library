from sklearn.decomposition import PCA

def embed_to_pump(embedding, psi_shape, amplitude=1.0, sigma=5):
    # Reduce to 2D coordinate
    pca = PCA(n_components=2)
    coord = pca.fit_transform(embedding.reshape(1, -1))[0]
    x_idx = int((coord[0] - coord[0].min())/(coord[0].ptp() + 1e-6) * psi_shape[0])
    y_idx = int((coord[1] - coord[1].min())/(coord[1].ptp() + 1e-6) * psi_shape[1])
    
    # Gaussian pump
    x = torch.arange(psi_shape[0])
    y = torch.arange(psi_shape[1])
    X, Y = torch.meshgrid(x, y, indexing='ij')
    pump = amplitude * torch.exp(-((X-x_idx)**2 + (Y-y_idx)**2)/sigma**2)
    return pump.cuda()
