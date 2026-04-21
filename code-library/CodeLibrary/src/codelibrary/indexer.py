"""
Code library indexer - extracts and indexes functions, classes, and documentation.
"""

import inspect
import importlib
from typing import List, Dict, Any
from codelibrary import utils, datastructures, string_helpers, file_operations, math_helpers, time_utils


class FunctionInfo:
    """Stores information about a function."""
    
    def __init__(self, name: str, module: str, doc: str, signature: str, is_class: bool = False):
        self.name = name
        self.module = module
        self.doc = doc
        self.signature = signature
        self.is_class = is_class
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for display."""
        return {
            "name": self.name,
            "module": self.module,
            "doc": self.doc,
            "signature": self.signature,
            "is_class": self.is_class
        }


class LibraryIndexer:
    """Indexes the code library for searching."""
    
    def __init__(self):
        self.modules = {
            "utils": utils,
            "datastructures": datastructures,
            "string_helpers": string_helpers,
            "file_operations": file_operations,
            "math_helpers": math_helpers,
            "time_utils": time_utils
        }
        self.index = self._build_index()
    
    def _build_index(self) -> Dict[str, List[FunctionInfo]]:
        """Build the index of all functions and classes."""
        index = {}
        
        for module_name, module in self.modules.items():
            functions = []
            
            # Get all functions
            for name, obj in inspect.getmembers(module, inspect.isfunction):
                if not name.startswith('_'):
                    sig = str(inspect.signature(obj))
                    doc = inspect.getdoc(obj) or "No documentation"
                    functions.append(FunctionInfo(name, module_name, doc, sig))
            
            # Get all classes
            for name, obj in inspect.getmembers(module, inspect.isclass):
                if not name.startswith('_') and obj.__module__.startswith('codelibrary'):
                    sig = str(inspect.signature(obj.__init__)) if hasattr(obj, '__init__') else "()"
                    doc = inspect.getdoc(obj) or "No documentation"
                    functions.append(FunctionInfo(name, module_name, doc, sig, is_class=True))
            
            index[module_name] = functions
        
        return index
    
    def search(self, query: str) -> List[FunctionInfo]:
        """Search for functions matching the query."""
        query = query.lower()
        results = []
        
        for module_name, functions in self.index.items():
            for func in functions:
                # Search in name, module, and docstring
                if (query in func.name.lower() or 
                    query in func.module.lower() or 
                    query in func.doc.lower()):
                    results.append(func)
        
        return results
    
    def get_all_functions(self) -> List[FunctionInfo]:
        """Get all indexed functions."""
        all_funcs = []
        for functions in self.index.values():
            all_funcs.extend(functions)
        return all_funcs
    
    def get_module_functions(self, module_name: str) -> List[FunctionInfo]:
        """Get all functions from a specific module."""
        return self.index.get(module_name, [])
    
    def get_function_info(self, module_name: str, function_name: str) -> FunctionInfo:
        """Get detailed info about a specific function."""
        for func in self.index.get(module_name, []):
            if func.name == function_name:
                return func
        return None
