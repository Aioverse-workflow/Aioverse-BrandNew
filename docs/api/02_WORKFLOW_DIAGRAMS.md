# 📊 WORKFLOW DIAGRAMS & VISUAL ARCHITECTURE

**Version:** 1.0.0  
**Last Updated:** February 2, 2026

---

## 📋 Table of Contents

1. [System Architecture Overview](#system-architecture-overview)
2. [Data Flow Diagrams](#data-flow-diagrams)
3. [Component Interaction Diagrams](#component-interaction-diagrams)
4. [Operation Workflows](#operation-workflows)
5. [API Architecture](#api-architecture)
6. [Token System Flow](#token-system-flow)
7. [Metadata Structure](#metadata-structure)
8. [Deployment Pipeline](#deployment-pipeline)

---

## 🏗️ System Architecture Overview

### Complete System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                      AIOVERSE ASSET AGENT SYSTEM                    │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  ┌──────────────────┐    ┌──────────────────┐   ┌─────────────────┐ │
│  │   USER INTERFACES│    │  DATA STORAGE    │   │  EXTERNAL SYSTEMS
│  ├──────────────────┤    ├──────────────────┤   ├─────────────────┤ │
│  │ • CLI (main.py)  │    │ • JSON Metadata  │   │ • Cloud Storage │
│  │ • REST API       │    │ • Asset Registry │   │ • Version Control
│  │ • Natural Lang   │    │ • Cache Files    │   │ • Monitoring    │
│  │ • Python API     │    │ • Logs           │   │ • Webhooks      │
│  └──────────────────┘    └──────────────────┘   └─────────────────┘
│         │                        │                        │
│         └────────────┬───────────┴────────────┬──────────┘
│                      │                        │
│              ┌───────▼────────────────────────▼────────┐
│              │   INTELLIGENCE LAYER                    │
│              ├────────────────────────────────────────┤
│              │ • AIAssetAgent (NLP Intent Detection)  │
│              │ • OperationDispatcher (Routing)        │
│              │ • Conversation Management              │
│              └───────┬────────────────────────────────┘
│                      │
│              ┌───────▼────────────────────────────────┐
│              │   CORE PROCESSING LAYER                │
│              ├────────────────────────────────────────┤
│              │ • AssetManager (Operations Orchestration
│              │ • Import/Export Handlers               │
│              │ • Organize/Refine Handlers             │
│              │ • Validation Handlers                  │
│              └───────┬────────────────────────────────┘
│                      │
│              ┌───────▼────────────────────────────────┐
│              │   VALIDATION & UTILITIES LAYER         │
│              ├────────────────────────────────────────┤
│              │ • Token Generation & Validation        │
│              │ • File Validation (Format/Size)        │
│              │ • Metadata Validation                  │
│              │ • Compliance Checking                  │
│              │ • File Hashing (SHA256)                │
│              └───────┬────────────────────────────────┘
│                      │
│              ┌───────▼────────────────────────────────┐
│              │   PERSISTENCE LAYER                    │
│              ├────────────────────────────────────────┤
│              │ • JSON File Storage                    │
│              │ • File System Operations               │
│              │ • Logging System                       │
│              └────────────────────────────────────────┘
│
└─────────────────────────────────────────────────────────────────────┘

       CONFIGURATION & SETTINGS
       ├── Token Configuration (Prefixes, Families, Variants)
       ├── Asset Paths (Directory Mappings)
       ├── Supported Formats
       ├── Metadata Schema
       ├── Storage Configuration
       └── Logging Configuration
```

---

## 🔄 Data Flow Diagrams

### Import Asset Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                        IMPORT ASSET WORKFLOW                         │
└─────────────────────────────────────────────────────────────────────┘

USER PROVIDES:
  ├─ File Path: /path/to/asset.png
  ├─ Category: Logos
  ├─ Family: AIOTIZE
  ├─ Tags: [primary, official]
  └─ Description: "Main brand logo"

        ▼

VALIDATION STAGE:
  ├─ ✓ File exists?
  ├─ ✓ Format supported? (.png, .jpg, .svg...)
  ├─ ✓ File size within limits? (< 100MB)
  ├─ ✓ File integrity valid? (calculate SHA256)
  └─ ✓ Metadata complete?

        ▼

TOKEN GENERATION:
  ├─ Prefix: LOGO (from category)
  ├─ Family: AIOTIZE (from user input)
  ├─ Variant: PFP (from file analysis)
  ├─ Sequence: 001 (auto-increment)
  └─ Final Token: LOGO-AIOTIZE-PFP001

        ▼

METADATA CREATION:
  ├─ Token: LOGO-AIOTIZE-PFP001
  ├─ Original Name: asset.png
  ├─ Standardized Name: LOGO-AIOTIZE-PFP001.png
  ├─ Category: Logos
  ├─ Family: AIOTIZE
  ├─ Variant: PFP
  ├─ File Size: 245612 bytes
  ├─ Created Date: 2024-02-02T10:00:00
  ├─ Tags: [primary, official]
  └─ Integrity Hash: sha256:abc123...

        ▼

STORAGE:
  ├─ Save Metadata → Agent/data/asset_metadata.json
  ├─ Update Registry → Agent/data/asset_registry.json
  ├─ Create Log Entry → logs/agent.log
  └─ Copy Asset (Optional) → ASSET_PATHS[category]/LOGO-AIOTIZE-PFP001.png

        ▼

RESPONSE:
  ├─ Token: LOGO-AIOTIZE-PFP001
  ├─ Status: Success
  ├─ Message: "Asset imported successfully"
  └─ Metadata: {...}
```

### Search & Tag Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                   SEARCH & TAG QUERY WORKFLOW                        │
└─────────────────────────────────────────────────────────────────────┘

SEARCH REQUEST:
  ├─ Query: "official"
  ├─ Type: "tag"
  └─ Filters: (optional)

        ▼

LOAD METADATA:
  Load Agent/data/asset_metadata.json into memory

        ▼

SEARCH EXECUTION:
  For each asset in metadata:
  ├─ Extract tags: ["primary", "official", "marketing"]
  ├─ Check if "official" in tags? ✓ YES
  └─ Add to results

        ▼

RESULTS COLLECTION:
  ├─ Result 1: LOGO-AIOTIZE-PFP001
  ├─ Result 2: ICON-AIOVERSE-UI001
  ├─ Result 3: COLOR-AIOTIZE-BRAND001
  └─ Total: 3 matches

        ▼

RESPONSE:
  ├─ Query: "official"
  ├─ Type: "tag"
  ├─ Total Results: 3
  └─ Results: [
       {
         token: "LOGO-AIOTIZE-PFP001",
         name: "LOGO-AIOTIZE-PFP001.png",
         tags: ["primary", "official", "marketing"]
       },
       ...
     ]
```

### Export Asset Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                       EXPORT ASSET WORKFLOW                          │
└─────────────────────────────────────────────────────────────────────┘

EXPORT REQUEST:
  ├─ Token: LOGO-AIOTIZE-PFP001
  └─ Export Path: /backups/exports

        ▼

VALIDATION:
  ├─ ✓ Asset exists? (check metadata)
  ├─ ✓ Export path accessible?
  ├─ ✓ Sufficient disk space?
  └─ ✓ Compliance check passed?

        ▼

RETRIEVE ASSET INFO:
  ├─ Load metadata from asset_metadata.json
  ├─ Load registry from asset_registry.json
  ├─ Verify integrity hash
  └─ Check version compatibility

        ▼

COPY ASSET FILE:
  ├─ Source: Original asset file location
  ├─ Destination: /backups/exports/LOGO-AIOTIZE-PFP001.png
  ├─ Preserve file attributes
  └─ Verify copy integrity

        ▼

EXPORT METADATA:
  ├─ Create: /backups/exports/LOGO-AIOTIZE-PFP001.json
  └─ Contents: {
       token: "LOGO-AIOTIZE-PFP001",
       original_name: "asset.png",
       standardized_name: "LOGO-AIOTIZE-PFP001.png",
       category: "Logos",
       family: "AIOTIZE",
       tags: ["primary", "official"],
       export_date: "2024-02-02T14:22:00",
       integrity_hash: "sha256:abc123..."
     }

        ▼

RESPONSE:
  ├─ Token: LOGO-AIOTIZE-PFP001
  ├─ Exported To: /backups/exports/LOGO-AIOTIZE-PFP001.png
  ├─ File Size: 245612 bytes
  ├─ Metadata Exported: true
  └─ Status: Success
```

---

## 🔌 Component Interaction Diagrams

### REST API to Core Engine

```
┌─────────────────────────────────────────────────────────────────────┐
│              REST API TO CORE ENGINE INTERACTION                     │
└─────────────────────────────────────────────────────────────────────┘

                    HTTP REQUEST
                        │
                        ▼
        ┌───────────────────────────────────┐
        │    REST API HANDLER               │
        │  (api/rest_api.py)                │
        │                                   │
        │  • Parse HTTP request             │
        │  • Validate parameters            │
        │  • Extract JSON body              │
        │  • Add CORS headers               │
        └───────────────┬───────────────────┘
                        │
            ┌───────────┴──────────────┐
            │                          │
            ▼                          ▼
      GET REQUEST              POST REQUEST
      (Read Operations)         (Write Operations)
      • /api/health          • /api/import
      • /api/assets          • /api/export
      • /api/asset           • /api/validate
      • /api/search          • /api/refine
      • /api/tags            • /api/add-tags
      • /api/categories      • /api/remove-tags
      • /api/statistics      • /api/organize
            │                          │
            └───────────────┬──────────┘
                            │
                            ▼
        ┌───────────────────────────────────┐
        │    ASSETAGENAPI CLASS             │
        │  (main.py)                        │
        │                                   │
        │  Creates unified interface        │
        │  Combines:                        │
        │  • AIAssetAgent (NLP)             │
        │  • AssetManager (Operations)      │
        │  • OperationDispatcher (Routing)  │
        └───────────────┬───────────────────┘
                        │
            ┌───────────┴──────────────┐
            │                          │
            ▼                          ▼
    ┌──────────────┐      ┌──────────────────┐
    │  AssetManager│      │OperationDispatcher
    │ (core/)      │      │ (handlers/)       │
    │              │      │                  │
    │ • import     │      │ Routes to        │
    │ • export     │      │ specific handler │
    │ • organize   │      │                  │
    │ • refine     │      └──────────────────┘
    │ • validate   │             │
    │ • search     │             ▼
    │ • get_info   │    ┌───────────────────┐
    │ • stats      │    │ Specific Handler  │
    └──────┬───────┘    │ (handlers/)       │
           │            │                   │
           │            │ • ImportHandler   │
           │            │ • ExportHandler   │
           │            │ • ValidateHandler │
           │            │ • RefineHandler   │
           │            │ • OrganizeHandler │
           │            └──────┬────────────┘
           │                   │
           └───────────┬───────┘
                       │
                       ▼
        ┌───────────────────────────────────┐
        │  VALIDATORS & UTILITIES           │
        │  (utils/)                         │
        │                                   │
        │  • TokenValidator                 │
        │  • FileValidator                  │
        │  • MetadataValidator              │
        │  • ComplianceChecker              │
        └───────────────┬───────────────────┘
                        │
                        ▼
        ┌───────────────────────────────────┐
        │  JSON FILE STORAGE                │
        │                                   │
        │  • asset_metadata.json            │
        │  • asset_registry.json            │
        └───────────────────────────────────┘
                        │
                        ▼
                HTTP RESPONSE
                (JSON)
```

### CLI to Core Engine

```
┌─────────────────────────────────────────────────────────────────────┐
│             CLI (INTERACTIVE MODE) TO CORE ENGINE                    │
└─────────────────────────────────────────────────────────────────────┘

USER INPUT:
"Agent> import /path/to/logo.png"

        ▼

COMMAND PARSING:
├─ Detect command: "import"
├─ Extract parameters: ["/path/to/logo.png"]
└─ Prepare metadata input

        ▼

AIAssetAgent.process_command():
├─ Analyze user intent
├─ Extract parameters
├─ Validate input format
└─ Route to appropriate method

        ▼

AssetAgentAPI.import_asset():
├─ Call AssetManager.import_asset()
├─ Apply operation handlers
├─ Execute validators
└─ Return result

        ▼

FORMAT RESPONSE:
├─ Convert to readable format
├─ Add status emoji (✓/✗)
├─ Display metadata preview
└─ Suggest next actions

        ▼

OUTPUT TO USER:
"✓ Asset imported: LOGO-AIOTIZE-PFP001
 Category: Logos
 Family: AIOTIZE
 Tags: [primary, official]
 File Size: 245.6 KB"

        ▼

WAIT FOR NEXT COMMAND:
"Agent> _"
```

---

## 📊 Operation Workflows

### Complete Import Workflow (Detailed)

```
┌──────────────────────────────────────────────────────────────────────┐
│                   IMPORT OPERATION DETAILED FLOW                      │
└──────────────────────────────────────────────────────────────────────┘

┌────────────────┐
│   USER INPUT   │
│ file_path:     │
│ metadata: {...}│
└────────┬───────┘
         │
         ▼
    ┌─────────────┐
    │ NORMALIZE   │
    │ file_path   │
    └────────┬────┘
             │
         ┌───┴───┐
         │       │
         ▼       ▼
      FILE      FORMAT
      EXISTS?   VALID?
      │         │
      ✓ YES     ✓ PNG/JPG/SVG
      │         │
      └───┬─────┘
          │
          ▼
    ┌────────────────┐
    │ FILE VALIDATION│
    ├────────────────┤
    │ Size: < 100MB? │
    │ Readable?      │
    │ Not corrupted? │
    └────────┬───────┘
             │
             ✓
             │
             ▼
    ┌────────────────┐
    │ HASH CREATION  │
    │ SHA256(file)   │
    └────────┬───────┘
             │
             ▼
    ┌────────────────┐
    │ TOKEN GEN      │
    │ PREFIX         │
    │ + FAMILY       │
    │ + VARIANT      │
    │ + SEQUENCE     │
    └────────┬───────┘
             │
             ▼
    ┌────────────────┐
    │ METADATA BUILD │
    │ token, name,   │
    │ category,      │
    │ family,        │
    │ tags, dates    │
    └────────┬───────┘
             │
             ▼
    ┌────────────────┐
    │ VALIDATION     │
    │ Schema check   │
    │ Type check     │
    │ Value check    │
    └────────┬───────┘
             │
             ✓
             │
             ▼
    ┌────────────────┐
    │ SAVE TO JSON   │
    │ update metadata│
    │ file           │
    └────────┬───────┘
             │
             ▼
    ┌────────────────┐
    │ UPDATE REGISTRY│
    │ record import  │
    │ timestamp      │
    └────────┬───────┘
             │
             ▼
    ┌────────────────┐
    │ LOG OPERATION  │
    │ Log to file    │
    │ Output message │
    └────────┬───────┘
             │
             ▼
    ┌────────────────┐
    │ RETURN RESULT  │
    │ token, status, │
    │ metadata       │
    └────────────────┘
```

### Tag Management Workflow

```
┌──────────────────────────────────────────────────────────────────────┐
│                  TAG MANAGEMENT WORKFLOW                              │
└──────────────────────────────────────────────────────────────────────┘

ADD TAGS:                          REMOVE TAGS:
┌──────────────┐                  ┌──────────────┐
│ REQUEST:     │                  │ REQUEST:     │
│ token        │                  │ token        │
│ tags: [...]  │                  │ tags: [...]  │
└──────┬───────┘                  └──────┬───────┘
       │                                  │
       ├──────────────┬───────────────────┤
       │              │                   │
       ▼              ▼                   ▼
    LOAD          VALIDATE          LOAD
    METADATA      TOKEN EXISTS?     METADATA
       │              │                │
       ├──────────────┤                │
       │ CURRENT TAGS:│                ▼
       │ [primary]    │            GET TAGS:
       │              │            [primary,
       ▼              ▼            official]
    ADD NEW:      EXTRACT TAGS
    EXTEND        TO REMOVE
    ARRAY
       │              │                │
       ▼              ▼                ▼
    [primary,    [official]       [primary]
     official,
     marketing]   UPDATE          UPDATE
                  METADATA        METADATA
       │              │                │
       └──────────────┼────────────────┘
                      │
                      ▼
                   SAVE JSON
                      │
                      ▼
                   LOG CHANGE
                      │
                      ▼
                   RETURN RESULT
                   (new tags list)
```

---

## 🔗 API Architecture

### REST API Endpoint Structure

```
┌─────────────────────────────────────────────────────────────────────┐
│                      REST API ARCHITECTURE                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  HTTP SERVER (Port 8000)                                             │
│  └── BaseHTTPRequestHandler                                          │
│      ├── GET Requests                                                │
│      │   ├── /api/health              → Health Check                │
│      │   ├── /api/statistics          → Get Stats                   │
│      │   ├── /api/assets              → List All Assets             │
│      │   ├── /api/asset?token=X       → Get Asset Info              │
│      │   ├── /api/search?query=X      → Search Assets               │
│      │   ├── /api/tags                → List All Tags               │
│      │   └── /api/categories          → List Categories             │
│      │                                                               │
│      ├── POST Requests                                               │
│      │   ├── /api/import              → Import Asset                │
│      │   ├── /api/export              → Export Asset                │
│      │   ├── /api/validate            → Validate Asset              │
│      │   ├── /api/refine              → Refine Asset                │
│      │   ├── /api/organize            → Organize Assets             │
│      │   ├── /api/add-tags            → Add Tags                    │
│      │   └── /api/remove-tags         → Remove Tags                 │
│      │                                                               │
│      └── OPTIONS Requests                                            │
│          └── CORS Preflight                                          │
│                                                                       │
│  RESPONSE FORMAT:                                                    │
│  {                                                                   │
│    "error": false,                                                   │
│    "status": 200,                                                    │
│    "data": {...},                                                    │
│    "message": "Operation successful"                                 │
│  }                                                                   │
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🏷️ Token System Flow

### Token Generation & Validation

```
┌──────────────────────────────────────────────────────────────────────┐
│                    TOKEN GENERATION FLOW                              │
└──────────────────────────────────────────────────────────────────────┘

INPUT PARAMETERS:
├─ file_path: "/path/to/logo.png"
├─ category: "Logos"
├─ family: "AIOTIZE"
├─ variant: (auto-detect or provided)
└─ sequence: (auto-increment)

        ▼

PREFIX LOOKUP:
├─ Category "Logos" → Prefix "LOGO"
├─ Validate prefix exists in TOKEN_CONFIG
└─ Result: PREFIX = "LOGO"

        ▼

FAMILY VALIDATION:
├─ Family "AIOTIZE" exists?
├─ Validate in TOKEN_CONFIG.families
└─ Result: FAMILY = "AIOTIZE"

        ▼

VARIANT DETECTION:
├─ File analysis or user input
├─ Common variants:
│  ├─ PFP (Profile Picture)
│  ├─ MARK (Mark)
│  ├─ WORD (Wordmark)
│  ├─ ICON (Icon)
│  └─ etc.
└─ Result: VARIANT = "PFP"

        ▼

SEQUENCE GENERATION:
├─ Count existing tokens with same PREFIX-FAMILY-VARIANT
├─ Increment counter: ###
├─ Format with leading zeros
└─ Result: SEQUENCE = "001"

        ▼

TOKEN ASSEMBLY:
├─ Combine: PREFIX-FAMILY-VARIANT###
├─ Check for duplicates
├─ Validate format
└─ Result: TOKEN = "LOGO-AIOTIZE-PFP001"

        ▼

TOKEN VALIDATION:
├─ Format: PREFIX-FAMILY-VARIANT###
├─ Regex: ^[A-Z]+-[A-Z]+-[A-Z]+\d{3}$
├─ Length: Valid?
└─ Result: ✓ VALID TOKEN

        ▼

RETURN TOKEN:
"LOGO-AIOTIZE-PFP001"
```

### Token Parsing

```
TOKEN: LOGO-AIOTIZE-PFP001

        ▼

SPLIT BY "-":
["LOGO", "AIOTIZE", "PFP001"]

        ▼

EXTRACT PARTS:
├─ Prefix: LOGO       (Position 0)
├─ Family: AIOTIZE    (Position 1)
├─ Variant: PFP       (Position 2, without numbers)
└─ Sequence: 001      (Position 2, numbers only)

        ▼

LOOKUP MEANINGS:
├─ LOGO → "Logos & Marks"
├─ AIOTIZE → "Aiotize Brand"
├─ PFP → "Profile Picture"
└─ 001 → "First in sequence"

        ▼

RETURN PARSED DATA:
{
  "token": "LOGO-AIOTIZE-PFP001",
  "prefix": "LOGO",
  "prefix_name": "Logos & Marks",
  "family": "AIOTIZE",
  "family_name": "Aiotize Brand",
  "variant": "PFP",
  "variant_name": "Profile Picture",
  "sequence": 1
}
```

---

## 🗂️ Metadata Structure

### Metadata JSON Schema

```
┌──────────────────────────────────────────────────────────────────────┐
│                   METADATA FILE STRUCTURE                             │
└──────────────────────────────────────────────────────────────────────┘

asset_metadata.json:
{
  "LOGO-AIOTIZE-PFP001": {
    ├─ IDENTIFICATION
    │  ├─ "token": "LOGO-AIOTIZE-PFP001"
    │  ├─ "original_name": "aiotize_profile.png"
    │  ├─ "standardized_name": "LOGO-AIOTIZE-PFP001.png"
    │  └─ "category": "Logos"
    │
    ├─ CLASSIFICATION
    │  ├─ "family": "AIOTIZE"
    │  ├─ "variant": "PFP"
    │  └─ "tags": ["primary", "official", "marketing"]
    │
    ├─ LOCATION & SIZE
    │  ├─ "file_path": "/full/path/to/asset.png"
    │  └─ "file_size": 245612
    │
    ├─ VERSIONING
    │  ├─ "created_date": "2024-01-15T10:30:00"
    │  ├─ "modified_date": "2024-02-01T14:22:00"
    │  └─ "version": "1.2.0"
    │
    ├─ DOCUMENTATION
    │  ├─ "description": "Primary profile picture for Aiotize"
    │  └─ "usage_rights": "Internal & licensed partners"
    │
    ├─ COLOR SPECIFIC (if applicable)
    │  └─ "color_hex": "#FF6B35"
    │
    └─ INTEGRITY
       └─ "integrity_hash": "sha256:abc123def456..."
  },

  "ICON-AIOVERSE-UI001": { ... },
  "COLOR-AIOTIZE-BRAND001": { ... },
  ...
}

asset_registry.json:
{
  "LOGO-AIOTIZE-PFP001": {
    ├─ "import_date": "2024-01-15T10:30:00"
    ├─ "imported_by": "admin"
    ├─ "format": "PNG"
    ├─ "integrity_hash": "sha256:abc123..."
    ├─ "last_accessed": "2024-02-01T15:45:00"
    ├─ "access_count": 42
    └─ "refinements": [
         {
           "date": "2024-02-01T14:22:00",
           "type": "compression",
           "level": "high"
         }
       ]
  },
  ...
}
```

---

## 🚀 Deployment Pipeline

### Full Deployment Pipeline

```
┌──────────────────────────────────────────────────────────────────────┐
│                    DEPLOYMENT PIPELINE                                │
└──────────────────────────────────────────────────────────────────────┘

1. DEVELOPMENT
   ┌───────────────────┐
   │ Write Code        │
   │ Create Tests      │
   │ Fix Bugs          │
   └─────────┬─────────┘
             │
             ▼
2. VERSION CONTROL
   ┌───────────────────┐
   │ Commit to Git     │
   │ Push to GitHub    │
   │ Create PR (if     │
   │ team project)     │
   └─────────┬─────────┘
             │
             ▼
3. TESTING
   ┌───────────────────┐
   │ Run Tests         │
   │ Check Format      │
   │ Lint Code         │
   │ Validate Docs     │
   └─────────┬─────────┘
             │
             ✓ PASS
             │
             ▼
4. BUILD
   ┌───────────────────┐
   │ Update Version    │
   │ Update Changelog  │
   │ Create Tag        │
   │ Build Archives    │
   └─────────┬─────────┘
             │
             ▼
5. DOCKER BUILD
   ┌───────────────────┐
   │ Build Image       │
   │ Tag Image         │
   │ Push to Registry  │
   │ (Docker Hub/ECR)  │
   └─────────┬─────────┘
             │
             ▼
6. DEPLOY OPTIONS
   ┌──────────────────────────────────────────┐
   │                                          │
   ├─ DOCKER           ├─ CLOUD              │
   │ Run Container     │ AWS ECS             │
   │ Docker Compose    │ Google Cloud Run    │
   │                   │ Azure App Service   │
   │                   │                     │
   ├─ STANDALONE       ├─ KUBERNETES        │
   │ Python Direct     │ Deploy Helm Chart   │
   │ EC2/Server        │ Scale Pods          │
   │                   │ Health Checks       │
   │                   │                     │
   └─ LOCAL            └─────────────────────┘
     Activate Venv
     Run main.py
     Run API

             │
             ▼
7. VERIFICATION
   ┌───────────────────┐
   │ Health Checks     │
   │ API Tests         │
   │ Smoke Tests       │
   │ Monitoring Setup  │
   └─────────┬─────────┘
             │
             ✓ PRODUCTION
             │
             ▼
8. MONITORING
   ┌───────────────────┐
   │ Monitor Logs      │
   │ Track Metrics     │
   │ Alert on Errors   │
   │ Update Status     │
   └───────────────────┘
```

---

## 📈 Common Operation Workflows

### Workflow 1: Import → Validate → Tag

```
START
  │
  ├─ Import Asset
  │  └─ Token: LOGO-AIOTIZE-PFP001
  │
  ├─ Validate Asset
  │  ├─ Format: ✓ PNG
  │  ├─ Size: ✓ OK
  │  ├─ Integrity: ✓ Valid
  │  └─ Metadata: ✓ Complete
  │
  ├─ Add Tags
  │  └─ Add: ["official", "featured"]
  │
  └─ END
     Status: ✓ Ready for Use
```

### Workflow 2: Search → Filter → Export

```
START
  │
  ├─ Search by Tag: "official"
  │  └─ Results: 5 assets
  │
  ├─ Filter by Family: "AIOTIZE"
  │  └─ Results: 3 assets
  │
  ├─ Export All Matched
  │  ├─ Export 1: LOGO-AIOTIZE-PFP001
  │  ├─ Export 2: ICON-AIOTIZE-BTN001
  │  └─ Export 3: COLOR-AIOTIZE-PRIMARY001
  │
  └─ END
     Status: ✓ Exported to /backups
```

---

**Version:** 1.0.0  
**Last Updated:** February 2, 2026  
**Status:** ✅ Complete with All Visual Aids
