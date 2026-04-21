# GitHub Wiki Setup Instructions

## Overview

This directory contains comprehensive wiki pages for the Automation Python Code Library. To add these wiki pages to your GitHub repository, follow the instructions below.

## Method 1: Using GitHub Web Interface (Recommended)

1. Go to your repository: https://github.com/AutoBotSolutions/Automation-Python-Code-Library
2. Click on the **Wiki** tab in the repository navigation
3. Click **Create the first page** or **Add Page**
4. For each wiki page in this directory:
   - Copy the content from the `.md` file
   - Paste it into the GitHub wiki editor
   - Set the page title (remove the `.md` extension)
   - Click **Save**

## Wiki Pages to Add

The following wiki pages have been generated:

1. **Home.md** - Main wiki page with overview and navigation
2. **Account-Functions.md** - Account management scripts
3. **Browser-Commands.md** - Web browser automation
4. **Browser-Functions.md** - Additional browser functionality
5. **Browser-Settings-Commands.md** - Browser configuration
6. **Code-Library.md** - Core library functions
7. **Custom-Functions.md** - Custom user functions
8. **Custom-Scripting.md** - Custom script templates
9. **Database-Commands.md** - Database operations
10. **Data-Commands.md** - Data manipulation
11. **Data-Functions.md** - Data processing
12. **Driver-Functions.md** - Driver management
13. **Email-Commands.md** - Email automation
14. **FTP-Commands.md** - FTP transfers
15. **File-Commands.md** - File operations
16. **File-Functions.md** - File handling
17. **Flow-Commands.md** - Control flow
18. **HTTP-Commands.md** - HTTP requests
19. **Headless-Functions.md** - Headless browser
20. **JavaScript-Commands.md** - JavaScript execution
21. **List-Commands.md** - List manipulation
22. **Log-Commands.md** - Logging
23. **Math-Functions.md** - Mathematical operations
24. **Operation-Commands.md** - General operations
25. **Proxy-Functions.md** - Proxy configuration
26. **Qualifier-Functions.md** - Qualification logic
27. **Refracted-Projects.md** - Refactored projects
28. **System-Commands.md** - System operations
29. **System-Functions.md** - System utilities
30. **Table-Commands.md** - Table operations
31. **Text-Functions.md** - String manipulation
32. **Threading-Functions.md** - Multi-threading
33. **Time-Functions.md** - Time and date
34. **User-Interface-Library.md** - GUI components
35. **Window-Commands.md** - Window management

## Method 2: Using Git Command Line

Alternatively, you can use git to push to the wiki repository:

```bash
# Clone the wiki repository (will create it if it doesn't exist)
git clone https://github.com/AutoBotSolutions/Automation-Python-Code-Library.wiki.git

# Copy all wiki markdown files to the wiki directory
cp wiki/*.md Automation-Python-Code-Library.wiki/

# Navigate to wiki directory
cd Automation-Python-Code-Library.wiki

# Add all files
git add .

# Commit changes
git commit -m "Add comprehensive wiki pages for Automation Python Code Library"

# Push to GitHub
git push origin master
```

## Method 3: Using GitHub CLI (gh)

If you have GitHub CLI installed:

```bash
# Install gh if not already installed
# https://cli.github.com/

# Navigate to wiki directory
cd wiki

# Push to GitHub wiki
gh repo edit AutoBotSolutions/Automation-Python-Code-Library --wiki --add "*.md"
```

## After Adding Wiki Pages

Once the wiki pages are added to GitHub:

1. Verify the wiki tab shows all pages
2. Check that navigation links work correctly
3. Ensure the Home page is set as the wiki sidebar
4. Update the wiki sidebar if needed

## Updating Wiki Pages

To update wiki pages in the future:

1. Edit the corresponding `.md` file in this directory
2. Repeat the steps above to update the GitHub wiki
3. Or edit directly in the GitHub web interface

## Regenerating Wiki Pages

To regenerate wiki pages after adding new scripts:

```bash
python3 generate_wiki.py
```

This will scan the `/info` directory and update all wiki pages with the latest script information.
