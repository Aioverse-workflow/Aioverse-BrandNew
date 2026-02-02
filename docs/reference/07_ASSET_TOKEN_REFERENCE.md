# Asset Token Reference Guide

## Quick Lookup Tables

### Logomark Tokens
| Token | Asset | Format | Use Case |
|-------|-------|--------|----------|
| LOGO-LM-TEAL001 | lm_midnightteal.svg | SVG | Scalable print & web |
| LOGO-LM-TEAL002 | lm_midnightteal.webp | WebP | Web-optimized dark theme |
| LOGO-LM-AQUA001 | lm_electricaqua.svg | SVG | Scalable print & web |
| LOGO-LM-AQUA002 | lm_electricaqua.webp | WebP | Web-optimized accent |
| LOGO-LM-WHITE001 | lm_softwhite.svg | SVG | Scalable print & web |
| LOGO-LM-WHITE002 | lm_softwhite.webp | WebP | Web-optimized light bg |
| LOGO-MARK-GRAD001 | Logomark_-_Grad.webp | WebP | Colorful gradient variant |
| LOGO-MARK-MIDNIGHT001 | Logomark_-_Midnight.webp | WebP | Dark minimal variant |
| LOGO-MARK-SOFT001 | Logomark_-_Soft.webp | WebP | Light minimal variant |

### Full Logo Tokens
| Token | Asset | Format | Use Case |
|-------|-------|--------|----------|
| LOGO-FULL-TEAL001 | logo_midnightteal.svg | SVG | Scalable wordmark print |
| LOGO-FULL-TEAL002 | logo_midnightteal.webp | WebP | Web dark variant |
| LOGO-FULL-AQUA001 | logo_electricaqua.svg | SVG | Scalable accent variant |
| LOGO-FULL-AQUA002 | logo_electricaqua.webp | WebP | Web accent variant |

### AI Brand Tokens
| Token | Asset | Format | Use Case |
|-------|-------|--------|----------|
| LOGO-AI-VECTOR001 | ai_vector.jpeg | JPEG | Master vector source |
| LOGO-AI-GRAD001 | Ai_-_Grad.webp | WebP | Gradient colorful |
| LOGO-AI-WBG001 | AI_-_W.BG.webp | WebP | White background variant |

### Aiotize Brand Tokens
| Token | Asset | Format | Use Case |
|-------|-------|--------|----------|
| LOGO-AIOTIZE-PFP001 | aiotize_pfp300x.webp | WebP | Social media profile |
| LOGO-AIOTIZE-VECTOR001 | aiotizeinc_vector.jpeg | JPEG | High-quality master |
| LOGO-AIOTIZE-PDF001 | Aiotize Inc vector.pdf.pdf | PDF | Print production ready |

---

## Token Naming Convention

### Pattern
```
{PREFIX}-{FAMILY}-{VARIANT}{NUMBER}
```

### Components

**PREFIX**
- `LOGO` = Logo/Mark asset
- `ICON` = Icon asset (future)
- `ILLUST` = Illustration asset (future)
- `FNT` = Font asset
- `IMG` = Image/Photo asset

**FAMILY**
- `LM` = Logomark
- `FULL` = Full Logo
- `MARK` = Alternate Marks
- `AI` = AI Brand
- `AIOTIZE` = Aiotize Brand

**VARIANT**
- `TEAL` = Midnight Teal color
- `AQUA` = Electric Aqua color
- `WHITE` = Soft White color
- `GRAD` = Gradient variant
- `VECTOR` = Vector master
- `PFP` = Profile Picture
- `PDF` = PDF format
- `WBG` = White Background

**NUMBER**
- Sequential counter: 001, 002, etc.
- Differentiates multiple files of same asset type

---

## Asset Organization

### Folder Structure
```
logos/
├── lm_*.svg                 (Logomark vectors)
├── lm_*.webp                (Logomark web-optimized)
├── logo_*.svg               (Full logo vectors)
├── logo_*.webp              (Full logo web-optimized)
├── Logomark_*.webp          (Alternate logomark variants)
├── Ai_*.webp                (AI brand variants)
├── ai_*.jpeg                (AI brand source)
├── aiotize_*.webp           (Aiotize brand web)
└── aiotizeinc_*.jpeg        (Aiotize brand source)

icons/
(empty - ready for icon tokens)

illustrations/
(empty - ready for illustration tokens)
```

---

## How to Find an Asset by Token

### Example 1: Find Midnight Teal Logomark
```
Search tokens file for: LOGO-LM-TEAL001
→ Location: logos/lm_midnightteal.svg
→ Also available: LOGO-LM-TEAL002 (logos/lm_midnightteal.webp)
```

