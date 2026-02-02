# 🎯 Aioverse Agent - Quick Command Reference Card

**Print this page for quick reference!**

---

## 🚀 Getting Started

### Start Interactive Agent
```bash
cd Agent
python main.py
```

### Use Python API
```python
from Agent.main import AssetAgentAPI
api = AssetAgentAPI()
```

### Run Examples
```bash
python Agent/examples/usage_examples.py
```

---

## 📋 Quick Command Cheat Sheet

### Interactive Mode Commands

```
Agent> help                           # Show help
Agent> stats                          # Show statistics
Agent> exit / quit                    # Exit agent

Agent> organize assets by category    # Organize by type
Agent> organize assets by family      # Organize by family
Agent> organize assets by status      # Organize by status

Agent> search for LOGO assets         # Find logos
Agent> search for AIOTIZE             # Find by family
Agent> find ICON                      # Find icons

Agent> validate TOKEN-FAMILY-VAR001   # Validate asset
Agent> get info LOGO-AIOTIZE-PFP001   # Get details
```

---

## 🐍 Python API Cheat Sheet

### Import & Initialize
```python
from Agent.main import AssetAgentAPI
api = AssetAgentAPI()
```

### Asset Operations

#### Import
```python
api.import_asset(
    file_path="/path/to/file.png",
    token="LOGO-AIOTIZE-PFP001",
    category="LOGO",
    family="AIOTIZE",
    variant="PFP",
    tags=["tag1", "tag2"],
    description="Description"
)
```

#### Export
```python
api.export_asset(
    token="LOGO-AIOTIZE-PFP001",
    export_path="./exports",
    include_metadata=True
)
```

#### Organize
```python
# By category
api.organize_assets("by_category")

# By family
api.organize_assets("by_family")

# By status
api.organize_assets("by_status")
```

#### Refine
```python
api.refine_asset(
    token="LOGO-AIOTIZE-PFP001",
    refinement_type="optimize",
    quality=95
)
```

#### Validate
```python
# Validate compliance
api.validate_asset("LOGO-AIOTIZE-PFP001")

# Check standards
api.check_compliance("LOGO-AIOTIZE-PFP001")
```

#### Search
```python
# By category
api.search_assets("LOGO", search_type="category")

# By family
api.search_assets("AIOTIZE", search_type="family")

# By name
api.search_assets("aiotize", search_type="name")

# By tag
api.search_assets("social", search_type="tag")
```

#### Get Information
```python
# Asset info
api.get_asset_info("LOGO-AIOTIZE-PFP001")

# Statistics
api.get_statistics()

# Conversation history
api.get_conversation_history()

# Available tools
api.get_available_tools()
```

---

## 🎨 Token Format Reference

### Structure
```
PREFIX-FAMILY-VARIANT###

Example: LOGO-AIOTIZE-PFP001
```

### Valid Prefixes
```
FNT    = Fonts
LOGO   = Logos & Marks
ICON   = Icons
ILLUST = Illustrations
IMG    = Images & Photos
COLOR  = Colors
TOKEN  = Design Tokens
```

### Valid Families
```
AIOTIZE  = Aiotize Brand
AIOVERSE = Aioverse Brand
SYSTEM   = System Assets
CUSTOM   = Custom Assets
```

### Common Variants
```
PFP       = Profile Picture
MARK      = Logo Mark
WORD      = Wordmark
ICON      = Icon
BG        = Background
ACCENT    = Accent Color
PRIMARY   = Primary
SECONDARY = Secondary
NAV       = Navigation
PROMO     = Promotional
```

---

## 🔍 Search Types Reference

```python
search_type="token"     # Search by token name
search_type="name"      # Search by asset name
search_type="category"  # Search by category
search_type="tag"       # Search by tags
search_type="family"    # Search by family
```

---

## 📁 File Structure Quick Map

```
Agent/
├── main.py                    # Main API entry
├── config/settings.py         # Configuration
├── core/asset_manager.py      # Core engine
├── core/ai_agent.py           # AI agent
├── handlers/operation_*.py    # Handlers
├── utils/validators.py        # Validators
├── examples/usage_*.py        # Examples
├── data/                      # Asset storage
├── logs/agent.log             # Operation logs
├── README.md                  # Full guide
├── QUICKREF.md                # API reference
├── COMPLETE_MASTER_GUIDE.md   # This guide
└── START_HERE.md              # Visual overview
```

---

## ⚙️ Common Configuration Changes

### Add New Asset Type
Edit `Agent/config/settings.py`:
```python
TOKEN_CONFIG["prefixes"]["VIDEO"] = "Videos"
TOKEN_CONFIG["families"]["PARTNER"] = "Partner Brand"
SUPPORTED_FORMATS["videos"] = [".mp4", ".mov"]
```

### Change Storage Location
Edit `Agent/config/settings.py`:
```python
STORAGE_CONFIG["metadata_file"] = Path("/new/path/metadata.json")
```

### Add Supported Format
Edit `Agent/config/settings.py`:
```python
SUPPORTED_FORMATS["images"].append(".webp")
```

---

## 🔧 Validation Functions Quick Map

