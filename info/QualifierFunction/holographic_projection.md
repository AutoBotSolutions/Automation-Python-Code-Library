# holographic_projection.py

**Path:** `QualifierFunction/holographic_projection.py`

**Automation Type:** General Automation
**Lines:** 9

## Usage Pattern

Object-oriented - Provides classes and methods

## Dependencies

- `torch`

## Functions

### __init__

**Parameters:** self, bulk_dim, boundary_dim

### project

**Parameters:** self, bulk_state

## Classes

### HolographicProjection

**Methods:**
- `__init__`
- `project`

## Code Examples

### __init__

```python
def __init__(self, bulk_dim, boundary_dim):
        self.P = torch.randn(boundary_dim, bulk_dim, device="cuda")
```

### project

```python
def project(self, bulk_state):
        return self.P @ bulk_state
```

