"""
Backend API for Code Library System
REST API providing endpoints for file operations, tracking, and statistics
"""

from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import os
import json
import hashlib
from datetime import datetime
import subprocess

app = Flask(__name__)
CORS(app)

# Configuration - Use environment variables or relative paths
from pathlib import Path
script_dir = Path(__file__).parent.resolve()
CODE_LIBRARY_PATH = os.environ.get('CODE_LIBRARY_PATH', str(script_dir / 'code-library'))
LOG_FILE = os.environ.get('TRACKING_LOG_FILE', str(script_dir / 'tracking_log.txt'))
STATS_FILE = os.environ.get('STATS_FILE', str(script_dir / 'usage_stats.json'))

# Initialize tracking data
def load_tracking_data():
    """Load tracking data from JSON file"""
    try:
        if os.path.exists(STATS_FILE):
            with open(STATS_FILE, 'r') as f:
                return json.load(f)
    except Exception as e:
        print(f"Error loading tracking data: {e}")
    return {
        'file_accesses': {},
        'category_accesses': {},
        'total_sessions': 0,
        'session_start': None
    }

def save_tracking_data(data):
    """Save tracking data to JSON file"""
    try:
        with open(STATS_FILE, 'w') as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"Error saving tracking data: {e}")

def log_event(event_type, details):
    """Log an event to the tracking log"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {event_type}: {details}\n"
    try:
        with open(LOG_FILE, 'a') as f:
            f.write(log_entry)
    except Exception as e:
        print(f"Error writing to log: {e}")

# API Endpoints

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'Code Library Backend API'
    })

@app.route('/api/library/categories', methods=['GET'])
def get_categories():
    """Get all categories (directories) in the code library"""
    try:
        categories = []
        for root, dirs, files in os.walk(CODE_LIBRARY_PATH):
            dirs[:] = [d for d in dirs if d != '__pycache__']
            for dir_name in dirs:
                full_path = os.path.join(root, dir_name)
                rel_path = os.path.relpath(full_path, CODE_LIBRARY_PATH)
                categories.append({
                    'name': dir_name,
                    'path': full_path,
                    'relative_path': rel_path
                })
        return jsonify({
            'success': True,
            'categories': categories,
            'count': len(categories)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/library/files', methods=['GET'])
def get_files():
    """Get files from a specific category"""
    category_path = request.args.get('path')
    if not category_path:
        return jsonify({
            'success': False,
            'error': 'Path parameter required'
        }), 400
    
    try:
        if not os.path.exists(category_path):
            return jsonify({
                'success': False,
                'error': 'Path not found'
            }), 404
        
        files = []
        for item in os.listdir(category_path):
            if item.endswith('.py'):
                file_path = os.path.join(category_path, item)
                files.append({
                    'name': item,
                    'path': file_path
                })
        
        return jsonify({
            'success': True,
            'files': files,
            'count': len(files)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/library/file', methods=['GET'])
def get_file_content():
    """Get content of a specific file"""
    file_path = request.args.get('path')
    if not file_path:
        return jsonify({
            'success': False,
            'error': 'Path parameter required'
        }), 400
    
    try:
        if not os.path.exists(file_path):
            return jsonify({
                'success': False,
                'error': 'File not found'
            }), 404
        
        with open(file_path, 'rb') as f:
            raw_bytes = f.read()
        
        # Try multiple encodings
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
        
        # Track file access
        stats = load_tracking_data()
        file_name = os.path.basename(file_path)
        category = os.path.basename(os.path.dirname(file_path))
        
        if file_name not in stats['file_accesses']:
            stats['file_accesses'][file_name] = 0
        stats['file_accesses'][file_name] += 1
        
        if category not in stats['category_accesses']:
            stats['category_accesses'][category] = 0
        stats['category_accesses'][category] += 1
        
        save_tracking_data(stats)
        log_event("FILE_ACCESS_API", f"{file_name} in category {category}")
        
        return jsonify({
            'success': True,
            'content': content,
            'filename': file_name,
            'encoding': encoding
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/library/search', methods=['GET'])
def search_library():
    """Search for files in the library"""
    query = request.args.get('q', '').lower()
    if not query:
        return jsonify({
            'success': False,
            'error': 'Query parameter required'
        }), 400
    
    try:
        results = []
        for root, dirs, files in os.walk(CODE_LIBRARY_PATH):
            dirs[:] = [d for d in dirs if d != '__pycache__']
            for file in files:
                if file.endswith('.py') and query in file.lower():
                    file_path = os.path.join(root, file)
                    results.append({
                        'name': file,
                        'path': file_path,
                        'relative_path': os.path.relpath(file_path, CODE_LIBRARY_PATH)
                    })
        
        return jsonify({
            'success': True,
            'results': results,
            'count': len(results)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/tracking/statistics', methods=['GET'])
def get_statistics():
    """Get usage statistics"""
    try:
        stats = load_tracking_data()
        
        most_accessed_files = sorted(
            stats['file_accesses'].items(),
            key=lambda x: x[1],
            reverse=True
        )[:10]
        
        most_accessed_categories = sorted(
            stats['category_accesses'].items(),
            key=lambda x: x[1],
            reverse=True
        )[:10]
        
        # Count total files
        total_files = 0
        for root, dirs, files in os.walk(CODE_LIBRARY_PATH):
            dirs[:] = [d for d in dirs if d != '__pycache__']
            total_files += len([f for f in files if f.endswith('.py')])
        
        return jsonify({
            'success': True,
            'statistics': {
                'total_sessions': stats['total_sessions'],
                'most_accessed_files': most_accessed_files,
                'most_accessed_categories': most_accessed_categories,
                'total_files': total_files
            }
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/tracking/changes', methods=['GET'])
def detect_changes():
    """Detect changes in the code library"""
    try:
        changes = []
        file_hashes = {}
        
        # Load existing hashes
        hashes_file = os.environ.get('HASHES_FILE', str(script_dir / 'file_hashes.json'))
        if os.path.exists(hashes_file):
            with open(hashes_file, 'r') as f:
                file_hashes = json.load(f)
        
        # Scan current files
        current_hashes = {}
        for root, dirs, files in os.walk(CODE_LIBRARY_PATH):
            dirs[:] = [d for d in dirs if d != '__pycache__']
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'rb') as f:
                            file_hash = hashlib.md5(f.read()).hexdigest()
                        file_key = os.path.relpath(file_path, CODE_LIBRARY_PATH)
                        current_hashes[file_key] = file_hash
                        
                        if file_key in file_hashes:
                            if file_hashes[file_key] != file_hash:
                                changes.append({
                                    'type': 'MODIFIED',
                                    'file': file_key
                                })
                                log_event("FILE_MODIFIED_API", file_key)
                        else:
                            changes.append({
                                'type': 'NEW',
                                'file': file_key
                            })
                            log_event("FILE_ADDED_API", file_key)
                    except Exception as e:
                        print(f"Error hashing file {file_path}: {e}")
        
        # Check for deleted files
        for file_key in list(file_hashes.keys()):
            if file_key not in current_hashes:
                changes.append({
                    'type': 'DELETED',
                    'file': file_key
                })
                log_event("FILE_DELETED_API", file_key)
        
        # Save current hashes
        with open(hashes_file, 'w') as f:
            json.dump(current_hashes, f, indent=2)
        
        return jsonify({
            'success': True,
            'changes': changes,
            'count': len(changes)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/tracking/session/start', methods=['POST'])
def start_session():
    """Start a new tracking session"""
    try:
        stats = load_tracking_data()
        stats['total_sessions'] += 1
        stats['session_start'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_tracking_data(stats)
        log_event("SESSION_START_API", f"Session #{stats['total_sessions']}")
        
        return jsonify({
            'success': True,
            'session_id': stats['total_sessions']
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/tracking/session/end', methods=['POST'])
def end_session():
    """End the current tracking session"""
    try:
        session_end = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_event("SESSION_END_API", f"Session ended at {session_end}")
        
        return jsonify({
            'success': True,
            'session_end': session_end
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/logs', methods=['GET'])
def get_logs():
    """Get tracking logs"""
    try:
        limit = request.args.get('limit', 100, type=int)
        if not os.path.exists(LOG_FILE):
            return jsonify({
                'success': True,
                'logs': [],
                'count': 0
            })
        
        with open(LOG_FILE, 'r') as f:
            lines = f.readlines()
        
        # Return last N lines
        logs = lines[-limit:] if len(lines) > limit else lines
        
        return jsonify({
            'success': True,
            'logs': [line.strip() for line in logs],
            'count': len(logs)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/config', methods=['GET'])
def get_config():
    """Get API configuration"""
    return jsonify({
        'success': True,
        'config': {
            'code_library_path': CODE_LIBRARY_PATH,
            'log_file': LOG_FILE,
            'stats_file': STATS_FILE,
            'version': '1.0.0'
        }
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
