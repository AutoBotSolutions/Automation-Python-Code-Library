@app.callback(
    Output('field-plot', 'figure'),
    Input('interval-component', 'n_intervals'),
    State('alpha-slider','value'),
    State('beta-slider','value'),
    ...
)
def update_dashboard(n, alpha, beta, ...):
    # Evolve fields
    psi_list = evolve_step(psi_list, ...)
    # Compute observables
    vortices = [detect_vortices(p) for p in psi_list]
    coherence = [torch.abs(p).mean().item() for p in psi_list]
    # Generate plotly figures
    fig = generate_figures(psi_list, vortices)
    return fig
