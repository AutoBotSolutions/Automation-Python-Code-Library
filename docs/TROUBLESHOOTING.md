# Troubleshooting Guide

This guide covers common issues and their solutions for the Code Library GUI system.

## Installation Issues

### Python Not Found

**Windows:**
```
'python' is not recognized as an internal or external command
```

**Solution:**
1. Reinstall Python from python.org
2. Check "Add Python to PATH" during installation
3. Restart Command Prompt
4. Verify with: `python --version`

**Linux:**
```
python3: command not found
```

**Solution:**
```bash
sudo apt install python3 python3-tk  # Ubuntu/Debian
sudo dnf install python3 python3-tkinter  # Fedora
sudo pacman -S python tk  # Arch Linux
```

**macOS:**
```
python3: command not found
```

**Solution:**
```bash
brew install python-tk
```

### tkinter Not Found

**Error:**
```
ModuleNotFoundError: No module named 'tkinter'
```

**Solution:**

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

## GUI Issues

### GUI Not Appearing

**Symptoms:** Script runs but no window appears

**Solutions:**
1. Check you're not in a headless environment
2. For Linux SSH: Use `ssh -X` or `ssh -Y` for X11 forwarding
3. Try running with `python3` instead of `python`
4. Check display settings: `echo $DISPLAY` (Linux)

### Window Closes Immediately

**Symptoms:** Window opens then closes instantly

**Solutions:**
1. Run from terminal to see error messages
2. Check for syntax errors in code_library_gui.py
3. Verify library path exists
4. Check for missing dependencies

### GUI Freezes

**Symptoms:** GUI becomes unresponsive

**Solutions:**
1. Large code library may take time to load
2. Check if directory scanning is stuck
3. Try with smaller directory first
4. Check system resources (CPU, RAM)

## File Access Issues

### Files Not Loading

**Symptoms:** Selected file doesn't display in viewer

**Solutions:**
1. Check file permissions
2. Verify file is readable
3. Check file encoding (should be UTF-8 or compatible)
4. Check for file corruption

### Encoding Errors

**Error:**
```
UnicodeDecodeError: 'utf-8' codec can't decode byte
```

**Solution:**
The GUI handles multiple encodings automatically. If errors persist:
1. Ensure files are UTF-8 encoded
2. Check for binary files in library
3. Verify file isn't corrupted

### Directory Not Found

**Error:**
```
Error: Library path not found
```

**Solutions:**
1. Update library_path in code_library_gui.py line 31
2. Verify path exists: `ls /path/to/code-library` (Linux/macOS) or `dir C:\path\to\code-library` (Windows)
3. Check path spelling and case sensitivity
4. Ensure path uses correct format for OS

## Tracking Issues

### Tracking Files Not Created

**Symptoms:** tracking_log.txt or usage_stats.json not created

**Solutions:**
1. Check write permissions in application directory
2. Run as administrator (Windows) if needed
3. Check disk space
4. Verify directory is writable

### Statistics Not Updating

**Symptoms:** Statistics show old or no data

**Solutions:**
1. Check usage_stats.json is writable
2. Verify tracker is initialized
3. Check for JSON syntax errors in stats file
4. Delete stats file and restart to regenerate

### Changes Not Detected

**Symptoms:** Refresh doesn't show new/modified files

**Solutions:**
1. Check file permissions for scanning
2. Verify subprocess `find` command works
3. Check for permission errors in directory
4. Ensure files have .py extension

## Editor Issues

### Editor Won't Open

**Symptoms:** Clicking "Open in Editor" does nothing

**Solutions:**
1. Check file exists and is accessible
2. Verify AdvancedTextEditor class is not throwing errors
3. Check for tkinter Toplevel issues
4. Run from terminal to see error messages

### Save Fails

**Error:**
```
PermissionError: [Errno 13] Permission denied
```

**Solutions:**
1. Check file write permissions
2. Ensure file is not open in another program
3. Run as administrator if needed (Windows)
4. Check disk space

### Syntax Highlighting Not Working

**Symptoms:** Code appears without colors

**Solutions:**
1. Verify configure_syntax_tags() is called
2. Check COLORS dictionary is defined
3. Ensure text widget tags are configured
4. Try reloading the file

## Performance Issues

### Slow Loading

**Symptoms:** GUI takes long time to start

**Solutions:**
1. Large code library takes time to scan
2. Reduce library size for testing
3. Check system resources
4. Disable tracking temporarily

### High Memory Usage

**Symptoms:** GUI uses excessive RAM

**Solutions:**
1. Large files in viewer consume memory
2. Close unused editor windows
3. Reduce number of files loaded
4. Check for memory leaks in tracking

