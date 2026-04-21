# entanglement_engine.py

**Path:** `QualifierFunction/entanglement_engine.py`

**Automation Type:** General Automation
**Lines:** 16

## Usage Pattern

Object-oriented - Provides classes and methods

## Dependencies

- `numpy`

## Functions

### __init__

**Parameters:** self, field

### covariance

**Parameters:** self

### entropy

**Parameters:** self

## Classes

### EntanglementEngine

**Methods:**
- `__init__`
- `covariance`
- `entropy`

## Code Examples

### __init__

```python
def __init__(self, field):
        self.field = field
```

### covariance

```python
def covariance(self):
        flat = self.field.reshape(-1)
        return np.outer(flat, flat)
```

### entropy

```python
def entropy(self):
        cov = self.covariance()
        eigvals = np.linalg.eigvalsh(cov + 1e-8*np.eye(cov.shape[0]))
        eigvals = eigvals[eigvals > 0]
        return -np.sum(eigvals * np.log(eigvals))
```

