"""
CodeLibrary GUI Application - A visual interface to library utilities.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from codelibrary import string_helpers, math_helpers, datastructures, time_utils
from codelibrary.indexer import LibraryIndexer


class CodeLibraryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("CodeLibrary Utilities")
        self.root.geometry("900x700")
        
        # Initialize the library indexer
        self.indexer = LibraryIndexer()
        
        # Create notebook (tabs)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create tabs
        self.create_search_tab()
        self.create_library_browser_tab()
        self.create_string_tab()
        self.create_math_tab()
        self.create_datastructures_tab()
        self.create_time_tab()
        
    def create_search_tab(self):
        """Create search tab for finding functions."""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="🔍 Search")
        
        # Search frame
        search_frame = ttk.Frame(tab, padding=10)
        search_frame.pack(fill='x', padx=10, pady=5)
        
        ttk.Label(search_frame, text="Search:").grid(row=0, column=0, sticky='w')
        self.search_input = ttk.Entry(search_frame, width=50)
        self.search_input.grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(search_frame, text="Search", command=self.perform_search).grid(row=0, column=2, padx=5)
        
        # Results treeview
        results_frame = ttk.LabelFrame(tab, text="Search Results", padding=10)
        results_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        columns = ('name', 'module', 'type')
        self.search_results_tree = ttk.Treeview(results_frame, columns=columns, show='headings')
        self.search_results_tree.heading('name', text='Function/Class')
        self.search_results_tree.heading('module', text='Module')
        self.search_results_tree.heading('type', text='Type')
        self.search_results_tree.column('name', width=200)
        self.search_results_tree.column('module', width=150)
        self.search_results_tree.column('type', width=100)
        self.search_results_tree.pack(fill='both', expand=True)
        
        self.search_results_tree.bind('<Double-1>', self.on_search_result_click)
        
        # Documentation display
        doc_frame = ttk.LabelFrame(tab, text="Documentation", padding=10)
        doc_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        self.doc_text = tk.Text(doc_frame, height=8, wrap='word')
        scrollbar = ttk.Scrollbar(doc_frame, orient='vertical', command=self.doc_text.yview)
        self.doc_text.configure(yscrollcommand=scrollbar.set)
        self.doc_text.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
    
    def create_library_browser_tab(self):
        """Create library browser tab to view all modules and functions."""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="📚 Library Browser")
        
        # Left panel - Module list
        left_panel = ttk.Frame(tab, padding=10)
        left_panel.pack(side='left', fill='y', padx=5)
        
        ttk.Label(left_panel, text="Modules:").pack(anchor='w')
        self.module_listbox = tk.Listbox(left_panel, width=20, height=20)
        self.module_listbox.pack(fill='y', pady=5)
        self.module_listbox.bind('<<ListboxSelect>>', self.on_module_select)
        
        # Populate module list
        for module_name in self.indexer.modules.keys():
            self.module_listbox.insert(tk.END, module_name)
        
        # Right panel - Functions list
        right_panel = ttk.Frame(tab, padding=10)
        right_panel.pack(side='left', fill='both', expand=True, padx=5)
        
        ttk.Label(right_panel, text="Functions/Classes:").pack(anchor='w')
        
        columns = ('name', 'type')
        self.function_tree = ttk.Treeview(right_panel, columns=columns, show='headings', height=15)
        self.function_tree.heading('name', text='Name')
        self.function_tree.heading('type', text='Type')
        self.function_tree.column('name', width=250)
        self.function_tree.column('type', width=100)
        self.function_tree.pack(fill='both', expand=True, pady=5)
        
        self.function_tree.bind('<Double-1>', self.on_function_select)
        
        # Documentation display
        doc_frame = ttk.LabelFrame(right_panel, text="Documentation", padding=10)
        doc_frame.pack(fill='both', expand=True, pady=5)
        
        self.browser_doc_text = tk.Text(doc_frame, height=10, wrap='word')
        browser_scrollbar = ttk.Scrollbar(doc_frame, orient='vertical', command=self.browser_doc_text.yview)
        self.browser_doc_text.configure(yscrollcommand=browser_scrollbar.set)
        self.browser_doc_text.pack(side='left', fill='both', expand=True)
        browser_scrollbar.pack(side='right', fill='y')
        
    def create_string_tab(self):
        """Create string utilities tab."""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="String Utilities")
        
        # Camel to Snake
        frame1 = ttk.LabelFrame(tab, text="CamelCase to snake_case", padding=10)
        frame1.pack(fill='x', padx=10, pady=5)
        
        ttk.Label(frame1, text="Input:").grid(row=0, column=0, sticky='w')
        self.camel_input = ttk.Entry(frame1, width=40)
        self.camel_input.grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(frame1, text="Convert", command=self.convert_camel_to_snake).grid(row=0, column=2, padx=5)
        ttk.Label(frame1, text="Output:").grid(row=1, column=0, sticky='w')
        self.camel_output = ttk.Entry(frame1, width=40)
        self.camel_output.grid(row=1, column=1, padx=5, pady=5)
        
        # Snake to Camel
        frame2 = ttk.LabelFrame(tab, text="snake_case to CamelCase", padding=10)
        frame2.pack(fill='x', padx=10, pady=5)
        
        ttk.Label(frame2, text="Input:").grid(row=0, column=0, sticky='w')
        self.snake_input = ttk.Entry(frame2, width=40)
        self.snake_input.grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(frame2, text="Convert", command=self.convert_snake_to_camel).grid(row=0, column=2, padx=5)
        ttk.Label(frame2, text="Output:").grid(row=1, column=0, sticky='w')
        self.snake_output = ttk.Entry(frame2, width=40)
        self.snake_output.grid(row=1, column=1, padx=5, pady=5)
        
        # Email Validation
        frame3 = ttk.LabelFrame(tab, text="Email Validation", padding=10)
        frame3.pack(fill='x', padx=10, pady=5)
        
        ttk.Label(frame3, text="Email:").grid(row=0, column=0, sticky='w')
        self.email_input = ttk.Entry(frame3, width=40)
        self.email_input.grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(frame3, text="Validate", command=self.validate_email).grid(row=0, column=2, padx=5)
        self.email_result = ttk.Label(frame3, text="")
        self.email_result.grid(row=0, column=3, padx=5)
        
        # Word Count
        frame4 = ttk.LabelFrame(tab, text="Word Count", padding=10)
        frame4.pack(fill='x', padx=10, pady=5)
        
        ttk.Label(frame4, text="Text:").grid(row=0, column=0, sticky='w')
        self.word_input = ttk.Entry(frame4, width=40)
        self.word_input.grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(frame4, text="Count", command=self.count_words).grid(row=0, column=2, padx=5)
        self.word_result = ttk.Label(frame4, text="")
        self.word_result.grid(row=0, column=3, padx=5)
        
    def create_math_tab(self):
        """Create math utilities tab."""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Math Utilities")
        
        # Mean
        frame1 = ttk.LabelFrame(tab, text="Mean (Average)", padding=10)
        frame1.pack(fill='x', padx=10, pady=5)
        
        ttk.Label(frame1, text="Numbers (comma-separated):").grid(row=0, column=0, sticky='w')
        self.mean_input = ttk.Entry(frame1, width=40)
        self.mean_input.grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(frame1, text="Calculate", command=self.calculate_mean).grid(row=0, column=2, padx=5)
        self.mean_result = ttk.Label(frame1, text="")
        self.mean_result.grid(row=0, column=3, padx=5)
        
        # Median
        frame2 = ttk.LabelFrame(tab, text="Median", padding=10)
        frame2.pack(fill='x', padx=10, pady=5)
        
        ttk.Label(frame2, text="Numbers (comma-separated):").grid(row=0, column=0, sticky='w')
        self.median_input = ttk.Entry(frame2, width=40)
        self.median_input.grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(frame2, text="Calculate", command=self.calculate_median).grid(row=0, column=2, padx=5)
        self.median_result = ttk.Label(frame2, text="")
        self.median_result.grid(row=0, column=3, padx=5)
        
        # Prime Check
        frame3 = ttk.LabelFrame(tab, text="Prime Number Check", padding=10)
        frame3.pack(fill='x', padx=10, pady=5)
        
        ttk.Label(frame3, text="Number:").grid(row=0, column=0, sticky='w')
        self.prime_input = ttk.Entry(frame3, width=20)
        self.prime_input.grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(frame3, text="Check", command=self.check_prime).grid(row=0, column=2, padx=5)
        self.prime_result = ttk.Label(frame3, text="")
        self.prime_result.grid(row=0, column=3, padx=5)
        
        # Fibonacci
        frame4 = ttk.LabelFrame(tab, text="Fibonacci Sequence", padding=10)
        frame4.pack(fill='x', padx=10, pady=5)
        
        ttk.Label(frame4, text="Count:").grid(row=0, column=0, sticky='w')
        self.fib_input = ttk.Entry(frame4, width=20)
        self.fib_input.grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(frame4, text="Generate", command=self.generate_fibonacci).grid(row=0, column=2, padx=5)
        self.fib_result = ttk.Label(frame4, text="")
        self.fib_result.grid(row=0, column=3, padx=5)
        
    def create_datastructures_tab(self):
        """Create data structures tab."""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Data Structures")
        
        # Stack
        frame1 = ttk.LabelFrame(tab, text="Stack Operations", padding=10)
        frame1.pack(fill='x', padx=10, pady=5)
        
        ttk.Label(frame1, text="Value:").grid(row=0, column=0, sticky='w')
        self.stack_input = ttk.Entry(frame1, width=20)
        self.stack_input.grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(frame1, text="Push", command=self.stack_push).grid(row=0, column=2, padx=5)
        ttk.Button(frame1, text="Pop", command=self.stack_pop).grid(row=0, column=3, padx=5)
        ttk.Button(frame1, text="Peek", command=self.stack_peek).grid(row=0, column=4, padx=5)
        self.stack_result = ttk.Label(frame1, text="")
        self.stack_result.grid(row=0, column=5, padx=5)
        ttk.Label(frame1, text="Stack contents:").grid(row=1, column=0, sticky='w')
        self.stack_display = ttk.Label(frame1, text="[]")
        self.stack_display.grid(row=1, column=1, columnspan=5, sticky='w')
        
        self.stack = datastructures.Stack()
        
        # Queue
        frame2 = ttk.LabelFrame(tab, text="Queue Operations", padding=10)
        frame2.pack(fill='x', padx=10, pady=5)
        
        ttk.Label(frame2, text="Value:").grid(row=0, column=0, sticky='w')
        self.queue_input = ttk.Entry(frame2, width=20)
        self.queue_input.grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(frame2, text="Enqueue", command=self.queue_enqueue).grid(row=0, column=2, padx=5)
        ttk.Button(frame2, text="Dequeue", command=self.queue_dequeue).grid(row=0, column=3, padx=5)
        ttk.Button(frame2, text="Peek", command=self.queue_peek).grid(row=0, column=4, padx=5)
        self.queue_result = ttk.Label(frame2, text="")
        self.queue_result.grid(row=0, column=5, padx=5)
        ttk.Label(frame2, text="Queue contents:").grid(row=1, column=0, sticky='w')
        self.queue_display = ttk.Label(frame2, text="[]")
        self.queue_display.grid(row=1, column=1, columnspan=5, sticky='w')
        
        self.queue = datastructures.Queue()
        
    def create_time_tab(self):
        """Create time utilities tab."""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Time Utilities")
        
        # Current Time
        frame1 = ttk.LabelFrame(tab, text="Current Time", padding=10)
        frame1.pack(fill='x', padx=10, pady=5)
        
        ttk.Button(frame1, text="Get Current Time", command=self.get_current_time).grid(row=0, column=0, padx=5)
        self.current_time_result = ttk.Label(frame1, text="")
        self.current_time_result.grid(row=0, column=1, padx=5)
        
        # Timestamp to DateTime
        frame2 = ttk.LabelFrame(tab, text="Timestamp to DateTime", padding=10)
        frame2.pack(fill='x', padx=10, pady=5)
        
        ttk.Label(frame2, text="Timestamp:").grid(row=0, column=0, sticky='w')
        self.timestamp_input = ttk.Entry(frame2, width=30)
        self.timestamp_input.grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(frame2, text="Convert", command=self.timestamp_to_datetime).grid(row=0, column=2, padx=5)
        self.timestamp_result = ttk.Label(frame2, text="")
        self.timestamp_result.grid(row=0, column=3, padx=5)
        
        # DateTime to Timestamp
        frame3 = ttk.LabelFrame(tab, text="DateTime to Timestamp", padding=10)
        frame3.pack(fill='x', padx=10, pady=5)
        
        ttk.Label(frame3, text="Date (YYYY-MM-DD HH:MM:SS):").grid(row=0, column=0, sticky='w')
        self.datetime_input = ttk.Entry(frame3, width=30)
        self.datetime_input.grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(frame3, text="Convert", command=self.datetime_to_timestamp).grid(row=0, column=2, padx=5)
        self.datetime_result = ttk.Label(frame3, text="")
        self.datetime_result.grid(row=0, column=3, padx=5)
        
        # Time Ago
        frame4 = ttk.LabelFrame(tab, text="Time Ago Calculator", padding=10)
        frame4.pack(fill='x', padx=10, pady=5)
        
        ttk.Label(frame4, text="Date (YYYY-MM-DD HH:MM:SS):").grid(row=0, column=0, sticky='w')
        self.timeago_input = ttk.Entry(frame4, width=30)
        self.timeago_input.grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(frame4, text="Calculate", command=self.calculate_time_ago).grid(row=0, column=2, padx=5)
        self.timeago_result = ttk.Label(frame4, text="")
        self.timeago_result.grid(row=0, column=3, padx=5)
    
    # String utility methods
    def convert_camel_to_snake(self):
        input_text = self.camel_input.get()
        result = string_helpers.camel_to_snake(input_text)
        self.camel_output.delete(0, tk.END)
        self.camel_output.insert(0, result)
    
    def convert_snake_to_camel(self):
        input_text = self.snake_input.get()
        result = string_helpers.snake_to_camel(input_text)
        self.snake_output.delete(0, tk.END)
        self.snake_output.insert(0, result)
    
    def validate_email(self):
        email = self.email_input.get()
        is_valid = string_helpers.is_email(email)
        self.email_result.config(text="Valid ✓" if is_valid else "Invalid ✗", 
                                  foreground="green" if is_valid else "red")
    
    def count_words(self):
        text = self.word_input.get()
        count = string_helpers.count_words(text)
        self.word_result.config(text=f"{count} words")
    
    # Math utility methods
    def calculate_mean(self):
        try:
            numbers = [float(x.strip()) for x in self.mean_input.get().split(',') if x.strip()]
            result = math_helpers.mean(numbers)
            self.mean_result.config(text=f"{result:.2f}")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
    
    def calculate_median(self):
        try:
            numbers = [float(x.strip()) for x in self.median_input.get().split(',') if x.strip()]
            result = math_helpers.median(numbers)
            self.median_result.config(text=f"{result:.2f}")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
    
    def check_prime(self):
        try:
            number = int(self.prime_input.get())
            is_prime = math_helpers.is_prime(number)
            self.prime_result.config(text="Prime ✓" if is_prime else "Not Prime ✗",
                                     foreground="green" if is_prime else "red")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
    
    def generate_fibonacci(self):
        try:
            count = int(self.fib_input.get())
            result = math_helpers.fibonacci(count)
            self.fib_result.config(text=str(result))
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
    
    # Data structure methods
    def stack_push(self):
        value = self.stack_input.get()
        self.stack.push(value)
        self.update_stack_display()
        self.stack_result.config(text="Pushed!")
    
    def stack_pop(self):
        try:
            value = self.stack.pop()
            self.update_stack_display()
            self.stack_result.config(text=f"Popped: {value}")
        except IndexError:
            messagebox.showerror("Error", "Stack is empty")
    
    def stack_peek(self):
        try:
            value = self.stack.peek()
            self.stack_result.config(text=f"Top: {value}")
        except IndexError:
            messagebox.showerror("Error", "Stack is empty")
    
    def update_stack_display(self):
        items = []
        temp_stack = datastructures.Stack()
        while not self.stack.is_empty():
            items.append(self.stack.pop())
            temp_stack.push(items[-1])
        while not temp_stack.is_empty():
            self.stack.push(temp_stack.pop())
        self.stack_display.config(text=str(items[::-1]))
    
    def queue_enqueue(self):
        value = self.queue_input.get()
        self.queue.enqueue(value)
        self.update_queue_display()
        self.queue_result.config(text="Enqueued!")
    
    def queue_dequeue(self):
        try:
            value = self.queue.dequeue()
            self.update_queue_display()
            self.queue_result.config(text=f"Dequeued: {value}")
        except IndexError:
            messagebox.showerror("Error", "Queue is empty")
    
    def queue_peek(self):
        try:
            value = self.queue.peek()
            self.queue_result.config(text=f"Front: {value}")
        except IndexError:
            messagebox.showerror("Error", "Queue is empty")
    
    def update_queue_display(self):
        items = []
        temp_queue = datastructures.Queue()
        while not self.queue.is_empty():
            items.append(self.queue.dequeue())
            temp_queue.enqueue(items[-1])
        while not temp_queue.is_empty():
            self.queue.enqueue(temp_queue.dequeue())
        self.queue_display.config(text=str(items))
    
    # Time utility methods
    def get_current_time(self):
        now = time_utils.now()
        formatted = time_utils.format_datetime(now)
        timestamp = time_utils.now_timestamp()
        self.current_time_result.config(text=f"{formatted} (Timestamp: {timestamp:.2f})")
    
    def timestamp_to_datetime(self):
        try:
            timestamp = float(self.timestamp_input.get())
            dt = time_utils.timestamp_to_datetime(timestamp)
            formatted = time_utils.format_datetime(dt)
            self.timestamp_result.config(text=formatted)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
    
    def datetime_to_timestamp(self):
        try:
            date_str = self.datetime_input.get()
            dt = time_utils.parse_datetime(date_str)
            timestamp = time_utils.datetime_to_timestamp(dt)
            self.datetime_result.config(text=f"{timestamp:.2f}")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
    
    def calculate_time_ago(self):
        try:
            date_str = self.timeago_input.get()
            dt = time_utils.parse_datetime(date_str)
            result = time_utils.time_ago(dt)
            self.timeago_result.config(text=result)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
    
    # Search and browser methods
    def perform_search(self):
        """Perform search and display results."""
        query = self.search_input.get()
        if not query:
            return
        
        results = self.indexer.search(query)
        
        # Clear previous results
        for item in self.search_results_tree.get_children():
            self.search_results_tree.delete(item)
        
        # Add new results
        for func in results:
            func_type = "Class" if func.is_class else "Function"
            self.search_results_tree.insert('', 'end', values=(func.name, func.module, func_type))
    
    def on_search_result_click(self, event):
        """Handle double-click on search result to show documentation."""
        selection = self.search_results_tree.selection()
        if not selection:
            return
        
        item = self.search_results_tree.item(selection[0])
        values = item['values']
        func_name = values[0]
        module_name = values[1]
        
        func_info = self.indexer.get_function_info(module_name, func_name)
        if func_info:
            self.show_documentation(func_info, self.doc_text)
    
    def on_module_select(self, event):
        """Handle module selection in browser."""
        selection = self.module_listbox.curselection()
        if not selection:
            return
        
        module_name = self.module_listbox.get(selection[0])
        functions = self.indexer.get_module_functions(module_name)
        
        # Clear previous functions
        for item in self.function_tree.get_children():
            self.function_tree.delete(item)
        
        # Add functions
        for func in functions:
            func_type = "Class" if func.is_class else "Function"
            self.function_tree.insert('', 'end', values=(func.name, func_type))
    
    def on_function_select(self, event):
        """Handle function selection in browser."""
        selection = self.function_tree.selection()
        if not selection:
            return
        
        # Get selected module
        module_selection = self.module_listbox.curselection()
        if not module_selection:
            return
        module_name = self.module_listbox.get(module_selection[0])
        
        # Get selected function
        item = self.function_tree.item(selection[0])
        func_name = item['values'][0]
        
        func_info = self.indexer.get_function_info(module_name, func_name)
        if func_info:
            self.show_documentation(func_info, self.browser_doc_text)
    
    def show_documentation(self, func_info, text_widget):
        """Display function documentation in text widget."""
        text_widget.delete('1.0', tk.END)
        
        doc = f"Name: {func_info.name}\n"
        doc += f"Module: {func_info.module}\n"
        doc += f"Type: {'Class' if func_info.is_class else 'Function'}\n"
        doc += f"Signature: {func_info.signature}\n\n"
        doc += f"Documentation:\n{func_info.doc}"
        
        text_widget.insert('1.0', doc)


def main():
    root = tk.Tk()
    app = CodeLibraryGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
