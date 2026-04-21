# curvature_learning.py

**Path:** `QualifierFunction/curvature_learning.py`

**Automation Type:** General Automation
**Lines:** 23

## Usage Pattern

Object-oriented - Provides classes and methods

## Dependencies

- `torch`

## Functions

### __init__

**Parameters:** self, dim

### loss

**Parameters:** self

### fisher_metric

**Parameters:** self

### natural_step

**Parameters:** self, lr

## Classes

### CurvatureLearner

**Methods:**
- `__init__`
- `loss`
- `fisher_metric`
- `natural_step`

## Code Examples

### __init__

```python
def __init__(self, dim):
        super().__init__()
        self.theta = torch.nn.Parameter(torch.randn(dim, device="cuda"))
```

### loss

```python
def loss(self):
        return torch.sum(self.theta**2)
```

### fisher_metric

```python
def fisher_metric(self):
        grad = torch.autograd.grad(self.loss(), self.theta, create_graph=True)[0]
        G = torch.outer(grad, grad) + 1e-3 * torch.eye(len(self.theta), device="cuda")
        return G
```

