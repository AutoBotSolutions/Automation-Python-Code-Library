# Backend API Documentation

## Overview

The Code Library Backend API provides RESTful endpoints for interacting with the code library system programmatically. The API is built using Flask and supports operations for file browsing, tracking, statistics, and more.

**Base URL:** `http://localhost:5000/api`

## Authentication

Currently, the API does not require authentication. This can be added in future versions.

## Endpoints

### Health Check

**GET** `/api/health`

Check if the API is running.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2026-04-20T23:00:00.000000",
  "service": "Code Library Backend API"
}
```

---

### Library Operations

#### Get Categories

**GET** `/api/library/categories`

Get all categories (directories) in the code library.

**Response:**
```json
{
  "success": true,
  "categories": [
    {
      "name": "BrowserCommands",
      "path": "/path/to/code-library/BrowserCommands",
      "relative_path": "BrowserCommands"
    }
  ],
  "count": 36
}
```

#### Get Files

**GET** `/api/library/files?path={category_path}`

Get all Python files in a specific category.

**Parameters:**
- `path` (required): Full path to the category directory

**Response:**
```json
{
  "success": true,
  "files": [
    {
      "name": "NavigateTo URL.py",
      "path": "/path/to/code-library/BrowserCommands/NavigateTo URL.py"
    }
  ],
  "count": 10
}
```

#### Get File Content

**GET** `/api/library/file?path={file_path}`

Get the content of a specific file.

**Parameters:**
- `path` (required): Full path to the file

**Response:**
```json
{
  "success": true,
  "content": "# File content here...",
  "filename": "NavigateTo URL.py",
  "encoding": "utf-8"
}
```

**Note:** This endpoint automatically tracks file access in the statistics.

#### Search Library

**GET** `/api/library/search?q={query}`

Search for files in the library.

**Parameters:**
- `q` (required): Search query

**Response:**
```json
{
  "success": true,
  "results": [
    {
      "name": "NavigateTo URL.py",
      "path": "/path/to/code-library/BrowserCommands/NavigateTo URL.py",
      "relative_path": "BrowserCommands/NavigateTo URL.py"
    }
  ],
  "count": 5
}
```

---

### Tracking Operations

#### Get Statistics

**GET** `/api/tracking/statistics`

Get usage statistics for the code library.

**Response:**
```json
{
  "success": true,
  "statistics": {
    "total_sessions": 10,
    "most_accessed_files": [
      ["NavigateTo URL.py", 25],
      ["Delete File.py", 20]
    ],
    "most_accessed_categories": [
      ["BrowserCommands", 50],
      ["FileCommands", 40]
    ],
    "total_files": 371
  }
}
```

#### Detect Changes

**GET** `/api/tracking/changes`

Detect changes in the code library (new, modified, deleted files).

**Response:**
```json
{
  "success": true,
  "changes": [
    {
      "type": "MODIFIED",
      "file": "BrowserCommands/NavigateTo URL.py"
    },
    {
      "type": "NEW",
      "file": "NewScript.py"
    }
  ],
  "count": 2
}
```

#### Start Session

**POST** `/api/tracking/session/start`

Start a new tracking session.

**Response:**
```json
{
  "success": true,
  "session_id": 11
}
```

#### End Session

**POST** `/api/tracking/session/end`

End the current tracking session.

**Response:**
```json
{
  "success": true,
  "session_end": "2026-04-20 23:00:00"
}
```

#### Get Logs

**GET** `/api/logs?limit={limit}`

Get tracking logs.

**Parameters:**
- `limit` (optional): Number of log entries to return (default: 100)

**Response:**
```json
{
  "success": true,
  "logs": [
    "[2026-04-20 23:00:00] FILE_ACCESS_API: NavigateTo URL.py in category BrowserCommands",
    "[2026-04-20 23:00:05] SESSION_START_API: Session #11"
  ],
  "count": 2
}
```

---

### Configuration

#### Get Configuration

**GET** `/api/config`

Get API configuration.

**Response:**
```json
{
  "success": true,
  "config": {
    "code_library_path": "/home/robbie/Desktop/CodeLibrary/code-library",
    "log_file": "/home/robbie/Desktop/CodeLibrary/tracking_log.txt",
    "stats_file": "/home/robbie/Desktop/CodeLibrary/usage_stats.json",
    "version": "1.0.0"
  }
}
```

---

## Error Responses

All endpoints may return error responses:

```json
{
  "success": false,
  "error": "Error message here"
}
```

Common HTTP status codes:
- `200` - Success
- `400` - Bad Request (missing required parameters)
- `404` - Not Found (file/directory not found)
- `500` - Internal Server Error

---

## Usage Examples

### Using cURL

```bash
# Health check
curl http://localhost:5000/api/health

