# GUI System Documentation

## Overview

The Code Library GUI is a modern, dark-themed Python application built with tkinter that provides a user-friendly interface for browsing, viewing, and editing automation scripts.

## Architecture

### Main Components

#### 1. CodeLibraryGUI Class
The main application class that manages the entire GUI system.

**Key Methods:**
- `__init__()` - Initializes the GUI, sets up tracking system
- `create_layout()` - Creates the main UI layout
- `load_categories()` - Loads the directory tree structure
- `build_tree()` - Recursively builds the category tree
- `load_files()` - Loads files from selected category
- `load_code()` - Displays code content in the viewer
- `refresh_library()` - Refreshes the library and detects changes
- `show_statistics()` - Displays usage statistics
- `on_search()` - Handles search functionality
- `on_category_select()` - Handles category selection events
- `on_file_select()` - Handles file selection events
- `copy_code()` - Copies code to clipboard
- `open_in_editor()` - Opens file in advanced text editor
- `on_closing()` - Handles window close event

#### 2. AdvancedTextEditor Class
A full-featured text editor with syntax highlighting and editing capabilities.

**Key Methods:**
- `__init__()` - Initializes the editor window
- `create_editor_layout()` - Creates the editor UI
- `load_file()` - Loads a file into the editor
- `save_file()` - Saves the current file
- `save_file_as()` - Saves file with a new name
- `new_file()` - Creates a new file
- `open_file()` - Opens a file
- `undo()` / `redo()` - Undo/redo operations
- `cut()` / `copy()` / `paste()` - Clipboard operations
- `show_find_dialog()` - Shows find dialog
- `show_replace_dialog()` - Shows find and replace dialog
- `apply_syntax_highlighting()` - Applies Python syntax highlighting
- `update_line_numbers()` - Updates line number sidebar

#### 3. SystemTracker Class
Tracks system usage, file changes, and provides statistics.

**Key Methods:**
- `__init__()` - Initializes the tracking system
- `load_tracking_data()` - Loads existing tracking data
- `save_tracking_data()` - Saves tracking data to JSON
- `log_event()` - Logs an event with timestamp
- `track_file_access()` - Tracks when a file is accessed
- `track_file_edit()` - Tracks when a file is edited
- `detect_changes()` - Detects file changes using MD5 hashing
- `start_session()` - Starts a new tracking session
- `end_session()` - Ends the current session
- `get_statistics()` - Returns usage statistics

## UI Components

### Main Window
- **Paned Window**: Horizontal split layout with resizable panels
- **Left Panel**: Categories tree and files list
- **Right Panel**: Code viewer with action buttons

### Left Panel Components
- **Search Box**: Real-time search filtering
- **Category Tree**: Hierarchical directory tree with nested support
- **Files Listbox**: List of Python files in selected category
- **Scrollbars**: Vertical scrollbars for both tree and listbox

### Right Panel Components
- **File Label**: Displays current file name
- **Action Buttons**: Refresh, Copy Code, Open in Editor, Statistics
- **Code Viewer**: ScrolledText widget with syntax highlighting
- **Status Bar**: Shows current status and messages

### Advanced Editor Components
- **Menu Bar**: File and Edit menus
- **Toolbar**: Quick-access buttons for common operations
- **Line Numbers**: Auto-updating line number sidebar
- **Text Editor**: Main editing area with syntax highlighting
- **Scrollbars**: Horizontal and vertical scrollbars

## Features

### Browsing Features
- **Nested Directory Support**: Browse through unlimited directory depth
- **Search Functionality**: Real-time filtering of categories
- **Refresh Capability**: Dynamically discover new scripts and folders
- **File Preview**: View code without opening editor

### Editing Features
- **Syntax Highlighting**: Python syntax with color coding
- **Line Numbers**: Auto-updating line number display
- **Find & Replace**: Search and replace functionality
- **Undo/Redo**: 50-level undo history
- **Multiple Encodings**: Support for UTF-8, Latin-1, CP1252, ISO-8859-1, ASCII
- **File Operations**: New, Open, Save, Save As

### Tracking Features
- **File Change Detection**: MD5 hashing to detect modifications
- **Usage Statistics**: Track most accessed files and categories
- **Session Tracking**: Monitor GUI usage sessions
- **Event Logging**: Comprehensive logging of all activities
- **Persistent Storage**: Usage data saved between sessions

## Color Scheme

The GUI uses a modern dark theme (Catppuccin-inspired):

```
Backgrounds:
- Primary: #1e1e2e (dark purple/blue)
- Secondary: #313244 (slate)
- Tertiary: #45475a (lighter slate)
- Code: #11111b (very dark)

Text:
- Primary: #cdd6f4 (light blue/white)
- Secondary: #a6adc8 (gray)

Accents:
- Accent: #89b4fa (blue)
- Success: #a6e3a1 (green)
- Warning: #f9e2af (yellow)
- Error: #f38ba8 (red)
- Highlight: #f5c2e7 (pink)
```

## Configuration

### Code Library Path
Configured in `code_library_gui.py` line 31:
```python
self.library_path = "/path/to/your/code-library"
```

### Tracking Files
- `tracking_log.txt`: Event logs (auto-generated)
- `usage_stats.json`: Usage statistics (auto-generated)

## Error Handling

The GUI includes comprehensive error handling for:
- File I/O errors
- Directory access permissions
- Encoding issues
- Syntax errors in code files
- Network errors (for subprocess calls)

## Security Features

- **Path Isolation**: Code library path removed from sys.path to prevent imports
- **Binary Mode Reading**: Files read in binary mode to prevent compilation
- **Working Directory**: Changed to /tmp to avoid Python compiling library files
- **Bytecode Disabled**: PYTHONDONTWRITEBYTECODE environment variable set

## Performance Optimizations

- **Subprocess for Directory Listing**: Uses `find` command to avoid Python compilation
- **Lazy Loading**: Files only loaded when selected
- **Efficient Tree Building**: Recursive algorithm with error handling
- **MD5 Hashing**: Efficient change detection

## Data Flow

### File Access Flow
1. User selects category in tree
2. System loads files list from directory
3. User selects file
4. System reads file in binary mode
5. Content decoded with multiple encoding attempts
6. Code displayed in viewer
7. File access tracked

### Change Detection Flow
1. Refresh button clicked
2. System walks directory tree
3. MD5 hash computed for each file
4. Compared with stored hashes
5. Changes logged and displayed

## Extensibility

The GUI is designed to be extensible:
- Additional syntax highlighting languages can be added
- New tracking metrics can be implemented
- Custom editors can be integrated
- Additional file operations can be added

## Dependencies

### Required
- Python 3.7+
- tkinter (usually included with Python)

### Optional
- None (pure Python implementation)

## Known Limitations

- Designed specifically for Python files (.py)
- Syntax highlighting only supports Python
- No built-in diff viewer
- No plugin system (currently)

## Future Enhancements

Potential areas for improvement:
- Multi-language syntax highlighting
- Diff viewer for file comparisons
- Bookmarking system
- Export functionality for statistics
- Plugin architecture
- Keyboard shortcuts
- Dark/light theme toggle
