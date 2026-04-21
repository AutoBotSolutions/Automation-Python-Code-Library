# zpf_substrate.py

**Path:** `QualifierFunction/zpf_substrate.py`

**Automation Type:** General Automation
**Lines:** 17

## Purpose

zpf_substrate.py

## Library Context

This script is part of the general automation library, providing utility functions for common automation tasks.

## Key Features

No specific features documented.

## Usage Pattern

Object-oriented - Provides classes and methods

## Dependencies

- `numpy`

## Function Descriptions

- __init__ - Parameters: self, grid_size. Performs a specific operation.
- apply_boundary - Parameters: self, mask. Performs a specific operation.
- energy_density - Parameters: self. Performs a specific operation.
- renormalize - Parameters: self. Performs a specific operation.

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

## External APIs

No external API interactions identified.

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

### renormalize

```python
def renormalize(self):
        self.grid -= np.mean(self.grid)
```

