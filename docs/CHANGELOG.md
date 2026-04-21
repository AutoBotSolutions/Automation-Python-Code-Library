# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-04-20

### Added
- Initial release of Code Library GUI
- Modern dark-themed GUI with Catppuccin-inspired color scheme
- Advanced text editor with syntax highlighting, line numbers, find/replace
- System tracking and statistics
- Support for nested directory structures
- Real-time search functionality
- File change detection using MD5 hashing
- Session tracking with start/end events
- Backend REST API with Flask
- Cross-platform installer build scripts (Windows, Linux, macOS)
- Comprehensive documentation system
- Installation guide for Windows, Linux, and macOS
- GitHub setup and 2FA authentication guides
- API documentation with all endpoints
- Troubleshooting guide
- Code library with 36 categories of automation scripts

### Features
- Browse code library with nested directory support
- View Python files with syntax highlighting
- Edit files in advanced text editor
- Copy code to clipboard
- Track file access and edits
- Detect file changes (new, modified, deleted)
- View usage statistics
- Search files by name
- Refresh library to detect new scripts
- REST API for programmatic access
- Multi-platform installers

### Documentation
- README with project overview and features
- CONTRIBUTING.md with contribution guidelines
- INSTALLATION_GUIDE.md with cross-platform instructions
- docs/ directory with comprehensive documentation
- API documentation for backend API
- Troubleshooting guide
- GitHub setup guides

### Security
- MIT License
- No external dependencies for core GUI
- Path isolation to prevent imports from code library
- Binary mode file reading to prevent compilation

---

## [Unreleased]

### Planned
- Authentication for backend API
- WebSocket support for real-time updates
- Plugin system for extensions
- Multi-language syntax highlighting
- Diff viewer for file comparisons
- Bookmarking system
- Export functionality for statistics
- Dark/light theme toggle
- Keyboard shortcuts
