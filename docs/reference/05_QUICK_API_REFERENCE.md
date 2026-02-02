# 🚀 QUICK API REFERENCE

**Version:** 1.0.0 | **Status:** ✅ Production Ready  
**Base URL:** `http://localhost:8000/api`

---

## ⚡ Quick Start (30 seconds)

```bash
# 1. Start API server
python Agent/api/rest_api.py

# 2. Check health
curl http://localhost:8000/api/health

# 3. View all assets
curl http://localhost:8000/api/assets

# Done! 🎉
```

---

## 📡 All Endpoints at a Glance

### Health & Status
| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/health` | Check API status |
| GET | `/statistics` | Get asset statistics |

### Assets
| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/assets` | List all assets |
| GET | `/asset?token=TOKEN` | Get asset details |
| POST | `/import` | Import new asset |
| POST | `/export` | Export asset |

### Operations
| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/validate` | Validate asset |
| POST | `/refine` | Refine/optimize asset |
| POST | `/organize` | Organize assets by method |

### Search & Filter
| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/search?query=Q&type=TYPE` | Search assets |
| GET | `/tags` | List all tags |
| GET | `/categories` | List categories |

### Tags
| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/add-tags` | Add tags to asset |
| POST | `/remove-tags` | Remove tags from asset |

---

## 💻 Common Commands

### Import Asset
```bash
curl -X POST http://localhost:8000/api/import \
  -H "Content-Type: application/json" \
  -d '{
    "file_path": "/path/to/logo.png",
    "metadata": {
      "category": "Logos",
      "family": "AIOTIZE",
      "tags": ["primary", "official"]
    }
  }'
```

### Search by Tag
```bash
curl "http://localhost:8000/api/search?query=official&type=tag"
```

### Add Tags
```bash
curl -X POST http://localhost:8000/api/add-tags \
  -H "Content-Type: application/json" \
  -d '{
    "token": "LOGO-AIOTIZE-PFP001",
    "tags": ["featured", "premium"]
  }'
```

### Export Asset
```bash
curl -X POST http://localhost:8000/api/export \
  -H "Content-Type: application/json" \
  -d '{
    "token": "LOGO-AIOTIZE-PFP001",
    "export_path": "/backups"
  }'
```

### Get Statistics
```bash
curl http://localhost:8000/api/statistics
```

---

## 🔍 Search Types

```
Type: "token"       → Search by token/ID (partial match)
Type: "name"        → Search by asset name (partial match)
Type: "category"    → Search by category (exact match)
Type: "tag"         → Search by tag (exact match)
```

---

## 📦 Common Metadata Fields

```json
{
  "category": "Logos",           // Required: Logos, Icons, Photos, etc.
  "family": "AIOTIZE",           // Required: AIOTIZE, AIOVERSE, SYSTEM, CUSTOM
  "variant": "PFP",              // Optional: Profile, Mark, Icon, etc.
  "tags": ["primary", "official"],  // Optional: Custom tags
  "description": "Main logo",    // Optional: Description
  "usage_rights": "Internal",    // Optional: Usage info
  "color_hex": "#FF6B35"         // Optional: For color assets
}
```

---

## 📊 Response Codes

| Code | Meaning |
|------|---------|
| 200 | OK - Request successful |
| 201 | Created - Asset imported |
| 400 | Bad Request - Invalid parameters |
| 404 | Not Found - Asset doesn't exist |
| 500 | Server Error - Internal error |

---

## 🐍 Python Quick Usage

```python
import requests

BASE_URL = "http://localhost:8000/api"

# Health check
response = requests.get(f"{BASE_URL}/health")
print(response.json())

# List assets
response = requests.get(f"{BASE_URL}/assets")
assets = response.json()
print(f"Total assets: {assets['total']}")

# Search
response = requests.get(f"{BASE_URL}/search", 
  params={"query": "official", "type": "tag"})
results = response.json()
print(f"Found {results['total']} assets")

# Import
response = requests.post(f"{BASE_URL}/import", json={
  "file_path": "/path/to/asset.png",
  "metadata": {
    "category": "Logos",
    "family": "AIOTIZE",
    "tags": ["primary"]
  }
})
print(f"Token: {response.json()['token']}")

# Add tags
response = requests.post(f"{BASE_URL}/add-tags", json={
  "token": "LOGO-AIOTIZE-PFP001",
  "tags": ["featured"]
})
print(response.json())
```

---

## 🎯 One-Liners

```bash
# Get all asset tokens
curl http://localhost:8000/api/assets | jq '.assets[].token'

# Count total assets
curl http://localhost:8000/api/statistics | jq '.total_assets'

# Find all "official" assets
curl "http://localhost:8000/api/search?query=official&type=tag" | jq '.results[].token'

# List all tags
curl http://localhost:8000/api/tags | jq '.tags'

# Get asset details
TOKEN="LOGO-AIOTIZE-PFP001"
curl "http://localhost:8000/api/asset?token=$TOKEN" | jq '.metadata'
```

---

## 🔄 Complete Workflow

```bash
# 1. Import
TOKEN=$(curl -s -X POST http://localhost:8000/api/import \
  -H "Content-Type: application/json" \
  -d '{"file_path": "/path/to/logo.png", "metadata": {"category": "Logos", "family": "AIOTIZE"}}' \
  | jq -r '.token')

# 2. Add tags
curl -X POST http://localhost:8000/api/add-tags \
  -H "Content-Type: application/json" \
  -d "{\"token\": \"$TOKEN\", \"tags\": [\"primary\", \"official\"]}"

# 3. Verify
curl "http://localhost:8000/api/asset?token=$TOKEN" | jq '.metadata.tags'

# 4. Export
curl -X POST http://localhost:8000/api/export \
  -H "Content-Type: application/json" \
  -d "{\"token\": \"$TOKEN\", \"export_path\": \"/backups\"}"
```

---

## ⚠️ Common Errors & Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| Connection refused | API not running | `python Agent/api/rest_api.py` |
| 404 Not Found | Wrong endpoint | Check endpoint spelling |
| 400 Bad Request | Missing parameter | Add required fields |
| 404 Asset not found | Token doesn't exist | Check token value |
| Invalid JSON | Malformed request | Validate JSON syntax |

---

## 🔗 Related Documentation

- [Full API Docs](API_DOCUMENTATION.md) - Complete endpoint reference
- [Storage Guide](STORAGE_DEPLOYMENT_GUIDE.md) - Deployment options
- [Workflows](WORKFLOW_DIAGRAMS.md) - Visual diagrams
- [Master Guide](COMPLETE_MASTER_GUIDE.md) - Everything in detail

---

**Made for Speed** ⚡ | **Quick Reference** 📖 | **Production Ready** ✅
