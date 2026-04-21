# curvature_learning.py

**Path:** `QualifierFunction/curvature_learning.py`

**Automation Type:** General Automation
**Lines:** 23

## Library Context

This script is part of the general automation library, providing utility functions for common automation tasks.

## Usage Pattern

Object-oriented - Provides classes and methods

## Dependencies

- `torch`

## Function Descriptions

- __init__ - Parameters: self, dim. Performs a specific operation.
- loss - Parameters: self. Performs a specific operation.
- fisher_metric - Parameters: self. Performs a specific operation.
- natural_step - Parameters: self, lr. Performs a specific operation.

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

### natural_step

```python
def natural_step(self, lr=0.01):
        L = self.loss()
        grad = torch.autograd.grad(L, self.theta)[0]
        G = self.fisher_metric()
        G_inv = torch.linalg.inv(G)
        update = G_inv @ grad
        self.theta.data -= lr * update
```

