# 💾 STORAGE & DEPLOYMENT GUIDE

**Version:** 1.0.0  
**Last Updated:** February 2, 2026

---

## 📋 Table of Contents

1. [Where to Store the Repository](#where-to-store-the-repository)
2. [Local Installation](#local-installation)
3. [GitHub Setup](#github-setup)
4. [Docker Containerization](#docker-containerization)
5. [Cloud Deployment](#cloud-deployment)
6. [Backup Strategies](#backup-strategies)
7. [Environment Configuration](#environment-configuration)
8. [Version Management](#version-management)

---

## 🏪 Where to Store the Repository

### Option 1: GitHub (Recommended)

**Advantages:**
- ✅ Version control with git
- ✅ Collaborative development
- ✅ Automatic backups
- ✅ CI/CD integration
- ✅ Public or private hosting
- ✅ Easy team access

**Steps:**
1. Create GitHub account (if not exists)
2. Create new repository: `https://github.com/Shivansh9000/Aioverse-BrandNew`
3. Clone locally: `git clone https://github.com/Shivansh9000/Aioverse-BrandNew.git`
4. Add files and commit
5. Push to GitHub

```bash
# Initialize git
cd Aioverse-BrandNew
git init
git add .
git commit -m "Initial commit: Aioverse Asset Agent"
git branch -M main
git remote add origin https://github.com/Shivansh9000/Aioverse-BrandNew.git
git push -u origin main
```

### Option 2: Local Storage

**Advantages:**
- ✅ Complete control
- ✅ No external dependencies
- ✅ Offline access
- ✅ Custom security

**Setup:**
```bash
# Create backup directory
mkdir -p /backups/Aioverse
cp -r Aioverse-BrandNew /backups/Aioverse/
```

### Option 3: Cloud Storage

**Services:**
- AWS S3
- Google Cloud Storage
- Azure Blob Storage
- Dropbox
- OneDrive

**Steps (AWS S3 example):**
```bash
# Install AWS CLI
pip install awscli

# Configure AWS
aws configure

# Create S3 bucket
aws s3 mb s3://aioverse-assets

# Upload repository
aws s3 sync Aioverse-BrandNew s3://aioverse-assets/repo/
```

### Option 4: Self-Hosted Server

**Requirements:**
- Linux server (Ubuntu, CentOS)
- SSH access
- Git installed
- Backup storage

**Setup:**
```bash
# SSH into server
ssh user@your-server.com

# Clone repository
git clone https://github.com/Shivansh9000/Aioverse-BrandNew.git /opt/aioverse

# Set permissions
chmod 755 /opt/aioverse
chown aioverse:aioverse /opt/aioverse -R
```

---

## 🚀 Local Installation

### Prerequisites
- Python 3.8 or higher
- 500 MB free disk space
- 2 GB RAM minimum

### Step 1: Clone/Download Repository

```bash
# Option A: Clone from GitHub
git clone https://github.com/Shivansh9000/Aioverse-BrandNew.git
cd Aioverse-BrandNew

# Option B: Download ZIP
# From GitHub, click "Code" → "Download ZIP"
# Extract the archive
unzip Aioverse-BrandNew.zip
cd Aioverse-BrandNew
```

### Step 2: Verify Python Installation

```bash
python --version
# Output: Python 3.8+ required
```

### Step 3: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### Step 4: Install Dependencies (None Required!)

```bash
# Optional: View requirements
cat requirements.txt
# Output: No external dependencies required!

# If you want optional features:
pip install requests  # For HTTP client examples
```

### Step 5: Verify Installation

```bash
cd Agent
python main.py
# You should see: Agent> prompt
Agent> help
Agent> exit
```

### Step 6: Configure Settings (Optional)

Edit `Agent/config/settings.py`:
```python
# Adjust paths for your system
ASSET_PATHS = {
    "fonts": "/path/to/fonts",
    "colours": "/path/to/colours",
    # ...
}
```

---

## 🐙 GitHub Setup

### Step 1: Create GitHub Repository

1. Go to `https://github.com/new`
2. Repository name: `Aioverse-BrandNew`
3. Description: "AI-powered asset management system for Aioverse brand"
4. Visibility: Public (or Private for internal use)
5. Initialize with README: No (we have our own)
6. Create repository

### Step 2: Add SSH Key (Optional but Recommended)

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your-email@example.com"

# Copy public key
cat ~/.ssh/id_ed25519.pub

# Add to GitHub: Settings → SSH and GPG keys → New SSH key
```

### Step 3: Push Repository to GitHub

```bash
cd Aioverse-BrandNew
git init
git add .
git commit -m "Initial commit: Aioverse Asset Agent System"
git branch -M main
git remote add origin https://github.com/Shivansh9000/Aioverse-BrandNew.git
git push -u origin main
```

### Step 4: Setup .gitignore

File: `.gitignore`
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
.venv

# IDE
.vscode/
.idea/
*.swp
*.swo

# Data (don't commit asset files, only metadata)
Agent/data/*.json
Agent/.cache/
Agent/logs/

# OS
.DS_Store
Thumbs.db

# Large files
*.zip
*.tar.gz
```

### Step 5: Setup GitHub Actions (CI/CD)

File: `.github/workflows/test.yml`
```yaml
name: Tests
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - run: python -m pytest tests/
```

### Step 6: Enable GitHub Pages (For Documentation)

1. Go to repository settings
2. Pages → Source: Deploy from a branch
3. Select: main branch / docs folder
4. Documentation will be available at: `https://username.github.io/Aioverse-BrandNew`

---

## 🐳 Docker Containerization

### Step 1: Create Dockerfile

File: `Dockerfile`
```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy files
COPY . .

# Install optional dependencies
RUN pip install --no-cache-dir requests

# Create data directory
RUN mkdir -p Agent/data Agent/logs

# Expose API port
EXPOSE 8000

# Set entry point
ENTRYPOINT ["python", "Agent/api/rest_api.py", "--host", "0.0.0.0", "--port", "8000"]
```

### Step 2: Create .dockerignore

File: `.dockerignore`
```
__pycache__
.git
.vscode
.idea
*.pyc
venv
.env
*.log
```

### Step 3: Build Docker Image

```bash
# Build image
docker build -t aioverse-asset-agent:1.0.0 .

# Verify build
docker images
```

### Step 4: Run Docker Container

```bash
# Run container
docker run -d \
  --name aioverse-agent \
  -p 8000:8000 \
  -v aioverse-data:/app/Agent/data \
  aioverse-asset-agent:1.0.0

# Check logs
docker logs aioverse-agent

# Verify API
curl http://localhost:8000/api/health
```

### Step 5: Docker Compose (Multiple Services)

File: `docker-compose.yml`
```yaml
version: '3.8'

services:
  api:
    build: .
    container_name: aioverse-api
    ports:
      - "8000:8000"
    volumes:
      - aioverse-data:/app/Agent/data
    environment:
      - LOG_LEVEL=INFO
    restart: unless-stopped

  # Optional: Add backup service
  backup:
    image: aioverse-asset-agent:1.0.0
    container_name: aioverse-backup
    command: python Agent/scripts/backup.py
    volumes:
      - aioverse-data:/app/Agent/data
      - ./backups:/backups
    environment:
      - BACKUP_INTERVAL=86400
    restart: unless-stopped

volumes:
  aioverse-data:
```

### Step 6: Deploy Docker Image

**To Docker Hub:**
```bash
# Tag image
docker tag aioverse-asset-agent:1.0.0 username/aioverse-asset-agent:1.0.0

# Login to Docker Hub
docker login

# Push image
docker push username/aioverse-asset-agent:1.0.0
```

**To Private Registry:**
```bash
# Tag for private registry
docker tag aioverse-asset-agent:1.0.0 registry.example.com/aioverse:1.0.0

# Push to private registry
docker push registry.example.com/aioverse:1.0.0
```

---

## ☁️ Cloud Deployment

### AWS Deployment

**Option 1: EC2**
```bash
# Launch EC2 instance
# Choose: Ubuntu 20.04 LTS
# Security group: Allow port 8000

# SSH into instance
ssh -i key.pem ubuntu@instance-ip

# Install Python
sudo apt update
sudo apt install python3.9 python3-pip git

# Clone repository
git clone https://github.com/Shivansh9000/Aioverse-BrandNew.git
cd Aioverse-BrandNew

# Run API
python Agent/api/rest_api.py --host 0.0.0.0 --port 8000
```

**Option 2: ECS (Docker)**
```bash
# Create ECS cluster
aws ecs create-cluster --cluster-name aioverse

# Register task definition
aws ecs register-task-definition --cli-input-json file://task-definition.json

# Create service
aws ecs create-service \
  --cluster aioverse \
  --service-name aioverse-api \
  --task-definition aioverse:1
```

### Google Cloud Deployment

**Cloud Run:**
```bash
# Build image
gcloud builds submit --tag gcr.io/PROJECT_ID/aioverse-agent

# Deploy
gcloud run deploy aioverse-agent \
  --image gcr.io/PROJECT_ID/aioverse-agent \
  --platform managed \
  --port 8000
```

### Azure Deployment

**App Service:**
```bash
# Create resource group
az group create -n aioverse-rg -l eastus

# Create App Service Plan
az appservice plan create -n aioverse-plan -g aioverse-rg --sku FREE

# Create Web App
az webapp create -n aioverse-app -g aioverse-rg -p aioverse-plan

# Deploy from GitHub
az webapp up --name aioverse-app --repo-url https://github.com/Shivansh9000/Aioverse-BrandNew
```

---

## 📦 Backup Strategies

### Strategy 1: Daily Local Backups

Script: `Agent/scripts/backup.py`
```python
import shutil
import json
from datetime import datetime
from pathlib import Path

def backup_assets():
    """Create daily backup of asset data"""
    backup_dir = Path("backups")
    backup_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = backup_dir / f"backup_{timestamp}"
    
    # Copy data
    src = Path("Agent/data")
    shutil.copytree(src, backup_path / "data")
    
    # Create manifest
    manifest = {
        "timestamp": timestamp,
        "files": list(backup_path.glob("**/*")),
        "size_mb": sum(f.stat().st_size for f in backup_path.glob("**/*")) / 1024 / 1024
    }
    
    with open(backup_path / "manifest.json", "w") as f:
        json.dump(manifest, f, indent=2)
    
    print(f"✅ Backup created: {backup_path}")
    return backup_path

if __name__ == "__main__":
    backup_assets()
```

### Strategy 2: GitHub Releases

```bash
# Create git tag
git tag -a v1.0.0 -m "Version 1.0.0: Initial release"

# Push tag
git push origin v1.0.0

# Create release on GitHub (manual or via API)
```

### Strategy 3: Cloud Backup

**AWS S3:**
```python
import boto3
import json
from pathlib import Path

def backup_to_s3():
    s3 = boto3.client('s3')
    
    # Upload data
    data_dir = Path("Agent/data")
    for file in data_dir.glob("*.json"):
        s3.upload_file(
            str(file),
            "aioverse-backups",
            f"data/{file.name}"
        )
    
    print("✅ Backup uploaded to S3")

if __name__ == "__main__":
    backup_to_s3()
```

### Strategy 4: Scheduled Backups

**Cron Job (Linux/macOS):**
```bash
# Edit crontab
crontab -e

# Add daily backup at 2 AM
0 2 * * * cd /path/to/Aioverse-BrandNew && python Agent/scripts/backup.py
```

**Windows Task Scheduler:**
```powershell
# Create scheduled task
$trigger = New-ScheduledTaskTrigger -Daily -At 2am
$action = New-ScheduledTaskAction -Execute "python" -Argument "Agent\scripts\backup.py"
Register-ScheduledTask -TaskName "Aioverse-Backup" -Trigger $trigger -Action $action
```

### Restore from Backup

```bash
# List backups
ls -la backups/

# Restore from specific backup
cp -r backups/backup_20240202_020000/data/* Agent/data/

# Verify restoration
python Agent/main.py
Agent> show statistics
```

---

## ⚙️ Environment Configuration

### .env File

Create: `Agent/.env`
```
# API Settings
API_HOST=localhost
API_PORT=8000
API_DEBUG=False

# Database
DB_PATH=./data/asset_metadata.json
REGISTRY_PATH=./data/asset_registry.json

# Logging
LOG_LEVEL=INFO
LOG_FILE=./logs/agent.log

# Security
API_KEY=your-secret-key-here
SECRET_KEY=your-jwt-secret-key

# Cloud Storage (Optional)
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_BUCKET=aioverse-assets

# Backup
BACKUP_ENABLED=True
BACKUP_INTERVAL=86400

# Monitoring
SENTRY_DSN=
```

### Load Environment Variables

```python
from dotenv import load_dotenv
import os

load_dotenv()

API_HOST = os.getenv("API_HOST", "localhost")
API_PORT = int(os.getenv("API_PORT", 8000))
DEBUG = os.getenv("API_DEBUG", "False") == "True"
```

---

## 📌 Version Management

### Semantic Versioning

Format: `MAJOR.MINOR.PATCH`

**Examples:**
- `1.0.0` - Initial release
- `1.1.0` - New features added
- `1.1.1` - Bug fix
- `2.0.0` - Breaking changes

### Update Version Number

File: `Agent/config/settings.py`
```python
AGENT_CONFIG = {
    "version": "1.0.0",  # Update here
    # ...
}
```

### Create Release

```bash
# Update version in code
# Update CHANGELOG.md
git add -A
git commit -m "Release v1.1.0"
git tag -a v1.1.0 -m "Version 1.1.0: Bug fixes and improvements"
git push origin main --tags
```

### CHANGELOG Template

File: `CHANGELOG.md`
```markdown
# Changelog

## [1.1.0] - 2024-02-02
### Added
- REST API endpoints
- Tag management system
- Docker containerization

### Changed
- Improved metadata schema
- Enhanced error handling

### Fixed
- Fixed token validation issue
- Fixed file path handling

## [1.0.0] - 2024-01-15
### Added
- Initial release
- Asset management
- AI agent interface
```

---

## ✅ Deployment Checklist

- [ ] Code tested locally
- [ ] Version number updated
- [ ] Changelog updated
- [ ] .gitignore configured properly
- [ ] README reviewed
- [ ] API documentation updated
- [ ] All endpoints tested
- [ ] Docker image built and tested
- [ ] Environment variables documented
- [ ] Backup strategy tested
- [ ] Git tag created
- [ ] GitHub release created
- [ ] Monitoring/logging configured
- [ ] Documentation deployed
- [ ] Team notified of release

---

**Version:** 1.0.0  
**Last Updated:** February 2, 2026  
**Status:** ✅ Production Ready
