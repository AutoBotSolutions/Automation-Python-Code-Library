# SubstrateCore.py

**Path:** `QualifierFunction/SubstrateCore.py`

**Automation Type:** General Automation
**Lines:** 24

## Usage Pattern

Object-oriented - Provides classes and methods

## Functions

### __init__

**Parameters:** self, dim

### apply_constraint

**Parameters:** self, C

### update_metric

**Parameters:** self

### entropy_proxy

**Parameters:** self

### forward

**Parameters:** self, C

## Classes

### SubstrateCore

**Methods:**
- `__init__`
- `apply_constraint`
- `update_metric`
- `entropy_proxy`
- `forward`

## Code Examples

### __init__

```python
def __init__(self, dim):
        self.zpf = ZPFTensor(dim)
        self.metric = torch.ones(dim, device="cuda")
```

### apply_constraint

```python
def apply_constraint(self, C):
        self.zpf.apply_constraint(C)
```

### update_metric

```python
def update_metric(self):
        energy = self.zpf.energy()
        self.metric += 0.001 * energy
```

