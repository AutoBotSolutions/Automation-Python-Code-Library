import plotly.express as px
fig = px.imshow(abs(psi.cpu().numpy())**2, color_continuous_scale='Viridis')
fig.show()

phase = torch.angle(psi).cpu().numpy()
vortex_mask = detect_vortices(psi).cpu().numpy()

fig = px.imshow(phase, color_continuous_scale='twilight')
fig.add_scatter(x=vortex_mask.nonzero()[1], y=vortex_mask.nonzero()[0],
                mode='markers', marker=dict(color='red', size=5))
fig.show()

import scipy.ndimage as nd
amplitude = abs(psi.cpu().numpy())**2
smooth = nd.gaussian_filter(amplitude, sigma=1)
fig = px.imshow(smooth, color_continuous_scale='Viridis')
fig.show()

fig = make_subplots(rows=1, cols=3)
fields = [psi1, psi2, psi3]  # Analytical, Creative, Ethical
for i, f in enumerate(fields):
    fig.add_trace(px.imshow(abs(f.cpu().numpy())**2).data[0], row=1, col=i+1)
fig.show() 