# Get categories
curl http://localhost:5000/api/library/categories

# Get files in a category
curl "http://localhost:5000/api/library/files?path=/path/to/code-library/BrowserCommands"

# Get file content
curl "http://localhost:5000/api/library/file?path=/path/to/code-library/BrowserCommands/NavigateTo URL.py"

# Search files
curl "http://localhost:5000/api/library/search?q=navigate"

# Get statistics
curl http://localhost:5000/api/tracking/statistics

# Detect changes
curl http://localhost:5000/api/tracking/changes

# Start session
curl -X POST http://localhost:5000/api/tracking/session/start

# End session
curl -X POST http://localhost:5000/api/tracking/session/end

# Get logs
curl "http://localhost:5000/api/logs?limit=50"
```

### Using Python

```python
import requests

# Health check
response = requests.get('http://localhost:5000/api/health')
print(response.json())

# Get categories
response = requests.get('http://localhost:5000/api/library/categories')
categories = response.json()['categories']

# Get file content
response = requests.get('http://localhost:5000/api/library/file', 
                       params={'path': '/path/to/file.py'})
content = response.json()['content']

# Search
response = requests.get('http://localhost:5000/api/library/search',
                       params={'q': 'navigate'})
results = response.json()['results']
```

### Using JavaScript/Fetch

```javascript
// Get categories
fetch('http://localhost:5000/api/library/categories')
  .then(response => response.json())
  .then(data => console.log(data));

// Get file content
fetch('http://localhost:5000/api/library/file?path=/path/to/file.py')
  .then(response => response.json())
  .then(data => console.log(data.content));

// Search
fetch('http://localhost:5000/api/library/search?q=navigate')
  .then(response => response.json())
  .then(data => console.log(data.results));
```

---

## Configuration

The API uses the following configuration (can be modified in `backend_api.py`):

- `CODE_LIBRARY_PATH`: Path to the code library directory
- `LOG_FILE`: Path to the tracking log file
- `STATS_FILE`: Path to the usage statistics JSON file
- `PORT`: API server port (default: 5000)
- `HOST`: API server host (default: 0.0.0.0)

---

## Running the API

### Prerequisites

Install required packages:
```bash
pip install flask flask-cors
```

### Start the Server

```bash
python backend_api.py
```

The API will be available at `http://localhost:5000`

### Production Deployment

For production, consider:
- Using a production WSGI server (gunicorn, uWSGI)
- Adding authentication
- Using environment variables for configuration
- Enabling HTTPS
- Rate limiting
- Logging and monitoring

---

## Integration with GUI

The backend API can be integrated with the existing GUI by:
1. Replacing direct file operations with API calls
2. Using API endpoints for tracking
3. Fetching statistics from the API
4. This would enable remote GUI instances

---

## Future Enhancements

Potential additions:
- Authentication and authorization
- File upload/modify endpoints
- Advanced search with filters
- Pagination for large result sets
- WebSocket support for real-time updates
- API versioning
- Rate limiting
- Request validation
- Comprehensive error handling
- API documentation with Swagger/OpenAPI

---

## Support

For issues or questions:
- Check the main [README.md](../README.md)
- Review [Troubleshooting Guide](TROUBLESHOOTING.md)
- Open an issue on GitHub
