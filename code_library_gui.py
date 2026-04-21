#!/usr/bin/env python3
"""
Simple GUI for accessing Automation Python Code Library
Provides easy browsing and copying of automation scripts
"""

import sys
import os
# Set environment variable before any other imports to prevent bytecode compilation
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
sys.dont_write_bytecode = True

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import subprocess
from pathlib import Path

# Prevent accidental imports from code library
# Use environment variable or resolve relative to script location
script_dir = Path(__file__).parent.resolve()
library_path = os.environ.get('CODE_LIBRARY_PATH', str(script_dir / 'code-library'))

# Resolve to absolute path before changing directory
library_path = str(Path(library_path).resolve())

if library_path in sys.path:
    sys.path.remove(library_path)

# Change working directory to avoid Python compiling files in code library
original_cwd = os.getcwd()
temp_dir = os.environ.get('TEMP_DIR', '/tmp')
os.chdir(temp_dir)

# Color Schemes
COLOR_SCHEMES = {
    'Dark': {
        'bg_primary': '#1e1e2e',
        'bg_secondary': '#313244',
        'bg_tertiary': '#45475a',
        'fg_primary': '#cdd6f4',
        'fg_secondary': '#a6adc8',
        'accent': '#89b4fa',
        'accent_hover': '#b4befe',
        'success': '#a6e3a1',
        'warning': '#f9e2af',
        'error': '#f38ba8',
        'border': '#45475a',
        'highlight': '#f5c2e7',
        'code_bg': '#11111b',
        'line_number_bg': '#1e1e2e',
        'line_number_fg': '#6c7086',
    },
    'Light': {
        'bg_primary': '#ffffff',
        'bg_secondary': '#f0f0f0',
        'bg_tertiary': '#e0e0e0',
        'fg_primary': '#333333',
        'fg_secondary': '#666666',
        'accent': '#0078d4',
        'accent_hover': '#106ebe',
        'success': '#107c10',
        'warning': '#d83b01',
        'error': '#d13438',
        'border': '#cccccc',
        'highlight': '#8b4789',
        'code_bg': '#f5f5f5',
        'line_number_bg': '#f0f0f0',
        'line_number_fg': '#999999',
    },
    'High Contrast': {
        'bg_primary': '#000000',
        'bg_secondary': '#0a0a0a',
        'bg_tertiary': '#1a1a1a',
        'fg_primary': '#ffffff',
        'fg_secondary': '#e0e0e0',
        'accent': '#ffff00',
        'accent_hover': '#e6e600',
        'success': '#00ff00',
        'warning': '#ffff00',
        'error': '#ff0000',
        'border': '#ffffff',
        'highlight': '#00ffff',
        'code_bg': '#000000',
        'line_number_bg': '#0a0a0a',
        'line_number_fg': '#ffffff',
    },
    'Ocean': {
        'bg_primary': '#0f172a',
        'bg_secondary': '#1e293b',
        'bg_tertiary': '#334155',
        'fg_primary': '#f1f5f9',
        'fg_secondary': '#cbd5e1',
        'accent': '#38bdf8',
        'accent_hover': '#0ea5e9',
        'success': '#4ade80',
        'warning': '#fbbf24',
        'error': '#f87171',
        'border': '#475569',
        'highlight': '#c084fc',
        'code_bg': '#020617',
        'line_number_bg': '#0f172a',
        'line_number_fg': '#64748b',
    },
}

# Current color scheme (default: Dark)
current_scheme = 'Dark'
COLORS = COLOR_SCHEMES[current_scheme]


