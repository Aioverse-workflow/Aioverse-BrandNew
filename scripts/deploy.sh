#!/bin/bash

# Aioverse Repository - One-Click GitHub Upload Script
# This script automates the process of committing and pushing changes to GitHub
# Usage: ./deploy.sh

set -e

echo ""
echo "================================"
echo "Aioverse GitHub Deployment Tool"
echo "================================"
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "ERROR: Git is not installed"
    echo "Please install Git from https://git-scm.com/download/linux"
    exit 1
fi

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo "ERROR: Not a git repository"
    echo "Please run this script from the root of the Aioverse repository"
    exit 1
fi

# Get current branch
BRANCH=$(git rev-parse --abbrev-ref HEAD)
echo "Current branch: $BRANCH"
echo ""

# Display uncommitted changes
echo "Checking for changes..."
git status --short
echo ""

# Ask for confirmation
read -p "Do you want to commit and push these changes? (yes/no): " CONFIRM
if [ "$CONFIRM" != "yes" ]; then
    echo "Operation cancelled"
    exit 0
fi

echo ""
echo "Proceeding with deployment..."
echo ""

# Stage all changes
echo "[1/4] Staging files..."
git add .
echo "✓ Files staged"

# Commit changes
echo "[2/4] Creating commit..."
read -p "Enter commit message (press Enter for default): " MESSAGE
if [ -z "$MESSAGE" ]; then
    MESSAGE="Repository cleanup and organization"
fi
git commit -m "$MESSAGE"
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to create commit. Maybe no changes to commit?"
    exit 1
fi
echo "✓ Commit created"

# Push to remote
echo "[3/4] Pushing to GitHub..."
git push origin "$BRANCH"
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to push to GitHub"
    echo "Make sure you have push access and proper authentication"
    exit 1
fi
echo "✓ Successfully pushed to GitHub"

# Optional: Create and push a tag/release
echo ""
echo "[4/4] Creating release tag (optional)..."
read -p "Create a release tag? (yes/no): " CREATE_TAG
if [ "$CREATE_TAG" = "yes" ]; then
    read -p "Enter tag name (e.g., v2.0.0): " TAG_NAME
    if [ ! -z "$TAG_NAME" ]; then
        git tag -a "$TAG_NAME" -m "Release $TAG_NAME"
        git push origin "$TAG_NAME"
        echo "✓ Tag created and pushed"
    fi
fi

echo ""
echo "================================"
echo "Deployment Complete!"
echo "================================"
echo "Your changes have been successfully pushed to GitHub"
echo "Repository: https://github.com/Shivansh9000/Aioverse-BrandNew"
echo "Branch: $BRANCH"
echo ""
