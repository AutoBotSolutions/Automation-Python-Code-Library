#!/usr/bin/env python3
import os
import glob

# Define categories with unique descriptions different from website
categories = {
    "AccountFuntions": {
        "name": "Account Functions",
        "short_desc": "Authentication and account management",
        "detailed_desc": "Comprehensive authentication mechanisms including login automation, session management, credential handling, and user account operations for secure access control systems.",
        "use_cases": ["User authentication", "Session management", "Credential storage", "Multi-factor authentication"],
        "dependencies": ["hashlib", "requests", "json"],
        "related": ["SystemCommands", "SystemFunctions", "CustomFunctions"]
    },
    "BrowserCommands": {
        "name": "Browser Commands",
        "short_desc": "Selenium-based web automation",
        "detailed_desc": "Core Selenium WebDriver operations for browser automation including navigation, element interaction, data extraction, screenshot capture, and window management for web testing and scraping tasks.",
        "use_cases": ["Web scraping", "Automated testing", "Data extraction", "Form filling"],
        "dependencies": ["selenium", "webdriver_manager"],
        "related": ["BrowserFunction", "BrowserSettingsCommands", "DriverFunctions", "HeadlessFunctions", "JavaScriptCommands"]
    },
    "BrowserFunction": {
        "name": "Browser Functions",
        "short_desc": "Extended browser capabilities",
        "detailed_desc": "Advanced browser automation functions covering complex interactions, dynamic content handling, JavaScript execution, cookie management, and browser profile configuration for sophisticated web automation scenarios.",
        "use_cases": ["Dynamic content handling", "JavaScript execution", "Profile management"],
        "dependencies": ["selenium", "json"],
        "related": ["BrowserCommands", "BrowserSettingsCommands", "HTTPCommands"]
    },
    "BrowserSettingsCommands": {
        "name": "Browser Settings Commands",
        "short_desc": "Browser configuration",
        "detailed_desc": "Browser configuration utilities for setting preferences, managing extensions, configuring download behavior, handling permissions, and customizing browser settings for automation environments.",
        "use_cases": ["Browser configuration", "Extension management", "Download handling"],
        "dependencies": ["selenium"],
        "related": ["BrowserCommands", "BrowserFunction", "DriverFunctions"]
    },
    "CodeLibrary": {
        "name": "Code Library",
        "short_desc": "Core library utilities",
        "detailed_desc": "Foundational library functions providing core utilities, helper methods, common patterns, and infrastructure code that supports the entire automation framework with reusable components and utilities.",
        "use_cases": ["Library initialization", "Core utilities", "Helper functions"],
        "dependencies": ["os", "sys", "json"],
        "related": ["CustomFunctions", "CustomScripting", "FlowCommands"]
    },
    "CustomFunctions": {
        "name": "Custom Functions",
        "short_desc": "User-defined function templates",
        "detailed_desc": "Template functions and patterns for creating custom automation routines, user-defined operations, and extensible function signatures that can be adapted for specific automation requirements.",
        "use_cases": ["Custom automation", "Function templates", "Extensibility"],
        "dependencies": ["typing", "functools"],
        "related": ["CustomScripting", "CodeLibrary", "FlowCommands"]
    },
    "CustomScripting": {
        "name": "Custom Scripting",
        "short_desc": "Script automation templates",
        "detailed_desc": "Pre-built script templates and automation patterns for common workflows, enabling rapid development of custom automation solutions through modular and reusable script components.",
        "use_cases": ["Workflow automation", "Script templates", "Modular automation"],
        "dependencies": ["subprocess", "threading"],
        "related": ["CustomFunctions", "CodeLibrary", "ThreadingFunctions"]
    },
    "DataBaseCommands": {
        "name": "Database Commands",
        "short_desc": "SQL database operations",
        "detailed_desc": "Database interaction utilities for SQL operations including connection management, query execution, transaction handling, result processing, and database administration tasks across multiple database systems.",
        "use_cases": ["Database queries", "Transaction management", "Data migration"],
        "dependencies": ["sqlite3", "psycopg2", "mysql-connector", "pymongo"],
        "related": ["DataCommands", "DataFunctions", "TableCommands"]
    },
    "DataCommands": {
        "name": "Data Commands",
        "short_desc": "Data structure manipulation",
        "detailed_desc": "Data structure manipulation commands for working with lists, dictionaries, sets, and other data structures, including sorting, filtering, transforming, and aggregating operations for data processing workflows.",
        "use_cases": ["Data transformation", "Structure manipulation", "Data aggregation"],
        "dependencies": ["pandas", "numpy"],
        "related": ["DataFunctions", "DataBaseCommands", "TableCommands", "ListCommands"]
    },
    "DataFunctions": {
        "name": "Data Functions",
        "short_desc": "Data processing algorithms",
        "detailed_desc": "Data processing algorithms and functions for cleaning, validation, transformation, analysis, and manipulation of structured and unstructured data with support for various data formats and sources.",
        "use_cases": ["Data cleaning", "Data validation", "Data transformation"],
        "dependencies": ["pandas", "numpy", "json", "csv"],
        "related": ["DataCommands", "DataBaseCommands", "TableCommands", "TextFunctions"]
    },
    "DriverFunctions": {
        "name": "Driver Functions",
        "short_desc": "WebDriver management",
        "detailed_desc": "WebDriver management functions for browser driver initialization, configuration, lifecycle management, and cleanup operations supporting multiple browser types and automation frameworks.",
        "use_cases": ["Driver management", "Browser initialization", "Driver cleanup"],
        "dependencies": ["selenium", "webdriver_manager"],
        "related": ["BrowserCommands", "BrowserFunction", "BrowserSettingsCommands"]
    },
    "EmailCommands": {
        "name": "Email Commands",
        "short_desc": "Email protocol automation",
        "detailed_desc": "Email automation utilities for SMTP/IMAP/POP3 operations including sending, receiving, parsing, filtering, and managing email communications with support for attachments and HTML content.",
        "use_cases": ["Email automation", "Notification systems", "Email parsing"],
        "dependencies": ["smtplib", "imaplib", "email"],
        "related": ["HTTPCommands", "FileCommands", "SystemCommands"]
    },
    "FTPCommands": {
        "name": "FTP Commands",
        "short_desc": "FTP file transfers",
        "detailed_desc": "FTP protocol operations for file transfer tasks including upload, download, directory navigation, permission management, and batch file operations across FTP servers with error handling.",
        "use_cases": ["File transfer", "Batch operations", "Remote file management"],
        "dependencies": ["ftplib"],
        "related": ["FileCommands", "FileFunctions", "HTTPCommands"]
    },
    "FileCommands": {
        "name": "File Commands",
        "short_desc": "File system operations",
        "detailed_desc": "File system operations for creating, reading, writing, copying, moving, deleting, and managing files and directories with support for permissions, metadata, and batch operations.",
        "use_cases": ["File management", "Batch operations", "System administration"],
        "dependencies": ["os", "shutil", "pathlib"],
        "related": ["FileFunctions", "FTPCommands", "SystemCommands"]
    },
    "FileFunctions": {
        "name": "File Functions",
        "short_desc": "File handling utilities",
        "detailed_desc": "File handling utilities for advanced file operations including encoding conversion, compression, encryption, hashing, and metadata extraction for comprehensive file management tasks.",
        "use_cases": ["File compression", "Encryption", "Metadata extraction"],
        "dependencies": ["gzip", "zipfile", "hashlib", "cryptography"],
        "related": ["FileCommands", "FTPCommands", "DataCommands"]
    },
    "FlowCommands": {
        "name": "Flow Commands",
        "short_desc": "Control flow operations",
        "detailed_desc": "Control flow and logic operations for conditional execution, looping, branching, error handling, and workflow orchestration enabling complex automation logic and decision-making processes.",
        "use_cases": ["Workflow orchestration", "Conditional logic", "Error handling"],
        "dependencies": ["typing", "contextlib"],
        "related": ["CustomFunctions", "CustomScripting", "QualifierFunction"]
    },
    "HTTPCommands": {
        "name": "HTTP Commands",
        "short_desc": "HTTP request handling",
        "detailed_desc": "HTTP request utilities for REST API interaction, web scraping, data retrieval, and network communication with support for various HTTP methods, headers, authentication, and error handling.",
        "use_cases": ["API integration", "Web scraping", "Data retrieval"],
        "dependencies": ["requests", "urllib3"],
        "related": ["BrowserCommands", "FTPCommands", "EmailCommands", "ProxyFunctions"]
    },
    "HeadlessFunctions": {
        "name": "Headless Functions",
        "short_desc": "Headless browser automation",
        "detailed_desc": "Headless browser operations for background automation without UI, useful for server-side scraping, testing, and automation where visual rendering is not required.",
        "use_cases": ["Server-side scraping", "Background automation", "CI/CD"],
        "dependencies": ["selenium", "pyvirtualdisplay"],
        "related": ["BrowserCommands", "BrowserFunction", "SystemCommands"]
    },
    "Info Lib": {
        "name": "Info Library",
        "short_desc": "Information retrieval",
        "detailed_desc": "Information retrieval utilities for gathering system information, process details, hardware specs, network configuration, and environment data for monitoring and diagnostic purposes.",
        "use_cases": ["System monitoring", "Diagnostics", "Environment detection"],
        "dependencies": ["psutil", "platform"],
        "related": ["SystemCommands", "SystemFunctions"]
    },
    "JavaScriptCommands": {
        "name": "JavaScript Commands",
        "short_desc": "JavaScript execution",
        "detailed_desc": "JavaScript execution capabilities for running JavaScript code within browser contexts, manipulating DOM elements, handling events, and interacting with web applications programmatically.",
        "use_cases": ["DOM manipulation", "Event handling", "Web interaction"],
        "dependencies": ["selenium"],
        "related": ["BrowserCommands", "BrowserFunction"]
    },
    "ListCommands": {
        "name": "List Commands",
        "short_desc": "List manipulation",
        "detailed_desc": "List and array manipulation functions for sorting, filtering, mapping, reducing, and transforming sequences with support for complex data structures and functional programming patterns.",
        "use_cases": ["Data transformation", "List processing", "Functional programming"],
        "dependencies": ["itertools", "functools"],
        "related": ["DataCommands", "DataFunctions", "TextFunctions"]
    },
    "LogCommands": {
        "name": "Log Commands",
        "short_desc": "Logging operations",
        "detailed_desc": "Logging and debugging utilities for structured logging, log rotation, log filtering, and output management with support for multiple log levels and custom handlers.",
        "use_cases": ["Debugging", "Audit trails", "System monitoring"],
        "dependencies": ["logging", "syslog"],
        "related": ["SystemCommands", "SystemFunctions", "Info Lib"]
    },
    "MathFunctions": {
        "name": "Math Functions",
        "short_desc": "Mathematical computations",
        "detailed_desc": "Mathematical functions for calculations, statistical operations, random number generation, geometric computations, and mathematical transformations supporting scientific and engineering applications.",
        "use_cases": ["Calculations", "Statistics", "Scientific computing"],
        "dependencies": ["math", "statistics", "random"],
        "related": ["DataFunctions", "DataCommands"]
    },
    "OporationCommands": {
        "name": "Operation Commands",
        "short_desc": "General operation handlers",
        "detailed_desc": "General operation handlers for common tasks including string operations, type conversions, data validation, and utility functions that support various automation workflows.",
        "use_cases": ["Data validation", "Type conversion", "Utility operations"],
        "dependencies": ["typing", "json"],
        "related": ["FlowCommands", "QualifierFunction"]
    },
    "ProxyFunction": {
        "name": "Proxy Functions",
        "short_desc": "Proxy configuration",
        "detailed_desc": "Network proxy configuration and management for HTTP requests, browser automation, and network operations with support for authentication, rotation, and proxy chaining.",
        "use_cases": ["Network operations", "Anonymization", "Geo-location"],
        "dependencies": ["requests"],
        "related": ["HTTPCommands", "ProxyFunctions"]
    },
    "ProxyFunctions": {
        "name": "Proxy Functions",
        "short_desc": "Proxy management",
        "detailed_desc": "Proxy management utilities for proxy pool management, health checking, failover handling, and performance optimization for high-volume network operations.",
        "use_cases": ["Proxy pool management", "Failover handling"],
        "dependencies": ["requests", "urllib3"],
        "related": ["HTTPCommands", "ProxyFunction"]
    },
    "QualifierFunction": {
        "name": "Qualifier Functions",
        "short_desc": "Data validation",
        "detailed_desc": "Data validation and qualification logic for type checking, range validation, pattern matching, schema validation, and data integrity verification ensuring data quality and consistency.",
        "use_cases": ["Data validation", "Type checking", "Schema validation"],
        "dependencies": ["typing", "pydantic", "jsonschema"],
        "related": ["FlowCommands", "OporationCommands", "DataFunctions"]
    },
    "Refracted Projects": {
        "name": "Refracted Projects",
        "short_desc": "Refactored automation projects",
        "detailed_desc": "Refactored and optimized automation projects demonstrating best practices, design patterns, and production-ready implementations of complex automation workflows and systems.",
        "use_cases": ["Production automation", "Best practices", "Design patterns"],
        "dependencies": ["varies by project"],
        "related": ["CustomScripting", "FlowCommands"]
    },
    "SystemCommands": {
        "name": "System Commands",
        "short_desc": "Operating system commands",
        "detailed_desc": "Operating system command execution utilities for running shell commands, process management, system administration tasks, and cross-platform system operations with proper error handling.",
        "use_cases": ["System administration", "Process management", "Cross-platform ops"],
        "dependencies": ["subprocess", "shutil", "platform"],
        "related": ["SystemFunctions", "Info Lib", "FileCommands", "WindowCommands"]
    },
    "SystemFunctions": {
        "name": "System Functions",
        "short_desc": "System utilities",
        "detailed_desc": "System utility functions for environment detection, path manipulation, resource monitoring, and system introspection providing comprehensive system information and capabilities.",
        "use_cases": ["Environment detection", "Resource monitoring", "System introspection"],
        "dependencies": ["os", "sys", "platform"],
        "related": ["SystemCommands", "Info Lib", "LogCommands"]
    },
    "TableCommands": {
        "name": "Table Commands",
        "short_desc": "Table operations",
        "detailed_desc": "Table and spreadsheet operations for reading, writing, manipulating, and analyzing tabular data in formats like CSV, Excel, and databases with support for complex transformations.",
        "use_cases": ["Spreadsheet operations", "Data import/export", "Tabular data"],
        "dependencies": ["pandas", "openpyxl", "csv"],
        "related": ["DataCommands", "DataFunctions", "DataBaseCommands"]
    },
    "TextFunctions": {
        "name": "Text Functions",
        "short_desc": "String manipulation",
        "detailed_desc": "Text processing functions for string manipulation, pattern matching, text extraction, encoding conversion, and natural language operations supporting various text processing needs.",
        "use_cases": ["Text processing", "Pattern matching", "NLP operations"],
        "dependencies": ["re", "string", "unicodedata"],
        "related": ["ListCommands", "DataFunctions", "FileFunctions"]
    },
    "ThreadingFunctions": {
        "name": "Threading Functions",
        "short_desc": "Concurrent execution",
        "detailed_desc": "Multi-threading and concurrency utilities for parallel execution, thread pool management, synchronization primitives, and asynchronous programming patterns for performance optimization.",
        "use_cases": ["Parallel processing", "Performance optimization", "Async operations"],
        "dependencies": ["threading", "concurrent.futures", "asyncio"],
        "related": ["CustomScripting", "FlowCommands", "SystemCommands"]
    },
    "TimeFunctions": {
        "name": "Time Functions",
        "short_desc": "Date and time operations",
        "detailed_desc": "Date and time operations for timestamp handling, timezone conversion, date arithmetic, formatting, parsing, and time zone aware operations supporting global time management.",
        "use_cases": ["Timestamp handling", "Timezone conversion", "Date arithmetic"],
        "dependencies": ["datetime", "pytz", "arrow"],
        "related": ["SystemFunctions", "SystemCommands"]
    },
    "UserInterfaceLib": {
        "name": "User Interface Library",
        "short_desc": "GUI components",
        "detailed_desc": "GUI component library for building user interfaces with widgets, layout managers, event handling, and theme support for creating desktop applications with modern, responsive interfaces.",
        "use_cases": ["GUI development", "Desktop applications", "Interface design"],
        "dependencies": ["tkinter", "customtkinter"],
        "related": ["WindowCommands", "SystemCommands"]
    },
    "WindowCommands": {
        "name": "Window Commands",
        "short_desc": "Window management",
        "detailed_desc": "Window management functions for controlling application windows, handling window states, managing multiple windows, and implementing window-related UI operations in desktop applications.",
        "use_cases": ["Window management", "UI operations", "Desktop applications"],
        "dependencies": ["tkinter", "win32gui"],
        "related": ["UserInterfaceLib", "SystemCommands"]
    }
}

