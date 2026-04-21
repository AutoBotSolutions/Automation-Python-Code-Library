# zpf_substrate.py

**Path:** `QualifierFunction/zpf_substrate.py`

**Automation Type:** General Automation
**Lines:** 17

## Purpose

zpf_substrate.py

## Usage Pattern

Object-oriented - Provides classes and methods

## Dependencies

- `numpy`

## Functions

### __init__

**Parameters:** self, grid_size

### apply_boundary

**Parameters:** self, mask

### energy_density

**Parameters:** self

### renormalize

**Parameters:** self

## Classes

### ZeroPointField

**Methods:**
- `__init__`
- `apply_boundary`
- `energy_density`
- `renormalize`

## Code Examples

### __init__

```python
def __init__(self, grid_size):
        self.grid = np.random.normal(0, 1, (grid_size, grid_size))
```

### apply_boundary

```python
def apply_boundary(self, mask):
        self.grid *= mask
```

### energy_density

```python
def energy_density(self):
        return np.mean(self.grid**2)
```

