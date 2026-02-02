"""
Aioverse Asset Agent Configuration Settings
Centralized configuration for the AI asset management agent
"""

import os
from pathlib import Path
from typing import Dict, List

# Project root directory
PROJECT_ROOT = Path(__file__).parent.parent.parent

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
        "ICON": "Icon",
        "BG": "Background",
        "ACCENT": "Accent",
        "PRIMARY": "Primary",
        "SECONDARY": "Secondary",
    },
}

# Agent configuration
AGENT_CONFIG = {
    "name": "Aioverse Asset Manager Agent",
    "description": "Intelligent asset management system for Aioverse brand ecosystem",
    "version": "1.0.0",
    "model": "gpt-4",  # Change based on your preferred model
    "temperature": 0.3,  # Lower temperature for deterministic asset operations
    "max_tokens": 4096,
}

# File handling
SUPPORTED_FORMATS = {
    "images": [".png", ".jpg", ".jpeg", ".webp", ".svg", ".gif"],
    "documents": [".md", ".pdf", ".docx", ".txt"],
    "fonts": [".ttf", ".otf", ".woff", ".woff2"],
    "config": [".json", ".yaml", ".yml"],
}

# Operation modes
OPERATION_MODES = {
    "import": "Import and register new assets",
    "export": "Export assets with metadata",
    "organize": "Organize and categorize assets",
    "refine": "Enhance and optimize assets",
    "validate": "Validate asset compliance",
}

# Metadata schema
METADATA_SCHEMA = {
    "token": str,
    "original_name": str,
    "standardized_name": str,
    "category": str,
    "family": str,
    "variant": str,
    "file_path": str,
    "file_size": int,
    "created_date": str,
    "modified_date": str,
    "version": str,
    "tags": list,
    "description": str,
    "usage_rights": str,
    "color_hex": str,  # For color assets
}

# Logging configuration
LOG_CONFIG = {
    "level": "INFO",
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "file": PROJECT_ROOT / "Agent" / "logs" / "agent.log",
}

# Database/Storage
STORAGE_CONFIG = {
    "metadata_file": PROJECT_ROOT / "Agent" / "data" / "asset_metadata.json",
    "registry_file": PROJECT_ROOT / "Agent" / "data" / "asset_registry.json",
    "cache_dir": PROJECT_ROOT / "Agent" / ".cache",
}
