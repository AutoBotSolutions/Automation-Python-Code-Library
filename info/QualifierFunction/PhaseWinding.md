# PhaseWinding.py

**Path:** `QualifierFunction/PhaseWinding.py`

**Automation Type:** General Automation
**Lines:** 12

## Purpose

No specific purpose documented in the file.

## Library Context

This script is part of the general automation library, providing utility functions for common automation tasks.

## Key Features

No specific features documented.

## Usage Pattern

Function-based - Provides reusable functions

## Dependencies

No external dependencies identified.

## Function Descriptions

- detect_vortices - Parameters: psi. Performs a specific operation.

## Functions

### detect_vortices

**Parameters:** psi

## Classes

No classes defined in this script.

## External APIs

No external API interactions identified.

## Code Examples

### detect_vortices

```python
def detect_vortices(psi):
    phase = torch.angle(psi)
    vortices = torch.zeros_like(phase)

    N = psi.shape[0]
    for i in range(N-1):
        for j in range(N-1):
            loop = [phase[i,j], phase[i+1,j], phase[i+1,j+1], phase[i,j+1], phase[i,j]]
            total = sum(torch.atan2(torch.
```

