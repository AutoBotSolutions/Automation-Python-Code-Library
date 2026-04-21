@echo off
REM Windows Installer Build Script for Code Library GUI
REM This script builds a Windows executable using PyInstaller

echo ========================================
echo Code Library GUI - Windows Installer Builder
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/downloads/windows/
    pause
    exit /b 1
)

echo Python found:
python --version
echo.

REM Install PyInstaller if not already installed
pip show pyinstaller >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing PyInstaller...
    pip install pyinstaller
    echo.
)

REM Create installers directory if it doesn't exist
if not exist "installers\dist" mkdir "installers\dist"

REM Build the executable
echo Building Windows executable...
cd ..
pyinstaller installers/windows_installer.spec --clean

if %errorlevel% neq 0 (
    echo ERROR: PyInstaller build failed
    pause
    exit /b 1
)

echo.
echo ========================================
echo Build completed successfully!
echo ========================================
echo.
echo Executable location: dist\CodeLibraryGUI.exe
echo.
echo To run the application:
echo   1. Navigate to the dist folder
echo   2. Double-click CodeLibraryGUI.exe
echo.
echo To create a portable installer:
echo   1. Copy CodeLibraryGUI.exe to a new folder
echo   2. Include the code-library directory
echo   3. Create a README with instructions
echo.

pause