# Wiki output directory
wiki_dir = "/home/robbie/Desktop/CodeLibrary/wiki"
info_dir = "/home/robbie/Desktop/CodeLibrary/info"

def generate_wiki_page(category_key):
    """Generate a unique wiki page for a category"""
    if category_key not in categories:
        return
    
    category = categories[category_key]
    wiki_name = category["name"].replace(" ", "-")
    wiki_file = os.path.join(wiki_dir, f"{wiki_name}.md")
    
    # Get the info directory for this category
    info_category_dir = os.path.join(info_dir, category_key)
    
    # Get all markdown files in the info directory
    md_files = glob.glob(os.path.join(info_category_dir, "*.md"))
    
    # Extract script names
    scripts = []
    for md_file in md_files:
        script_name = os.path.basename(md_file).replace(".md", "")
        scripts.append(script_name)
    
    scripts.sort()
    
    # Generate unique wiki content focused on developer documentation with SEO
    content = f"# {category['name']} - Python Automation Scripts Documentation\n\n"
    content += f"**Keywords:** Python automation, {category['short_desc'].lower()}, automation scripts, Python development, automated workflows\n\n"
    content += f"## Overview\n\n"
    content += f"{category['detailed_desc']} This category provides comprehensive Python automation solutions for developers and automation engineers.\n\n"
    content += f"## Use Cases\n\n"
    
    for use_case in category["use_cases"]:
        content += f"- {use_case}\n"
    
    content += f"\n## Dependencies\n\n"
    content += f"The scripts in this category may require the following Python dependencies:\n\n"
    
    for dep in category["dependencies"]:
        content += f"- `{dep}` - Install via `pip install {dep}`\n"
    
    content += f"\n## Available Scripts\n\n"
    content += f"This category contains **{len(scripts)} Python automation scripts**:\n\n"
    
    for script in scripts:
        content += f"- `{script}`\n"
    
    content += f"\n## Implementation Details\n\n"
    content += f"For detailed implementation documentation, parameter specifications, and usage examples, refer to the [info/{category_key}](https://github.com/AutoBotSolutions/Automation-Python-Code-Library/tree/main/info/{category_key.replace(' ', '%20')}) directory in the repository.\n\n"
    
    content += f"## Integration Examples\n\n"
    content += f"### Basic Usage\n\n"
    content += f"```python\n# Import the required script\nfrom code_library.{category_key.replace(' ', '')} import example_script\n\n# Use the script\nresult = example_script(parameters)\n```\n\n"
    
    content += f"### Error Handling\n\n"
    content += f"```python\ntry:\n    result = example_script(parameters)\nexcept Exception as e:\n    print(f\"Error: {{e}}\")\n```\n\n"
    
    content += f"## Best Practices\n\n"
    content += f"- Always validate inputs before processing\n- Implement proper error handling\n- Use appropriate logging for debugging\n- Test scripts in isolation before integration\n- Monitor resource usage for long-running operations\n- Follow Python PEP 8 style guidelines\n- Document your automation workflows\n\n"
    
    content += f"## Related Documentation\n\n"
    content += f"- [Home](Home) - Main documentation hub\n"
    content += f"- [All Categories](Home#category-index) - Complete category list\n"
    content += f"- [API Reference](https://github.com/AutoBotSolutions/Automation-Python-Code-Library/blob/main/docs/API_REFERENCE.md) - Complete API documentation\n"
    content += f"- [Installation Guide](https://github.com/AutoBotSolutions/Automation-Python-Code-Library/blob/main/docs/INSTALLATION_GUIDE.md) - Setup and installation\n\n"
    
    content += f"## Related Categories\n\n"
    if "related" in category and category["related"]:
        content += f"Explore related Python automation categories:\n\n"
        for related_key in category["related"]:
            if related_key in categories:
                related_name = categories[related_key]["name"].replace(" ", "-")
                content += f"- [{categories[related_key]['name']}]({related_name}) - {categories[related_key]['short_desc']}\n"
        content += f"\n"
    
    content += f"## External Resources\n\n"
    content += f"- [Python Documentation](https://docs.python.org/) - Official Python documentation\n"
    content += f"- [Selenium Documentation](https://www.selenium.dev/documentation/) - WebDriver documentation\n"
    content += f"- [GitHub Repository](https://github.com/AutoBotSolutions/Automation-Python-Code-Library) - Source code and issues\n"
    
    # Write the wiki page
    with open(wiki_file, 'w') as f:
        f.write(content)
    
    print(f"Generated: {wiki_file}")

# Generate wiki pages for all categories
for category_key in categories.keys():
    info_category_dir = os.path.join(info_dir, category_key)
    if os.path.exists(info_category_dir):
        generate_wiki_page(category_key)

print("Wiki pages generated successfully with unique content!")