### Example 2: Find Aiotize Profile Picture
```
Search tokens file for: LOGO-AIOTIZE-PFP001
→ Location: logos/aiotize_pfp300x.webp
→ Dimensions: 300x300px
→ Format: WebP (web-optimized)
```

### Example 3: Find Print-Ready Aiotize Logo
```
Search tokens file for: LOGO-AIOTIZE-PDF001
→ Location: logos/Aiotize Inc vector.pdf.pdf
→ Format: PDF
→ Use: Professional printing
```

---

## Color Variants Quick Reference

### By Token Pattern
- `TEAL` or `MIDNIGHT` = Deep Teal (#002426)
- `AQUA` or `ELECTRIC` = Cyan Light (#73EFFB)
- `WHITE` or `SOFT` = Off-White (#FAFAFA)
- `GRAD` or `GRADIENT` = Multi-color

### Complete Color Palette
```
Primary:
  Deep Teal:    #002426
  Cyan Light:   #73EFFB
  Off-White:    #FAFAFA

Usage:
  Deep Teal:    Brand primary, backgrounds, headers
  Cyan Light:   Accents, highlights, interactive elements
  Off-White:    Backgrounds, text areas, content sections
```

---

## Format Recommendations

### File Format by Use Case

| Use Case | Recommended Format | Token Pattern |
|----------|-------------------|---|
| Print & Signage | SVG or PDF | `*-VECTOR001` or `*-PDF001` |
| Web - Primary | WebP | `*002` (WebP suffixed) |
| Email & Fallback | JPEG | `*-VECTOR001` (JPEG) |
| Social Media | WebP (square) | `*-PFP001` or `*-GRAD001` |
| High-Quality Master | JPEG | `*-VECTOR001` |
| Scalable Display | SVG | `*001` (SVG suffixed) |

### Web Optimization
- WebP format preferred (smaller file size)
- All web assets already optimized
- Look for tokens ending in `002` for web-ready versions

---

## Asset Metadata

### What Each Token Includes
Every asset token contains:

```json
{
  "token": "Unique identifier",
  "original_name": "Original filename",
  "standardized_name": "Standardized filename",
  "category": "Asset category",
  "family": "Asset family/group",
  "variant": "Color/style variant",
  "size_bytes": "File size in bytes",
  "size_mb": "File size in MB",
  "path": "Relative file path",
  "metadata": {
    "file_format": "SVG/WebP/PDF/JPEG",
    "web_optimized": "true/false",
    "has_transparency": "true/false",
    "scalable": "true/false (SVG only)",
    "printable": "true/false (PDF only)",
    "dimensions": "optional resolution"
  },
  "ai_prompt_tags": ["searchable", "keywords"],
  "color_palette": {
    "deep_teal": "#002426",
    "cyan_light": "#73EFFB",
    "off_white": "#FAFAFA"
  },
  "created": "ISO timestamp"
}
```

---

## Adding New Logo Assets

When adding new logo assets:

1. **Follow naming convention:**
   - Use standardized format: `LogoName_Variant_TOKEN.extension`
   - Example: `Logo_Midnight-Variant_LOGO-NEW-VARIANT001.svg`

2. **Generate token:**
   - Use pattern: `LOGO-{FAMILY}-{VARIANT}{###}`
   - Increment number if variant already exists
   - Example: If `LOGO-NEW-TEAL001` exists, use `LOGO-NEW-TEAL002`

3. **Add to tokens file:**
   - Insert in "assets" array section (around line 3650+)
   - Insert reference in "brand-logos" section (around line 9623+)

4. **Update metadata:**
   - Fill in all required fields (see metadata template above)
   - Include appropriate AI prompt tags
   - Specify color palette usage

---

## Common Tasks

### Task: Find all Dark Variant Logos
```
Search tokens file for: "TEAL\|MIDNIGHT\|DARK"
Filter results in brand-logos section
```

### Task: Get all Web-Optimized Assets
```
Search tokens file for: "LOGO-*002"
All 002-numbered logo tokens are WebP web-optimized
```

### Task: Find Original Vector Masters
```
Search tokens file for: "VECTOR"
Look for SVG or JPEG format (highest quality)
```

### Task: Get Social Media Ready Assets
```
Search tokens file for: "PFP\|GRAD"
These are typically square, optimized, social-ready
```

---

**Document Version:** 1.0  
**Last Updated:** February 2, 2026  
**System:** Aioverse Token Management System v1.0
