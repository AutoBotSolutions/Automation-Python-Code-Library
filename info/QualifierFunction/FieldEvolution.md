# FieldEvolution.py

**Path:** `QualifierFunction/FieldEvolution.py`

**Automation Type:** General Automation
**Lines:** 29

## Purpose

Field update step for N x N complex tensor Laplacian via roll (discrete diffusion) Multi-field evolution Cross-field coupling Euler integration

## Usage Pattern

Function-based - Provides reusable functions

## Functions

### evolve_step

**Parameters:** psi_list, alpha_list, beta_list, gamma_list, pump_list, kappa, dt

### laplacian

**Parameters:** f

## Code Examples

### laplacian

```python
def laplacian(f):
        return torch.roll(f, 1, 0) + torch.roll(f, -1, 0) + \
               torch.roll(f, 1, 1) + torch.roll(f, -1, 1) - 4*f
```

