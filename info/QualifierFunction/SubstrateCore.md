# SubstrateCore.py

**Path:** `QualifierFunction/SubstrateCore.py`

**Automation Type:** General Automation
**Lines:** 24

## Library Context

This script is part of the general automation library, providing utility functions for common automation tasks.

## Usage Pattern

Object-oriented - Provides classes and methods

## Function Descriptions

- __init__ - Parameters: self, dim. Performs a specific operation.
- apply_constraint - Parameters: self, C. Performs a specific operation.
- update_metric - Parameters: self. Performs a specific operation.
- entropy_proxy - Parameters: self. Performs a specific operation.
- forward - Parameters: self, C. Performs a specific operation.

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

### entropy_proxy

```python
def entropy_proxy(self):
        state = self.zpf.state
        cov = torch.outer(state, state)
        eigvals = torch.linalg.eigvalsh(cov + 1e-6*torch.eye(len(state), device="cuda"))
        eigvals = eigvals[eigvals > 0]
        return -torch.sum(eigvals * torch.log(eigvals))
```

### forward

```python
def forward(self, C):
        self.apply_constraint(C)
        self.update_metric()
        return self.entropy_proxy()
```

