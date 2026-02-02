# 📡 AIOVERSE ASSET AGENT - REST API DOCUMENTATION

**Version:** 1.0.0  
**Last Updated:** February 2, 2026  
**Base URL:** `http://localhost:8000/api`

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Getting Started](#getting-started)
3. [API Endpoints](#api-endpoints)
4. [Request/Response Format](#requestresponse-format)
5. [Error Handling](#error-handling)
6. [Authentication](#authentication)
7. [Rate Limiting](#rate-limiting)
8. [Examples](#examples)
9. [Webhooks](#webhooks)
10. [Best Practices](#best-practices)

---

## 🌐 Overview

The Aioverse Asset Agent REST API provides HTTP endpoints for managing digital assets in the Aioverse brand ecosystem. It's built with zero external dependencies using Python's native http.server.

### Key Features
- ✅ RESTful design
- ✅ JSON request/response
- ✅ CORS support
- ✅ Comprehensive error handling
- ✅ Tag management
- ✅ Advanced search
- ✅ Asset organization
- ✅ Metadata management

### Technology Stack
- **Server:** Python 3.8+ (http.server)
- **Protocol:** HTTP/1.1
- **Data Format:** JSON
- **Dependencies:** None (pure Python stdlib)

---

## 🚀 Getting Started

### 1. Start the API Server

**Option A: Command Line**
```bash
cd Agent
python api/rest_api.py
# Or specify host and port
python api/rest_api.py --host 0.0.0.0 --port 8080
```

**Option B: Python Code**
```python
from api.rest_api import run_api_server

# Start server
run_api_server(host='localhost', port=8000)
```

### 2. Verify Health
```bash
curl http://localhost:8000/api/health
```

**Response:**
```json
{
  "status": "healthy",
  "service": "Aioverse Asset Agent API",
  "version": "1.0.0",
  "timestamp": "1707000000.0"
}
```

### 3. Make Your First Request
```bash
curl http://localhost:8000/api/statistics
```

---

## 📡 API Endpoints

### Health & Status Endpoints

#### GET /api/health
Check API server health and connectivity.

**Request:**
```bash
curl -X GET http://localhost:8000/api/health
```

**Response (200 OK):**
```json
{
  "status": "healthy",
  "service": "Aioverse Asset Agent API",
  "version": "1.0.0",
  "timestamp": "1707000000.0"
}
```

---

### Asset Management Endpoints

#### GET /api/assets
List all assets in the system.

**Request:**
```bash
curl -X GET http://localhost:8000/api/assets
```

**Response (200 OK):**
```json
{
  "total": 3,
  "assets": [
    {
      "token": "LOGO-AIOTIZE-PFP001",
      "name": "logo-aiotize-pfp001.png",
      "category": "Logos",
      "family": "AIOTIZE",
      "tags": ["primary", "official", "marketing"]
    },
    {
      "token": "ICON-AIOVERSE-UI001",
      "name": "icon-aioverse-ui001.svg",
      "category": "Icons",
      "family": "AIOVERSE",
      "tags": ["ui", "interface", "component"]
    }
  ]
}
```

**Query Parameters:**
- None

**Status Codes:**
- `200` - Success
- `500` - Server error

---

#### GET /api/asset
Get detailed information about a specific asset.

**Request:**
```bash
curl -X GET "http://localhost:8000/api/asset?token=LOGO-AIOTIZE-PFP001"
```

**Response (200 OK):**
```json
{
  "metadata": {
    "token": "LOGO-AIOTIZE-PFP001",
    "original_name": "aiotize_profile_picture.png",
    "standardized_name": "LOGO-AIOTIZE-PFP001.png",
    "category": "Logos",
    "family": "AIOTIZE",
    "variant": "PFP",
    "file_path": "/path/to/logos/LOGO-AIOTIZE-PFP001.png",
    "file_size": 245612,
    "created_date": "2024-01-15T10:30:00",
    "modified_date": "2024-02-01T14:22:00",
    "version": "1.2.0",
    "tags": ["primary", "official", "marketing"],
    "description": "Primary profile picture for Aiotize brand",
    "usage_rights": "Internal & licensed partners"
  },
  "registry": {
    "import_date": "2024-01-15T10:30:00",
    "imported_by": "admin",
    "format": "PNG",
    "integrity_hash": "sha256:abc123..."
  }
}
```

**Query Parameters:**
- `token` (required) - Asset token

**Status Codes:**
- `200` - Success
- `400` - Missing token parameter
- `404` - Asset not found
- `500` - Server error

---

#### POST /api/import
Import a new asset into the system.

**Request:**
```bash
curl -X POST http://localhost:8000/api/import \
  -H "Content-Type: application/json" \
  -d '{
    "file_path": "/path/to/asset.png",
    "metadata": {
      "category": "Logos",
      "family": "AIOTIZE",
      "variant": "PFP",
      "description": "Profile picture",
      "tags": ["primary", "official"],
      "usage_rights": "Internal"
    }
  }'
```

**Response (201 Created):**
```json
{
  "token": "LOGO-AIOTIZE-PFP001",
  "message": "Asset imported successfully",
  "metadata": {
    "token": "LOGO-AIOTIZE-PFP001",
    "file_path": "/path/to/asset.png",
    "created_date": "2024-02-02T10:00:00",
    "tags": ["primary", "official"]
  }
}
```

**Request Body:**
```json
{
  "file_path": "string (required)",
  "metadata": {
    "category": "string",
    "family": "string",
    "variant": "string",
    "description": "string",
    "tags": ["string"],
    "usage_rights": "string",
    "color_hex": "string (for colors only)"
  }
}
```

**Status Codes:**
- `201` - Asset imported successfully
- `400` - Invalid request
- `500` - Server error

---

#### POST /api/export
Export an asset from the system.

**Request:**
```bash
curl -X POST http://localhost:8000/api/export \
  -H "Content-Type: application/json" \
  -d '{
    "token": "LOGO-AIOTIZE-PFP001",
    "export_path": "/backup/exports"
  }'
```

**Response (200 OK):**
```json
{
  "token": "LOGO-AIOTIZE-PFP001",
  "exported_to": "/backup/exports/LOGO-AIOTIZE-PFP001.png",
  "file_size": 245612,
  "metadata_exported": true,
  "message": "Asset exported successfully"
}
```

**Request Body:**
```json
{
  "token": "string (required)",
  "export_path": "string (required)"
}
```

**Status Codes:**
- `200` - Successfully exported
- `400` - Invalid request
- `404` - Asset not found
- `500` - Server error

---

#### POST /api/validate
Validate an asset against compliance standards.

**Request:**
```bash
curl -X POST http://localhost:8000/api/validate \
  -H "Content-Type: application/json" \
  -d '{"token": "LOGO-AIOTIZE-PFP001"}'
```

**Response (200 OK):**
```json
{
  "token": "LOGO-AIOTIZE-PFP001",
  "compliant": true,
  "validation_results": {
    "token_format": true,
    "file_format": true,
    "file_size": true,
    "integrity": true,
    "metadata": true
  },
  "issues": []
}
```

**Request Body:**
```json
{
  "token": "string (required)"
}
```

**Status Codes:**
- `200` - Validation complete
- `400` - Invalid request
- `500` - Server error

---

### Search Endpoints

#### GET /api/search
Search for assets using various criteria.

**Request:**
```bash
# Search by token
curl -X GET "http://localhost:8000/api/search?query=LOGO&type=token"

# Search by name
curl -X GET "http://localhost:8000/api/search?query=profile&type=name"

# Search by category
curl -X GET "http://localhost:8000/api/search?query=Logos&type=category"

# Search by tag
curl -X GET "http://localhost:8000/api/search?query=official&type=tag"
```

**Response (200 OK):**
```json
{
  "query": "official",
  "search_type": "tag",
  "total": 2,
  "results": [
    {
      "token": "LOGO-AIOTIZE-PFP001",
      "metadata": {
        "standardized_name": "LOGO-AIOTIZE-PFP001.png",
        "category": "Logos",
        "tags": ["primary", "official"]
      }
    },
    {
      "token": "ICON-AIOVERSE-UI001",
      "metadata": {
        "standardized_name": "ICON-AIOVERSE-UI001.svg",
        "category": "Icons",
        "tags": ["ui", "official"]
      }
    }
  ]
}
```

**Query Parameters:**
- `query` (required) - Search query
- `type` (optional, default: "token") - Search type: "token", "name", "category", "tag"

**Status Codes:**
- `200` - Search successful
- `400` - Missing query parameter
- `500` - Server error

---

#### GET /api/tags
Get all unique tags in the system.

**Request:**
```bash
curl -X GET http://localhost:8000/api/tags
```

**Response (200 OK):**
```json
{
  "total": 8,
  "tags": [
    "component",
    "interface",
    "marketing",
    "official",
    "primary",
    "secondary",
    "ui",
    "watermark"
  ]
}
```

**Status Codes:**
- `200` - Success
- `500` - Server error

---

#### GET /api/categories
Get all asset categories in the system.

**Request:**
```bash
curl -X GET http://localhost:8000/api/categories
```

**Response (200 OK):**
```json
{
  "total": 6,
  "categories": [
    "Colors",
    "Fonts",
    "Icons",
    "Illustrations",
    "Logos",
    "Photos"
  ]
}
```

**Status Codes:**
- `200` - Success
- `500` - Server error

---

### Tag Management Endpoints

#### POST /api/add-tags
Add tags to an existing asset.

**Request:**
```bash
curl -X POST http://localhost:8000/api/add-tags \
  -H "Content-Type: application/json" \
  -d '{
    "token": "LOGO-AIOTIZE-PFP001",
    "tags": ["featured", "premium"]
  }'
```

**Response (200 OK):**
```json
{
  "token": "LOGO-AIOTIZE-PFP001",
  "tags": ["primary", "official", "marketing", "featured", "premium"],
  "message": "Tags added successfully"
}
```

**Request Body:**
```json
{
  "token": "string (required)",
  "tags": ["string"] (required)
}
```

**Status Codes:**
- `200` - Tags added successfully
- `400` - Invalid request
- `404` - Asset not found
- `500` - Server error

---

#### POST /api/remove-tags
Remove tags from an existing asset.

**Request:**
```bash
curl -X POST http://localhost:8000/api/remove-tags \
  -H "Content-Type: application/json" \
  -d '{
    "token": "LOGO-AIOTIZE-PFP001",
    "tags": ["featured"]
  }'
```

**Response (200 OK):**
```json
{
  "token": "LOGO-AIOTIZE-PFP001",
  "tags": ["primary", "official", "marketing", "premium"],
  "message": "Tags removed successfully"
}
```

**Request Body:**
```json
{
  "token": "string (required)",
  "tags": ["string"] (required)
}
```

**Status Codes:**
- `200` - Tags removed successfully
- `400` - Invalid request
- `404` - Asset not found
- `500` - Server error

---

### Organization Endpoints

#### POST /api/organize
Organize assets by specified method.

**Request:**
```bash
curl -X POST http://localhost:8000/api/organize \
  -H "Content-Type: application/json" \
  -d '{"method": "category"}'
```

**Response (200 OK):**
```json
{
  "method": "category",
  "organization": {
    "Logos": ["LOGO-AIOTIZE-PFP001", "LOGO-AIOVERSE-MARK001"],
    "Icons": ["ICON-AIOVERSE-UI001", "ICON-AIOTIZE-BTN001"],
    "Photos": ["IMG-AIOVERSE-BG001"]
  },
  "message": "Assets organized successfully"
}
```

**Request Body:**
```json
{
  "method": "string (required)" /* "category", "family", or "status" */
}
```

**Status Codes:**
- `200` - Organization successful
- `400` - Invalid method
- `500` - Server error

---

### Quality & Enhancement Endpoints

#### POST /api/refine
Refine and enhance an asset with specified refinements.

**Request:**
```bash
curl -X POST http://localhost:8000/api/refine \
  -H "Content-Type: application/json" \
  -d '{
    "token": "LOGO-AIOTIZE-PFP001",
    "refinements": {
      "compression": "high",
      "color_correction": true,
      "resolution_boost": "2x"
    }
  }'
```

**Response (200 OK):**
```json
{
  "token": "LOGO-AIOTIZE-PFP001",
  "refinements_applied": {
    "compression": "high",
    "color_correction": true,
    "resolution_boost": "2x"
  },
  "message": "Asset refined successfully"
}
```

**Request Body:**
```json
{
  "token": "string (required)",
  "refinements": {
    "compression": "string",
    "color_correction": "boolean",
    "resolution_boost": "string"
  }
}
```

**Status Codes:**
- `200` - Refinement successful
- `400` - Invalid request
- `500` - Server error

---

#### GET /api/statistics
Get comprehensive statistics about the asset collection.

**Request:**
```bash
curl -X GET http://localhost:8000/api/statistics
```

**Response (200 OK):**
```json
{
  "total_assets": 15,
  "by_category": {
    "Logos": 3,
    "Icons": 5,
    "Photos": 4,
    "Fonts": 2,
    "Colors": 1
  },
  "by_family": {
    "AIOTIZE": 7,
    "AIOVERSE": 6,
    "SYSTEM": 2
  },
  "total_size_mb": 125.4,
  "oldest_asset": "2024-01-01T08:00:00",
  "newest_asset": "2024-02-02T15:30:00",
  "avg_asset_size_kb": 8365.3
}
```

**Status Codes:**
- `200` - Success
- `500` - Server error

---

## 📋 Request/Response Format

### Request Headers
```
Content-Type: application/json
Accept: application/json
```

### Response Headers
```
Content-Type: application/json
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET, POST, OPTIONS
```

### Standard Response Structure
```json
{
  "success": true,
  "status": 200,
  "data": {
    /* operation-specific data */
  },
  "message": "Operation successful"
}
```

### Error Response Structure
```json
{
  "error": true,
  "status": 400,
  "message": "Descriptive error message"
}
```

---

## ⚠️ Error Handling

### HTTP Status Codes

| Code | Meaning | Example |
|------|---------|---------|
| `200` | OK | Request successful |
| `201` | Created | Asset imported |
| `400` | Bad Request | Invalid JSON or missing parameters |
| `404` | Not Found | Asset token not found |
| `500` | Server Error | Internal server error |

### Error Response Examples

**400 - Bad Request:**
```json
{
  "error": true,
  "status": 400,
  "message": "Token parameter required"
}
```

**404 - Not Found:**
```json
{
  "error": true,
  "status": 404,
  "message": "Asset not found: INVALID-TOKEN-001"
}
```

**500 - Server Error:**
```json
{
  "error": true,
  "status": 500,
  "message": "Failed to get statistics: <error details>"
}
```

---

## 🔐 Authentication

Currently, the API has **no authentication** enabled. For production use, implement:

### Option 1: API Key
```python
# In rest_api.py
def _check_api_key(self, request):
    key = self.headers.get('X-API-Key')
    return key == os.getenv('API_KEY')
```

### Option 2: JWT Tokens
```python
import jwt

def _verify_jwt_token(self, token):
    try:
        payload = jwt.decode(token, os.getenv('SECRET_KEY'))
        return payload
    except jwt.InvalidTokenError:
        return None
```

### Option 3: OAuth 2.0
Implement OAuth 2.0 flow for third-party integrations.

---

## 🚦 Rate Limiting

Currently **no rate limiting** is implemented. To add it:

```python
from collections import defaultdict
from time import time

class RateLimiter:
    def __init__(self, max_requests=100, window_seconds=60):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = defaultdict(list)
    
    def is_allowed(self, ip):
        now = time()
        # Clean old requests
        self.requests[ip] = [t for t in self.requests[ip] 
                            if now - t < self.window_seconds]
        
        # Check limit
        if len(self.requests[ip]) < self.max_requests:
            self.requests[ip].append(now)
            return True
        return False
```

---

## 📝 Examples

### Complete Workflow: Import → Search → Tag → Export

```bash
# 1. Import asset
TOKEN=$(curl -s -X POST http://localhost:8000/api/import \
  -H "Content-Type: application/json" \
  -d '{
    "file_path": "/path/to/logo.png",
    "metadata": {
      "category": "Logos",
      "family": "AIOTIZE",
      "tags": ["primary"]
    }
  }' | jq -r '.token')

echo "Asset imported with token: $TOKEN"

# 2. Add tags
curl -X POST http://localhost:8000/api/add-tags \
  -H "Content-Type: application/json" \
  -d "{
    \"token\": \"$TOKEN\",
    \"tags\": [\"official\", \"featured\"]
  }"

# 3. Verify asset
curl "http://localhost:8000/api/asset?token=$TOKEN"

# 4. Export asset
curl -X POST http://localhost:8000/api/export \
  -H "Content-Type: application/json" \
  -d "{
    \"token\": \"$TOKEN\",
    \"export_path\": \"/backups\"
  }"

# 5. Search by tag
curl "http://localhost:8000/api/search?query=official&type=tag"
```

### Python Client Example

```python
import requests
import json

class AssetAPIClient:
    def __init__(self, base_url="http://localhost:8000/api"):
        self.base_url = base_url
        self.session = requests.Session()
    
    def import_asset(self, file_path, metadata):
        """Import a new asset"""
        payload = {
            "file_path": file_path,
            "metadata": metadata
        }
        response = self.session.post(
            f"{self.base_url}/import",
            json=payload
        )
        return response.json()
    
    def get_asset(self, token):
        """Get asset information"""
        response = self.session.get(
            f"{self.base_url}/asset",
            params={"token": token}
        )
        return response.json()
    
    def add_tags(self, token, tags):
        """Add tags to asset"""
        payload = {"token": token, "tags": tags}
        response = self.session.post(
            f"{self.base_url}/add-tags",
            json=payload
        )
        return response.json()
    
    def search(self, query, search_type="token"):
        """Search for assets"""
        response = self.session.get(
            f"{self.base_url}/search",
            params={"query": query, "type": search_type}
        )
        return response.json()

# Usage
client = AssetAPIClient()

# Import asset
result = client.import_asset(
    "/path/to/asset.png",
    {
        "category": "Logos",
        "family": "AIOTIZE",
        "tags": ["primary"]
    }
)
token = result["token"]

# Add tags
client.add_tags(token, ["official", "featured"])

# Search
results = client.search("official", search_type="tag")
print(json.dumps(results, indent=2))
```

---

## 🪝 Webhooks

Webhooks allow you to receive notifications about asset events.

### Setup Webhook
```python
# In rest_api.py
def _trigger_webhook(event, data):
    webhook_url = os.getenv('WEBHOOK_URL')
    if webhook_url:
        payload = {"event": event, "data": data}
        requests.post(webhook_url, json=payload)
```

### Events
- `asset.imported` - Asset imported
- `asset.exported` - Asset exported
- `asset.validated` - Asset validated
- `asset.refined` - Asset refined
- `tag.added` - Tag added to asset
- `tag.removed` - Tag removed from asset

---

## ✨ Best Practices

### 1. Error Handling
Always check response status codes:
```python
response = requests.get("http://localhost:8000/api/health")
if response.status_code == 200:
    data = response.json()
else:
    print(f"Error: {response.status_code}")
```

### 2. Token Management
Store tokens securely:
```python
import json

# Save tokens
tokens = {"logo_pfp": "LOGO-AIOTIZE-PFP001"}
with open("asset_tokens.json", "w") as f:
    json.dump(tokens, f)

# Load tokens
with open("asset_tokens.json") as f:
    tokens = json.load(f)
```

### 3. Batch Operations
Process multiple assets efficiently:
```python
assets = [
    {"name": "logo1.png", "tags": ["primary"]},
    {"name": "logo2.png", "tags": ["secondary"]},
]

for asset in assets:
    result = client.import_asset(asset["name"], asset)
    print(f"Imported: {result['token']}")
```

### 4. Tag Standardization
Use consistent tag naming:
```
✅ Good: ["official", "marketing", "primary"]
❌ Bad: ["Official", "MARKETING", "Primary"]
```

### 5. Caching
Implement caching to reduce API calls:
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def get_asset_cached(token):
    return client.get_asset(token)
```

---

## 📚 Related Documentation

- [Quick API Reference](QUICK_API_REFERENCE.md)
- [Python Client Guide](PYTHON_CLIENT_GUIDE.md)
- [API Usage Examples](API_USAGE_EXAMPLES.md)
- [Storage & Deployment](STORAGE_DEPLOYMENT_GUIDE.md)

---

**API Documentation Version:** 1.0.0  
**Last Updated:** February 2, 2026  
**Status:** ✅ Production Ready