### CPU Spikes

**Symptoms:** High CPU usage during operation

**Solutions:**
1. Directory scanning may be intensive
2. Check for infinite loops in code
3. Verify subprocess commands complete
4. Disable change detection if not needed

## Platform-Specific Issues

### Windows-Specific

#### Path Issues
**Error:** Invalid path format

**Solution:** Use raw strings for Windows paths:
```python
self.library_path = r"C:\path\to\code-library"
```

#### Firewall Blocking
**Symptoms:** Network operations blocked

**Solution:** Add Python to Windows Firewall exceptions

#### Defender Blocking
**Symptoms:** Application blocked by Windows Defender

**Solution:** Add folder to exclusion list in Windows Security

### Linux-Specific

#### X11 Forwarding
**Error:** Cannot open display

**Solution:** Use SSH with X forwarding:
```bash
ssh -X user@server
```

#### Permission Denied
**Error:** Permission denied accessing directory

**Solution:**
```bash
chmod +r /path/to/code-library
```

#### Library Path Issues
**Error:** Library path not accessible

**Solution:** Ensure path is correct and user has read permissions

### macOS-Specific

#### Gatekeeper Blocking
**Error:** App can't be opened

**Solution:**
```bash
xattr -d com.apple.quarantine code_library_gui.py
```

#### Path Issues
**Error:** Library path not found

**Solution:** Use macOS-style paths:
```python
self.library_path = "/Users/username/code-library"
```

#### Notarization Issues
**Symptoms:** macOS security warnings

**Solution:** Run with right-click → Open if blocked

## Network Issues

### GitHub Clone Fails

**Error:**
```
fatal: unable to access 'https://github.com/...'
```

**Solutions:**
1. Check internet connection
2. Verify repository URL is correct
3. Use SSH instead of HTTPS if needed
4. Check firewall settings

### 2FA Authentication Fails

**Error:**
```
Authentication failed
```

**Solutions:**
1. Use Personal Access Token instead of password
2. Verify token has correct scopes
3. Check token hasn't expired
4. Regenerate token if needed

## Data Loss Prevention

### Accidental File Deletion

**Prevention:**
1. Backup code-library directory regularly
2. Use version control (git)
3. Keep copies of important scripts
4. Test changes on copies first

### Tracking Data Loss

**Prevention:**
1. Backup usage_stats.json regularly
2. Monitor tracking_log.txt size
3. Archive old logs periodically
4. Don't delete tracking files

## Debugging

### Enable Debug Mode

Add logging to identify issues:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Check Logs

Review tracking_log.txt for error patterns:
```bash
cat tracking_log.txt
```

### Test Individual Components

Test tracker separately:
```python
from code_library_gui import SystemTracker
tracker = SystemTracker("/path/to/library")
tracker.detect_changes()
```

Test editor separately:
```python
from code_library_gui import AdvancedTextEditor
import tkinter as tk
root = tk.Tk()
editor = AdvancedTextEditor(root, "/path/to/file.py")
root.mainloop()
```

## Getting Help

If issues persist:

1. Check this guide first
2. Review main README.md
3. Check Installation Guide
4. Open GitHub issue with:
   - Python version
   - Operating system
   - Error messages
   - Steps to reproduce
   - Expected vs actual behavior

## Common Error Messages

### `SyntaxError: invalid syntax`
- Check code_library_gui.py for syntax errors
- Verify Python version compatibility

### `ModuleNotFoundError: No module named 'tkinter'`
- Install tkinter for your platform
- Reinstall Python with tkinter included

### `PermissionError: [Errno 13] Permission denied`
- Check file/directory permissions
- Run as administrator if needed

### `FileNotFoundError: [Errno 2] No such file or directory`
- Verify library path is correct
- Check path exists and is accessible

### `UnicodeDecodeError`
- File encoding issue (GUI handles automatically)
- Check file isn't corrupted

### `ConnectionRefusedError`
- Network connection issue
- Check internet connection
- Verify URL is correct

## Maintenance

### Regular Maintenance Tasks

1. **Clean tracking logs:** Archive old logs periodically
2. **Backup code library:** Regular backups of scripts
3. **Update dependencies:** Keep Python and libraries updated
4. **Review statistics:** Check usage patterns
5. **Clean temporary files:** Remove .pyc files

### System Health Checks

1. Verify all scripts are accessible
2. Check for corrupted files
3. Test GUI functionality
4. Verify tracking is working
5. Check disk space

---

Still having issues? Open a GitHub issue with detailed information about your problem.