```python
from utils import (
    MetadataManager,      # Metadata operations
    FileValidator,        # File verification
    TokenGenerator,       # Token management
    FileHelper,           # File utilities
    ComplianceChecker,    # Compliance checking
)

# Validate token
TokenGenerator.validate_token("LOGO-AIOTIZE-PFP001")

# Validate file format
FileValidator.validate_file_format("/path/file.png", "LOGO")

# Validate file size
FileValidator.validate_file_size("/path/file.png", max_size_mb=100)

# Generate token
TokenGenerator.generate_token("LOGO", "AIOTIZE", "PFP", 1)

# Parse token
TokenGenerator.parse_token("LOGO-AIOTIZE-PFP001")

# Check compliance
ComplianceChecker.check_compliance(metadata)

# Get file hash
FileHelper.get_file_hash("/path/file")
```

---

## 🎯 Common Workflows One-Liners

```python
# Import asset
api.import_asset("/path/file.png", "LOGO-AIOTIZE-PFP001", "LOGO", "AIOTIZE", "PFP")

# Validate then export
api.validate_asset(token) and api.export_asset(token, "./exports")

# Find and export all logos
[api.export_asset(a['token'], "./exports") for a in api.search_assets("LOGO", search_type="category")]

# Get stats
stats = api.get_statistics(); print(f"Total: {stats['total_assets']}, Size: {stats['total_size_mb']}MB")

# Organize and validate
api.organize_assets("by_category"); all_ok = all(api.validate_asset(a['token'])['compliant'] for a in api.search_assets("", search_type="token"))

# Search and refine
[api.refine_asset(a['token'], "optimize", quality=95) for a in api.search_assets("AIOTIZE", search_type="family")]
```

---

## 🚨 Error Recovery Quick Guide

```
Error: Token validation failed
Fix: Use TokenGenerator.generate_token() or check format

Error: File not found
Fix: Verify path exists with Path(path).exists()

Error: File format not supported
Fix: Check SUPPORTED_FORMATS in settings.py

Error: Storage corrupted
Fix: Restore from backup or delete to regenerate

Error: Module not found
Fix: Ensure you're in Agent directory and Python path is correct
```

---

## 📊 Output Format Reference

### Import Result
```python
{
    "success": True,
    "token": "LOGO-AIOTIZE-PFP001",
    "metadata": {...}
}
```

### Search Result
```python
[
    {
        "token": "LOGO-AIOTIZE-PFP001",
        "metadata": {...}
    }
]
```

### Statistics Result
```python
{
    "total_assets": 25,
    "by_category": {"LOGO": 5, "ICON": 12, ...},
    "by_family": {"AIOTIZE": 10, "AIOVERSE": 15},
    "total_size_mb": 5.0
}
```

### Validation Result
```python
{
    "token": "LOGO-AIOTIZE-PFP001",
    "compliant": True,
    "issues": [],
    "warnings": []
}
```

---

## 🔑 Key Methods at a Glance

| Method | Purpose | Return |
|--------|---------|--------|
| `import_asset()` | Add new asset | Success bool + token |
| `export_asset()` | Export asset | File path |
| `organize_assets()` | Organize collection | Grouped assets |
| `refine_asset()` | Optimize asset | Refinement record |
| `validate_asset()` | Check compliance | Validation result |
| `search_assets()` | Find assets | List of assets |
| `get_asset_info()` | Get details | Metadata + registry |
| `get_statistics()` | Get stats | Stats dict |
| `check_compliance()` | Verify standards | Compliance result |
| `process_command()` | Natural language | Operation result |

---

## 💡 Pro Tips

```python
# Tip 1: Cache search results
results = api.search_assets("LOGO", search_type="category")
# Reuse 'results' variable instead of searching again

# Tip 2: Batch operations
tokens = [a['token'] for a in api.search_assets("AIOTIZE", search_type="family")]
for token in tokens:
    api.export_asset(token, "./exports")

# Tip 3: Check before operations
token = "LOGO-AIOTIZE-PFP001"
if api.validate_asset(token)['compliant']:
    api.export_asset(token, "./exports")

# Tip 4: Use try-except
try:
    api.import_asset(...)
except Exception as e:
    print(f"Error: {e}")

# Tip 5: Log important operations
import logging
logging.basicConfig(level=logging.INFO)
```

---

## 📞 Getting Help

```
Interactive Mode:     Type "help" or "?"
Documentation:        Read COMPLETE_MASTER_GUIDE.md
Examples:             Run examples/usage_examples.py
Quick Reference:      Check QUICKREF.md
Configuration:        Edit config/settings.py
```

---

## 🎓 Learning Path

1. **5 min** → Read START_HERE.md
2. **10 min** → Run `python Agent/main.py`
3. **20 min** → Read README.md
4. **15 min** → Run examples
5. **30 min** → Read COMPLETE_MASTER_GUIDE.md
6. **1 hour** → Implement workflows

---

## ✨ At a Glance

- **Start:** `python Agent/main.py`
- **API:** `from Agent.main import AssetAgentAPI`
- **Examples:** `python Agent/examples/usage_examples.py`
- **Config:** `Agent/config/settings.py`
- **Help:** `COMPLETE_MASTER_GUIDE.md`

---

**Print & Bookmark This Page!**

**Version:** 1.0.0 | **Last Updated:** Feb 2, 2026 | **Status:** ✓ Ready
