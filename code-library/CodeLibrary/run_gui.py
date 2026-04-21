#!/usr/bin/env python3
"""
Launcher script for CodeLibrary GUI application.
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from codelibrary.gui import main

if __name__ == "__main__":
    main()
