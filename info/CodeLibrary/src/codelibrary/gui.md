# gui.py

**Path:** `CodeLibrary/src/codelibrary/gui.py`

**Automation Type:** Browser Automation
**Lines:** 550

## Purpose

CodeLibrary GUI Application - A visual interface to library utilities.

## Key Features

- Web browser control

## Usage Pattern

Object-oriented - Provides classes and methods with standalone execution capability

## Dependencies

- `tkinter`
- `tkinter.ttk`
- `tkinter.messagebox`
- `datetime.datetime`
- `codelibrary.string_helpers`
- `codelibrary.math_helpers`
- `codelibrary.datastructures`
- `codelibrary.time_utils`
- `codelibrary.indexer.LibraryIndexer`

## Functions

### main

### __init__

**Parameters:** self, root

### create_search_tab

**Parameters:** self

Create search tab for finding functions.

### create_library_browser_tab

**Parameters:** self

Create library browser tab to view all modules and functions.

### create_string_tab

**Parameters:** self

Create string utilities tab.

### create_math_tab

**Parameters:** self

Create math utilities tab.

### create_datastructures_tab

**Parameters:** self

Create data structures tab.

### create_time_tab

**Parameters:** self

Create time utilities tab.

### convert_camel_to_snake

**Parameters:** self

### convert_snake_to_camel

**Parameters:** self

... and 23 more functions

## Classes

### CodeLibraryGUI

**Methods:**
- `__init__`
- `create_search_tab`
- `create_library_browser_tab`
- `create_string_tab`
- `create_math_tab`
- ... and 27 more

## Code Examples

### main

```python
def main():
    root = tk.Tk()
    app = CodeLibraryGUI(root)
    root.mainloop()
```

### convert_camel_to_snake

```python
def convert_camel_to_snake(self):
        input_text = self.camel_input.get()
        result = string_helpers.camel_to_snake(input_text)
        self.camel_output.delete(0, tk.END)
        self.camel_output.insert(0, result)
```

### convert_snake_to_camel

```python
def convert_snake_to_camel(self):
        input_text = self.snake_input.get()
        result = string_helpers.snake_to_camel(input_text)
        self.snake_output.delete(0, tk.END)
        self.snake_output.insert(0, result)
```

