# Aioverse Asset Management Agent

**Version:** 1.0.0  
**Purpose:** Intelligent AI-powered management system for Aioverse brand assets  
**Status:** ✓ Production Ready

---

## 🎯 Overview

The Aioverse Asset Management Agent is a comprehensive, AI-driven system designed to handle all aspects of digital asset lifecycle management for the Aioverse brand ecosystem. It leverages intelligent automation to streamline importing, exporting, organizing, and refining brand assets while maintaining strict compliance with Aioverse standards.

### Key Features

- **🤖 AI-Powered Operations** - Natural language commands processed by intelligent agent
- **📦 Asset Import** - Register new assets with automatic token generation and metadata
- **📤 Asset Export** - Export assets with metadata and compliance verification
- **🏗️ Asset Organization** - Automatically organize assets by category, family, or status
- **✨ Asset Refinement** - Enhance and optimize assets (compress, convert, enhance)
- **✅ Compliance Validation** - Automatic validation against Aioverse standards
- **🔍 Smart Search** - Find assets by token, name, category, or tags
- **📊 Analytics** - Detailed statistics and reporting on asset collection

---

## 📁 Project Structure

```
Agent/
├── config/
│   ├── __init__.py
│   └── settings.py          # Configuration and constants
├── core/
│   ├── __init__.py
│   ├── asset_manager.py     # Core asset management engine
│   └── ai_agent.py          # AI agent with tool integration
├── handlers/
│   ├── __init__.py
│   └── operation_handlers.py # Operation-specific handlers
├── utils/
│   ├── __init__.py
│   └── validators.py        # Validation and utility functions
├── examples/
│   └── usage_examples.py    # Usage examples and patterns
├── data/                    # Asset metadata storage (auto-created)
├── logs/                    # Operation logs (auto-created)
├── main.py                  # Main entry point and API
├── README.md               # This file
├── requirements.txt        # Python dependencies
└── .gitignore             # Git ignore rules
```

---

## 🚀 Quick Start

### Installation

1. **Clone or navigate to the Agent directory:**
```bash
cd Agent
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Initialize storage directories:**
```bash
python main.py
```

### Basic Usage

#### Interactive Mode
```bash
python main.py
```

Then enter commands:
```
Agent> organize all assets by category
Agent> search for LOGO assets
Agent> show statistics
Agent> help
Agent> exit
```

#### Python API
```python
from main import AssetAgentAPI

api = AssetAgentAPI()

# Get statistics
stats = api.get_statistics()
print(f"Total assets: {stats['total_assets']}")

# Search assets
logos = api.search_assets("LOGO", search_type="category")

# Process natural language command
result = api.process_command("Show me all assets organized by family")
```

---

## 📚 Core Modules

### 1. AssetManager (`core/asset_manager.py`)

The heart of the system. Handles all asset operations.

**Key Methods:**
- `import_asset()` - Register new asset
- `export_asset()` - Export asset with metadata
- `organize_assets()` - Organize by category, family, or status
- `refine_asset()` - Apply refinements (optimize, compress, etc.)
- `validate_asset()` - Validate compliance
- `search_assets()` - Find assets by various criteria
- `get_statistics()` - Get collection statistics

**Example:**
```python
from core import AssetManager

manager = AssetManager()

# Import asset
result = manager.import_asset(
    file_path="/path/to/logo.png",
    token="LOGO-AIOTIZE-PFP001",
    category="LOGO",
    family="AIOTIZE",
    variant="PFP",
    metadata={"tags": ["primary", "profile"], "description": "Profile picture"}
)

# Export asset
export = manager.export_asset("LOGO-AIOTIZE-PFP001", "./exports")

# Organize
organized = manager.organize_assets("by_category")

# Search
results = manager.search_assets("AIOTIZE", search_type="family")
```

### 2. AIAssetAgent (`core/ai_agent.py`)

Intelligent agent that processes natural language commands and routes to appropriate operations.

**Key Methods:**
- `process_command()` - Process natural language input
- `get_available_tools()` - List available tools
- `get_conversation_history()` - Get chat history

**Example:**
```python
from core import AIAssetAgent

