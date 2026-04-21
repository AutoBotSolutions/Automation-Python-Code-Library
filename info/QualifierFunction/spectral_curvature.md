# spectral_curvature.py

**Path:** `QualifierFunction/spectral_curvature.py`

**Automation Type:** General Automation
**Lines:** 7

## Usage Pattern

Function-based - Provides reusable functions

## Dependencies

- `numpy`

## Functions

### spectral_curvature

**Parameters:** adj

## Code Examples

### spectral_curvature

```python
def spectral_curvature(adj):
    D = np.diag(np.sum(adj, axis=1))
    L = D - adj
    eigvals = np.linalg.eigvalsh(L)
    return np.var(eigvals)
```

