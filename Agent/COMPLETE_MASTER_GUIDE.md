# 📘 Aioverse Asset Agent - Complete Master Guide

**Version:** 1.0.0  
**Date:** February 2, 2026  
**Status:** Production Ready  
**Purpose:** Complete reference for all Agent components, operations, and workflows

---

## Table of Contents

1. [System Architecture](#-system-architecture)
2. [Component Breakdown](#-component-breakdown-detailed)
3. [How to Use the Agent](#-how-to-use-the-agent)
4. [How to Update the Repository](#-how-to-update-the-repository)
5. [How to Export Components](#-how-to-export-components)
6. [Comprehensive Operation Guide](#-comprehensive-operation-guide)
7. [FAQ & Common Queries](#-faq--common-queries)
8. [Troubleshooting](#-troubleshooting)
9. [Advanced Topics](#-advanced-topics)
10. [Best Practices](#-best-practices)

---

## 🏗️ System Architecture

### High-Level Overview

```
┌─────────────────────────────────────────────────────────┐
│                    USER INTERFACE LAYER                  │
├─────────────────────────────────────────────────────────┤
│  Interactive CLI (main.py)  │  Python API (main.py)    │
│  Natural Language Commands  │  Programmatic Access     │
└──────────────────┬──────────────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────────────┐
│            AI AGENT & ROUTING LAYER                      │
├──────────────────────────────────────────────────────────┤
│  AIAssetAgent (core/ai_agent.py)                        │
│  - Intent Detection                                      │
│  - Command Routing                                       │
│  - Tool Management                                       │
│  - Conversation Tracking                                │
└──────────────────┬──────────────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────────────┐
│          OPERATION DISPATCH LAYER                        │
├──────────────────────────────────────────────────────────┤
│  OperationDispatcher (handlers/operation_handlers.py)   │
│  - Input Validation                                      │
│  - Handler Selection                                     │
│  - Error Handling                                        │
└──────────────────┬──────────────────────────────────────┘
                   │
        ┌──────────┼──────────┐
        │          │          │
┌───────▼────┐ ┌──▼──────┐ ┌─▼──────────┐
│Import      │ │Export   │ │Organize    │
│Handler     │ │Handler  │ │Handler     │
└───────┬────┘ └──┬──────┘ └─┬──────────┘
        │         │          │
        └─────────┼──────────┘
                  │
┌─────────────────▼──────────────────────────────────────┐
│          CORE BUSINESS LOGIC LAYER                      │
├──────────────────────────────────────────────────────────┤
│  AssetManager (core/asset_manager.py)                  │
│  - Asset Lifecycle Management                           │
│  - Metadata Handling                                     │
│  - Search & Query                                        │
│  - Statistics Generation                                │
└─────────────────┬──────────────────────────────────────┘
                  │
┌─────────────────▼──────────────────────────────────────┐
│          VALIDATION & UTILITIES LAYER                   │
├──────────────────────────────────────────────────────────┤
│  Validators (utils/validators.py)                      │
│  - MetadataManager                                      │
│  - FileValidator                                        │
│  - TokenGenerator                                       │
│  - ComplianceChecker                                    │
│  - FileHelper                                           │
└─────────────────┬──────────────────────────────────────┘
                  │
┌─────────────────▼──────────────────────────────────────┐
│          PERSISTENCE LAYER                              │
├──────────────────────────────────────────────────────────┤
│  JSON Storage (data/)                                   │
│  - asset_metadata.json                                  │
│  - asset_registry.json                                  │
│  - Logs (logs/agent.log)                               │
└─────────────────────────────────────────────────────────┘
```

### Data Flow

```
User Input
    │
    ▼
┌─────────────────┐
│ AIAssetAgent    │  (Intent Detection)
│ .process_command│
└────────┬────────┘
         │
         ▼
    ┌─────────┐
    │ Intent? │
    └────┬────┘
         │
    ┌────┴─────────────────────┬─────────────────┐
    │                           │                 │
    ▼                           ▼                 ▼
┌─────────┐          ┌──────────────┐    ┌──────────────┐
│ Import? │          │ Export?      │    │ Organize?    │
└────┬────┘          └──────┬───────┘    └──────┬───────┘
     │                      │                   │
     ▼                      ▼                   ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│InputHandler  │   │OutputHandler │   │OrgHandler    │
│- Validate    │   │- Validate    │   │- Validate    │
│- Sanitize    │   │- Export      │   │- Organize    │
└──────┬───────┘   └──────┬───────┘   └──────┬───────┘
       │                  │                  │
       └──────┬───────────┴──────────────────┘
              │
              ▼
     ┌────────────────────┐
     │ AssetManager       │
     │ Execute Operation  │
     └────────┬───────────┘
              │
              ▼
     ┌────────────────────┐
     │ Persist to JSON    │
     │ Log Operation      │
     └────────────────────┘
```

---

## 📦 Component Breakdown (Detailed)

### 1. **AIAssetAgent** (`core/ai_agent.py`)

**Purpose:** Bridge between user commands and system operations through AI-powered intent recognition.

**Key Responsibilities:**
- Parse natural language commands
- Detect user intent
- Route to appropriate operation
- Maintain conversation history
- Provide tool information

**Main Methods:**

```python
# Initialize agent
agent = AIAssetAgent()

# Process user command
result = agent.process_command("organize assets by category")

# Get available tools
tools = agent.get_available_tools()

# Get conversation history
history = agent.get_conversation_history()

# Clear history
agent.clear_conversation_history()
```

**How It Works:**
1. User inputs natural language command
2. Agent analyzes command using keyword matching
3. Agent determines intent (import, export, organize, etc.)
4. Agent routes to appropriate handler
5. Handler executes operation
6. Result returned to user

**Intent Recognition:**
```python
# Recognized intents:
"import" - Keywords: import, add, register, upload
"export" - Keywords: export, download, extract, save
"organize" - Keywords: organize, categorize, sort, group
"refine" - Keywords: refine, enhance, optimize, improve
"validate" - Keywords: validate, check, verify, audit
"search" - Keywords: search, find, look for, query
"info" - Keywords: info, detail, metadata, status
"statistics" - Keywords: stat, report, summary, count
```

**Conversation History:**
```python
# Stored as:
[
    {"role": "user", "content": "command text"},
    {"role": "assistant", "content": "result"}
]
```

---

### 2. **AssetManager** (`core/asset_manager.py`)

**Purpose:** Core engine handling all asset lifecycle operations.

**Key Responsibilities:**
- Import assets with metadata
- Export assets with metadata
- Organize assets
- Refine assets
- Validate compliance
- Search assets
- Generate statistics

**Main Methods:**

#### **import_asset()**
```python
result = manager.import_asset(
    file_path="/path/to/asset.png",
    token="LOGO-AIOTIZE-PFP001",
    category="LOGO",
    family="AIOTIZE",
    variant="PFP",
    metadata={
        "tags": ["social", "profile"],
        "description": "Profile picture",
        "usage_rights": "Brand exclusive"
    }
)

# Returns:
{
    "success": True,
    "token": "LOGO-AIOTIZE-PFP001",
    "metadata": {...}
}
```

**Validation Steps:**
1. Check file exists
2. Verify file format
3. Validate file size
4. Generate standardized name
5. Create metadata
6. Store in registry
7. Log operation

#### **export_asset()**
```python
result = manager.export_asset(
    token="LOGO-AIOTIZE-PFP001",
    export_path="/exports",
    include_metadata=True
)

# Returns:
{
    "success": True,
    "token": "LOGO-AIOTIZE-PFP001",
    "exported_file": "/exports/LOGO_AIOTIZE_PFP001.png",
    "metadata_file": "/exports/LOGO-AIOTIZE-PFP001_metadata.json"
}
```

**Export Process:**
1. Verify asset exists
2. Copy file to destination
3. Generate metadata JSON
4. Update last accessed timestamp
5. Log operation

#### **organize_assets()**
```python
result = manager.organize_assets("by_category")

# Returns:
{
    "success": True,
    "method": "by_category",
    "organization": {
        "LOGO": [
            {"token": "LOGO-AIOTIZE-PFP001", "name": "..."},
            ...
        ],
        "ICON": [...],
        ...
    },
    "total_assets": 25
}
```

**Supported Methods:**
- `"by_category"` - Group by LOGO, ICON, etc.
- `"by_family"` - Group by AIOTIZE, AIOVERSE, etc.
- `"by_status"` - Group by active, archived, etc.

#### **refine_asset()**
```python
result = manager.refine_asset(
    token="LOGO-AIOTIZE-PFP001",
    refinement_type="optimize",
    parameters={"quality": 95, "format": "webp"}
)

# Returns:
{
    "success": True,
    "token": "LOGO-AIOTIZE-PFP001",
    "refinement_type": "optimize",
    "result": {
        "type": "optimize",
        "parameters": {...},
        "timestamp": "2025-02-02T...",
        "status": "applied"
    }
}
```

**Refinement Types:**
- `"compress"` - Reduce file size
- `"optimize"` - Improve quality
- `"convert"` - Change format
- `"enhance"` - Improve visuals

#### **validate_asset()**
```python
result = manager.validate_asset("LOGO-AIOTIZE-PFP001")

# Returns:
{
    "token": "LOGO-AIOTIZE-PFP001",
    "issues": [],
    "warnings": ["Source file not found"],
    "compliant": True
}
```

**Validation Checks:**
- Token format validity
- Required metadata fields
- File existence
- File format compatibility

#### **search_assets()**
```python
# By token
results = manager.search_assets("LOGO", search_type="token")

# By name
results = manager.search_assets("aiotize", search_type="name")

# By category
results = manager.search_assets("LOGO", search_type="category")

# By tag
results = manager.search_assets("social", search_type="tag")

# Returns:
[
    {
        "token": "LOGO-AIOTIZE-PFP001",
        "metadata": {...}
    },
    ...
]
```

#### **get_statistics()**
```python
stats = manager.get_statistics()

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

### 3. **Operation Handlers** (`handlers/operation_handlers.py`)

**Purpose:** Specialized handlers for each operation type with validation.

#### **ImportHandler**
```python
handler = ImportHandler(asset_manager)

result = handler.handle_import(
    file_path="/path/to/asset.png",
    token="LOGO-AIOTIZE-PFP001",
    category="LOGO",
    family="AIOTIZE",
    variant="PFP",
    metadata={...}
)
```

**Validation Steps:**
1. Validate token format
2. Validate file format
3. Check file size
4. Verify file integrity
5. Pass to AssetManager

#### **ExportHandler**
```python
handler = ExportHandler(asset_manager)

result = handler.handle_export(
    token="LOGO-AIOTIZE-PFP001",
    export_path="/exports",
    include_metadata=True,
    include_compliance=True
)
```

**Capabilities:**
- Export with metadata
- Include compliance report
- Verify asset exists
- Handle errors gracefully

#### **OrganizeHandler**
```python
handler = OrganizeHandler(asset_manager)

result = handler.handle_organize(method="by_category")
```

#### **RefineHandler**
```python
handler = RefineHandler(asset_manager)

result = handler.handle_refine(
    token="LOGO-AIOTIZE-PFP001",
    refinement_type="optimize",
    parameters={"quality": 95}
)
```

#### **OperationDispatcher**
```python
dispatcher = OperationDispatcher(asset_manager)

# Dispatch any operation
result = dispatcher.execute(
    "import",
    file_path="/path/to/file",
    token="TOKEN",
    category="CATEGORY",
    family="FAMILY",
    variant="VARIANT",
    metadata={...}
)
```

---

### 4. **Validators & Utilities** (`utils/validators.py`)

**Purpose:** Comprehensive validation and utility functions.

#### **MetadataManager**
```python
from utils import MetadataManager

# Validate metadata
valid, errors = MetadataManager.validate_metadata(metadata_dict)

# Merge metadata
merged = MetadataManager.merge_metadata(existing, updates)

# Generate hash
hash_val = MetadataManager.generate_metadata_hash(metadata)
```

#### **FileValidator**
```python
from utils import FileValidator

# Validate format
valid, error = FileValidator.validate_file_format(
    file_path="/path/to/file.png",
    category="LOGO"
)

# Validate size
valid, error = FileValidator.validate_file_size(
    file_path="/path/to/file.png",
    max_size_mb=100
)

# Validate integrity
valid, error = FileValidator.validate_file_integrity(
    file_path="/path/to/file.png"
)
```

#### **TokenGenerator**
```python
from utils import TokenGenerator

# Generate token
token = TokenGenerator.generate_token(
    prefix="LOGO",
    family="AIOTIZE",
    variant="PFP",
    sequence_number=1
)
# Returns: "LOGO-AIOTIZE-PFP001"

# Validate token
valid, error = TokenGenerator.validate_token("LOGO-AIOTIZE-PFP001")

# Parse token
parsed = TokenGenerator.parse_token("LOGO-AIOTIZE-PFP001")
# Returns: {
#   "prefix": "LOGO",
#   "family": "AIOTIZE",
#   "variant": "PFP",
#   "number": "001",
#   "full_token": "LOGO-AIOTIZE-PFP001"
# }
```

#### **FileHelper**
```python
from utils import FileHelper

# Get file hash
hash_val = FileHelper.get_file_hash("/path/to/file")

# Copy file
FileHelper.copy_file("/source", "/destination", preserve_metadata=True)

# List files
files = FileHelper.list_files_in_directory("/dir", extension=".png")

# Calculate directory size
size = FileHelper.calculate_directory_size("/dir")
```

#### **ComplianceChecker**
```python
from utils import ComplianceChecker

# Check compliance
result = ComplianceChecker.check_compliance(metadata)
# Returns: {
#   "compliant": True,
#   "issues": [],
#   "warnings": [],
#   "checked_at": "2025-02-02T..."
# }
```

---

### 5. **Configuration** (`config/settings.py`)

**Purpose:** Centralized configuration management.

**Key Settings:**

```python
# Asset paths
ASSET_PATHS = {
    "fonts": PROJECT_ROOT / "fonts",
    "colours": PROJECT_ROOT / "colours",
    "icons": PROJECT_ROOT / "icons",
    "illustrations": PROJECT_ROOT / "illustrations",
    "logos": PROJECT_ROOT / "logos",
    "photos": PROJECT_ROOT / "photos",
    "tokens": PROJECT_ROOT / "tokens",
}

# Token configuration
TOKEN_CONFIG = {
    "prefixes": {
        "FNT": "Fonts",
        "LOGO": "Logos & Marks",
        "ICON": "Icons",
        "ILLUST": "Illustrations",
        "IMG": "Images & Photos",
        "COLOR": "Colors",
        "TOKEN": "Design Tokens",
    },
    "families": {
        "AIOTIZE": "Aiotize Brand",
        "AIOVERSE": "Aioverse Brand",
        "SYSTEM": "System",
        "CUSTOM": "Custom",
    },
    "variants": {
        "PFP": "Profile Picture",
        "MARK": "Mark",
        "WORD": "Wordmark",
        # ... more variants
    },
}

# Supported formats
SUPPORTED_FORMATS = {
    "images": [".png", ".jpg", ".jpeg", ".webp", ".svg", ".gif"],
    "documents": [".md", ".pdf", ".docx", ".txt"],
    "fonts": [".ttf", ".otf", ".woff", ".woff2"],
    "config": [".json", ".yaml", ".yml"],
}

# Storage configuration
STORAGE_CONFIG = {
    "metadata_file": PROJECT_ROOT / "Agent" / "data" / "asset_metadata.json",
    "registry_file": PROJECT_ROOT / "Agent" / "data" / "asset_registry.json",
    "cache_dir": PROJECT_ROOT / "Agent" / ".cache",
}
```

**How to Customize:**
1. Open `Agent/config/settings.py`
2. Modify relevant configuration
3. Save file
4. Restart agent (if running)
5. New settings take effect immediately

---

### 6. **Main API** (`main.py`)

**Purpose:** High-level interface combining all components.

**AssetAgentAPI Class:**

```python
from main import AssetAgentAPI

api = AssetAgentAPI()

# All available methods:
api.import_asset(...)
api.export_asset(...)
api.organize_assets(...)
api.refine_asset(...)
api.validate_asset(...)
api.check_compliance(...)
api.search_assets(...)
api.get_asset_info(...)
api.get_statistics(...)
api.process_command(...)
api.get_available_tools()
api.get_conversation_history()
```

---

## 🎯 How to Use the Agent

### Method 1: Interactive CLI Mode

**Start the Agent:**
```bash
cd Agent
python main.py
```

**You'll see:**
```
✓ Aioverse Asset Manager Agent v1.0.0
✓ Ready for operations

Agent>
```

**Available Commands:**

#### **Basic Commands**
```bash
# Get help
Agent> help

# Show statistics
Agent> stats

# Exit
Agent> exit
Agent> quit
```

#### **Organization**
```bash
Agent> organize assets by category
Agent> organize assets by family
Agent> organize assets by status
```

#### **Search**
```bash
Agent> search for LOGO assets
Agent> find AIOTIZE assets
Agent> search ICON
```

#### **Information**
```bash
Agent> get information about LOGO-AIOTIZE-PFP001
Agent> show details of ICON-SYSTEM-NAV001
Agent> get metadata for TOKEN
```

#### **Validation**
```bash
Agent> validate LOGO-AIOTIZE-PFP001
Agent> check compliance of ICON-SYSTEM-NAV001
```

#### **Natural Language Examples**
```bash
Agent> show me all assets
Agent> find all logos organized by category
Agent> get collection statistics
Agent> search for profile picture assets
Agent> display assets grouped by family
Agent> check asset compliance
```

**Output Example:**
```
Agent> organize assets by category

Result: {
  'success': True,
  'method': 'by_category',
  'organization': {
    'LOGO': [
      {'token': 'LOGO-AIOTIZE-PFP001', 'name': 'LOGO_AIOTIZE_PFP001.png'},
      ...
    ],
    'ICON': [...],
    ...
  },
  'total_assets': 25
}
```

---

### Method 2: Python API

**Import and Use:**
```python
from Agent.main import AssetAgentAPI

# Initialize
api = AssetAgentAPI()

# All operations are available
stats = api.get_statistics()
logos = api.search_assets("LOGO", search_type="category")
info = api.get_asset_info("LOGO-AIOTIZE-PFP001")
```

**Complete Example:**
```python
from Agent.main import AssetAgentAPI

def manage_assets():
    api = AssetAgentAPI()
    
    # 1. Get statistics
    stats = api.get_statistics()
    print(f"Total assets: {stats['total_assets']}")
    
    # 2. Import new asset
    result = api.import_asset(
        file_path="/path/to/new_logo.svg",
        token="LOGO-AIOTIZE-PFP002",
        category="LOGO",
        family="AIOTIZE",
        variant="PFP",
        tags=["brand", "profile"],
        description="Updated logo"
    )
    print(f"Import result: {result['success']}")
    
    # 3. Validate it
    validation = api.validate_asset("LOGO-AIOTIZE-PFP002")
    print(f"Valid: {validation['compliant']}")
    
    # 4. Check compliance
    compliance = api.check_compliance("LOGO-AIOTIZE-PFP002")
    print(f"Compliant: {compliance['compliant']}")
    
    # 5. Organize
    organized = api.organize_assets("by_category")
    print(f"Categories: {list(organized['organization'].keys())}")
    
    # 6. Export
    export = api.export_asset(
        token="LOGO-AIOTIZE-PFP002",
        export_path="./exports"
    )
    print(f"Exported to: {export['exported_file']}")
    
    # 7. Search
    logos = api.search_assets("LOGO", search_type="category")
    print(f"Found {len(logos)} logos")

if __name__ == "__main__":
    manage_assets()
```

---

### Method 3: Using Examples

**Run Pre-built Examples:**
```bash
python Agent/examples/usage_examples.py
```

**Includes:**
1. Basic operations
2. Validation & compliance
3. Direct API usage
4. Workflow scenarios
5. Interactive mode

---

## 🔄 How to Update the Repository

### 1. **Adding New Asset Types**

**Step 1: Update Configuration**
```python
# Edit: Agent/config/settings.py

TOKEN_CONFIG = {
    "prefixes": {
        # ... existing ...
        "VIDEO": "Videos",  # NEW
    },
    "families": {
        # ... existing ...
        "PARTNER": "Partner Brand",  # NEW
    },
    "variants": {
        # ... existing ...
        "PROMO": "Promotional",  # NEW
    },
}

SUPPORTED_FORMATS = {
    # ... existing ...
    "videos": [".mp4", ".mov", ".webm"],  # NEW
}
```

**Step 2: Test the Change**
```python
from utils import TokenGenerator

# Verify new token works
token = TokenGenerator.generate_token(
    prefix="VIDEO",
    family="PARTNER",
    variant="PROMO",
    sequence_number=1
)
print(token)  # VIDEO-PARTNER-PROMO001
```

---

### 2. **Adding New Validation Rules**

**Update: `Agent/utils/validators.py`**

```python
class ComplianceChecker:
    # Add new rule
    COMPLIANCE_RULES = {
        # ... existing ...
        "custom_rule": "Your custom rule description",
    }

    @staticmethod
    def check_compliance(metadata: Dict[str, Any]) -> Dict[str, Any]:
        """Enhanced compliance checking"""
        # ... existing code ...
        
        # Add your new check
        if "custom_field" not in metadata:
            warnings.append("Missing custom field")
        
        return {
            "compliant": len(issues) == 0,
            "issues": issues,
            "warnings": warnings,
            "checked_at": datetime.now().isoformat(),
        }
```

---

### 3. **Adding New Operations**

**Step 1: Create Handler**
```python
# Edit: Agent/handlers/operation_handlers.py

class CustomHandler:
    """Handler for custom operations"""
    
    def __init__(self, asset_manager: AssetManager):
        self.asset_manager = asset_manager
        self.logger = logging.getLogger(__name__)
    
    def handle_custom(self, **kwargs) -> Dict[str, Any]:
        """Handle custom operation"""
        try:
            # Your operation logic
            return {"success": True, "result": "..."}
        except Exception as e:
            return {"success": False, "error": str(e)}
```

**Step 2: Register in Dispatcher**
```python
class OperationDispatcher:
    def __init__(self, asset_manager: AssetManager):
        # ... existing ...
        self.custom_handler = CustomHandler(asset_manager)
    
    def execute(self, operation: str, **kwargs) -> Dict[str, Any]:
        # ... existing conditions ...
        elif operation == "custom":
            return self.custom_handler.handle_custom(**kwargs)
```

**Step 3: Add to AI Agent**
```python
# Edit: Agent/core/ai_agent.py

def _initialize_tools(self) -> Dict[str, Callable]:
    return {
        # ... existing ...
        "custom_operation": self.asset_manager.custom_operation,
    }

def _analyze_intent(self, user_input: str) -> str:
    # ... existing code ...
    intent_keywords = {
        # ... existing ...
        "custom": ["custom", "do_something", ...],
    }
```

---

### 4. **Extending Metadata Schema**

**Update: `Agent/config/settings.py`**

```python
METADATA_SCHEMA = {
    # ... existing fields ...
    "custom_field": str,  # NEW
    "custom_list": list,  # NEW
    "custom_dict": dict,  # NEW
}
```

**Update: AssetManager to use new fields**
```python
# Edit: Agent/core/asset_manager.py

def import_asset(self, ..., metadata=None):
    asset_metadata = {
        # ... existing ...
        "custom_field": metadata.get("custom_field", "") if metadata else "",
    }
    # ...
```

---

### 5. **Version Control (Git)**

**Track Changes:**
```bash
# Check status
git status

# View changes
git diff

# Stage changes
git add Agent/

# Commit
git commit -m "feat: Add new asset type VIDEO"

# Push
git push origin main
```

**Best Practices:**
- Create feature branches for major changes
- Write descriptive commit messages
- Test before committing
- Update documentation

---

### 6. **Backing Up Before Updates**

```bash
# Create backup
cp -r Agent Agent.backup

# Or zip entire Agent folder
zip -r Agent_backup_2025-02-02.zip Agent/

# Store backup safely
mv Agent_backup_2025-02-02.zip backups/
```

---

## 📤 How to Export Components

### 1. **Export Entire Agent Folder**

**Using Python:**
```python
import shutil
import os

# Create archive
shutil.make_archive(
    base_name="Aioverse_Agent_full",
    format="zip",
    root_dir=os.path.dirname(os.path.abspath("Agent")),
    base_dir="Agent"
)

print("Created: Aioverse_Agent_full.zip")
```

**Using Command Line:**
```bash
# Windows
powershell -Command "Compress-Archive -Path .\Agent -DestinationPath Aioverse_Agent_full.zip"

# Linux/Mac
zip -r Aioverse_Agent_full.zip Agent/
```

---

### 2. **Export Specific Components**

**Export Only Code:**
```bash
# Create new folder
mkdir Agent_code_only

# Copy only Python files
cp Agent/*.py Agent_code_only/
cp -r Agent/core Agent_code_only/
cp -r Agent/handlers Agent_code_only/
cp -r Agent/utils Agent_code_only/
cp -r Agent/config Agent_code_only/

# Zip it
zip -r Agent_code.zip Agent_code_only/
```

**Export Only Documentation:**
```bash
mkdir Agent_docs_only
cp Agent/*.md Agent_docs_only/
zip -r Agent_docs.zip Agent_docs_only/
```

**Export Only Examples:**
```bash
mkdir Agent_examples_only
cp -r Agent/examples Agent_examples_only/
cp Agent/main.py Agent_examples_only/
zip -r Agent_examples.zip Agent_examples_only/
```

---

### 3. **Export Assets with Metadata**

**Export Single Asset:**
```python
from main import AssetAgentAPI

api = AssetAgentAPI()

result = api.export_asset(
    token="LOGO-AIOTIZE-PFP001",
    export_path="./exports/logo",
    include_metadata=True
)

print(f"Exported to: {result['exported_file']}")
print(f"Metadata: {result['metadata_file']}")
```

**Export Multiple Assets:**
```python
from main import AssetAgentAPI

api = AssetAgentAPI()

# Find all logos
logos = api.search_assets("LOGO", search_type="category")

# Export each
for asset in logos:
    api.export_asset(
        token=asset['token'],
        export_path=f"./exports/{asset['token']}",
        include_metadata=True
    )
    print(f"Exported: {asset['token']}")
```

---

### 4. **Export Configuration**

**Backup Current Configuration:**
```python
import json
from pathlib import Path
from config import (
    TOKEN_CONFIG,
    SUPPORTED_FORMATS,
    ASSET_PATHS,
    METADATA_SCHEMA,
)

# Create backup
config_backup = {
    "TOKEN_CONFIG": TOKEN_CONFIG,
    "SUPPORTED_FORMATS": SUPPORTED_FORMATS,
    "ASSET_PATHS": {k: str(v) for k, v in ASSET_PATHS.items()},
    "METADATA_SCHEMA": {k: str(v) for k, v in METADATA_SCHEMA.items()},
}

# Save
with open("config_backup.json", "w") as f:
    json.dump(config_backup, f, indent=2)

print("Configuration backed up to: config_backup.json")
```

---

### 5. **Export Asset Metadata**

**Export All Metadata:**
```python
import json
from pathlib import Path

# Read metadata file
metadata_file = Path("Agent/data/asset_metadata.json")

if metadata_file.exists():
    with open(metadata_file, "r") as f:
        all_metadata = json.load(f)
    
    # Export to CSV for analysis
    import csv
    
    with open("assets_metadata.csv", "w", newline="") as f:
        if all_metadata:
            fieldnames = list(all_metadata[list(all_metadata.keys())[0]].keys())
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            
            for token, metadata in all_metadata.items():
                metadata['token'] = token
                writer.writerow(metadata)
    
    print(f"Exported {len(all_metadata)} assets to: assets_metadata.csv")
```

---

### 6. **Export Statistics Report**

```python
from main import AssetAgentAPI
import json
from datetime import datetime

api = AssetAgentAPI()

# Get all data
stats = api.get_statistics()

# Create report
report = {
    "generated_at": datetime.now().isoformat(),
    "statistics": stats,
    "total_categories": len(stats.get('by_category', {})),
    "total_families": len(stats.get('by_family', {})),
}

# Save report
with open("asset_report.json", "w") as f:
    json.dump(report, f, indent=2)

print("Report saved to: asset_report.json")
```

---

### 7. **Create Portable Version**

**Create Self-Contained Package:**
```python
import shutil
import os
from pathlib import Path

# Create package directory
pkg_dir = Path("Aioverse_Agent_portable")
pkg_dir.mkdir(exist_ok=True)

# Copy core files
for item in ["config", "core", "handlers", "utils", "main.py"]:
    src = Path(f"Agent/{item}")
    dst = pkg_dir / item
    if src.is_dir():
        shutil.copytree(src, dst)
    else:
        shutil.copy2(src, dst)

# Copy documentation
for doc in ["README.md", "QUICKREF.md", "requirements.txt"]:
    shutil.copy2(f"Agent/{doc}", pkg_dir / doc)

# Create README for package
readme = """# Aioverse Asset Agent - Portable Version

## Usage

1. Extract this folder
2. Install dependencies: pip install -r requirements.txt
3. Run: python main.py

Or use as Python library:
    from main import AssetAgentAPI
    api = AssetAgentAPI()
"""

(pkg_dir / "README_PORTABLE.txt").write_text(readme)

# Create archive
shutil.make_archive(
    "Aioverse_Agent_portable",
    "zip",
    pkg_dir.parent,
    pkg_dir.name
)

print("Portable version created: Aioverse_Agent_portable.zip")
shutil.rmtree(pkg_dir)
```

---

## 📋 Comprehensive Operation Guide

### Basic Workflow

#### **Workflow 1: Import → Validate → Export**

```python
from main import AssetAgentAPI

api = AssetAgentAPI()

# Step 1: Import asset
print("1. Importing asset...")
import_result = api.import_asset(
    file_path="/design/new_logo.svg",
    token="LOGO-AIOTIZE-PFP002",
    category="LOGO",
    family="AIOTIZE",
    variant="PFP",
    tags=["brand", "new"],
    description="New brand logo"
)

if not import_result['success']:
    print(f"Import failed: {import_result['error']}")
    exit(1)

print(f"✓ Asset imported: {import_result['token']}")

# Step 2: Validate asset
print("\n2. Validating asset...")
validation = api.validate_asset(import_result['token'])

if validation['compliant']:
    print("✓ Asset is compliant")
else:
    print(f"✗ Issues found: {validation['issues']}")

# Step 3: Check compliance
print("\n3. Checking compliance...")
compliance = api.check_compliance(import_result['token'])

if compliance['compliant']:
    print("✓ Asset meets all standards")
else:
    print(f"⚠ Warnings: {compliance['warnings']}")

# Step 4: Export asset
print("\n4. Exporting asset...")
export_result = api.export_asset(
    token=import_result['token'],
    export_path="./exports",
    include_metadata=True
)

print(f"✓ Exported to: {export_result['exported_file']}")
```

---

#### **Workflow 2: Search → Organize → Refine**

```python
from main import AssetAgentAPI

api = AssetAgentAPI()

# Step 1: Find assets
print("1. Searching for assets...")
results = api.search_assets("AIOTIZE", search_type="family")
print(f"Found {len(results)} AIOTIZE assets")

# Step 2: Organize
print("\n2. Organizing assets...")
organized = api.organize_assets("by_category")

for category, assets in organized['organization'].items():
    print(f"  {category}: {len(assets)} assets")

# Step 3: Refine each asset
print("\n3. Refining assets...")
for asset in results:
    token = asset['token']
    print(f"\n  Refining {token}...")
    
    # Optimize quality
    result = api.refine_asset(
        token=token,
        refinement_type="optimize",
        quality=95,
        format="webp"
    )
    
    if result['success']:
        print(f"    ✓ Optimized")
    else:
        print(f"    ✗ Failed: {result['error']}")
```

---

#### **Workflow 3: Audit → Report → Backup**

```python
from main import AssetAgentAPI
import json
from datetime import datetime

api = AssetAgentAPI()

# Step 1: Get statistics
print("1. Collecting statistics...")
stats = api.get_statistics()
print(f"Total assets: {stats['total_assets']}")
print(f"Total size: {stats['total_size_mb']} MB")

# Step 2: Validate all assets
print("\n2. Validating all assets...")
search_results = api.search_assets("", search_type="token")
issues_found = 0

for asset in search_results:
    validation = api.validate_asset(asset['token'])
    if not validation['compliant']:
        issues_found += 1
        print(f"  ✗ {asset['token']}: {validation['issues']}")

print(f"Total issues: {issues_found}")

# Step 3: Generate report
print("\n3. Generating audit report...")
report = {
    "timestamp": datetime.now().isoformat(),
    "total_assets": stats['total_assets'],
    "by_category": stats['by_category'],
    "by_family": stats['by_family'],
    "total_size_mb": stats['total_size_mb'],
    "issues_found": issues_found,
}

# Step 4: Save report
with open(f"audit_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json", "w") as f:
    json.dump(report, f, indent=2)

print("✓ Audit report saved")

# Step 5: Backup metadata
print("\n4. Backing up metadata...")
info = api.get_asset_info("LOGO-AIOTIZE-PFP001")  # Example
backup_file = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

with open(backup_file, "w") as f:
    json.dump(search_results, f, indent=2, default=str)

print(f"✓ Backup saved to: {backup_file}")
```

---

### Advanced Operations

#### **Batch Import Multiple Assets**

```python
from main import AssetAgentAPI
from pathlib import Path

api = AssetAgentAPI()

# Batch import from directory
assets_dir = Path("/designs/logos")

for i, file_path in enumerate(assets_dir.glob("*.png"), 1):
    token = f"LOGO-AIOTIZE-{file_path.stem.upper()}{i:03d}"
    
    print(f"Importing {file_path.name}...")
    
    result = api.import_asset(
        file_path=str(file_path),
        token=token,
        category="LOGO",
        family="AIOTIZE",
        variant="PFP",
        tags=["imported", "batch"]
    )
    
    if result['success']:
        print(f"  ✓ {token}")
    else:
        print(f"  ✗ Failed: {result['error']}")
```

---

#### **Export Assets by Criteria**

```python
from main import AssetAgentAPI
from pathlib import Path

api = AssetAgentAPI()

# Export all AIOTIZE assets
print("Exporting all AIOTIZE assets...")
assets = api.search_assets("AIOTIZE", search_type="family")

export_dir = Path("./exports/aiotize")
export_dir.mkdir(parents=True, exist_ok=True)

for asset in assets:
    result = api.export_asset(
        token=asset['token'],
        export_path=str(export_dir / asset['token']),
        include_metadata=True
    )
    
    if result['success']:
        print(f"✓ {asset['token']}")
    else:
        print(f"✗ {asset['token']}: {result['error']}")

print(f"\nExported {len(assets)} assets to: {export_dir}")
```

---

## ❓ FAQ & Common Queries

### **Q1: How do I import an asset?**

**A:** Use the import_asset method:
```python
api.import_asset(
    file_path="/path/to/asset.png",
    token="LOGO-AIOTIZE-PFP001",
    category="LOGO",
    family="AIOTIZE",
    variant="PFP"
)
```

---

### **Q2: What's the correct token format?**

**A:** Format is `PREFIX-FAMILY-VARIANT###`
- PREFIX: FNT, LOGO, ICON, ILLUST, IMG, COLOR, TOKEN
- FAMILY: AIOTIZE, AIOVERSE, SYSTEM, CUSTOM
- VARIANT: PFP, MARK, WORD, etc.
- ###: 001-999 (sequential)

Example: `LOGO-AIOTIZE-PFP001`

---

### **Q3: How do I search for assets?**

**A:** Use search_assets with different search types:
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

---

### **Q4: Can I customize the token format?**

**A:** Yes, edit `Agent/config/settings.py`:
```python
TOKEN_CONFIG = {
    "prefixes": {
        "CUSTOM": "Custom Type",
    },
    "families": {
        "MYCOMPANY": "My Company",
    },
}
```

---

### **Q5: How do I validate if an asset is compliant?**

**A:** Use validate_asset or check_compliance:
```python
# Validate compliance
validation = api.validate_asset("LOGO-AIOTIZE-PFP001")
if validation['compliant']:
    print("✓ Compliant")
else:
    print(f"Issues: {validation['issues']}")

# Check specific standards
compliance = api.check_compliance("LOGO-AIOTIZE-PFP001")
print(f"Standards met: {compliance['compliant']}")
```

---

### **Q6: How do I export multiple assets?**

**A:** Loop through search results:
```python
results = api.search_assets("LOGO", search_type="category")

for asset in results:
    api.export_asset(
        token=asset['token'],
        export_path="./exports"
    )
```

---

### **Q7: Can I modify metadata?**

**A:** Not directly through API, but you can:
1. Export asset with metadata
2. Edit the JSON metadata file
3. Re-import with updated info

---

### **Q8: How do I get statistics?**

**A:** Use get_statistics:
```python
stats = api.get_statistics()
print(stats['total_assets'])
print(stats['by_category'])
print(stats['total_size_mb'])
```

---

### **Q9: Can I add custom asset types?**

**A:** Yes, update config/settings.py:
```python
TOKEN_CONFIG = {
    "prefixes": {
        "VIDEO": "Videos",  # NEW
    },
}
```

---

### **Q10: How do I backup my data?**

**A:** Copy the data folder:
```bash
cp -r Agent/data Agent/data.backup
```

Or use the backup workflow provided in the guide.

---

### **Q11: What if an import fails?**

**A:** Check:
1. File exists at path
2. Token format is valid
3. File format is supported
4. File size is within limits
5. Required metadata is provided

---

### **Q12: How do I clear conversation history?**

**A:** Use the API:
```python
api.ai_agent.clear_conversation_history()
```

---

### **Q13: Can I use this without Python?**

**A:** Yes, use the interactive CLI:
```bash
python Agent/main.py
```

Type commands naturally.

---

### **Q14: How often should I back up?**

**A:** Recommendations:
- After major imports (weekly)
- Before system updates
- Before configuration changes
- Before trying new features

---

### **Q15: Where is asset data stored?**

**A:** In JSON files:
- `Agent/data/asset_metadata.json` - Asset metadata
- `Agent/data/asset_registry.json` - Asset registry
- `Agent/logs/agent.log` - Operation logs

---

## 🔧 Troubleshooting

### **Issue: "Token validation failed"**

**Cause:** Invalid token format

**Solution:**
```python
from utils import TokenGenerator

# Check format
valid, error = TokenGenerator.validate_token("YOUR-TOKEN")
print(error)

# Generate correct token
token = TokenGenerator.generate_token(
    prefix="LOGO",
    family="AIOTIZE",
    variant="PFP",
    sequence_number=1
)
```

---

### **Issue: "File not found"**

**Cause:** File path doesn't exist

**Solution:**
```python
from pathlib import Path

# Verify path exists
file_path = "/path/to/asset.png"
if Path(file_path).exists():
    print("File found")
else:
    print(f"File not found: {file_path}")
    print(f"Current dir: {Path.cwd()}")
```

---

### **Issue: "File format not supported"**

**Cause:** File extension not in supported list

**Solution:**
```python
# Check supported formats
from config import SUPPORTED_FORMATS

print(SUPPORTED_FORMATS['images'])  # Check if your format is listed

# Add new format if needed (edit config/settings.py)
SUPPORTED_FORMATS = {
    "images": [".png", ".jpg", ".svg", ".custom"],  # Add here
}
```

---

### **Issue: "Storage files corrupted"**

**Cause:** JSON files were manually edited incorrectly

**Solution:**
```bash
# Restore from backup
cp Agent/data.backup/* Agent/data/

# Or start fresh
rm Agent/data/*.json
# Agent will recreate them on next run
```

---

### **Issue: "No module named 'config'"**

**Cause:** Running from wrong directory

**Solution:**
```bash
# Make sure you're in Agent directory
cd Agent

# Run from Agent directory
python main.py
```

---

### **Issue: "Agent not responding"**

**Cause:** Agent is waiting for input or stuck

**Solution:**
```bash
# Press Ctrl+C to interrupt
# Restart agent
python main.py
```

---

## 🚀 Advanced Topics

### **Custom Handler Implementation**

```python
# 1. Create handler class
class ArchiveHandler:
    def __init__(self, asset_manager):
        self.asset_manager = asset_manager
    
    def archive_assets(self, tokens):
        """Archive multiple assets"""
        results = {}
        for token in tokens:
            try:
                # Get asset
                info = self.asset_manager.get_asset_info(token)
                # Mark as archived
                info['metadata']['status'] = 'archived'
                results[token] = {'archived': True}
            except Exception as e:
                results[token] = {'error': str(e)}
        return results

# 2. Register in dispatcher
dispatcher.archive_handler = ArchiveHandler(asset_manager)

# 3. Use via dispatcher
result = dispatcher.execute("archive", tokens=[...])
```

---

### **Integrating with External Services**

```python
import requests

class CloudExportHandler:
    """Export assets to cloud storage"""
    
    def __init__(self, asset_manager, api_key):
        self.asset_manager = asset_manager
        self.api_key = api_key
        self.api_url = "https://api.example.com/upload"
    
    def export_to_cloud(self, token):
        """Export asset to cloud"""
        info = self.asset_manager.get_asset_info(token)
        metadata = info['metadata']
        
        # Upload to cloud
        response = requests.post(
            self.api_url,
            json=metadata,
            headers={"Authorization": f"Bearer {self.api_key}"}
        )
        
        return response.json()
```

---

### **Performance Optimization**

```python
# 1. Cache search results
cache = {}

def cached_search(query, search_type):
    key = f"{query}_{search_type}"
    if key not in cache:
        cache[key] = api.search_assets(query, search_type)
    return cache[key]

# 2. Batch operations
def batch_export(tokens, export_path):
    for token in tokens:
        api.export_asset(token, export_path)

# 3. Lazy loading
class LazyAssetLoader:
    def __init__(self):
        self._assets = None
    
    @property
    def assets(self):
        if self._assets is None:
            self._assets = api.get_statistics()
        return self._assets
```

---

## ✅ Best Practices

### **1. Always Validate Before Import**

```python
# Check file before import
from utils import FileValidator

file_path = "/path/to/asset.png"

# Validate format
valid, error = FileValidator.validate_file_format(file_path, "LOGO")
if not valid:
    print(f"Invalid format: {error}")
    exit(1)

# Validate size
valid, error = FileValidator.validate_file_size(file_path, max_size_mb=100)
if not valid:
    print(f"File too large: {error}")
    exit(1)

# Then import
api.import_asset(...)
```

---

### **2. Use Meaningful Tokens**

```python
# ✓ GOOD
token = "LOGO-AIOTIZE-PFP001"
token = "ICON-SYSTEM-NAV002"
token = "FONT-AIOVERSE-HEAD001"

# ✗ BAD
token = "LOGO-TEST-ABC123"  # Invalid family/variant
token = "LOGO-AIOTIZE-1"     # Incomplete variant
```

---

### **3. Document Your Assets**

```python
# Add comprehensive metadata
api.import_asset(
    file_path="/path/to/asset.png",
    token="LOGO-AIOTIZE-PFP001",
    category="LOGO",
    family="AIOTIZE",
    variant="PFP",
    tags=["social", "profile", "primary"],  # Meaningful tags
    description="Main profile picture for Aiotize brand",  # Clear description
    usage_rights="Exclusive brand use"  # Define usage
)
```

---

### **4. Regular Backups**

```python
import shutil
from datetime import datetime

def backup_assets():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    shutil.copytree(
        "Agent/data",
        f"backups/data_{timestamp}"
    )
    print(f"Backup created: data_{timestamp}")

# Run weekly
backup_assets()
```

---

### **5. Monitor & Audit**

```python
# Regular compliance checks
stats = api.get_statistics()
print(f"Total assets: {stats['total_assets']}")

# Validate all assets
all_assets = api.search_assets("", search_type="token")
issues = 0

for asset in all_assets:
    validation = api.validate_asset(asset['token'])
    if not validation['compliant']:
        issues += 1
        print(f"Issue: {asset['token']}")

print(f"Total issues: {issues}")
```

---

### **6. Version Control**

```bash
# Track changes
git add Agent/
git commit -m "feat: Add new logo asset LOGO-AIOTIZE-PFP002"
git push origin main

# Tag releases
git tag -a v1.0.0 -m "Initial release"
git push origin v1.0.0
```

---

### **7. Error Handling**

```python
from main import AssetAgentAPI

try:
    api = AssetAgentAPI()
    
    # Try operation
    result = api.import_asset(...)
    
    if not result['success']:
        print(f"Operation failed: {result['error']}")
        # Handle gracefully
    else:
        print(f"Success: {result}")

except Exception as e:
    print(f"Unexpected error: {e}")
    # Log error
    # Notify admin
```

---

### **8. Documentation**

```python
"""
Asset Management Workflow

Step 1: Import asset
  - Validate file
  - Generate token
  - Add metadata

Step 2: Verify
  - Check compliance
  - Validate format
  - Test export

Step 3: Organize
  - Categorize
  - Tag appropriately
  - Update metadata

Step 4: Archive
  - Export backup
  - Update version
  - Document changes
"""
```

---

## 🎓 Conclusion

This guide covers:
- ✅ Complete system architecture
- ✅ All components in detail
- ✅ How to use all features
- ✅ How to update and extend
- ✅ How to export components
- ✅ Comprehensive operations
- ✅ FAQ & troubleshooting
- ✅ Advanced topics
- ✅ Best practices

### **Next Steps:**

1. **Review Architecture** - Understand system design
2. **Try Examples** - Run provided examples
3. **Read API Docs** - Study method signatures
4. **Implement Workflows** - Build your processes
5. **Monitor & Optimize** - Track and improve

### **Resources:**

- 📖 [README.md](README.md) - Feature documentation
- 🚀 [QUICKREF.md](QUICKREF.md) - API quick reference
- 📝 [examples/](examples/) - Working code examples
- ⚙️ [config/settings.py](config/settings.py) - Configuration
- 💻 [main.py](main.py) - Main API

---

**Version:** 1.0.0  
**Last Updated:** February 2, 2026  
**Status:** Production Ready  
**Maintained By:** Aioverse Development Team
