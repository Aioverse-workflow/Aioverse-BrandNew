# 📄 PDF EXPORT GUIDE

**Version:** 2.0  
**Date:** February 2, 2026  
**Status:** Complete

---

## 📋 TABLE OF CONTENTS

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Method 1: Using Markdown to PDF Tools](#method-1-markdown-pdf-tools)
4. [Method 2: Using Pandoc](#method-2-pandoc)
5. [Method 3: Online Converters](#method-3-online-converters)
6. [Method 4: GitBook PDF Export](#method-4-gitbook-pdf-export)
7. [Including Logos & Images](#including-logos--images)
8. [PDF Formatting & Page Numbers](#pdf-formatting--page-numbers)
9. [Creating Table of Contents](#creating-table-of-contents)
10. [Quality Assurance Checklist](#quality-assurance-checklist)

---

## INTRODUCTION

This guide provides 4 methods to export your complete Aioverse documentation into professional PDF documents with proper page numbering, table of contents, logos, and formatting.

**Expected Output:**
- ✅ Single PDF file with all documentation (~350+ pages)
- ✅ Proper page numbering (1-380+)
- ✅ Table of Contents with page references
- ✅ Logos and images included
- ✅ Professional formatting
- ✅ Clickable links within PDF
- ✅ Search functionality

---

## PREREQUISITES

### Files Needed
Ensure you have all documentation files:
```
Aioverse-BrandNew/
├── README.md
├── SYSTEM_SUMMARY_v2.md
├── API_DOCUMENTATION.md
├── INTEGRATIONS_GUIDE.md
├── STORAGE_DEPLOYMENT_GUIDE.md
├── WORKFLOW_DIAGRAMS.md
├── TABLE_OF_CONTENTS_WITH_PAGES.md
├── logos/
│   ├── logo.png
│   ├── logo-white.png
│   └── logo-mark.png
├── colours/
│   └── COLOUR_PALETTE.md
├── fonts/
│   └── (Font files)
└── ... (all other documentation)
```

### Software Requirements

**Method 1:** VS Code + Extensions  
**Method 2:** Pandoc (command-line tool)  
**Method 3:** Online tool (no installation)  
**Method 4:** GitBook account  

---

## METHOD 1: MARKDOWN PDF TOOLS

### Option A: VS Code with Markdown PDF Extension

#### Installation
```bash
# 1. Open VS Code
# 2. Extensions → Search "Markdown PDF"
# 3. Install by yzane
# 4. Or via CLI:
code --install-extension yzane.markdown-pdf
```

#### Configuration
Create `.vscode/settings.json`:
```json
{
  "markdown-pdf.displayHeaderFooter": true,
  "markdown-pdf.headerTemplate": "<div style='width: 100%; font-size: 9pt; padding: 10px; text-align: center;'><span class='title'></span></div>",
  "markdown-pdf.footerTemplate": "<div style='width: 100%; font-size: 9pt; padding: 10px; text-align: center;'><span class='pageNumber'></span>/<span class='totalPages'></span></div>",
  "markdown-pdf.margin.top": "1cm",
  "markdown-pdf.margin.bottom": "1.5cm",
  "markdown-pdf.margin.left": "1cm",
  "markdown-pdf.margin.right": "1cm",
  "markdown-pdf.scale": 1.0,
  "markdown-pdf.format": "A4",
  "markdown-pdf.quality": 100,
  "markdown-pdf.highlight": true,
  "markdown-pdf.breakOnPage": true
}
```

#### Export Steps
```bash
# Method A: Single File
1. Open any markdown file
2. Ctrl+Shift+P → Markdown PDF: Export (pdf)
3. Choose location and filename

# Method B: Combine Multiple Files (Recommended)
# Create COMBINED_DOCUMENT.md that includes all files
# See "Creating Combined Document" section below
```

### Option B: Using Markdown Preview Enhanced

#### Installation
```bash
# VS Code Extensions → Search "Markdown Preview Enhanced"
# Install by Yiyi Wang
```

#### Export Settings
1. Right-click in editor → Markdown Preview Enhanced → Open in Browser
2. Right-click preview → HTML to PDF
3. Configure settings for page numbers

---

## METHOD 2: PANDOC

### Installation
```bash
# macOS
brew install pandoc

# Windows (with Chocolatey)
choco install pandoc

# Windows (manual)
# Download from: https://github.com/jgm/pandoc/releases

# Linux
sudo apt-get install pandoc
```

### Creating Pandoc Configuration

Create `pandoc-config.yaml`:
```yaml
---
title: "Aioverse BrandNew: Complete Documentation"
author: "Aioverse Team"
date: "February 2, 2026"
toc: true
toc-depth: 3
number-sections: true
# PDF options
pdf-engine: xelatex
margin-left: 1in
margin-right: 1in
margin-top: 1in
margin-bottom: 1in
fontsize: 11pt
linestretch: 1.5
colorlinks: true
# Metadata
description: "Complete documentation for Aioverse BrandNew asset management system"
keywords: [aioverse, documentation, api, branding]
...
```

### Export Command

#### Single File to PDF
```bash
pandoc input.md -o output.pdf \
  --from markdown \
  --to pdf \
  --toc \
  --toc-depth=3 \
  --number-sections \
  --variable geometry:margin=1in \
  --variable linestretch=1.5
```

#### Multiple Files Combined
```bash
pandoc README.md \
  SYSTEM_SUMMARY_v2.md \
  API_DOCUMENTATION.md \
  INTEGRATIONS_GUIDE.md \
  STORAGE_DEPLOYMENT_GUIDE.md \
  WORKFLOW_DIAGRAMS.md \
  -o Aioverse-Complete-Documentation.pdf \
  --toc \
  --toc-depth=2 \
  --number-sections \
  --variable geometry:margin=1in \
  --table-of-contents \
  --metadata title="Aioverse BrandNew Complete Documentation" \
  --metadata author="Aioverse Team" \
  --metadata date="February 2, 2026"
```

#### With CSS Styling
```bash
pandoc *.md \
  -o Aioverse-Complete-Documentation.pdf \
  -f markdown \
  -t pdf \
  --css=style.css \
  --pdf-engine=xelatex \
  --toc \
  --number-sections \
  --variable geometry:"margin=1in"
```

### Advanced Pandoc Options
```bash
# With custom header/footer
pandoc input.md \
  -o output.pdf \
  --include-in-header header.tex \
  --include-before-body before.tex \
  --include-after-body after.tex

# With syntax highlighting
pandoc input.md \
  -o output.pdf \
  --highlight-style=pygments

# With LaTeX template
pandoc input.md \
  -o output.pdf \
  --template=template.tex
```

---

## METHOD 3: ONLINE CONVERTERS

### Recommended Tools

#### Markdown to PDF Online
```
1. Go to: https://md-to-pdf.herokuapp.com/
2. Paste your markdown content
3. Click "Convert"
4. Download PDF
```

**Limitations:** Single file, limited formatting

#### Pandoc Online
```
1. Go to: https://pandoc.org/try/
2. Enter markdown on left
3. Select PDF output on right
4. Copy/download result
```

**Limitations:** Size restrictions, basic formatting

#### Print to PDF (Browser Method)
```bash
# For HTML versions:
1. Deploy docs to GitHub Pages (see next guide)
2. Open in browser
3. Ctrl+P / Cmd+P → "Save as PDF"
4. Configure margins and header/footer
```

**Advantages:** 
- Professional formatting
- Clickable links preserved
- CSS styling applied
- Better page breaks

---

## METHOD 4: GITBOOK PDF EXPORT

### Setup in GitBook

#### 1. Create GitBook Account
```
1. Go to https://www.gitbook.com
2. Sign up or log in
3. Create new space: "Aioverse-BrandNew"
```

#### 2. Configure Export Settings
```
In GitBook Settings:
  → PDF Export Options
  → Enable PDF Export
  → Configure:
     • Title: "Aioverse BrandNew: Complete Documentation"
     • Author: "Aioverse Team"
     • Include Table of Contents: YES
     • Include Page Numbers: YES
     • Paper Size: A4
     • Margins: 1 inch all sides
```

#### 3. Add Custom Cover
```
1. Create cover.md with frontmatter:

---
title: "Aioverse BrandNew"
subtitle: "Complete Documentation & Integration Guide"
author: "Aioverse Team"
date: "February 2, 2026"
logo: "logos/logo.png"
---

[Include your introduction and cover content here]
```

#### 4. Export to PDF
```
1. In GitBook, click Settings
2. → PDF Export
3. Click "Export as PDF"
4. Configure options:
   - Include theme colors
   - Include page numbers
   - Generate TOC
5. Download PDF file
```

### GitBook Export Quality
**Pros:**
- ✅ Professional formatting
- ✅ Automatic TOC generation
- ✅ Proper page numbering
- ✅ Image handling
- ✅ Multi-column support

**Output:** Single professional PDF with ~350+ pages

---

## INCLUDING LOGOS & IMAGES

### Prepare Your Assets

#### Logo Files Needed
```
logos/
├── logo.png (main logo, 300x300px minimum)
├── logo-white.png (for dark backgrounds)
├── logo-mark.png (symbol only)
├── logo-horizontal.png (landscape format)
└── favicon.ico
```

### Image Paths in Markdown

#### Correct Format
```markdown
# Aioverse BrandNew

![Aioverse Logo](./logos/logo.png)

## Section with Image
![Color Palette](./colours/colour-palette.png)

## More Images
![System Architecture](./diagrams/architecture.png)
```

#### Image Sizing
```markdown
# With custom width
![Logo](./logos/logo.png){width=200px}

# Percentage width (Pandoc)
![Logo](./logos/logo.png){width=50%}

# HTML format (works in most exporters)
<img src="./logos/logo.png" width="300" alt="Aioverse Logo"/>
```

### Optimize Images for PDF

#### Size Optimization
```bash
# Using ImageMagick
convert input.png -quality 85 -resize 1920x output.png

# Using ffmpeg
ffmpeg -i input.png -vf "scale=1920:-1" output.png
```

#### Recommended Specs
- **Resolution:** 72-150 DPI (screen), 300 DPI (print)
- **Format:** PNG (transparent), JPG (photos)
- **Max Size:** 5MB per image
- **Dimensions:** Scale to 1920px width max

### Including PDF Metadata

```markdown
---
title: "Aioverse BrandNew Complete Documentation"
author: "Aioverse Team"
date: "February 2, 2026"
cover_image: "logos/logo.png"
logo_url: "logos/logo.png"
keywords: "aioverse, documentation, api, branding, integrations"
description: "Complete documentation including API, integrations, deployment, and branding guidelines"
---
```

---

## PDF FORMATTING & PAGE NUMBERS

### Pandoc Formatting

Create `formatting.tex`:
```latex
\documentclass{article}
\usepackage{fancyhdr}
\usepackage{lastpage}

\pagestyle{fancy}
\fancyhf{}

% Header
\rhead{Aioverse BrandNew Documentation}
\lhead{\today}

% Footer
\rfoot{Page \thepage\ of \pageref{LastPage}}
\lfoot{© 2026 Aioverse Team}

% Styling
\usepackage{xcolor}
\usepackage{hyperref}
\hypersetup{
  colorlinks=true,
  linkcolor=blue,
  urlcolor=blue,
  citecolor=blue
}

% Title page
\title{Aioverse BrandNew}
\subtitle{Complete Documentation \& Integration Guide}
\author{Aioverse Team}
\date{February 2, 2026}

\begin{document}

\maketitle
\tableofcontents
\newpage

% Content goes here

\end{document}
```

### CSS for HTML-to-PDF

Create `print-styles.css`:
```css
@page {
  margin: 1in;
  @bottom-center {
    content: "Page " counter(page) " of " counter(pages);
  }
  @top-center {
    content: "Aioverse BrandNew Documentation";
  }
}

body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  line-height: 1.6;
  color: #333;
}

h1, h2, h3 {
  page-break-after: avoid;
  color: #1f4788;
}

code {
  background: #f5f5f5;
  padding: 0.2em 0.4em;
  border-radius: 3px;
}

pre {
  background: #f5f5f5;
  padding: 1em;
  overflow-x: auto;
  page-break-inside: avoid;
}

table {
  width: 100%;
  border-collapse: collapse;
  page-break-inside: avoid;
}

th, td {
  border: 1px solid #ddd;
  padding: 0.5em;
}

th {
  background: #1f4788;
  color: white;
}

img {
  max-width: 100%;
  height: auto;
  page-break-inside: avoid;
}

a {
  color: #0066cc;
  text-decoration: underline;
}

.page-break {
  page-break-after: always;
}
```

---

## CREATING TABLE OF CONTENTS

### Automatic TOC in Pandoc
```bash
pandoc input.md -o output.pdf --toc --toc-depth=3
```

### Markdown TOC Format
```markdown
# Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
   - [Installation](#installation)
   - [Configuration](#configuration)
3. [API Documentation](#api-documentation)
   - [Endpoints](#endpoints)
   - [Examples](#examples)
4. [Deployment](#deployment)

---

# Introduction

Content here...

# Getting Started

## Installation

Content here...
```

### Using GitHub ToC Generator
```bash
# Install:
npm install -g markdown-toc

# Generate:
markdown-toc -i README.md

# This updates markdown files with automatic TOC
```

### Linking Page Numbers

For Pandoc with page numbers:
```markdown
# Table of Contents (with page numbers)

- [Introduction](#introduction) ....... Page 1
- [Getting Started](#getting-started) ....... Page 5
- [API Documentation](#api) ....... Page 15
- [Deployment](#deployment) ....... Page 25
```

---

## QUALITY ASSURANCE CHECKLIST

Before finalizing your PDF export:

### Content Verification
- ✅ All sections included and in correct order
- ✅ No missing files or chapters
- ✅ All internal links working (if interactive PDF)
- ✅ Code blocks properly formatted and readable
- ✅ All images visible and correctly positioned
- ✅ Tables properly formatted and legible
- ✅ Lists (numbered and bulleted) correct

### Formatting Verification
- ✅ Page numbers present and correct
- ✅ Header/footer text appropriate
- ✅ Font size readable (12pt+ body, 14pt+ headers)
- ✅ Line spacing comfortable (1.5 or double)
- ✅ Margins consistent (1 inch all sides)
- ✅ Page breaks appropriate (no orphan titles/text)
- ✅ Color usage is print-friendly

### Table of Contents
- ✅ TOC present at beginning
- ✅ All sections listed in TOC
- ✅ Page numbers in TOC accurate
- ✅ Clickable links in TOC (if digital)

### Images & Assets
- ✅ All logos present and visible
- ✅ All diagrams clear and readable
- ✅ Image quality acceptable (not blurry)
- ✅ Image size reasonable (not too large)
- ✅ Color diagrams readable in B&W print

### Metadata
- ✅ Title page with correct information
- ✅ Author/organization name present
- ✅ Date current and accurate
- ✅ Keywords/description included
- ✅ PDF properties set correctly

### Final Review
- ✅ Open in PDF reader and verify all pages
- ✅ Print test page to verify print quality
- ✅ Check file size (should be <50MB for web)
- ✅ Verify search functionality works
- ✅ Test all links (if digital)
- ✅ Get team review/approval

---

## COMPLETE EXPORT WORKFLOW

### Step-by-Step Process

#### Step 1: Prepare Documentation
```bash
# Ensure all files are updated and in correct location
git pull origin main
git status  # Make sure everything is committed

# Verify all images are accessible
find . -name "*.png" -o -name "*.jpg" | head -20
```

#### Step 2: Create Master Document
```markdown
# Aioverse BrandNew: Complete Documentation

[Cover content]

---

# Table of Contents

[Auto-generated or manual TOC]

---

# Main Content

[Include all sections in order]
```

#### Step 3: Export to PDF (Choose Method)
```bash
# Method A: Pandoc (Recommended)
pandoc master-document.md -o Aioverse-Complete-Documentation.pdf \
  --toc \
  --number-sections \
  --variable geometry:margin=1in

# Method B: VS Code Markdown PDF
# Open master-document.md → Ctrl+Shift+P → Export PDF

# Method C: GitBook
# Upload to GitBook → Settings → Export as PDF
```

#### Step 4: Quality Assurance
```bash
# Check PDF properties
pdfinfo Aioverse-Complete-Documentation.pdf

# Verify page count
# Expected: ~350+ pages

# Test in different PDF readers
# - Adobe Reader
# - Browser PDF viewer
# - Print preview
```

#### Step 5: Optimize & Finalize
```bash
# Compress for web (optional)
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 \
  -dPDFSETTINGS=/screen \
  -dNOPAUSE -dQUIET -dBATCH \
  -sOutputFile=Aioverse-Documentation-Web.pdf \
  Aioverse-Complete-Documentation.pdf

# Check final size
ls -lh Aioverse-*.pdf
```

#### Step 6: Distribution
```bash
# Option A: GitHub Releases
# Go to GitHub → Releases → Create new release
# Upload PDF file
# Add version tag (v2.0.0)

# Option B: GitBook
# Publish to GitBook → Share link

# Option C: Website
# Upload to web server
# Create download link
```

---

## TROUBLESHOOTING PDF EXPORT

### Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| **Missing images** | Check relative paths, use absolute URLs, verify file exists |
| **Page numbers not showing** | Check footer template settings, use --include-in-header with Pandoc |
| **Large file size** | Use compression, reduce image quality, remove unused fonts |
| **Poor formatting** | Check CSS/styling, use compatible Pandoc version, test with basic markdown first |
| **Broken internal links** | Verify anchor tags match heading IDs, use Pandoc --section-divs |
| **Characters appear wrong** | Use UTF-8 encoding, specify font explicitly, use xelatex engine |
| **Fonts not embedded** | Include font files in directory, specify fonts in config, use web-safe fonts |

---

## FINAL CHECKLIST BEFORE PUBLISHING

```
PDF Creation Complete? ✅
File Size Reasonable (<100MB)? ✅
Page Count Correct (~350+ pages)? ✅
TOC Present & Accurate? ✅
Page Numbers Visible? ✅
All Images Visible? ✅
Logos Included? ✅
Links Working (if digital)? ✅
Print Test Passed? ✅
Team Approval? ✅
Version Tag Set? ✅
Published to GitHub? ✅
Shared with Team? ✅
```

---

**PDF Export Guide Complete!** 📄

**Next:** Follow GitBook publishing guide to also publish online!
