# constraint_field.py

**Path:** `QualifierFunction/constraint_field.py`

**Automation Type:** General Automation
**Lines:** 8

## Usage Pattern

Object-oriented - Provides classes and methods

## Functions

### __init__

**Parameters:** self, dim

### update

**Parameters:** self, entropy_gradient, lr

## Classes

### ConstraintField

**Methods:**
- `__init__`
- `update`

## Code Examples

### __init__

```python
def __init__(self, dim):
        self.C = torch.randn(dim, dim, device="cuda")
```

### update

```python
def update(self, entropy_gradient, lr=0.001):
        self.C += lr * entropy_gradient
        self.C = (self.C + self.C.T) / 2
```

