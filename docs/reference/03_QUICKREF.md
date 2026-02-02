# Aioverse Asset Agent - Quick Reference Guide

## 🚀 Quick Start

### Run Interactive Agent
```bash
cd Agent
python main.py
```

### Basic Commands
```
Agent> organize assets by category
Agent> search for LOGO assets
Agent> show statistics
Agent> help
Agent> exit
```

---

## 📚 Python API Quick Reference

### Initialize API
```python
from main import AssetAgentAPI
api = AssetAgentAPI()
```

### Common Operations

#### 1. Get Statistics
```python
stats = api.get_statistics()
print(f"Total assets: {stats['total_assets']}")
print(f"Total size: {stats['total_size_mb']} MB")
```

#### 2. Import Asset
```python
result = api.import_asset(
    file_path="/path/to/asset.png",
    token="LOGO-AIOTIZE-PFP001",
    category="LOGO",
    family="AIOTIZE",
    variant="PFP",
    tags=["social", "profile"],
    description="Profile picture"
)
```

#### 3. Export Asset
```python
result = api.export_asset(
    token="LOGO-AIOTIZE-PFP001",
    export_path="./exports",
    include_metadata=True
)
```

#### 4. Organize Assets
```python
# By category
organized = api.organize_assets("by_category")

# By family
organized = api.organize_assets("by_family")

# By status
organized = api.organize_assets("by_status")
```

#### 5. Refine Asset
```python
result = api.refine_asset(
    token="LOGO-AIOTIZE-PFP001",
    refinement_type="optimize",
    quality=95,
    format="webp"
)
```

#### 6. Validate Asset
```python
result = api.validate_asset("LOGO-AIOTIZE-PFP001")
if result['compliant']:
    print("✓ Asset is compliant")
else:
    print(f"✗ Issues: {result['issues']}")
```

#### 7. Search Assets
```python
# By token
results = api.search_assets("LOGO", search_type="category")

# By name
results = api.search_assets("aiotize", search_type="name")

# By tag
results = api.search_assets("social", search_type="tag")
```

#### 8. Get Asset Info
```python
info = api.get_asset_info("LOGO-AIOTIZE-PFP001")
print(info['metadata'])
print(info['registry'])
```

#### 9. Check Compliance
```python
compliance = api.check_compliance("LOGO-AIOTIZE-PFP001")
if compliance['compliant']:
    print("✓ Compliant with standards")
```

#### 10. Process Natural Language Command
```python
result = api.process_command("Show me all logos organized by family")
print(result)
```

---

## 🎨 Token Format Reference

### Valid Token Formats
- `LOGO-AIOTIZE-PFP001` - Logo asset
- `ICON-SYSTEM-NAV001` - System icon
- `FNT-AIOVERSE-HEAD001` - Font asset
- `ILLUST-CUSTOM-BG001` - Custom illustration
- `COLOR-AIOTIZE-PRIMARY001` - Color token

### Token Components
```
PREFIX-FAMILY-VARIANT###

PREFIX:   FNT, LOGO, ICON, ILLUST, IMG, COLOR, TOKEN
FAMILY:   AIOTIZE, AIOVERSE, SYSTEM, CUSTOM
VARIANT:  PFP, MARK, WORD, ICON, BG, ACCENT, PRIMARY, SECONDARY, NAV, etc.
###:      Sequential number (001, 002, etc.)
```

---

## 🔍 Search Examples

### Search by Category
```python
api.search_assets("LOGO", search_type="category")
api.search_assets("ICON", search_type="category")
api.search_assets("FNT", search_type="category")
```

### Search by Family
```python
api.search_assets("AIOTIZE", search_type="family")
api.search_assets("AIOVERSE", search_type="family")
```

### Search by Name
```python
api.search_assets("profile", search_type="name")
api.search_assets("aiotize", search_type="name")
```

### Search by Tag
```python
api.search_assets("social", search_type="tag")
api.search_assets("primary", search_type="tag")
```

---

## 🎯 Common Workflows

### Workflow 1: Import New Logo
```python
import api = AssetAgentAPI()

# Import the asset
result = api.import_asset(
    file_path="./assets/new_logo.svg",
    token="LOGO-AIOTIZE-PFP002",
    category="LOGO",
    family="AIOTIZE",
    variant="PFP",
    tags=["brand", "profile"],
    description="Updated Aiotize profile logo"
)

# Validate it
validation = api.validate_asset("LOGO-AIOTIZE-PFP002")

# Check compliance
compliance = api.check_compliance("LOGO-AIOTIZE-PFP002")

# Export it
export = api.export_asset("LOGO-AIOTIZE-PFP002", "./exports")
```

