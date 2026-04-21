#!/bin/bash
# macOS Installer Build Script for Code Library GUI
# This script builds a macOS executable using PyInstaller

echo "========================================"
echo "Code Library GUI - macOS Installer Builder"
echo "========================================"
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3 using Homebrew:"
    echo "  brew install python-tk"
    exit 1
fi

echo "Python 3 found:"
python3 --version
echo ""

# Install PyInstaller if not already installed
if ! python3 -m pip show pyinstaller &> /dev/null; then
    echo "Installing PyInstaller..."
    # Try user installation first
    python3 -m pip install pyinstaller --user 2>/dev/null || {
        echo "User installation failed. Trying pipx..."
        pipx install pyinstaller 2>/dev/null || {
            echo "pipx not available. Creating virtual environment..."
            python3 -m venv venv_installer
            source venv_installer/bin/activate
            pip install pyinstaller
            deactivate
        }
    }
    echo ""
fi

# Create installers directory if it doesn't exist
mkdir -p installers/dist

# Build the executable
echo "Building macOS executable..."
cd ..
python3 -m PyInstaller installers/windows_installer.spec --clean

if [ $? -ne 0 ]; then
    echo "ERROR: PyInstaller build failed"
    exit 1
fi

echo ""
echo "========================================"
echo "Build completed successfully!"
echo "========================================"
echo ""
echo "Executable location: dist/CodeLibraryGUI"
echo ""
echo "To run the application:"
echo "  1. Navigate to the dist folder"
echo "  2. Run: ./CodeLibraryGUI"
echo ""
echo "To create a .app bundle (optional):"
echo "  1. Create .app structure: mkdir -p CodeLibraryGUI.app/Contents/MacOS"
echo "  2. Move executable: mv dist/CodeLibraryGUI CodeLibraryGUI.app/Contents/MacOS/"
echo "  3. Create Info.plist in Contents/"
echo ""
echo "To create a DMG installer:"
echo "  1. Create a folder with the app and code-library"
echo "  2. Use Disk Utility to create a DMG"
echo "  3. Or use: hdiutil create CodeLibraryGUI.dmg -srcfolder ./CodeLibraryGUI.app"
echo ""
