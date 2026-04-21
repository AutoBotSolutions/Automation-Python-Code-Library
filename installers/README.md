# Installers

This directory contains build scripts and configuration files for creating standalone installers for the Code Library GUI on different platforms.

## Platform-Specific Installers

### Windows

**Files:**
- `windows_installer.spec` - PyInstaller configuration
- `build_windows.bat` - Windows build script

**Building:**
```batch
cd installers
build_windows.bat
```

**Requirements:**
- Python 3.7+ installed
- PyInstaller: `pip install pyinstaller`

**Output:**
- `dist/CodeLibraryGUI.exe` - Standalone Windows executable

**Distribution:**
- Copy `CodeLibraryGUI.exe` to desired location
- Include code-library directory if needed
- Create a README with instructions

### Linux

**Files:**
- `windows_installer.spec` - PyInstaller configuration (shared)
- `build_linux.sh` - Linux build script

**Building:**
```bash
cd installers
chmod +x build_linux.sh
./build_linux.sh
```

**Requirements:**
- Python 3.7+ installed
- tkinter: `sudo apt install python3-tk`
- PyInstaller: `python3 -m pip install pyinstaller --user`

**Output:**
- `dist/CodeLibraryGUI` - Standalone Linux executable

**Distribution:**
- Make executable: `chmod +x CodeLibraryGUI`
- Create tarball: `tar -czf CodeLibraryGUI-Linux.tar.gz CodeLibraryGUI`
- Include code-library directory if needed

### macOS

**Files:**
- `windows_installer.spec` - PyInstaller configuration (shared)
- `build_macos.sh` - macOS build script

**Building:**
```bash
cd installers
chmod +x build_macos.sh
./build_macos.sh
```

**Requirements:**
- Python 3.7+ installed
- tkinter: `brew install python-tk`
- PyInstaller: `python3 -m pip install pyinstaller`

**Output:**
- `dist/CodeLibraryGUI` - Standalone macOS executable

**Distribution:**
- Create .app bundle (optional)
- Create DMG installer
- Include code-library directory if needed

## Configuration

### PyInstaller Spec File

The `windows_installer.spec` file is shared across all platforms and contains:
- Application entry point
- Hidden imports for tkinter modules
- Console window disabled (set `console=True` for debugging)
- UPX compression enabled

### Customizing the Spec

To customize the build:
1. Edit `windows_installer.spec`
2. Modify parameters as needed
3. Rebuild with platform-specific script

## Debugging

### Console Output

To see console output for debugging:
1. Edit `windows_installer.spec`
2. Set `console=True` in the EXE section
3. Rebuild the installer

### Common Issues

**Build Fails:**
- Ensure PyInstaller is installed
- Check Python version compatibility
- Verify all dependencies are available

**Runtime Errors:**
- Run with `console=True` to see errors
- Check that tkinter is properly included
- Verify file paths in the executable

**Missing Modules:**
- Add to `hiddenimports` in spec file
- Rebuild the installer

## Distribution Packages

### Windows Package
```
CodeLibraryGUI-Windows/
├── CodeLibraryGUI.exe
├── code-library/ (optional)
└── README.txt
```

### Linux Package
```
CodeLibraryGUI-Linux.tar.gz
└── Contains:
    ├── CodeLibraryGUI
    ├── code-library/ (optional)
    └── README.txt
```

### macOS Package
```
CodeLibraryGUI-macOS.dmg
└── Contains:
    ├── CodeLibraryGUI.app/
    ├── code-library/ (optional)
    └── README.txt
```

## Platform-Specific Notes

### Windows
- Windows Defender may flag the executable as unknown
- Add to exclusions if needed
- Test on Windows 7, 10, 11

### Linux
- Different distributions may have different tkinter packages
- Test on Ubuntu, Fedora, Arch
- Ensure executable permissions are set

### macOS
- Gatekeeper may block unsigned apps
- Users may need to right-click → Open
- Test on macOS 10.13+

## Code Library Path

The executable will use the default code library path from the source code. Users can:
1. Modify the path before building
2. Edit the executable (not recommended)
3. Use environment variables (if implemented)
4. Use a configuration file (if implemented)

## Building for Distribution

### Prerequisites
1. Clean build environment
2. All dependencies installed
3. Code library path configured
4. Test the build locally first

### Steps
1. Run the appropriate build script
2. Test the executable
3. Package with code library (optional)
4. Create distribution package
5. Test on clean system
6. Upload to release repository

## Automated Building

For automated CI/CD pipelines:
```bash
# Windows
pip install pyinstaller
pyinstaller installers/windows_installer.spec

# Linux
python3 -m pip install pyinstaller
python3 -m PyInstaller installers/windows_installer.spec

# macOS
python3 -m pip install pyinstaller
python3 -m PyInstaller installers/windows_installer.spec
```

## Support

For issues with installers:
1. Check the main [Troubleshooting Guide](../docs/TROUBLESHOOTING.md)
2. Verify platform-specific requirements
3. Test with console output enabled
4. Check PyInstaller documentation: https://pyinstaller.org/