### Workflow 2: Batch Organization
```python
# Get all assets
stats = api.get_statistics()
print(f"Total assets: {stats['total_assets']}")

# Organize by category
by_category = api.organize_assets("by_category")
for category, assets in by_category.items():
    print(f"{category}: {len(assets)} assets")

# Organize by family
by_family = api.organize_assets("by_family")
for family, assets in by_family.items():
    print(f"{family}: {len(assets)} assets")
```

### Workflow 3: Asset Search and Export
```python
# Find all AIOTIZE assets
results = api.search_assets("AIOTIZE", search_type="family")

# Get info on each
for asset in results:
    info = api.get_asset_info(asset['token'])
    print(f"Found: {asset['token']}")
    
    # Export each one
    api.export_asset(asset['token'], "./exports")
```

### Workflow 4: Quality Check
```python
# Get all assets
stats = api.get_statistics()

# Check each category
for category in stats['by_category']:
    assets = api.search_assets(category, search_type="category")
    
    for asset in assets:
        # Validate
        validation = api.validate_asset(asset['token'])
        
        # Check compliance
        compliance = api.check_compliance(asset['token'])
        
        if not validation['compliant']:
            print(f"⚠️  {asset['token']}: {validation['issues']}")
```

---

## ⚙️ Configuration

Edit `config/settings.py` to customize:

```python
# Token configuration
TOKEN_CONFIG = {
    "prefixes": {...},
    "families": {...},
    "variants": {...},
}

# Supported formats
SUPPORTED_FORMATS = {
    "images": [".png", ".jpg", ".svg", ...],
    "fonts": [".ttf", ".otf", ...],
}

# Storage
STORAGE_CONFIG = {
    "metadata_file": Path(...),
    "registry_file": Path(...),
}
```

---

## 📊 Data Storage

### Metadata File
Location: `Agent/data/asset_metadata.json`
Contains: Complete metadata for all assets

### Registry File
Location: `Agent/data/asset_registry.json`
Contains: Status and tracking info for each asset

### Logs
Location: `Agent/logs/agent.log`
Contains: All operation logs

---

## 🐛 Troubleshooting

### Import Not Working
```python
# Check file exists
from pathlib import Path
assert Path("/path/to/file").exists()

# Validate token format
from utils import TokenGenerator
valid, error = TokenGenerator.validate_token("LOGO-AIOTIZE-PFP001")
assert valid, error
```

### Search Returning No Results
```python
# Check asset exists in registry
info = api.get_asset_info("LOGO-AIOTIZE-PFP001")

# Try different search type
results = api.search_assets("LOGO", search_type="category")
results = api.search_assets("aiotize", search_type="family")
```

### Compliance Issues
```python
# Check what issues exist
result = api.validate_asset("TOKEN")
print(result['issues'])
print(result['warnings'])

# Get detailed info
info = api.get_asset_info("TOKEN")
print(info['metadata'])
```

---

## 📞 Getting Help

### View Available Tools
```python
tools = api.get_available_tools()
for tool in tools:
    print(f"{tool['name']}: {tool['description']}")
    print(f"Parameters: {tool['parameters']}")
```

### View Conversation History
```python
history = api.get_conversation_history()
for message in history:
    print(f"{message['role']}: {message['content']}")
```

### Example Usage
```bash
python examples/usage_examples.py
```

---

## 🔗 File Locations

```
Agent/
├── config/settings.py       # Configuration
├── core/                    # Core modules
│   ├── asset_manager.py     # Main engine
│   └── ai_agent.py          # AI agent
├── handlers/                # Operation handlers
├── utils/                   # Utilities
├── examples/                # Example code
├── data/                    # Asset metadata (auto-created)
│   ├── asset_metadata.json
│   └── asset_registry.json
├── logs/                    # Logs (auto-created)
│   └── agent.log
├── main.py                  # Main API
├── README.md                # Full documentation
└── QUICKREF.md             # This file
```

---

**Version:** 1.0.0  
**Updated:** February 2, 2025
