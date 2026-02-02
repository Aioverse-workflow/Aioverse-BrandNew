@echo off
REM Aioverse Repository - One-Click GitHub Upload Script
REM This script automates the process of committing and pushing changes to GitHub

setlocal enabledelayedexpansion

echo.
echo ================================
echo Aioverse GitHub Deployment Tool
echo ================================
echo.

REM Check if git is installed
where git >nul 2>nul
if !errorlevel! neq 0 (
    echo ERROR: Git is not installed or not in PATH
    echo Please install Git from https://git-scm.com/download/win
    pause
    exit /b 1
)

REM Check if we're in a git repository
if not exist ".git" (
    echo ERROR: Not a git repository
    echo Please run this script from the root of the Aioverse repository
    pause
    exit /b 1
)

REM Get current branch
for /f "delims=" %%i in ('git rev-parse --abbrev-ref HEAD') do set BRANCH=%%i
echo Current branch: %BRANCH%
echo.

REM Display uncommitted changes
echo Checking for changes...
git status --short
echo.

REM Ask for confirmation
set /p CONFIRM="Do you want to commit and push these changes? (yes/no): "
if /i not "%CONFIRM%"=="yes" (
    echo Operation cancelled
    exit /b 0
)

echo.
echo Proceeding with deployment...
echo.

REM Stage all changes
echo [1/4] Staging files...
git add .
if !errorlevel! neq 0 (
    echo ERROR: Failed to stage files
    pause
    exit /b 1
)
echo ✓ Files staged

REM Commit changes
echo [2/4] Creating commit...
set /p MESSAGE="Enter commit message (default: Repository cleanup and organization): "
if "!MESSAGE!"=="" set MESSAGE=Repository cleanup and organization
git commit -m "!MESSAGE!"
if !errorlevel! neq 0 (
    echo ERROR: Failed to create commit. Maybe no changes to commit?
    pause
    exit /b 1
)
echo ✓ Commit created

REM Push to remote
echo [3/4] Pushing to GitHub...
git push origin %BRANCH%
if !errorlevel! neq 0 (
    echo ERROR: Failed to push to GitHub
    echo Make sure you have push access and proper authentication
    pause
    exit /b 1
)
echo ✓ Successfully pushed to GitHub

REM Optional: Create and push a tag/release
echo.
echo [4/4] Creating release tag (optional)...
set /p CREATE_TAG="Create a release tag? (yes/no): "
if /i "%CREATE_TAG%"=="yes" (
    set /p TAG_NAME="Enter tag name (e.g., v2.0.0): "
    if not "!TAG_NAME!"=="" (
        git tag -a !TAG_NAME! -m "Release !TAG_NAME!"
        git push origin !TAG_NAME!
        echo ✓ Tag created and pushed
    )
)

echo.
echo ================================
echo Deployment Complete!
echo ================================
echo Your changes have been successfully pushed to GitHub
echo Repository: https://github.com/Shivansh9000/Aioverse-BrandNew
echo Branch: %BRANCH%
echo.

pause
