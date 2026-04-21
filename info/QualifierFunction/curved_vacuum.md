# curved_vacuum.py

**Path:** `QualifierFunction/curved_vacuum.py`

**Automation Type:** General Automation
**Lines:** 24

## Purpose

curved_vacuum.py

## Usage Pattern

Object-oriented - Provides classes and methods

## Dependencies

- `numpy`

## Functions

### __init__

**Parameters:** self, size

### inject_mass

**Parameters:** self, x, y, strength

### update

**Parameters:** self

### energy_density

**Parameters:** self

## Classes

### CurvedVacuum

**Methods:**
- `__init__`
- `inject_mass`
- `update`
- `energy_density`

## Code Examples

### __init__

```python
def __init__(self, size=256):
        self.size = size
        self.field = np.random.normal(0, 1, (size, size))
        self.curvature = np.zeros((size, size))
```

### inject_mass

```python
def inject_mass(self, x, y, strength=10):
        for i in range(self.size):
            for j in range(self.size):
                r = np.sqrt((i-x)**2 + (j-y)**2)
                self.curvature[i, j] += strength / (1 + r)
```

### update

```python
def update(self):
        noise = np.random.normal(0, 1, (self.size, self.size))
        self.field += noise * (1 + self.curvature)
        self.field -= np.mean(self.field)
```

