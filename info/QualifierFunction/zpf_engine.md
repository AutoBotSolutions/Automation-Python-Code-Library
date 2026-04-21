# zpf_engine.py

**Path:** `QualifierFunction/zpf_engine.py`

**Automation Type:** General Automation
**Lines:** 20

## Purpose

zpf_engine.py

## Usage Pattern

Object-oriented - Provides classes and methods

## Dependencies

- `numpy`

## Functions

### __init__

**Parameters:** self, dim

### apply_constraint

**Parameters:** self, constraint_matrix

### energy

**Parameters:** self

### gradient

**Parameters:** self

### renormalize

**Parameters:** self

## Classes

### ZPFEngine

**Methods:**
- `__init__`
- `apply_constraint`
- `energy`
- `gradient`
- `renormalize`

## Code Examples

### __init__

```python
def __init__(self, dim):
        self.state = np.random.normal(0, 1, dim)
```

### apply_constraint

```python
def apply_constraint(self, constraint_matrix):
        self.state = constraint_matrix @ self.state
```

### energy

```python
def energy(self):
        return np.dot(self.state, self.state)
```

