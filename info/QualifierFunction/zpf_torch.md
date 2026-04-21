# zpf_torch.py

**Path:** `QualifierFunction/zpf_torch.py`

**Automation Type:** General Automation
**Lines:** 23

## Purpose

zpf_torch.py

## Usage Pattern

Object-oriented - Provides classes and methods

## Dependencies

- `torch`

## Functions

### __init__

**Parameters:** self, dim

### apply_constraint

**Parameters:** self, C

### energy

**Parameters:** self

### renormalize

**Parameters:** self

### step

**Parameters:** self

## Classes

### ZPFTensor

**Methods:**
- `__init__`
- `apply_constraint`
- `energy`
- `renormalize`
- `step`

## Code Examples

### __init__

```python
def __init__(self, dim):
        super().__init__()
        self.state = torch.randn(dim, device="cuda")
```

### apply_constraint

```python
def apply_constraint(self, C):
        self.state = C @ self.state
```

### energy

```python
def energy(self):
        return torch.sum(self.state**2)
```

