# 📤 REPOSITORY IMPORT/EXPORT GUIDE

**Version:** 1.0.0  
**Last Updated:** February 2, 2026

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Export Repository](#export-repository)
3. [Import Repository](#import-repository)
4. [Export Specific Components](#export-specific-components)
5. [Migration Guide](#migration-guide)
6. [Version Management](#version-management)
7. [Backup & Restore](#backup--restore)

---

## 🎯 Overview

The Aioverse Asset Agent system supports complete repository export/import for:
- ✅ Full repository migration
- ✅ Component sharing
- ✅ Backup and recovery
- ✅ Team collaboration
- ✅ Version management

---

## 📤 Export Repository

### Full Repository Export

**What Gets Exported:**
- ✅ All source code
- ✅ Configuration files
- ✅ Documentation
- ✅ Asset metadata (optional)
- ✅ Examples

**What NOT Exported (By Default):**
- ❌ Large asset files (referenced, not copied)
- ❌ Temporary logs
- ❌ Cache files
- ❌ Virtual environment

### Method 1: Git Export (Recommended)

**Step 1: Clone Repository**
```bash
git clone https://github.com/Shivansh9000/Aioverse-BrandNew.git
cd Aioverse-BrandNew
```

**Step 2: Remove Git History (Optional)**
```bash
# Create clean copy without git history
rm -rf .git
```

**Step 3: Create Archive**
```bash
# Windows
powershell -Command "Compress-Archive -Path . -DestinationPath Aioverse-BrandNew-v1.0.0.zip"

# macOS/Linux
tar -czf Aioverse-BrandNew-v1.0.0.tar.gz --exclude='.git' --exclude='__pycache__' .

# Exclude large files
tar -czf Aioverse-BrandNew-v1.0.0.tar.gz \
  --exclude='*.zip' \
  --exclude='__pycache__' \
  --exclude='.git' \
  --exclude='venv' \
  .
```

**Step 4: Verify Archive**
```bash
# List contents
tar -tzf Aioverse-BrandNew-v1.0.0.tar.gz | head -20

# Check size
du -h Aioverse-BrandNew-v1.0.0.tar.gz
```

### Method 2: Manual Export Script

Script: `Agent/scripts/export_repo.py`
```python
#!/usr/bin/env python3
"""Export repository to archive"""

import shutil
import json
from pathlib import Path
from datetime import datetime

def export_repository(output_dir="./exports"):
    """Export full repository"""
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    # Create export directory
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    export_name = f"Aioverse-BrandNew-{timestamp}"
    export_path = output_path / export_name
    
    # Copy repository (excluding large files)
    ignore_patterns = [
        "__pycache__",
        ".git",
        "*.pyc",
        ".venv",
        "venv",
        ".DS_Store",
        "*.zip",
        "*.tar.gz"
    ]
    
    def ignore_func(directory, contents):
        ignored = []
        for item in contents:
            for pattern in ignore_patterns:
                if pattern in item or item.startswith("."):
                    ignored.append(item)
                    break
        return ignored
    
    # Copy directory
    shutil.copytree(
        ".",
        export_path,
        ignore=ignore_func,
        dirs_exist_ok=True
    )
    
    # Create manifest
    manifest = {
        "export_timestamp": timestamp,
        "version": "1.0.0",
        "contents": {
            "code": True,
            "documentation": True,
            "metadata": True,
            "assets": False
        },
        "size_mb": sum(
            f.stat().st_size for f in export_path.rglob("*") if f.is_file()
        ) / 1024 / 1024
    }
    
    # Save manifest
    with open(export_path / "EXPORT_MANIFEST.json", "w") as f:
        json.dump(manifest, f, indent=2)
    
    # Create archive
    archive_path = shutil.make_archive(
        str(export_path),
        "zip",
        str(export_path.parent),
        export_name
    )
    
    print(f"✅ Repository exported to: {archive_path}")
    return archive_path

if __name__ == "__main__":
    export_repository()
```

**Run Export:**
```bash
python Agent/scripts/export_repo.py
# Output: Aioverse-BrandNew-20240202_120000.zip
```

### Method 3: GitHub Releases

**Step 1: Commit Changes**
```bash
git add -A
git commit -m "Release v1.0.0"
```

**Step 2: Create Tag**
```bash
git tag -a v1.0.0 -m "Version 1.0.0: Initial release"
git push origin main --tags
```

**Step 3: Create Release on GitHub**
```bash
# Via GitHub CLI
gh release create v1.0.0 \
  --title "Aioverse Asset Agent v1.0.0" \
  --notes "First production release"

# Via GitHub Web Interface
# 1. Go to Releases
# 2. Click "Create a new release"
# 3. Select tag: v1.0.0
# 4. Fill title and description
# 5. Attach files if needed
# 6. Publish release
```

---

## 📥 Import Repository

### Method 1: From GitHub

**Step 1: Clone Repository**
```bash
git clone https://github.com/Shivansh9000/Aioverse-BrandNew.git
cd Aioverse-BrandNew
```

**Step 2: Checkout Specific Version (Optional)**
```bash
# List available tags
git tag

# Checkout specific version
git checkout v1.0.0
```

**Step 3: Verify Installation**
```bash
cd Agent
python main.py
Agent> show statistics
Agent> exit
```

### Method 2: From Archive

**Step 1: Extract Archive**
```bash
# ZIP file
unzip Aioverse-BrandNew-v1.0.0.zip

# TAR.GZ file
tar -xzf Aioverse-BrandNew-v1.0.0.tar.gz
```

**Step 2: Navigate to Directory**
```bash
cd Aioverse-BrandNew
```

**Step 3: Initialize as Git Repository (Optional)**
```bash
git init
git add .
git commit -m "Import Aioverse Asset Agent"
```

**Step 4: Setup Environment**
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # or: venv\Scripts\activate (Windows)

# Verify Python
python --version
```

**Step 5: Test Installation**
```bash
cd Agent
python main.py
Agent> help
Agent> exit
```

### Method 3: Docker Import

**Step 1: Pull Docker Image**
```bash
docker pull username/aioverse-asset-agent:1.0.0
```

**Step 2: Run Container**
```bash
docker run -it \
  -p 8000:8000 \
  -v aioverse-data:/app/Agent/data \
  username/aioverse-asset-agent:1.0.0
```

**Step 3: Verify API**
```bash
curl http://localhost:8000/api/health
```

---

## 📦 Export Specific Components

### Export Only Core Code

```bash
# Copy only essential modules
mkdir -p export/Agent/{core,config,handlers,utils,api}
cp Agent/main.py export/Agent/
cp Agent/core/*.py export/Agent/core/
cp Agent/config/*.py export/Agent/config/
cp Agent/handlers/*.py export/Agent/handlers/
cp Agent/utils/*.py export/Agent/utils/
cp Agent/api/*.py export/Agent/api/
```

### Export Only Documentation

```bash
# Copy only documentation files
mkdir -p export/Agent
cp Agent/*.md export/Agent/
cp README.md export/
```

### Export Only Metadata

```bash
# Copy asset metadata and registry
mkdir -p export/Agent/data
cp Agent/data/*.json export/Agent/data/
```

### Export Asset Metadata as CSV

Script: `Agent/scripts/export_metadata_csv.py`
```python
import json
import csv
from pathlib import Path

def export_metadata_csv(output_file="asset_metadata.csv"):
    """Export asset metadata to CSV"""
    metadata_file = Path("Agent/data/asset_metadata.json")
    
    if not metadata_file.exists():
        print("❌ Metadata file not found")
        return
    
    # Load metadata
    with open(metadata_file, 'r') as f:
        metadata = json.load(f)
    
    # Write CSV
    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=[
            'token', 'name', 'category', 'family', 
            'variant', 'tags', 'created_date', 'size_kb'
        ])
        
        writer.writeheader()
        for token, meta in metadata.items():
            writer.writerow({
                'token': token,
                'name': meta.get('standardized_name', ''),
                'category': meta.get('category', ''),
                'family': meta.get('family', ''),
                'variant': meta.get('variant', ''),
                'tags': ', '.join(meta.get('tags', [])),
                'created_date': meta.get('created_date', ''),
                'size_kb': meta.get('file_size', 0) / 1024
            })
    
    print(f"✅ Metadata exported to: {output_file}")

if __name__ == "__main__":
    export_metadata_csv()
```

---

## 🔄 Migration Guide

### Migrate to New System

**Step 1: Export from Old System**
```bash
# Create clean export of repository
python Agent/scripts/export_repo.py
```

**Step 2: Import to New System**
```bash
# Extract archive on new system
unzip Aioverse-BrandNew-20240202_120000.zip

# Navigate to directory
cd Aioverse-BrandNew
```

**Step 3: Setup New Environment**
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install optional dependencies
pip install -r requirements.txt
```

**Step 4: Initialize Git (If Needed)**
```bash
git init
git remote add origin https://github.com/new-org/Aioverse-BrandNew.git
git add .
git commit -m "Migrate Aioverse Asset Agent"
git push -u origin main
```

**Step 5: Migrate Asset Data**
```bash
# Copy old metadata
cp /old/system/Agent/data/asset_metadata.json Agent/data/

# Verify data
python Agent/main.py
Agent> show statistics
```

### Migrate Between Hosts

**From Host A to Host B:**

```bash
# On Host A: Create export
tar -czf aioverse-backup.tar.gz Aioverse-BrandNew/

# Transfer to Host B
scp aioverse-backup.tar.gz user@hostb:/tmp/

# On Host B: Extract and setup
ssh user@hostb
tar -xzf /tmp/aioverse-backup.tar.gz
cd Aioverse-BrandNew
python Agent/main.py
```

---

## 🏷️ Version Management

### Semantic Versioning

Use format: `MAJOR.MINOR.PATCH-SUFFIX`

**Examples:**
- `1.0.0` - Initial release
- `1.0.1` - Patch (bug fix)
- `1.1.0` - Minor (new features)
- `2.0.0` - Major (breaking changes)
- `1.0.0-alpha` - Pre-release
- `1.0.0-beta.1` - Beta release

### Update Version

File: `Agent/config/settings.py`
```python
AGENT_CONFIG = {
    "version": "1.0.0",  # Update here
}
```

### Track Changes in CHANGELOG

File: `CHANGELOG.md`
```markdown
# Changelog

All notable changes to Aioverse Asset Agent.

## [1.1.0] - 2024-02-02
### Added
- REST API endpoints
- Tag management system
- Docker containerization

### Changed
- Improved error messages
- Enhanced metadata schema

### Fixed
- Fixed file handling bug
- Fixed token validation

### Deprecated
- Legacy CLI commands

### Removed
- Old configuration format

### Security
- Added input validation

## [1.0.0] - 2024-01-15
### Added
- Initial release
- Asset management core
- AI agent interface
- Validation system
```

---

## 💾 Backup & Restore

### Automated Backup

Script: `Agent/scripts/backup_restore.py`
```python
import json
import shutil
from datetime import datetime
from pathlib import Path

class BackupManager:
    def __init__(self, backup_dir="./backups"):
        self.backup_dir = Path(backup_dir)
        self.backup_dir.mkdir(exist_ok=True)
    
    def create_backup(self, name=""):
        """Create backup of current system"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = name or f"backup_{timestamp}"
        backup_path = self.backup_dir / backup_name
        
        # Copy data directory
        src = Path("Agent/data")
        if src.exists():
            shutil.copytree(src, backup_path / "data")
        
        # Create manifest
        manifest = {
            "timestamp": timestamp,
            "version": "1.0.0",
            "includes": ["metadata", "registry"]
        }
        
        with open(backup_path / "manifest.json", "w") as f:
            json.dump(manifest, f, indent=2)
        
        print(f"✅ Backup created: {backup_path}")
        return backup_path
    
    def restore_backup(self, backup_name):
        """Restore from backup"""
        backup_path = self.backup_dir / backup_name
        
        if not backup_path.exists():
            print(f"❌ Backup not found: {backup_name}")
            return False
        
        # Restore data
        src = backup_path / "data"
        dst = Path("Agent/data")
        
        if dst.exists():
            shutil.rmtree(dst)
        
        shutil.copytree(src, dst)
        print(f"✅ Restored from: {backup_name}")
        return True
    
    def list_backups(self):
        """List all available backups"""
        backups = list(self.backup_dir.glob("backup_*"))
        for backup in sorted(backups, reverse=True):
            manifest_file = backup / "manifest.json"
            if manifest_file.exists():
                with open(manifest_file) as f:
                    manifest = json.load(f)
                    print(f"📦 {backup.name}: {manifest['timestamp']}")

if __name__ == "__main__":
    manager = BackupManager()
    
    # Create backup
    manager.create_backup("pre-migration")
    
    # List backups
    manager.list_backups()
    
    # Restore backup
    manager.restore_backup("backup_20240202_120000")
```

### Restore from Backup

```bash
# List available backups
ls -la backups/

# Restore specific backup
python Agent/scripts/backup_restore.py --restore backup_20240202_120000

# Verify restoration
python Agent/main.py
Agent> show statistics
```

---

## ✅ Export/Import Checklist

**Before Export:**
- [ ] All changes committed to git
- [ ] Tests passed
- [ ] Documentation updated
- [ ] Version number updated
- [ ] CHANGELOG updated
- [ ] Clean git history (optional)

**Export Process:**
- [ ] Run export script
- [ ] Verify archive contents
- [ ] Check file size
- [ ] Test extraction on different machine

**Before Import:**
- [ ] Backup existing system
- [ ] Check disk space
- [ ] Verify Python version
- [ ] Plan downtime (if applicable)

**Import Process:**
- [ ] Extract archive
- [ ] Verify directory structure
- [ ] Run verification script
- [ ] Test core functionality
- [ ] Migrate data if needed
- [ ] Update configuration

**After Import:**
- [ ] Test all endpoints
- [ ] Verify API health
- [ ] Check asset metadata
- [ ] Run backup
- [ ] Update documentation
- [ ] Notify team

---

## 🔗 Related Guides

- [Storage & Deployment](STORAGE_DEPLOYMENT_GUIDE.md)
- [API Documentation](API_DOCUMENTATION.md)
- [Complete Master Guide](COMPLETE_MASTER_GUIDE.md)

---

**Version:** 1.0.0  
**Last Updated:** February 2, 2026  
**Status:** ✅ Production Ready
