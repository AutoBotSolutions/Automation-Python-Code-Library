# API Reference

This document provides API reference for the Code Library GUI system.

## CodeLibraryGUI Class

### Constructor

```python
CodeLibraryGUI(root)
```

**Parameters:**
- `root` (tk.Tk): The main tkinter window

**Example:**
```python
root = tk.Tk()
app = CodeLibraryGUI(root)
root.mainloop()
```

### Methods

#### create_layout()
Creates the main GUI layout with paned windows, panels, and widgets.

**Returns:** None

#### load_categories()
Loads all categories (directories) from the code library with nested structure.

**Returns:** None

#### build_tree(parent, path)
Recursively builds directory tree structure.

**Parameters:**
- `parent` (str): Parent node ID in tree
- `path` (str): Directory path to scan

**Returns:** None

#### on_category_select(event)
Handles category selection events from the tree.

**Parameters:**
- `event` (tk.Event): Selection event

**Returns:** None

#### load_files(category_path)
Loads files from selected category directory.

**Parameters:**
- `category_path` (str): Path to category directory

**Returns:** None

#### on_file_select(event)
Handles file selection events from the listbox.

**Parameters:**
- `event` (tk.Event): Selection event

**Returns:** None

#### load_code(category_path, filename)
Loads and displays code from selected file.

**Parameters:**
- `category_path` (str): Path to category directory
- `filename` (str): Name of file to load

**Returns:** None

#### copy_code()
Copies code from the viewer to clipboard.

**Returns:** None

#### open_in_editor()
Opens selected file in advanced text editor.

**Returns:** None

#### refresh_library()
Refreshes the library to discover new scripts and folders.

**Returns:** None

#### show_statistics()
Displays usage statistics in a new window.

**Returns:** None

#### on_search(event)
Handles search functionality for filtering categories.

**Parameters:**
- `event` (tk.Event): Key release event

**Returns:** None

#### filter_tree(search_term)
Filters the tree based on search term.

**Parameters:**
- `search_term` (str): Term to search for

**Returns:** None

#### on_closing()
Handles window closing event.

**Returns:** None

### Attributes

- `root` (tk.Tk): Main window
- `library_path` (str): Path to code library directory
- `tracker` (SystemTracker): Tracking system instance
- `category_tree` (ttk.Treeview): Category tree widget
- `files_listbox` (tk.Listbox): Files list widget
- `code_text` (scrolledtext.ScrolledText): Code viewer widget
- `current_file_path` (str): Currently selected file path
- `status_var` (tk.StringVar): Status bar variable

## AdvancedTextEditor Class

### Constructor

```python
AdvancedTextEditor(parent, file_path=None, tracker=None)
```

**Parameters:**
- `parent` (tk.Tk): Parent window
- `file_path` (str, optional): Path to file to edit
- `tracker` (SystemTracker, optional): Tracking system instance

**Example:**
```python
editor = AdvancedTextEditor(root, "/path/to/file.py", tracker)
```

### Methods

#### create_editor_layout()
Creates the editor layout with menu, toolbar, and text area.

**Returns:** None

#### load_file(file_path)
Loads a file into the editor.

**Parameters:**
- `file_path` (str): Path to file to load

**Returns:** None

#### save_file()
Saves the current file.

**Returns:** None

#### save_file_as()
Saves the file with a new name.

**Returns:** None

#### new_file()
Creates a new file.

**Returns:** None

#### open_file()
Opens a file using file dialog.

**Returns:** None

#### close_editor()
Closes the editor window.

**Returns:** None

#### undo()
Undoes the last action.

**Returns:** None

#### redo()
Redoes the last undone action.

**Returns:** None

#### cut()
Cuts selected text to clipboard.

**Returns:** None

#### copy()
Copies selected text to clipboard.

**Returns:** None

#### paste()
Pastes text from clipboard.

**Returns:** None

#### show_find_dialog()
Shows find dialog for text search.

**Returns:** None

#### show_replace_dialog()
Shows find and replace dialog.

**Returns:** None

#### on_key_press(event)
Handles key press events.

**Parameters:**
- `event` (tk.Event): Key press event

**Returns:** None

#### update_line_numbers(event=None)
Updates the line number sidebar.

**Parameters:**
- `event` (tk.Event, optional): Event that triggered update

**Returns:** None

#### apply_syntax_highlighting()
Applies Python syntax highlighting to the text.

**Returns:** None

#### highlight_pattern(pattern, tag, word=False)
Highlights a pattern with a specific tag.

**Parameters:**
- `pattern` (str): Regex pattern to highlight
- `tag` (str): Tag name for highlighting
- `word` (bool, optional): Match whole words only

**Returns:** None

### Attributes

- `editor_window` (tk.Toplevel): Editor window
- `file_path` (str): Current file path
- `modified` (bool): Whether file has been modified
- `tracker` (SystemTracker): Tracking system instance
- `text` (tk.Text): Main text editor widget
- `line_numbers` (tk.Text): Line number widget
- `file_label` (ttk.Label): File name label

