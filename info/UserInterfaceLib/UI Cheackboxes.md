# UI Cheackboxes.py

**Path:** `UserInterfaceLib/UI Cheackboxes.py`

**Automation Type:** HTTP Requests
**Lines:** 71

## Library Context

This script is part of the HTTP/Network library, providing functions for making HTTP requests, interacting with web APIs, and handling network communications.

## Key Features

- Web API interaction

## Usage Pattern

Function-based - Provides reusable functions

## Dependencies

- `tkinter`
- `tkinter.messagebox`

## Function Descriptions

- show_selection - Performs a specific operation.
- start - Initializes a connection or process.

## Functions

### show_selection

### start

## Code Examples

### show_selection

```python
def show_selection():
    print(f"Checkbox 1: {var1.get()}")
    print(f"Checkbox 2: {var2.get()}")
    print(f"Checkbox 3: {var3.get()}")
    print(f"Checkbox 4: {var4.get()}")
```

### start

```python
def start():
    username = "johnsmith"
    password = "12345"
    if follow_entry.get()==username and unfollow_entry.get()==password:
        messagebox.showinfo(title="Start Success", message="You successfully logged in.")
    else:
        messagebox.showerror(title="Error", message="Invalid Star
```

