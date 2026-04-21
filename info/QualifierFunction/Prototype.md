# Prototype.py

**Path:** `QualifierFunction/Prototype.py`

**Automation Type:** General Automation
**Lines:** 34

## Purpose

Initialize complex field

## Usage Pattern

Function-based - Provides reusable functions

## Dependencies

- `torch`
- `torch.fft`

## Functions

### laplacian

**Parameters:** field

### pump_field

**Parameters:** x0, y0, amplitude, sigma

## Code Examples

### laplacian

```python
def laplacian(field):
    return (
        torch.roll(field, 1, 0) +
        torch.roll(field, -1, 0) +
        torch.roll(field, 1, 1) +
        torch.roll(field, -1, 1) -
        4 * field
    )
```

### pump_field

```python
def pump_field(x0, y0, amplitude=1.0, sigma=5):
    x = torch.arange(N, device="cuda")
    y = torch.arange(N, device="cuda")
    X, Y = torch.meshgrid(x, y, indexing="ij")
    return amplitude * torch.exp(-((X-x0)**2 + (Y-y0)**2)/sigma**2)
```