agent = AIAssetAgent()

result = agent.process_command("Find all logo assets")
print(agent.get_conversation_history())
```

### 3. OperationDispatcher (`handlers/operation_handlers.py`)

Routes operations to specialized handlers with validation.

**Handlers:**
- `ImportHandler` - Validates and imports assets
- `ExportHandler` - Exports with compliance checks
- `OrganizeHandler` - Organizes asset collection
- `RefineHandler` - Applies refinements

### 4. Validators (`utils/validators.py`)

Comprehensive validation and utility functions.

**Classes:**
- `MetadataManager` - Metadata validation and merging
- `FileValidator` - File format and integrity checks
- `TokenGenerator` - Token generation and validation
- `FileHelper` - File operations utilities
- `ComplianceChecker` - Compliance validation

---

## 🎨 Token System

Aioverse uses a structured token format for unique asset identification.

### Token Format
```
{PREFIX}-{FAMILY}-{VARIANT}{NUMBER}

Example: LOGO-AIOTIZE-PFP001
```

### Components

| Component | Description | Examples |
|-----------|-------------|----------|
| PREFIX | Asset type | FNT, LOGO, ICON, ILLUST, IMG, COLOR, TOKEN |
| FAMILY | Asset group | AIOTIZE, AIOVERSE, SYSTEM, CUSTOM |
| VARIANT | Specific variant | PFP, MARK, WORD, ICON, BG, ACCENT |
| NUMBER | Sequential ID | 001, 002, 003... |

### Token Validation
```python
from utils import TokenGenerator

# Validate token
valid, error = TokenGenerator.validate_token("LOGO-AIOTIZE-PFP001")
if valid:
    parsed = TokenGenerator.parse_token("LOGO-AIOTIZE-PFP001")
    print(f"Prefix: {parsed['prefix']}")
    print(f"Family: {parsed['family']}")
```

---

## 📋 Asset Metadata Schema

Each asset is tracked with comprehensive metadata:

```json
{
  "token": "LOGO-AIOTIZE-PFP001",
  "original_name": "aiotize_profile.png",
  "standardized_name": "LOGO_AIOTIZE_PFP001.png",
  "category": "LOGO",
  "family": "AIOTIZE",
  "variant": "PFP",
  "file_path": "/path/to/logo.png",
  "file_size": 102400,
  "created_date": "2025-02-02T10:30:00",
  "modified_date": "2025-02-02T10:30:00",
  "version": "1.0",
  "tags": ["primary", "profile", "social"],
  "description": "Aiotize profile picture logo",
  "usage_rights": "Exclusive brand use",
  "refinements": []
}
```

---

## 🔄 Operation Examples

### Import an Asset
```python
api = AssetAgentAPI()

result = api.import_asset(
    file_path="/path/to/aioverse_logo.svg",
    token="LOGO-AIOVERSE-MARK001",
    category="LOGO",
    family="AIOVERSE",
    variant="MARK",
    tags=["primary", "brand"],
    description="Main Aioverse brand mark"
)
```

### Export an Asset
```python
result = api.export_asset(
    token="LOGO-AIOVERSE-MARK001",
    export_path="./exports",
    include_metadata=True
)
```

### Organize Assets
```python
# By category
result = api.organize_assets("by_category")
# Returns: {"LOGO": [...], "ICON": [...], "FONT": [...]}

# By family
result = api.organize_assets("by_family")
# Returns: {"AIOTIZE": [...], "AIOVERSE": [...]}
```

### Refine an Asset
```python
result = api.refine_asset(
    token="LOGO-AIOTIZE-PFP001",
    refinement_type="optimize",
    quality=95,
    format="webp"
)
```

### Validate Compliance
```python
result = api.validate_asset("LOGO-AIOTIZE-PFP001")
# Returns: {"compliant": True, "issues": [], "warnings": []}
```

### Search Assets
```python
# By token
logos = api.search_assets("LOGO", search_type="category")

# By name
results = api.search_assets("aiotize", search_type="name")