class SystemTracker:
    """Track system usage, file changes, and statistics"""
    
    def __init__(self, library_path):
        self.library_path = library_path
        script_dir = Path(__file__).parent.resolve()
        log_file = os.environ.get('TRACKING_LOG_FILE', str(script_dir / 'tracking_log.txt'))
        stats_file = os.environ.get('STATS_FILE', str(script_dir / 'usage_stats.json'))
        
        # Resolve to absolute paths
        self.log_file = str(Path(log_file).resolve())
        self.stats_file = str(Path(stats_file).resolve())
        
        self.file_hashes = {}
        self.usage_stats = {
            'file_accesses': {},
            'category_accesses': {},
            'total_sessions': 0,
            'session_start': None
        }

        self.load_tracking_data()
    
    def load_tracking_data(self):
        """Load existing tracking data"""
        import json
        try:
            if os.path.exists(self.stats_file):
                with open(self.stats_file, 'r') as f:
                    self.usage_stats = json.load(f)
        except Exception as e:
            print(f"Error loading tracking data: {e}")
    
    def save_tracking_data(self):
        """Save tracking data to file"""
        import json
        try:
            with open(self.stats_file, 'w') as f:
                json.dump(self.usage_stats, f, indent=2)
        except Exception as e:
            print(f"Error saving tracking data: {e}")
    
    def log_event(self, event_type, details):
        """Log an event to the tracking log"""
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {event_type}: {details}\n"
        
        try:
            with open(self.log_file, 'a') as f:
                f.write(log_entry)
        except Exception as e:
            print(f"Error writing to log: {e}")
    
    def track_file_access(self, file_path):
        """Track when a file is accessed"""
        import os
        file_name = os.path.basename(file_path)
        category = os.path.basename(os.path.dirname(file_path))
        
        # Update file access count
        if file_name not in self.usage_stats['file_accesses']:
            self.usage_stats['file_accesses'][file_name] = 0
        self.usage_stats['file_accesses'][file_name] += 1
        
        # Update category access count
        if category not in self.usage_stats['category_accesses']:
            self.usage_stats['category_accesses'][category] = 0
        self.usage_stats['category_accesses'][category] += 1
        
        self.log_event("FILE_ACCESS", f"{file_name} in category {category}")
        self.save_tracking_data()
    
    def track_file_edit(self, file_path):
        """Track when a file is edited"""
        import os
        file_name = os.path.basename(file_path)
        self.log_event("FILE_EDIT", f"{file_name} was edited")
    
    def detect_changes(self):
        """Detect changes in the code library"""
        import hashlib
        changes = []
        
        for root, dirs, files in os.walk(self.library_path):
            # Skip __pycache__ directories
            dirs[:] = [d for d in dirs if d != '__pycache__']
            
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'rb') as f:
                            file_hash = hashlib.md5(f.read()).hexdigest()
                        
                        file_key = os.path.relpath(file_path, self.library_path)
                        
                        if file_key in self.file_hashes:
                            if self.file_hashes[file_key] != file_hash:
                                changes.append(f"MODIFIED: {file_key}")
                                self.log_event("FILE_MODIFIED", file_key)
                        else:
                            changes.append(f"NEW: {file_key}")
                            self.log_event("FILE_ADDED", file_key)
                        
                        self.file_hashes[file_key] = file_hash
                    except Exception as e:
                        print(f"Error hashing file {file_path}: {e}")
        
        # Check for deleted files
        existing_files = set()
        for root, dirs, files in os.walk(self.library_path):
            dirs[:] = [d for d in dirs if d != '__pycache__']
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    file_key = os.path.relpath(file_path, self.library_path)
                    existing_files.add(file_key)
        
        for file_key in list(self.file_hashes.keys()):
            if file_key not in existing_files:
                changes.append(f"DELETED: {file_key}")
                self.log_event("FILE_DELETED", file_key)
                del self.file_hashes[file_key]
        
        return changes
    
    def start_session(self):
        """Start a new tracking session"""
        import datetime
        self.usage_stats['total_sessions'] += 1
        self.usage_stats['session_start'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.log_event("SESSION_START", f"Session #{self.usage_stats['total_sessions']}")
        self.save_tracking_data()
    
    def end_session(self):
        """End the current tracking session"""
        import datetime
        session_end = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.log_event("SESSION_END", f"Session ended at {session_end}")
        self.save_tracking_data()
    
    def get_statistics(self):
        """Get usage statistics"""
        return {
            'total_sessions': self.usage_stats['total_sessions'],
            'most_accessed_files': sorted(self.usage_stats['file_accesses'].items(), 
                                         key=lambda x: x[1], reverse=True)[:10],
            'most_accessed_categories': sorted(self.usage_stats['category_accesses'].items(), 
                                             key=lambda x: x[1], reverse=True)[:10],
            'total_files_tracked': len(self.file_hashes)
        }


class AdvancedTextEditor:
    """Advanced text editor with syntax highlighting and editing features"""
    
    def __init__(self, parent, file_path=None, tracker=None):
        self.editor_window = tk.Toplevel(parent)
        self.editor_window.title("Advanced Text Editor")
        self.editor_window.geometry("1000x700")
        
        # Apply modern theme to window
        self.editor_window.configure(bg=COLORS['bg_primary'])
        
        self.file_path = file_path
        self.modified = False
        self.tracker = tracker
        self.parent = parent
        
        self.create_editor_layout()
        
        if file_path:
            self.load_file(file_path)
    
    def create_editor_layout(self):
        """Create the editor layout"""
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Menu bar
        menubar = tk.Menu(self.editor_window, bg=COLORS['bg_secondary'], 
                         fg=COLORS['fg_primary'], activebackground=COLORS['accent'],
                         activeforeground=COLORS['bg_primary'])
        self.editor_window.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0, bg=COLORS['bg_secondary'], 
                           fg=COLORS['fg_primary'], activebackground=COLORS['accent'],
                           activeforeground=COLORS['bg_primary'])
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Close", command=self.close_editor)
        
        # Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0, bg=COLORS['bg_secondary'], 
                           fg=COLORS['fg_primary'], activebackground=COLORS['accent'],
                           activeforeground=COLORS['bg_primary'])
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", command=self.undo)
        edit_menu.add_command(label="Redo", command=self.redo)
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=self.cut)
        edit_menu.add_command(label="Copy", command=self.copy)
        edit_menu.add_command(label="Paste", command=self.paste)
        edit_menu.add_separator()
        edit_menu.add_command(label="Find", command=self.show_find_dialog)
        edit_menu.add_command(label="Replace", command=self.show_replace_dialog)
        
        # Toolbar
        toolbar = ttk.Frame(self.editor_window)
        toolbar.pack(fill=tk.X, padx=5, pady=5)
        
        # Style buttons
        style.configure('TButton', background=COLORS['bg_tertiary'], 
                       foreground=COLORS['fg_primary'], borderwidth=0,
                       focuscolor='none')
        style.map('TButton', background=[('active', COLORS['accent'])])
        
        ttk.Button(toolbar, text="New", command=self.new_file).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="Open", command=self.open_file).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="Save", command=self.save_file).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="Save As", command=self.save_file_as).pack(side=tk.LEFT, padx=2)
        ttk.Separator(toolbar, orient=tk.VERTICAL).pack(side=tk.LEFT, padx=5, fill=tk.Y)
        ttk.Button(toolbar, text="Find", command=self.show_find_dialog).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="Replace", command=self.show_replace_dialog).pack(side=tk.LEFT, padx=2)
        
        # File label
        self.file_label = ttk.Label(toolbar, text="No file", 
                                   foreground=COLORS['fg_secondary'], background=COLORS['bg_secondary'])
        self.file_label.pack(side=tk.RIGHT, padx=5)
        
        # Main content area
        content_frame = tk.Frame(self.editor_window, bg=COLORS['bg_primary'])
        content_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Line numbers
        self.line_numbers = tk.Text(content_frame, width=4, padx=3, takefocus=0,
                                   font=('Consolas', 10), state=tk.DISABLED,
                                   bg=COLORS['line_number_bg'], fg=COLORS['line_number_fg'],
                                   insertbackground=COLORS['accent'])
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)
        
        # Text editor
        self.text = tk.Text(content_frame, font=('Consolas', 10), wrap=tk.NONE,
                           undo=True, maxundo=50, bg=COLORS['code_bg'],
                           fg=COLORS['fg_primary'], insertbackground=COLORS['accent'],
                           selectbackground=COLORS['accent'])
        self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Scrollbars
        v_scrollbar = ttk.Scrollbar(content_frame, orient=tk.VERTICAL, command=self.text.yview)
        h_scrollbar = ttk.Scrollbar(self.editor_window, orient=tk.HORIZONTAL, command=self.text.xview)
        self.text.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        h_scrollbar.pack(fill=tk.X)
        
        # Style scrollbars
        style.configure('TScrollbar', background=COLORS['bg_tertiary'], 
                       troughcolor=COLORS['bg_secondary'])
        
        # Bind events
        self.text.bind('<Key>', self.on_key_press)
        self.text.bind('<ButtonRelease-1>', self.update_line_numbers)
        self.text.bind('<KeyRelease>', self.update_line_numbers)
        
        # Configure tags for syntax highlighting
        self.configure_syntax_tags()
    
    def configure_syntax_tags(self):
        """Configure syntax highlighting tags"""
        self.text.tag_config('keyword', foreground=COLORS['accent'], font=('Consolas', 10, 'bold'))
        self.text.tag_config('string', foreground=COLORS['success'])
        self.text.tag_config('comment', foreground=COLORS['fg_secondary'], font=('Consolas', 10, 'italic'))
        self.text.tag_config('function', foreground=COLORS['highlight'])
        self.text.tag_config('number', foreground=COLORS['warning'])
    
    def load_file(self, file_path):
        """Load a file into the editor"""
        try:
            with open(file_path, 'rb') as f:
                raw_bytes = f.read()
            
            # Try to decode with multiple encodings
            content = None
            encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1', 'ascii']
            
            for encoding in encodings:
                try:
                    content = raw_bytes.decode(encoding, errors='ignore')
                    break
                except Exception:
                    continue
            
            if content is None:
                content = raw_bytes.decode('utf-8', errors='replace')
            
            self.text.delete(1.0, tk.END)
            self.text.insert(1.0, content)
            self.file_path = file_path
            self.file_label.config(text=os.path.basename(file_path))
            self.modified = False
            self.update_line_numbers()
            self.apply_syntax_highlighting()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {str(e)}")
    
    def save_file(self):
        """Save the current file"""
        if not self.file_path:
            return self.save_file_as()
        
        try:
            content = self.text.get(1.0, tk.END)
            with open(self.file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            self.modified = False
            self.file_label.config(text=os.path.basename(self.file_path))
            
            # Track file edit
            if self.tracker:
                self.tracker.track_file_edit(self.file_path)
            
            messagebox.showinfo("Success", "File saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {str(e)}")
    
    def save_file_as(self):
        """Save the file with a new name"""
        from tkinter import filedialog
        file_path = filedialog.asksaveasfilename(
            defaultextension=".py",
            filetypes=[("Python files", "*.py"), ("All files", "*.*")]
        )
        if file_path:
            self.file_path = file_path
            self.save_file()
    
    def new_file(self):
        """Create a new file"""
        self.text.delete(1.0, tk.END)
        self.file_path = None
        self.modified = False
        self.file_label.config(text="New file")
        self.update_line_numbers()
    
    def open_file(self):
        """Open a file"""
        from tkinter import filedialog
        file_path = filedialog.askopenfilename(
            filetypes=[("Python files", "*.py"), ("All files", "*.*")]
        )
        if file_path:
            self.load_file(file_path)
    
    def close_editor(self):
        """Close the editor"""
        if self.modified:
            if messagebox.askyesno("Unsaved Changes", "You have unsaved changes. Close anyway?"):
                self.editor_window.destroy()
        else:
            self.editor_window.destroy()
    
    def undo(self):
        """Undo last action"""
        self.text.edit_undo()
    
    def redo(self):
        """Redo last action"""
        self.text.edit_redo()
    
    def cut(self):
        """Cut selected text"""
        self.text.event_generate("<<Cut>>")
    
    def copy(self):
        """Copy selected text"""
        self.text.event_generate("<<Copy>>")
    
    def paste(self):
        """Paste text"""
        self.text.event_generate("<<Paste>>")
    
    def show_find_dialog(self):
        """Show find dialog"""
        find_window = tk.Toplevel(self.editor_window)
        find_window.title("Find")
        find_window.geometry("300x100")
        
        ttk.Label(find_window, text="Find:").pack(padx=5, pady=5)
        find_entry = ttk.Entry(find_window)
        find_entry.pack(padx=5, pady=5, fill=tk.X)
        
        def find_text():
            search_term = find_entry.get()
            if search_term:
                self.text.tag_remove('found', '1.0', tk.END)
                pos = '1.0'
                while True:
                    pos = self.text.search(search_term, pos, stopindex=tk.END, 
                                          nocase=True, regexp=False)
                    if not pos:
                        break
                    end_pos = f"{pos}+{len(search_term)}c"
                    self.text.tag_add('found', pos, end_pos)
                    self.text.tag_config('found', background='yellow')
                    pos = end_pos
        
        ttk.Button(find_window, text="Find", command=find_text).pack(pady=5)
    
    def show_replace_dialog(self):
        """Show replace dialog"""
        replace_window = tk.Toplevel(self.editor_window)
        replace_window.title("Find and Replace")
        replace_window.geometry("400x150")
        
        ttk.Label(replace_window, text="Find:").pack(padx=5, pady=2)
        find_entry = ttk.Entry(replace_window)
        find_entry.pack(padx=5, pady=2, fill=tk.X)
        
        ttk.Label(replace_window, text="Replace with:").pack(padx=5, pady=2)
        replace_entry = ttk.Entry(replace_window)
        replace_entry.pack(padx=5, pady=2, fill=tk.X)
        
        button_frame = ttk.Frame(replace_window)
        button_frame.pack(pady=5)
        
        def replace_all():
            search_term = find_entry.get()
            replace_term = replace_entry.get()
            if search_term:
                content = self.text.get(1.0, tk.END)
                new_content = content.replace(search_term, replace_term)
                self.text.delete(1.0, tk.END)
                self.text.insert(1.0, new_content)
        
        ttk.Button(button_frame, text="Replace All", command=replace_all).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Close", command=replace_window.destroy).pack(side=tk.LEFT, padx=5)
    
    def on_key_press(self, event):
        """Handle key press events"""
        self.modified = True
        if not self.file_label.cget('text').startswith('*'):
            self.file_label.config(text=f"*{self.file_label.cget('text')}")
    
    def update_line_numbers(self, event=None):
        """Update line numbers"""
        self.line_numbers.config(state=tk.NORMAL)
        self.line_numbers.delete(1.0, tk.END)
        
        line_count = int(self.text.index('end-1c').split('.')[0])
        for i in range(1, line_count + 1):
            self.line_numbers.insert(tk.END, f"{i}\n")
        
        self.line_numbers.config(state=tk.DISABLED)
    
    def apply_syntax_highlighting(self):
        """Apply basic syntax highlighting for Python"""
        # Remove existing tags
        for tag in ['keyword', 'string', 'comment', 'function', 'number']:
            self.text.tag_remove(tag, '1.0', tk.END)
        
        content = self.text.get(1.0, tk.END)
        
        # Keywords
        keywords = ['def', 'class', 'if', 'else', 'elif', 'for', 'while', 'try', 'except',
                   'import', 'from', 'return', 'print', 'pass', 'break', 'continue', 'with',
                   'as', 'lambda', 'yield', 'raise', 'finally', 'assert', 'global', 'nonlocal',
                   'True', 'False', 'None', 'and', 'or', 'not', 'in', 'is']
        
        for keyword in keywords:
            self.highlight_pattern(keyword, 'keyword', word=True)
        
        # Strings
        self.highlight_pattern(r'".*?"', 'string')
        self.highlight_pattern(r".*?'", 'string')
        
        # Comments
        self.highlight_pattern(r'#.*$', 'comment')
        
        # Numbers
        self.highlight_pattern(r'\b\d+\b', 'number')
    
    def highlight_pattern(self, pattern, tag, word=False):
        """Highlight a pattern with a tag"""
        import re
        content = self.text.get(1.0, tk.END)
        
        flags = re.MULTILINE
        if word:
            pattern = rf'\b{pattern}\b'
        
        for match in re.finditer(pattern, content, flags):
            start = match.start()
            end = match.end()
            start_index = f"1.0+{start}c"
            end_index = f"1.0+{end}c"
            self.text.tag_add(tag, start_index, end_index)
    
    def update_editor_colors(self):
        """Update editor colors when color scheme changes"""
        # Update window background
        self.editor_window.configure(bg=COLORS['bg_primary'])
        
        # Update text widget
        self.text.configure(bg=COLORS['code_bg'], fg=COLORS['fg_primary'],
                          insertbackground=COLORS['accent'], selectbackground=COLORS['accent'])
        
        # Update line numbers
        self.line_numbers.configure(bg=COLORS['line_number_bg'], fg=COLORS['line_number_fg'])
        
        # Update file label
        self.file_label.configure(bg=COLORS['bg_secondary'], fg=COLORS['fg_secondary'])
        
        # Re-configure syntax highlighting tags
        self.configure_syntax_tags()
        
        # Re-apply syntax highlighting if content exists
        if self.text.get(1.0, tk.END).strip():
            self.apply_syntax_highlighting()


class CodeLibraryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Automation Code Library")
        self.root.geometry("1200x800")
        self.root.minsize(1000, 600)
        
        # Apply modern theme to main window
        self.root.configure(bg=COLORS['bg_primary'])
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Set the code library path from the already-resolved module-level variable
        self.library_path = library_path
        
        # Initialize tracker
        self.tracker = SystemTracker(self.library_path)
        self.tracker.start_session()
        self.tracker.detect_changes()  # Initial scan
        
        # Track open editor windows for color scheme updates
        self.open_editors = []
        
        # Create main layout
        self.create_layout()
        
        # Load categories
        self.load_categories()
        
        # Handle window close
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def create_layout(self):
        """Create the main GUI layout"""
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Style configuration with Windows-friendly fonts
        font_family = 'Segoe UI' if sys.platform == 'win32' else 'Arial'
        style.configure('TFrame', background=COLORS['bg_primary'])
        style.configure('TPanedWindow', background=COLORS['bg_primary'])
        style.configure('TLabel', background=COLORS['bg_primary'], foreground=COLORS['fg_primary'], 
                       font=(font_family, 10))
        style.configure('TButton', background=COLORS['bg_tertiary'], foreground=COLORS['fg_primary'], 
                       borderwidth=0, focuscolor='none', padding=(8, 4), font=(font_family, 9))
        style.map('TButton', background=[('active', COLORS['accent'])])
        style.configure('TEntry', fieldbackground=COLORS['bg_secondary'], foreground=COLORS['fg_primary'],
                       borderwidth=1, insertcolor=COLORS['accent'], font=(font_family, 9))
        style.configure('TCombobox', fieldbackground=COLORS['bg_secondary'], foreground=COLORS['fg_primary'],
                       background=COLORS['bg_tertiary'], borderwidth=1, font=(font_family, 9),
                       arrowcolor=COLORS['fg_primary'])
        style.map('TCombobox', fieldbackground=[('readonly', COLORS['bg_secondary']),
                                                ('focus', COLORS['bg_secondary'])],
                  foreground=[('readonly', COLORS['fg_primary']),
                             ('focus', COLORS['fg_primary'])])
        style.configure('Treeview', background=COLORS['bg_secondary'], foreground=COLORS['fg_primary'],
                       fieldbackground=COLORS['bg_secondary'], borderwidth=0, font=(font_family, 9))
        style.configure('Treeview.Heading', background=COLORS['bg_tertiary'], foreground=COLORS['fg_primary'],
                       borderwidth=0, font=(font_family, 9, 'bold'))
        style.map('Treeview', background=[('selected', COLORS['accent'])], 
                  foreground=[('selected', COLORS['bg_primary'])])
        style.configure('TScrollbar', background=COLORS['bg_tertiary'], troughcolor=COLORS['bg_secondary'])
        
        # Main container with paned window
        self.paned_window = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        self.paned_window.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Left panel - Categories and Files
        left_frame = tk.Frame(self.paned_window, bg=COLORS['bg_primary'])
        self.paned_window.add(left_frame, weight=1)
        
        # Right panel - Code viewer
        right_frame = tk.Frame(self.paned_window, bg=COLORS['bg_primary'])
        self.paned_window.add(right_frame, weight=3)
        
        # === LEFT PANEL ===
        # Search box
        search_frame = tk.Frame(left_frame, bg=COLORS['bg_primary'])
        search_frame.pack(fill=tk.X, padx=8, pady=(8, 5))
        
        font_family = 'Segoe UI' if sys.platform == 'win32' else 'Arial'
        tk.Label(search_frame, text="Search:", bg=COLORS['bg_primary'], fg=COLORS['fg_secondary'], 
                font=(font_family, 9)).pack(side=tk.LEFT)
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(search_frame, textvariable=self.search_var)
        self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=8)
        self.search_entry.bind('<KeyRelease>', self.on_search)
        
        # Categories tree
        tk.Label(left_frame, text="Categories", font=(font_family, 11, 'bold'), 
                bg=COLORS['bg_primary'], fg=COLORS['accent']).pack(anchor=tk.W, padx=8, pady=(12, 5))
        
        tree_frame = tk.Frame(left_frame, bg=COLORS['bg_primary'])
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=(0, 5))
        
        self.category_tree = ttk.Treeview(tree_frame, columns=('name',), show='tree headings', height=15)
        self.category_tree.heading('#0', text='Category')
        self.category_tree.column('#0', width=200)
        self.category_tree.bind('<<TreeviewSelect>>', self.on_category_select)
        
        # Tree scrollbar
        tree_scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.category_tree.yview)
        self.category_tree.configure(yscrollcommand=tree_scrollbar.set)
        
        self.category_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tree_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Files list
        tk.Label(left_frame, text="Files", font=(font_family, 11, 'bold'), 
                bg=COLORS['bg_primary'], fg=COLORS['accent']).pack(anchor=tk.W, padx=8, pady=(12, 5))
        
        files_frame = tk.Frame(left_frame, bg=COLORS['bg_primary'])
        files_frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=(0, 8))
        
        self.files_listbox = tk.Listbox(files_frame, height=15, bg=COLORS['bg_secondary'], 
                                       fg=COLORS['fg_primary'], selectbackground=COLORS['accent'],
                                       selectforeground=COLORS['bg_primary'], borderwidth=0,
                                       highlightthickness=0)
        self.files_listbox.bind('<<ListboxSelect>>', self.on_file_select)
        
        # Files scrollbar
        files_scrollbar = ttk.Scrollbar(files_frame, orient=tk.VERTICAL, command=self.files_listbox.yview)
        self.files_listbox.configure(yscrollcommand=files_scrollbar.set)
        
        self.files_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        files_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # === RIGHT PANEL ===
        # Code viewer header - top row with file label
        header_top = tk.Frame(right_frame, bg=COLORS['bg_primary'])
        header_top.pack(fill=tk.X, padx=8, pady=(8, 5))
        
        self.file_label = tk.Label(header_top, text="Select a file to view code", 
                                  font=(font_family, 11, 'bold'), bg=COLORS['bg_primary'], fg=COLORS['accent'])
        self.file_label.pack(side=tk.LEFT)
        
        # Header bottom row with controls and buttons
        header_bottom = tk.Frame(right_frame, bg=COLORS['bg_primary'])
        header_bottom.pack(fill=tk.X, padx=8, pady=(0, 5))
        
        # Theme and wrap controls on the left
        controls_frame = tk.Frame(header_bottom, bg=COLORS['bg_primary'])
        controls_frame.pack(side=tk.LEFT)
        
        # Color scheme selector
        tk.Label(controls_frame, text="Theme:", bg=COLORS['bg_primary'], fg=COLORS['fg_secondary'],
                font=(font_family, 9)).pack(side=tk.LEFT, padx=(0, 5))
        self.scheme_var = tk.StringVar(value=current_scheme)
        self.scheme_combo = ttk.Combobox(controls_frame, textvariable=self.scheme_var, 
                                        values=list(COLOR_SCHEMES.keys()), state='readonly', width=10)
        self.scheme_combo.pack(side=tk.LEFT, padx=2)
        self.scheme_combo.bind('<<ComboboxSelected>>', self.change_color_scheme)
        
        # Wrap mode selector
        tk.Label(controls_frame, text="Wrap:", bg=COLORS['bg_primary'], fg=COLORS['fg_secondary'],
                font=(font_family, 9)).pack(side=tk.LEFT, padx=(10, 5))
        self.wrap_var = tk.StringVar(value='None')
        self.wrap_combo = ttk.Combobox(controls_frame, textvariable=self.wrap_var,
                                      values=['None', 'Word', 'Char'], state='readonly', width=8)
        self.wrap_combo.pack(side=tk.LEFT, padx=2)
        self.wrap_combo.bind('<<ComboboxSelected>>', self.change_wrap_mode)
        
        # Action buttons on the right
        button_frame = tk.Frame(header_bottom, bg=COLORS['bg_primary'])
        button_frame.pack(side=tk.RIGHT)
        
        self.stats_btn = ttk.Button(button_frame, text="Statistics", command=self.show_statistics)
        self.stats_btn.pack(side=tk.LEFT, padx=2)
        
        self.refresh_btn = ttk.Button(button_frame, text="Refresh", command=self.refresh_library)
        self.refresh_btn.pack(side=tk.LEFT, padx=2)
        
        self.copy_btn = ttk.Button(button_frame, text="Copy Code", command=self.copy_code, state=tk.DISABLED)
        self.copy_btn.pack(side=tk.LEFT, padx=2)
        
        self.open_btn = ttk.Button(button_frame, text="Open in Editor", command=self.open_in_editor, state=tk.DISABLED)
        self.open_btn.pack(side=tk.LEFT, padx=2)
        
        # Code text area
        tk.Label(right_frame, text="Code Content", font=(font_family, 11, 'bold'), 
                bg=COLORS['bg_primary'], fg=COLORS['accent']).pack(anchor=tk.W, padx=8, pady=(12, 5))
        
        code_font = 'Consolas' if sys.platform == 'win32' else 'Courier New'
        self.code_text = scrolledtext.ScrolledText(right_frame, wrap=tk.NONE, font=(code_font, 10),
                                                   bg=COLORS['code_bg'], fg=COLORS['fg_primary'],
                                                   insertbackground=COLORS['accent'],
                                                   selectbackground=COLORS['accent'],
                                                   borderwidth=0, highlightthickness=0)
        self.code_text.pack(fill=tk.BOTH, expand=True, padx=8, pady=(0, 8))
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        self.status_bar = tk.Label(self.root, textvariable=self.status_var, relief=tk.FLAT, anchor=tk.W,
                            bg=COLORS['bg_secondary'], fg=COLORS['fg_secondary'], padx=5, pady=3)
        self.status_bar.pack(fill=tk.X, side=tk.BOTTOM)
        
        self.current_file_path = None
    
    def load_categories(self):
        """Load all categories (directories) from the code library with nested structure"""
        try:
            if os.path.exists(self.library_path):
                self.category_tree.delete(*self.category_tree.get_children())
                self.build_tree('', self.library_path)
                
                total_items = len(self.category_tree.get_children())
                self.status_var.set(f"Loaded directory structure with {total_items} top-level categories")
            else:
                messagebox.showerror("Error", f"Library path not found: {self.library_path}")
                self.status_var.set("Error: Library path not found")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load categories: {str(e)}")
            self.status_var.set(f"Error: {str(e)}")
    
    def build_tree(self, parent, path):
        """Recursively build directory tree using subprocess to avoid Python compilation"""
        try:
            if not os.path.exists(path):
                print(f"Path does not exist: {path}")
                return
            
            if not os.path.isdir(path):
                print(f"Path is not a directory: {path}")
                return
            
            try:
                # Use subprocess to list directories to avoid Python compilation
                result = subprocess.run(['find', path, '-maxdepth', '1', '-type', 'd', 
                                      '-not', '-name', '_*', '-not', '-name', '__pycache__'],
                                      capture_output=True, text=True, timeout=10)
                
                if result.returncode != 0:
                    print(f"Error listing directory {path}: {result.stderr}")
                    return
                
                # Parse output and filter
                items = []
                for line in result.stdout.strip().split('\n'):
                    if line and line != path:
                        item_name = os.path.basename(line)
                        if item_name and not item_name.startswith('_') and item_name != '__pycache__':
                            items.append(item_name)
                
                items = sorted(items)
            except subprocess.TimeoutExpired:
                print(f"Timeout listing directory {path}")
                return
            except Exception as e:
                print(f"Error listing directory {path}: {str(e)}")
                return
            
            for item in items:
                item_path = os.path.join(path, item)
                try:
                    node = self.category_tree.insert(parent, tk.END, text=item, values=(item_path,))
                    self.build_tree(node, item_path)
                except Exception as e:
                    print(f"Error adding node {item} to tree: {str(e)}")
                    continue
        except Exception as e:
            print(f"Error building tree for {path}: {str(e)}")
    
    def on_category_select(self, event):
        """Handle category selection"""
        selection = self.category_tree.selection()
        if selection:
            category_path = self.category_tree.item(selection[0])['values'][0]
            self.load_files(category_path)
    
    def load_files(self, category_path):
        """Load files from selected category using subprocess to avoid Python compilation"""
        try:
            if not os.path.exists(category_path):
                self.files_listbox.delete(0, tk.END)
                self.status_var.set(f"Directory not found: {category_path}")
                return
            
            if not os.path.isdir(category_path):
                self.files_listbox.delete(0, tk.END)
                self.status_var.set(f"Not a directory: {category_path}")
                return
            
            try:
                # Use subprocess to list files to avoid Python compilation
                result = subprocess.run(['find', category_path, '-maxdepth', '1', '-type', 'f',
                                      '-name', '*.py', '-not', '-name', '_*'],
                                      capture_output=True, text=True, timeout=10)
                
                if result.returncode != 0:
                    self.files_listbox.delete(0, tk.END)
                    self.status_var.set(f"Error listing directory: {result.stderr}")
                    return
                
                # Parse output and filter
                files = []
                for line in result.stdout.strip().split('\n'):
                    if line:
                        file_name = os.path.basename(line)
                        if file_name and not file_name.startswith('_'):
                            files.append(file_name)
                
                files = sorted(files)
            except subprocess.TimeoutExpired:
                self.files_listbox.delete(0, tk.END)
                self.status_var.set(f"Timeout listing directory: {category_path}")
                return
            except Exception as e:
                self.files_listbox.delete(0, tk.END)
                self.status_var.set(f"Error listing directory: {str(e)}")
                return
            
            self.files_listbox.delete(0, tk.END)
            for file in files:
                self.files_listbox.insert(tk.END, file)
            
            category_name = os.path.basename(category_path)
            self.status_var.set(f"Loaded {len(files)} files from {category_name}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load files: {str(e)}")
            self.status_var.set(f"Error: {str(e)}")
    
    def on_file_select(self, event):
        """Handle file selection"""
        selection = self.files_listbox.curselection()
        if selection:
            filename = self.files_listbox.get(selection[0])
            category_selection = self.category_tree.selection()
            if category_selection:
                category_path = self.category_tree.item(category_selection[0])['values'][0]
                self.load_code(category_path, filename)
    
    def load_code(self, category_path, filename):
        """Load and display code from selected file"""
        try:
            file_path = os.path.join(category_path, filename)
            self.current_file_path = file_path
            
            # Track file access
            self.tracker.track_file_access(file_path)
            
            # Always read in binary mode to prevent Python from trying to compile
            with open(file_path, 'rb') as f:
                raw_bytes = f.read()
            
            # Try to decode with multiple encodings
            code = None
            encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1', 'ascii']
            
            for encoding in encodings:
                try:
                    code = raw_bytes.decode(encoding, errors='ignore')
                    break
                except Exception:
                    continue
            
            if code is None:
                code = raw_bytes.decode('utf-8', errors='replace')
            
            self.code_text.delete(1.0, tk.END)
            self.code_text.insert(1.0, code)
            category_name = os.path.basename(category_path)
            self.file_label.config(text=f"{category_name}/{filename}")
            
            # Apply syntax highlighting
            self.apply_code_syntax_highlighting()
            
            # Enable buttons
            self.copy_btn.config(state=tk.NORMAL)
            self.open_btn.config(state=tk.NORMAL)
            
            self.status_var.set(f"Loaded: {filename}")
        except Exception as e:
            error_msg = f"Failed to load code: {str(e)}\nFile: {filename}"
            self.code_text.delete(1.0, tk.END)
            self.code_text.insert(1.0, f"Error loading file:\n{error_msg}")
            self.file_label.config(text=f"Error: {filename}")
            self.status_var.set(f"Error loading {filename}")
            print(f"Error loading file {filename}: {str(e)}")
    
    def copy_code(self):
        """Copy code to clipboard"""
        try:
            code = self.code_text.get(1.0, tk.END)
            self.root.clipboard_clear()
            self.root.clipboard_append(code)
            self.status_var.set("Code copied to clipboard")
            messagebox.showinfo("Success", "Code copied to clipboard!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to copy code: {str(e)}")
    
    def open_in_editor(self):
        """Open file in advanced text editor"""
        try:
            if self.current_file_path and os.path.exists(self.current_file_path):
                editor = AdvancedTextEditor(self.root, self.current_file_path, self.tracker)
                self.open_editors.append(editor)
                
                # Clean up from list when editor is closed
                def on_editor_close():
                    if editor in self.open_editors:
                        self.open_editors.remove(editor)
                
                editor.editor_window.protocol("WM_DELETE_WINDOW", lambda: [on_editor_close(), editor.editor_window.destroy()])
                
                self.status_var.set(f"Opened {os.path.basename(self.current_file_path)} in editor")
            else:
                messagebox.showerror("Error", "No file selected or file not found")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open file: {str(e)}")
    
    def refresh_library(self):
        """Refresh the library to discover new scripts and folders"""
        try:
            # Detect changes
            changes = self.tracker.detect_changes()
            
            # Clear current selection
            self.files_listbox.delete(0, tk.END)
            self.code_text.delete(1.0, tk.END)
            self.file_label.config(text="Select a file to view code")
            self.copy_btn.config(state=tk.DISABLED)
            self.open_btn.config(state=tk.DISABLED)
            
            # Reload categories
            self.load_categories()
            
            # Show changes if any
            if changes:
                change_msg = f"Detected {len(changes)} changes:\n" + "\n".join(changes[:5])
                if len(changes) > 5:
                    change_msg += f"\n... and {len(changes) - 5} more"
                messagebox.showinfo("Changes Detected", change_msg)
            
            self.status_var.set("Library refreshed successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to refresh library: {str(e)}")
            self.status_var.set(f"Error refreshing library: {str(e)}")
    
    def show_statistics(self):
        """Show usage statistics in a new window"""
        stats = self.tracker.get_statistics()
        
        stats_window = tk.Toplevel(self.root)
        stats_window.title("Usage Statistics")
        stats_window.geometry("600x600")
        stats_window.configure(bg=COLORS['bg_primary'])
        
        # Content frame
        content = tk.Frame(stats_window, bg=COLORS['bg_primary'])
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        tk.Label(content, text="Code Library Statistics", font=('Arial', 14, 'bold'),
                bg=COLORS['bg_primary'], fg=COLORS['accent']).pack(pady=(0, 20))
        
        # Current file statistics (if a file is selected)
        if self.current_file_path:
            current_file_name = os.path.basename(self.current_file_path)
            file_access_count = self.tracker.usage_stats['file_accesses'].get(current_file_name, 0)
            
            # Find file rank
            sorted_files = sorted(self.tracker.usage_stats['file_accesses'].items(), 
                                 key=lambda x: x[1], reverse=True)
            file_rank = next((i + 1 for i, (name, _) in enumerate(sorted_files) if name == current_file_name), "N/A")
            
            current_file_frame = tk.Frame(content, bg=COLORS['bg_secondary'], padx=10, pady=10)
            current_file_frame.pack(fill=tk.X, pady=5)
            
            tk.Label(current_file_frame, text=f"Current File: {current_file_name}", font=('Arial', 11, 'bold'),
                    bg=COLORS['bg_secondary'], fg=COLORS['accent']).pack(anchor=tk.W)
            tk.Label(current_file_frame, text=f"Access Count: {file_access_count}",
                    bg=COLORS['bg_secondary'], fg=COLORS['fg_primary'], font=('Arial', 11)).pack(anchor=tk.W)
            tk.Label(current_file_frame, text=f"Popularity Rank: #{file_rank} of {len(sorted_files)}",
                    bg=COLORS['bg_secondary'], fg=COLORS['fg_primary'], font=('Arial', 11)).pack(anchor=tk.W)
        
        # Session info
        session_frame = tk.Frame(content, bg=COLORS['bg_secondary'], padx=10, pady=10)
        session_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(session_frame, text=f"Total Sessions: {stats['total_sessions']}",
                bg=COLORS['bg_secondary'], fg=COLORS['fg_primary'], font=('Arial', 11)).pack(anchor=tk.W)
        tk.Label(session_frame, text=f"Files Tracked: {stats['total_files_tracked']}",
                bg=COLORS['bg_secondary'], fg=COLORS['fg_primary'], font=('Arial', 11)).pack(anchor=tk.W)
        
        # Most accessed files
        tk.Label(content, text="Most Accessed Files", font=('Arial', 12, 'bold'),
                bg=COLORS['bg_primary'], fg=COLORS['accent']).pack(pady=(20, 10))
        
        files_frame = tk.Frame(content, bg=COLORS['bg_secondary'], padx=10, pady=10)
        files_frame.pack(fill=tk.X, pady=5)
        
        if stats['most_accessed_files']:
            for file_name, count in stats['most_accessed_files']:
                tk.Label(files_frame, text=f"{file_name}: {count} accesses",
                        bg=COLORS['bg_secondary'], fg=COLORS['fg_primary'], font=('Arial', 10)).pack(anchor=tk.W)
        else:
            tk.Label(files_frame, text="No file access data yet",
                    bg=COLORS['bg_secondary'], fg=COLORS['fg_secondary'], font=('Arial', 10)).pack(anchor=tk.W)
        
        # Most accessed categories
        tk.Label(content, text="Most Accessed Categories", font=('Arial', 12, 'bold'),
                bg=COLORS['bg_primary'], fg=COLORS['accent']).pack(pady=(20, 10))
        
        cats_frame = tk.Frame(content, bg=COLORS['bg_secondary'], padx=10, pady=10)
        cats_frame.pack(fill=tk.X, pady=5)
        
        if stats['most_accessed_categories']:
            for cat_name, count in stats['most_accessed_categories']:
                tk.Label(cats_frame, text=f"{cat_name}: {count} accesses",
                        bg=COLORS['bg_secondary'], fg=COLORS['fg_primary'], font=('Arial', 10)).pack(anchor=tk.W)
        else:
            tk.Label(cats_frame, text="No category access data yet",
                    bg=COLORS['bg_secondary'], fg=COLORS['fg_secondary'], font=('Arial', 10)).pack(anchor=tk.W)
        
        # Close button
        ttk.Button(content, text="Close", command=stats_window.destroy).pack(pady=20)
    
    def change_color_scheme(self, event=None):
        """Change the color scheme and update all UI elements"""
        global current_scheme, COLORS
        new_scheme = self.scheme_var.get()
        if new_scheme in COLOR_SCHEMES:
            current_scheme = new_scheme
            COLORS = COLOR_SCHEMES[current_scheme]
            self.update_colors()
            
            # Update all open editor windows
            for editor in self.open_editors:
                editor.update_editor_colors()
    
    def update_colors(self):
        """Update all UI elements with new color scheme"""
        # Update main window
        self.root.configure(bg=COLORS['bg_primary'])
        
        # Update style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Style configuration with Windows-friendly fonts
        font_family = 'Segoe UI' if sys.platform == 'win32' else 'Arial'
        style.configure('TFrame', background=COLORS['bg_primary'])
        style.configure('TPanedWindow', background=COLORS['bg_primary'])
        style.configure('TLabel', background=COLORS['bg_primary'], foreground=COLORS['fg_primary'], 
                       font=(font_family, 10))
        style.configure('TButton', background=COLORS['bg_tertiary'], foreground=COLORS['fg_primary'], 
                       borderwidth=0, focuscolor='none', padding=(8, 4), font=(font_family, 9))
        style.map('TButton', background=[('active', COLORS['accent'])])
        style.configure('TEntry', fieldbackground=COLORS['bg_secondary'], foreground=COLORS['fg_primary'],
                       borderwidth=1, insertcolor=COLORS['accent'], font=(font_family, 9))
        style.configure('TCombobox', fieldbackground=COLORS['bg_secondary'], foreground=COLORS['fg_primary'],
                       background=COLORS['bg_tertiary'], borderwidth=1, font=(font_family, 9),
                       arrowcolor=COLORS['fg_primary'])
        style.map('TCombobox', fieldbackground=[('readonly', COLORS['bg_secondary']),
                                                ('focus', COLORS['bg_secondary'])],
                  foreground=[('readonly', COLORS['fg_primary']),
                             ('focus', COLORS['fg_primary'])])
        style.configure('Treeview', background=COLORS['bg_secondary'], foreground=COLORS['fg_primary'],
                       fieldbackground=COLORS['bg_secondary'], borderwidth=0, font=(font_family, 9))
        style.configure('Treeview.Heading', background=COLORS['bg_tertiary'], foreground=COLORS['fg_primary'],
                       borderwidth=0, font=(font_family, 9, 'bold'))
        style.map('Treeview', background=[('selected', COLORS['accent'])], 
                  foreground=[('selected', COLORS['bg_primary'])])
        style.configure('TScrollbar', background=COLORS['bg_tertiary'], troughcolor=COLORS['bg_secondary'])
        
        # Update search frame and all children
        for widget in self.paned_window.winfo_children():
            self.update_widget_colors(widget)
        
        # Update code text
        self.code_text.configure(bg=COLORS['code_bg'], fg=COLORS['fg_primary'], 
                               insertbackground=COLORS['accent'], selectbackground=COLORS['accent'])
        
        # Update status bar
        self.status_bar.configure(bg=COLORS['bg_secondary'], fg=COLORS['fg_secondary'])
        
        # Update labels
        self.file_label.configure(bg=COLORS['bg_primary'], fg=COLORS['accent'])
        
        # Update header labels (Theme and Wrap)
        for widget in self.paned_window.winfo_children():
            for child in widget.winfo_children():
                if child.winfo_class() == 'Label':
                    text = child.cget('text')
                    if text in ['Theme:', 'Wrap:', 'Search:']:
                        child.configure(bg=COLORS['bg_primary'], fg=COLORS['fg_secondary'])
                    elif text in ['Categories', 'Files', 'Code Content']:
                        child.configure(bg=COLORS['bg_primary'], fg=COLORS['accent'])
                # Update nested frames (header_top, header_bottom, controls_frame)
                elif child.winfo_class() == 'Frame':
                    for grandchild in child.winfo_children():
                        if grandchild.winfo_class() == 'Label':
                            text = grandchild.cget('text')
                            if text in ['Theme:', 'Wrap:']:
                                grandchild.configure(bg=COLORS['bg_primary'], fg=COLORS['fg_secondary'])
                        elif grandchild.winfo_class() == 'Frame':
                            for ggchild in grandchild.winfo_children():
                                if ggchild.winfo_class() == 'Label':
                                    text = ggchild.cget('text')
                                    if text in ['Theme:', 'Wrap:']:
                                        ggchild.configure(bg=COLORS['bg_primary'], fg=COLORS['fg_secondary'])
        
        # Re-apply syntax highlighting if code is loaded
        if self.current_file_path:
            self.apply_code_syntax_highlighting()
    
    def update_widget_colors(self, widget):
        """Recursively update widget colors"""
        try:
            widget_class = widget.winfo_class()
            
            if widget_class == 'Frame':
                widget.configure(bg=COLORS['bg_primary'])
            elif widget_class == 'Label':
                widget.configure(bg=COLORS['bg_primary'], fg=COLORS['fg_primary'])
            elif widget_class == 'Listbox':
                widget.configure(bg=COLORS['bg_secondary'], fg=COLORS['fg_primary'],
                               selectbackground=COLORS['accent'], selectforeground=COLORS['bg_primary'])
            elif widget_class == 'Entry':
                widget.configure(bg=COLORS['bg_secondary'], fg=COLORS['fg_primary'],
                               insertbackground=COLORS['accent'])
            elif widget_class == 'Text':
                # Don't update code_text here, it's handled separately
                if widget != self.code_text:
                    widget.configure(bg=COLORS['bg_secondary'], fg=COLORS['fg_primary'],
                                   insertbackground=COLORS['accent'])
            elif widget_class == 'Toplevel':
                widget.configure(bg=COLORS['bg_primary'])
            elif widget_class == 'Panedwindow':
                # Panedwindow uses style, not direct bg config
                pass
            
            # Recursively update children
            for child in widget.winfo_children():
                self.update_widget_colors(child)
        except Exception:
            pass
    
    def change_wrap_mode(self, event=None):
        """Change text wrapping mode"""
        wrap_mode = self.wrap_var.get()
        if wrap_mode == 'None':
            self.code_text.configure(wrap=tk.NONE)
        elif wrap_mode == 'Word':
            self.code_text.configure(wrap=tk.WORD)
        elif wrap_mode == 'Char':
            self.code_text.configure(wrap=tk.CHAR)
    
    def apply_code_syntax_highlighting(self):
        """Apply syntax highlighting to the code text widget"""
        import re
        
        # Configure syntax highlighting tags
        self.code_text.tag_config('keyword', foreground=COLORS['accent'], font=('Consolas', 10, 'bold'))
        self.code_text.tag_config('string', foreground=COLORS['success'])
        self.code_text.tag_config('comment', foreground=COLORS['fg_secondary'], font=('Consolas', 10, 'italic'))
        self.code_text.tag_config('function', foreground=COLORS['highlight'])
        self.code_text.tag_config('number', foreground=COLORS['warning'])
        self.code_text.tag_config('decorator', foreground=COLORS['highlight'], font=('Consolas', 10, 'bold'))
        self.code_text.tag_config('builtin', foreground=COLORS['accent'])
        
        # Remove existing tags
        for tag in ['keyword', 'string', 'comment', 'function', 'number', 'decorator', 'builtin']:
            self.code_text.tag_remove(tag, '1.0', tk.END)
        
        content = self.code_text.get(1.0, tk.END)
        
        # Keywords
        keywords = ['def', 'class', 'if', 'else', 'elif', 'for', 'while', 'try', 'except',
                   'import', 'from', 'return', 'print', 'pass', 'break', 'continue', 'with',
                   'as', 'lambda', 'yield', 'raise', 'finally', 'assert', 'global', 'nonlocal',
                   'True', 'False', 'None', 'and', 'or', 'not', 'in', 'is', 'async', 'await']
        
        for keyword in keywords:
            self.highlight_code_pattern(keyword, 'keyword', word=True)
        
        # Built-in functions
        builtins = ['len', 'range', 'str', 'int', 'float', 'list', 'dict', 'set', 'tuple',
                   'bool', 'type', 'isinstance', 'hasattr', 'getattr', 'setattr', 'open',
                   'print', 'input', 'abs', 'min', 'max', 'sum', 'sorted', 'enumerate', 'zip']
        
        for builtin in builtins:
            self.highlight_code_pattern(builtin, 'builtin', word=True)
        
        # Decorators
        self.highlight_code_pattern(r'@\w+', 'decorator')
        
        # Strings (single and double quoted, including triple quotes)
        self.highlight_code_pattern(r'""".*?"""', 'string', multiline=True)
        self.highlight_code_pattern(r"'''.*?'''", 'string', multiline=True)
        self.highlight_code_pattern(r'".*?"', 'string')
        self.highlight_code_pattern(r".*?'", 'string')
        
        # Comments
        self.highlight_code_pattern(r'#.*$', 'comment')
        
        # Numbers
        self.highlight_code_pattern(r'\b\d+\b', 'number')
        self.highlight_code_pattern(r'\b\d+\.\d+\b', 'number')
        
        # Function definitions
        self.highlight_code_pattern(r'def\s+(\w+)', 'function')
    
    def highlight_code_pattern(self, pattern, tag, word=False, multiline=False):
        """Highlight a pattern with a tag in the code text"""
        import re
        content = self.code_text.get(1.0, tk.END)
        
        flags = 0
        if multiline:
            flags = re.DOTALL
        else:
            flags = re.MULTILINE
        
        if word:
            pattern = rf'\b{pattern}\b'
        
        try:
            for match in re.finditer(pattern, content, flags):
                start = match.start()
                end = match.end()
                start_index = f"1.0+{start}c"
                end_index = f"1.0+{end}c"
                self.code_text.tag_add(tag, start_index, end_index)
        except Exception:
            pass

    def on_closing(self):
        """Handle window closing event"""
        try:
            self.tracker.end_session()
        except Exception as e:
            print(f"Error ending session: {e}")
        self.root.destroy()
    
    def on_search(self, event):
        """Handle search functionality"""
        search_term = self.search_var.get().lower()
        
        if not search_term:
            # Reset to show all categories
            self.load_categories()
            return
        
        # Filter tree based on search - show matching directories and their parents
        self.filter_tree(search_term)
    
    def filter_tree(self, search_term):
        """Filter tree to show only matching directories"""
        def should_show(item):
            """Recursively check if item or its children match search"""
            item_text = self.category_tree.item(item)['text'].lower()
            children = self.category_tree.get_children(item)
            
            # Check if current item matches
            if search_term in item_text:
                return True
            
            # Check if any children match
            for child in children:
                if should_show(child):
                    return True
            
            return False
        
        def delete_non_matching(item):
            """Delete items that don't match and have no matching children"""
            children = self.category_tree.get_children(item)
            for child in children:
                delete_non_matching(child)
            
            # After processing children, check if this item should be shown
            if not should_show(item) and item != '':
                self.category_tree.delete(item)
        
        # Start filtering from root
        delete_non_matching('')


def main():
    root = tk.Tk()
    app = CodeLibraryGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