## SystemTracker Class

### Constructor

```python
SystemTracker(library_path)
```

**Parameters:**
- `library_path` (str): Path to code library directory

**Example:**
```python
tracker = SystemTracker("/path/to/code-library")
tracker.start_session()
```

### Methods

#### load_tracking_data()
Loads existing tracking data from JSON file.

**Returns:** None

#### save_tracking_data()
Saves tracking data to JSON file.

**Returns:** None

#### log_event(event_type, details)
Logs an event with timestamp.

**Parameters:**
- `event_type` (str): Type of event (e.g., "FILE_ACCESS")
- `details` (str): Event details

**Returns:** None

#### track_file_access(file_path)
Tracks when a file is accessed.

**Parameters:**
- `file_path` (str): Path to accessed file

**Returns:** None

#### track_file_edit(file_path)
Tracks when a file is edited.

**Parameters:**
- `file_path` (str): Path to edited file

**Returns:** None

#### detect_changes()
Detects changes in the code library using MD5 hashing.

**Returns:** list: List of detected changes (new, modified, deleted files)

#### start_session()
Starts a new tracking session.

**Returns:** None

#### end_session()
Ends the current tracking session.

**Returns:** None

#### get_statistics()
Returns usage statistics.

**Returns:** dict: Dictionary containing:
- `total_sessions` (int): Total number of sessions
- `most_accessed_files` (list): Top 10 most accessed files
- `most_accessed_categories` (list): Top 10 most accessed categories
- `total_files_tracked` (int): Total number of tracked files

### Attributes

- `library_path` (str): Path to code library
- `log_file` (str): Path to log file
- `stats_file` (str): Path to statistics JSON file
- `file_hashes` (dict): Dictionary of file MD5 hashes
- `usage_stats` (dict): Usage statistics dictionary

## Constants

### COLORS Dictionary

Color palette for dark theme:

```python
COLORS = {
    'bg_primary': '#1e1e2e',        # Main background
    'bg_secondary': '#313244',      # Secondary background
    'bg_tertiary': '#45475a',       # Tertiary background
    'fg_primary': '#cdd6f4',       # Primary text
    'fg_secondary': '#a6adc8',      # Secondary text
    'accent': '#89b4fa',            # Accent color
    'accent_hover': '#b4befe',      # Accent hover
    'success': '#a6e3a1',           # Success
    'warning': '#f9e2af',           # Warning
    'error': '#f38ba8',             # Error
    'border': '#45475a',            # Border
    'highlight': '#f5c2e7',         # Highlight
    'code_bg': '#11111b',           # Code background
    'line_number_bg': '#1e1e2e',    # Line number background
    'line_number_fg': '#6c7086',    # Line number text
}
```

## Usage Examples

### Basic GUI Usage

```python
import tkinter as tk
from code_library_gui import CodeLibraryGUI

root = tk.Tk()
app = CodeLibraryGUI(root)
root.mainloop()
```

### Using the Tracker Standalone

```python
from code_library_gui import SystemTracker

tracker = SystemTracker("/path/to/code-library")
tracker.start_session()

# Track file access
tracker.track_file_access("/path/to/script.py")

# Detect changes
changes = tracker.detect_changes()
print(f"Detected {len(changes)} changes")

# Get statistics
stats = tracker.get_statistics()
print(f"Total sessions: {stats['total_sessions']}")

tracker.end_session()
```

### Using the Advanced Editor Standalone

```python
import tkinter as tk
from code_library_gui import AdvancedTextEditor

root = tk.Tk()
editor = AdvancedTextEditor(root, "/path/to/file.py")
root.mainloop()
```

## Event Types

The tracking system logs the following event types:

- `SESSION_START`: When the GUI starts
- `SESSION_END`: When the GUI closes
- `FILE_ACCESS`: When a file is viewed
- `FILE_EDIT`: When a file is saved/edited
- `FILE_MODIFIED`: When a file's content changes
- `FILE_ADDED`: When a new file is detected
- `FILE_DELETED`: When a file is removed

## Error Handling

All methods include try-except blocks to handle errors gracefully. Errors are logged to the tracking log and displayed in the GUI where appropriate.

## Thread Safety

The GUI runs on the main thread. For long-running operations, consider using threading or async operations to prevent UI freezing.

## Extension Points

### Adding New Features

To extend the GUI:
1. Add new methods to CodeLibraryGUI class
2. Update the create_layout() method to add UI elements
3. Add event handlers as needed
4. Update tracking if needed

### Adding New Tracking Metrics

To add new tracking:
1. Add new fields to usage_stats dictionary
2. Create tracking methods
3. Update get_statistics() to include new metrics
4. Update statistics display in show_statistics()

### Adding New Syntax Highlighting

To add new languages:
1. Add language keywords to the keywords list
2. Add language-specific patterns
3. Create language-specific tag configurations
