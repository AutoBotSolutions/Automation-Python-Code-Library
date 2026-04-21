# zpf_torch.py

**Path:** `QualifierFunction/zpf_torch.py`

**Automation Type:** General Automation
**Lines:** 23

## Purpose

zpf_torch.py

## Library Context

This script is part of the general automation library, providing utility functions for common automation tasks.

## Usage Pattern

Object-oriented - Provides classes and methods

## Dependencies

- `torch`

## Function Descriptions

- __init__ - Parameters: self, dim. Performs a specific operation.
- apply_constraint - Parameters: self, C. Performs a specific operation.
- energy - Parameters: self. Performs a specific operation.
- renormalize - Parameters: self. Performs a specific operation.
- step - Parameters: self. Performs a specific operation.

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

### renormalize

```python
def renormalize(self):
        self.state -= torch.mean(self.state)
```

### step

```python
def step(self):
        noise = torch.randn_like(self.state)
        self.state += 0.01 * noise
        self.renormalize()
```

