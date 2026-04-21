# Cross-Platform Installation and Usage Guide

This guide provides detailed instructions for installing and using the Automation Python Code Library GUI on Windows, Linux, and macOS.

## Table of Contents
- [System Requirements](#system-requirements)
- [Windows Installation](#windows-installation)
- [Linux Installation](#linux-installation)
- [macOS Installation](#macos-installation)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)

---

## System Requirements

### Common Requirements (All Platforms)
- **Python**: Version 3.7 or higher
- **tkinter**: Usually included with Python
- **Disk Space**: ~50 MB for the application
- **RAM**: Minimum 512 MB recommended

### Platform-Specific Notes
- **Windows**: Windows 7, 8, 10, or 11
- **Linux**: Most distributions (Ubuntu, Debian, Fedora, etc.)
- **macOS**: macOS 10.13 (High Sierra) or later

---

## Windows Installation

### Step 1: Install Python

1. Download Python from [python.org](https://www.python.org/downloads/windows/)
2. Run the installer
3. **IMPORTANT**: Check "Add Python to PATH" during installation
4. Click "Install Now"

### Step 2: Verify Installation

Open Command Prompt and run:
```cmd
python --version
```

### Step 3: Install tkinter (if not included)

```cmd
pip install tk
```

### Step 4: Download the Application

1. Go to the repository: https://github.com/AutoBotSolutions/Automation-Python-Code-Library
2. Click "Code" → "Download ZIP"
3. Extract the ZIP file to your desired location

### Step 5: Run the Application

**Using Command Prompt:**
```cmd
cd C:\path\to\Automation-Python-Code-Library
python code_library_gui.py
```

**Using PowerShell:**
```powershell
cd C:\path\to\Automation-Python-Code-Library
python code_library_gui.py
```

**Using Windows Explorer:**
1. Navigate to the extracted folder
2. Right-click on `code_library_gui.py`
3. Select "Open with" → "Python"
4. Or create a desktop shortcut

### Step 6: Create Desktop Shortcut (Optional)

1. Right-click on `code_library_gui.py`
2. Select "Send to" → "Desktop (create shortcut)"
3. Right-click the shortcut → "Properties"
4. Change "Target" to include full path to Python:
   ```
   "C:\Python39\python.exe" "C:\path\to\code_library_gui.py"
   ```

### Windows-Specific Configuration

The code library path in `code_library_gui.py` uses Linux-style paths. For Windows, update line 31:
```python
self.library_path = r"C:\path\to\your\code-library"
```

---

## Linux Installation

### Step 1: Install Python

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install python3 python3-tk
```

**Fedora:**
```bash
sudo dnf install python3 python3-tkinter
```

**Arch Linux:**
```bash
sudo pacman -S python tk
```

### Step 2: Verify Installation

```bash
python3 --version
```

### Step 3: Clone or Download the Repository

**Option A: Clone with Git (Recommended)**
```bash
git clone https://github.com/AutoBotSolutions/Automation-Python-Code-Library.git
cd Automation-Python-Code-Library
```

**Option B: Download ZIP**
1. Download from: https://github.com/AutoBotSolutions/Automation-Python-Code-Library
2. Extract the archive
3. Navigate to the extracted directory

### Step 4: Run the Application

```bash
python3 code_library_gui.py
```

### Step 5: Make Executable (Optional)

```bash
chmod +x code_library_gui.py
./code_library_gui.py
```

### Step 6: Create Desktop Entry (Optional)

Create `~/.local/share/applications/code-library-gui.desktop`:
```ini
[Desktop Entry]
Version=1.0
Type=Application
Name=Code Library GUI
Comment=Automation Python Code Library Browser
Exec=/usr/bin/python3 /path/to/Automation-Python-Code-Library/code_library_gui.py
Icon=python
Terminal=false
Categories=Development;IDE;
```

### Linux-Specific Configuration

The default path should work for Linux:
```python
self.library_path = "/home/username/code-library"
```

---

## macOS Installation

### Step 1: Install Python

**Using Homebrew (Recommended):**
```bash
brew install python-tk
```

**Using Official Installer:**
1. Download from [python.org](https://www.python.org/downloads/macos/)
2. Run the PKG installer
3. Follow the installation prompts

### Step 2: Verify Installation

```bash
python3 --version
```

### Step 3: Install tkinter (if not included)

```bash
brew install python-tk
# or
pip3 install tk
```

### Step 4: Clone or Download the Repository

**Option A: Clone with Git (Recommended)**
```bash
git clone https://github.com/AutoBotSolutions/Automation-Python-Code-Library.git
cd Automation-Python-Code-Library
```

**Option B: Download ZIP**
1. Download from: https://github.com/AutoBotSolutions/Automation-Python-Code-Library
2. Double-click the ZIP to extract
3. Open Terminal and navigate to the extracted folder

### Step 5: Run the Application

```bash
python3 code_library_gui.py
```

### Step 6: Create Application Shortcut (Optional)

1. Open "Script Editor"
2. Create new script:
```applescript
tell application "Terminal"
    activate
    do script "cd /path/to/Automation-Python-Code-Library && python3 code_library_gui.py"
end tell
```
3. Save as "Code Library GUI" in "Applications" folder
4. File Format: "Application"

### macOS-Specific Configuration

The default path should work for macOS:
```python
self.library_path = "/Users/username/code-library"
```

---

## Configuration

### Setting Your Code Library Path

The code library path is configured in `code_library_gui.py` at line 31:

**Windows:**
```python
self.library_path = r"C:\Users\YourName\code-library"
```

**Linux:**
```python
self.library_path = "/home/username/code-library"
```

**macOS:**
```python
self.library_path = "/Users/username/code-library"
```

### Configuring the Library Path

1. Open `code_library_gui.py` in a text editor
2. Find line 31
3. Update the path to point to your code library directory
4. Save the file

### Path Format Notes

- **Windows**: Use raw strings (r"path") or double backslashes (\\)
- **Linux/macOS**: Use forward slashes (/)
- **Network Paths**: 
  - Windows: `r"\\network\share\path"`
  - Linux: `"/mnt/share/path"`

---

## Troubleshooting

### Common Issues

#### Python Not Found

**Windows:**
```cmd
where python
```
Ensure Python is in your PATH. Reinstall Python with "Add to PATH" checked.

**Linux:**
```bash
which python3
```
Install Python3 if not found.

**macOS:**
```bash
which python3
```
Ensure Python3 is installed via Homebrew or official installer.

#### tkinter Module Not Found

**Linux:**
```bash
sudo apt install python3-tk
```

**macOS:**
```bash
brew install python-tk
```

**Windows:**
Reinstall Python and ensure tkinter is selected during installation.

#### Permission Denied

**Linux/macOS:**
```bash
chmod +x code_library_gui.py
```

#### GUI Not Appearing

- Ensure you're not running in a headless environment
- Check that X11 forwarding is enabled (Linux SSH)
- Try running with `python3` instead of `python`

#### File Encoding Errors

The application handles multiple encodings automatically. If you encounter issues:
- Ensure your code library files are UTF-8 encoded
- Check for binary files that shouldn't be in the library

#### Tracking Files Not Created

Ensure you have write permissions in the application directory:
```bash
# Linux/macOS
chmod +w .

# Windows
# Run as Administrator
```

### Platform-Specific Issues

#### Windows Defender Blocking Execution

1. Open Windows Security
2. Go to "Virus & threat protection" → "Virus & threat protection settings"
3. Add exclusions for the application folder

#### Linux Display Issues

If GUI doesn't appear on remote SSH:
```bash
ssh -X user@server
# or
ssh -Y user@server
```

#### macOS Gatekeeper Blocking Execution

```bash
xattr -d com.apple.quarantine code_library_gui.py
```

---

## Advanced Configuration

### Virtual Environment (Recommended for Development)

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install tk
python code_library_gui.py
```

**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
pip install tk
python code_library_gui.py
```

### System-Wide Installation

**Linux:**
```bash
sudo cp code_library_gui.py /usr/local/bin/
sudo chmod +x /usr/local/bin/code_library_gui.py
```

**macOS:**
```bash
sudo cp code_library_gui.py /usr/local/bin/
sudo chmod +x /usr/local/bin/code_library_gui.py
```

---

## Support

For issues or questions:
1. Check this guide first
2. Review the main README.md
3. Open an issue on GitHub: https://github.com/AutoBotSolutions/Automation-Python-Code-Library/issues

---

## Quick Start Summary

**Windows:**
1. Install Python (add to PATH)
2. Download ZIP from GitHub
3. Extract and run `python code_library_gui.py`

**Linux:**
1. `sudo apt install python3 python3-tk`
2. `git clone https://github.com/AutoBotSolutions/Automation-Python-Code-Library.git`
3. `cd Automation-Python-Code-Library`
4. `python3 code_library_gui.py`

**macOS:**
1. `brew install python-tk`
2. `git clone https://github.com/AutoBotSolutions/Automation-Python-Code-Library.git`
3. `cd Automation-Python-Code-Library`
4. `python3 code_library_gui.py`

---

**Enjoy using the Automation Python Code Library GUI!**