# By tag
social_assets = api.search_assets("social", search_type="tag")
```

---

## 🤖 Natural Language Commands

The AI agent understands natural language commands:

```
"Show me all assets"
"Find logo assets"
"Organize by category"
"Export LOGO-AIOTIZE-PFP001 to exports"
"Get collection statistics"
"Search for AIOTIZE assets"
"Check compliance of LOGO-AIOTIZE-PFP001"
"List all fonts"
"Refine ICON-SYSTEM-NAV001"
```

---

## 📊 Statistics & Reporting

Get comprehensive insights into your asset collection:

```python
stats = api.get_statistics()

# Returns:
{
  "total_assets": 25,
  "by_category": {
    "LOGO": 5,
    "ICON": 12,
    "FONT": 3,
    "ILLUST": 5
  },
  "by_family": {
    "AIOTIZE": 10,
    "AIOVERSE": 15
  },
  "total_size_bytes": 5242880,
  "total_size_mb": 5.0
}
```

---

## ✅ Compliance & Validation

The system enforces compliance with Aioverse standards:

**Validation Checks:**
- ✓ Valid token format
- ✓ Complete metadata
- ✓ File existence
- ✓ Proper naming conventions
- ✓ Proper tagging
- ✓ File format compatibility

**Run Compliance Check:**
```python
compliance = api.check_compliance("LOGO-AIOTIZE-PFP001")

# Returns:
{
  "compliant": True,
  "issues": [],
  "warnings": [],
  "checked_at": "2025-02-02T10:30:00"
}
```

---

## 🔧 Configuration

Edit `config/settings.py` to customize:

- Asset paths
- Supported file formats
- Token configuration
- Metadata schema
- Logging settings
- Storage locations

---

## 📝 Logging

All operations are logged to:
- **File:** `logs/agent.log`
- **Console:** Real-time output
- **Level:** Configurable (INFO, DEBUG, ERROR)

---

## 🧪 Examples

Run example scenarios:

```bash
python examples/usage_examples.py
```

This includes:
1. Basic operations
2. Validation & compliance
3. Direct API usage
4. Workflow scenarios
5. Interactive mode

---

## 📦 Dependencies

See `requirements.txt` for all dependencies:
- Python 3.8+
- Standard library modules (json, pathlib, logging, etc.)

---

## 🔐 Security Considerations

- File integrity validation
- Metadata hash generation
- Path validation
- Format verification
- Size limits

---

## 🎓 Advanced Usage

### Custom Operation Handler
```python
from handlers import OperationDispatcher

dispatcher = OperationDispatcher(asset_manager)
result = dispatcher.execute(
    "import",
    file_path="/path/to/asset",
    token="TOKEN-FAMILY-VAR001",
    category="CATEGORY",
    family="FAMILY",
    variant="VAR"
)
```

### Batch Operations
```python
import os
from pathlib import Path

# Import multiple assets
for file_path in Path("/path/to/assets").glob("*.png"):
    token = f"LOGO-AIOTIZE-{file_path.stem.upper()}"
    api.import_asset(
        str(file_path),
        token,
        "LOGO",
        "AIOTIZE",
        "PFP"
    )
```

---

## 📞 Support & Troubleshooting

### Common Issues

**Token Validation Error**
- Ensure token format: `PREFIX-FAMILY-VARIANT###`
- Check PREFIX and FAMILY are in valid lists

**File Not Found**
- Verify file path exists
- Check file permissions

**Storage Issues**
- Ensure `data/` and `logs/` directories exist
- Check disk space

---

## 📄 License

Part of the Aioverse BrandNew project.

---

## 🚀 Future Enhancements

- [ ] LLM integration for advanced processing
- [ ] Batch import/export operations
- [ ] Asset versioning system
- [ ] Integration with design tools
- [ ] Cloud storage support
- [ ] Advanced analytics dashboard
- [ ] Multi-user permissions system
- [ ] Automated backup system

---

**Last Updated:** February 2, 2025  
**Maintained By:** Aioverse Development Team
