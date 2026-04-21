# Automation Code Library GUI

A modern, dark-themed Python code library browser with advanced text editing capabilities and comprehensive tracking system.

## Features

### Code Library Browser
- **Modern Dark Theme**: Beautiful Catppuccin-inspired color scheme
- **Hierarchical Navigation**: Browse through nested directory structures
- **Search Functionality**: Filter categories and files instantly
- **Code Preview**: View code snippets with syntax highlighting
- **Copy to Clipboard**: One-click code copying
- **Refresh Capability**: Dynamically discover new scripts and folders

### Advanced Text Editor
- **Syntax Highlighting**: Python syntax with multiple color schemes
- **Line Numbers**: Auto-updating line number sidebar
- **Find & Replace**: Search and replace functionality
- **Undo/Redo**: 50-level undo history
- **Multiple Encodings**: Support for UTF-8, Latin-1, CP1252, ISO-8859-1, ASCII
- **File Operations**: New, Open, Save, Save As
- **Modern UI**: Matching dark theme with the main browser

### Tracking System
- **File Change Detection**: MD5 hashing to detect new, modified, and deleted files
- **Usage Statistics**: Track most accessed files and categories
- **Session Tracking**: Monitor GUI usage sessions
- **Event Logging**: Comprehensive logging of all activities
- **Persistent Storage**: Usage data saved between sessions
- **Statistics Dashboard**: Visual display of usage metrics

## Installation

### Requirements
- Python 3.7 or higher
- tkinter (usually included with Python)
- No external dependencies required for core functionality

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/code-library-gui.git
cd code-library-gui
```

2. Run the application:
```bash
python3 code_library_gui.py
```

## Configuration

The code library path is configured in the `code_library_gui.py` file. To change the default path:

```python
self.library_path = "/path/to/your/code/library"
```

## Usage

### Browsing the Library
1. Select a category from the left panel tree
2. Choose a file from the file list
3. View the code in the right panel
4. Use the "Copy Code" button to copy to clipboard
5. Use "Open in Editor" to edit in the advanced text editor

### Using the Advanced Editor
1. Click "Open in Editor" when viewing a file
2. Edit the code with syntax highlighting
3. Use Find/Replace for text operations
4. Save changes directly to the file
5. Track file edits automatically

### Tracking & Statistics
1. Click "Statistics" button to view usage data
2. Click "Refresh" to detect file changes
3. View tracking logs in `tracking_log.txt`
4. Usage stats saved in `usage_stats.json`

## Project Structure

```
CodeLibrary/
├── code_library_gui.py    # Main application
├── tracking_log.txt        # Event logs (auto-generated)
├── usage_stats.json        # Usage statistics (auto-generated)
├── README.md              # This file
├── LICENSE                # License file
└── .gitignore            # Git ignore rules
```

## Tracking Data

The application automatically generates:
- **tracking_log.txt**: Timestamped log of all events
- **usage_stats.json**: Persistent usage statistics

These files are created in the application directory and should not be committed to version control.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Catppuccin color palette for the modern dark theme
- Python tkinter for the GUI framework
- The automation code library community

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

## Roadmap

- [ ] Add support for additional programming languages
- [ ] Implement file comparison/diff viewer
- [ ] Add bookmarking functionality
- [ ] Export usage reports
- [ ] Add plugin system for custom features
