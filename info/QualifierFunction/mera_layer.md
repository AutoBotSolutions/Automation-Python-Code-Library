# mera_layer.py

**Path:** `QualifierFunction/mera_layer.py`

**Automation Type:** General Automation
**Lines:** 11

## Usage Pattern

Object-oriented - Provides classes and methods

## Functions

### __init__

**Parameters:** self, dim

### forward

**Parameters:** self, x

## Classes

### MERALayer

**Methods:**
- `__init__`
- `forward`

## Code Examples

### __init__

```python
def __init__(self, dim):
        super().__init__()
        self.U = torch.nn.Linear(dim, dim, bias=False)
        self.C = torch.nn.Linear(dim, dim//2)
```

### forward

```python
def forward(self, x):
        x = self.U(x)
        x = torch.tanh(x)
        return self.C(x)
```

