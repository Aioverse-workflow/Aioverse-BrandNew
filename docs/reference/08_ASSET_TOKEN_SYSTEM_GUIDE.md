# Aioverse Asset Token System Documentation

## System Overview

The Aioverse Asset Token System is a comprehensive digital asset management and governance framework that assigns unique, standardized identifiers to all brand assets. This system ensures consistency, traceability, and efficient asset discovery across the entire brand ecosystem.

### Purpose
- **Unique Identification** - Every asset has a globally unique token
- **Asset Governance** - Centralized tracking and version control
- **Discovery & Search** - AI/ML enabled asset finding
- **Standardization** - Consistent naming and metadata across all formats
- **Brand Compliance** - Ensures all assets follow Aioverse standards
- **Cross-Platform Support** - Compatible with web, print, mobile, and emerging platforms

---

## Token System Architecture

### Core Components

#### 1. Token Structure
```
{PREFIX}-{FAMILY}-{VARIANT}{NUMBER}

Example: LOGO-AIOTIZE-PFP001
├─ PREFIX: LOGO (asset type identifier)
├─ FAMILY: AIOTIZE (asset grouping)
├─ VARIANT: PFP (specific variant)
└─ NUMBER: 001 (sequential counter)
```

#### 2. Asset Classification

| Prefix | Category | Use | Examples |
|--------|----------|-----|----------|
| `FNT` | Fonts | Typography system | Anek, Nohemi, Helvetica |
| `LOGO` | Logos & Marks | Brand identity | Logomark, Wordmark, Aiotize |
| `ICON` | Icons | UI & Interface (future) | Navigation, Controls, Status |
| `ILLUST` | Illustrations | Visual content (future) | Backgrounds, Decorative, Editorial |
| `IMG` | Images & Photos | Media content | Gallery, Product, Promotional |

#### 3. Metadata Requirements

Every token must include:

```json
{
  "token": "LOGO-AIOTIZE-PFP001",
  "original_name": "original_filename.ext",
  "standardized_name": "Family_Variant_TOKEN.ext",
  "category": "Icons/Logos",
  "family": "Aiotize-Brand",
  "variant": "Profile-Picture",
  "size_bytes": 8516,
  "size_mb": 0.008,
  "path": "relative/path/to/asset",
  "metadata": {
    "file_format": "WEBP",
    "web_optimized": true,
    "has_transparency": true,
    "scalable": false,
    "printable": false,
    "dimensions": "300x300px"
  },
  "ai_prompt_tags": ["aiotize", "profile", "avatar"],
  "color_palette": {
    "deep_teal": "#002426",
    "cyan_light": "#73EFFB",
    "off_white": "#FAFAFA"
  },
  "created": "2026-02-02T00:00:00.000000"
}
```

---

## Current Token Inventory

### Fonts (65 Tokens)
**Prefix:** `FNT-`

**Families:**
- Anek (10 variants) - Multi-script variable font
- Nohemi (40+ variants) - Display & body text font
- Nebula (2 variants) - Decorative font
- Tokyo Trail Mono (4 variants) - Code/monospace font
- Helvetica Neue (10 variants) - Fallback/web safe font

**Variants Include:** Light, Regular, Medium, Bold, Black, Variable, Web-safe, Print-ready

**Token Count:** 65 active tokens

### Logos (19 Tokens)
**Prefix:** `LOGO-`

**Families:**
- Logomark (9 tokens) - Brand symbol variants
- Logo-Full (4 tokens) - Complete wordmark
- AI-Logo (3 tokens) - AI brand identity
- Aiotize-Brand (3 tokens) - Aiotize company brand

**Color Variants:** Midnight Teal, Electric Aqua, Soft White, Gradient

**Format Coverage:** SVG (scalable), WebP (web-optimized), JPEG (master source), PDF (print-ready)

**Token Count:** 19 active tokens

### Product Images & Content (90+ Tokens)
**Prefix:** `IMG-`

**Categories:**
- Content Gallery - Product photography
- Hero/Cover Images - Page headers & promotional
- UI Elements - Interface components
- Miscellaneous - Supporting visuals

**Formats:** WebP (optimized), PNG, JPEG, SVG

**Token Count:** 90+ active tokens

### **Total Active Tokens: 174+**

---

## Token Naming Conventions

### Family Naming

Consistent family names ensure logical grouping:

```
Pattern: {Descriptor}[-{SubType}]

Examples:
- Logomark (primary brand symbol)
- Logo-Full (complete logo with wordmark)
- AI-Logo (AI brand variant)
- Aiotize-Brand (company brand)
- Content-Gallery (photo collection)
- Hero-Images (banner/header images)
```

### Variant Naming

Variants describe the specific asset characteristics:

```
Color Variants:
- Midnight-Teal  (deep brand primary)
- Electric-Aqua  (bright accent)
- Soft-White     (clean, light)
- Gradient       (multi-color)

Format Variants:
- Vector         (SVG, scalable)
- Web-Optimized  (WebP, compressed)
- Print-Ready    (PDF, high-res)
- Mobile         (optimized for phones)

Style Variants:
- Light, Regular, Medium, Bold, Black (weights)
- Regular, Italic, Condensed (styles)
- Variable (adaptive font)
```

### Sequential Numbering

Numbers differentiate multiple files of the same asset:

```
LOGO-LM-TEAL001  = SVG version (vector master)
LOGO-LM-TEAL002  = WebP version (web-optimized)
LOGO-LM-TEAL003  = JPEG version (fallback)

Why Number?
- Same asset, different formats
- Different resolution versions
- Variant iterations
- Multi-language versions
```

---

## Asset Management Lifecycle

### Phase 1: Asset Creation
1. Designer creates asset in native format
2. Export to necessary formats (SVG, PDF, WebP, JPEG)
3. Optimize for web/print as needed
4. Store in appropriate folder (logos/, icons/, etc.)

### Phase 2: Tokenization
1. Generate unique token following naming convention
2. Create comprehensive metadata entry
3. Add to tokens file "assets" array
4. Add reference to appropriate categorical section

### Phase 3: Documentation
1. Update quick reference guides
2. Add to asset registry
3. Update version control
4. Communicate changes to team

### Phase 4: Implementation
1. Use tokens in design systems
2. Reference in documentation
3. Link in asset management systems
4. Integrate into design tools (Figma, etc.)

### Phase 5: Maintenance
1. Track usage across projects
2. Monitor format compatibility
3. Update metadata as needed
4. Retire deprecated assets

---

## Usage Guidelines

### When to Create a New Token

✅ **Create New Token When:**
- Adding completely new asset to system
- Creating new asset variant (color, style, format)
- Adding new family of related assets
- Updating major versions of existing asset

❌ **Don't Create New Token For:**
- Minor tweaks (alignment, spacing)
- Temporary test versions
- Work-in-progress files
- Duplicate files with same content

### Naming New Assets

1. **Identify the family:**
   - Is this an existing family? (Logomark, AI-Logo, etc.)
   - Or creating a new family?

2. **Determine variant:**
   - Color? (Teal, Aqua, White, Custom)
   - Format? (Vector, Web, Print)
   - Style? (Light, Bold, Gradient)

3. **Assign number:**
   - Check if family-variant exists
   - If yes, increment number
   - If no, start with 001

4. **Complete full entry:**
   - Add to tokens file
   - Fill all metadata fields
   - Add AI prompt tags
   - Set creation timestamp

---

## Color System Integration

### Aioverse Color Palette

Every asset token links to the core color system:

```
Primary Brand Colors:
├─ Deep Teal (#002426)
│  Usage: Primary brand color, backgrounds, headers, dark themes
│  Tokens: *-TEAL*, *-MIDNIGHT*
│
├─ Cyan Light (#73EFFB)
│  Usage: Accent color, highlights, interactive elements, light themes
│  Tokens: *-AQUA*, *-ELECTRIC*, *-GRADIENT*
│
└─ Off-White (#FAFAFA)
   Usage: Background, text areas, content sections, light backgrounds
   Tokens: *-WHITE*, *-SOFT*
```

### Color Variant Selection

Choose appropriate color variant based on usage context:

| Context | Recommended Variant | Token Example |
|---------|-------------------|---|
| Dark backgrounds | Soft-White, Cyan-Light | LOGO-LM-WHITE002 |
| Light backgrounds | Midnight-Teal, Dark variants | LOGO-LM-TEAL001 |
| Brand presentations | Any primary color | LOGO-FULL-AQUA001 |
| Web dark mode | Light colors | LOGO-LM-WHITE002 |
| Print (4-color) | Original color or gradient | LOGO-AIOTIZE-VECTOR001 |
| Accent/Highlight | Cyan-Light, Gradient | LOGO-MARK-GRAD001 |

---

## AI/ML Integration

### AI Prompt Tags

Each asset includes searchable tags for AI/ML applications:

```json
"ai_prompt_tags": [
  "logomark",           // Primary classification
  "brand",              // Category
  "midnight-teal",      // Color
  "vector",             // Format
  "mark",               // Type
  "identity",           // Usage
  "symbol"              // Additional descriptors
]
```

### Enabling AI Search

Tags enable intelligent queries like:
- "Find all gradient logos"
- "Show me vector assets in the Aiotize family"
- "Get cyan-light accent marks"
- "List all web-optimized brand logos"

### Future AI Applications

Tokens enable:
- Automated asset selection for layouts
- Smart color matching
- Format conversion recommendations
- Brand consistency checking
- Asset usage analytics

---

## Future Expansion

### Planned Token Categories

#### Icons (Coming Soon)
```
Token Pattern: ICON-{FAMILY}-{VARIANT}{###}
Examples:
  ICON-NAV-DARK001     (Dark navigation icon)
  ICON-CTL-LIGHT001    (Light control icon)
  ICON-STATUS-GRAD001  (Status indicator gradient)
```

#### Illustrations (Coming Soon)
```
Token Pattern: ILLUST-{FAMILY}-{VARIANT}{###}
Examples:
  ILLUST-HERO-TEAL001      (Hero illustration, teal variant)
  ILLUST-PATTERN-GRAD001   (Pattern, gradient variant)
  ILLUST-EDITORIAL-AQUA001 (Editorial, aqua variant)
```

#### Animations (Future)
```
Token Pattern: ANIM-{FAMILY}-{VARIANT}{###}
Examples:
  ANIM-LOGO-PULSE001   (Logo pulse animation)
  ANIM-TRANSITION001   (Page transition)
```

#### Components (Future)
```
Token Pattern: COMP-{TYPE}-{VARIANT}{###}
Examples:
  COMP-BUTTON-PRIMARY001
  COMP-CARD-FEATURED001
  COMP-HERO-FULL001
```

---

## Implementation Checklist

### For New Projects

- [ ] Import current tokens file
- [ ] Familiarize with token patterns
- [ ] Use existing tokens for all brand assets
- [ ] Request new tokens only if needed
- [ ] Document token usage in your project
- [ ] Report any missing or incorrect tokens

### For Asset Managers

- [ ] Review new assets weekly
- [ ] Verify tokens before use
- [ ] Update central registry
- [ ] Monitor token versioning
- [ ] Maintain consistency across projects
- [ ] Archive deprecated tokens with reason

### For Developers

- [ ] Map tokens to asset URLs
- [ ] Implement token lookup system
- [ ] Create asset reference documentation
- [ ] Enable programmatic token access
- [ ] Monitor token performance metrics
- [ ] Report unused or broken tokens

---

## Troubleshooting

### Common Issues

**Issue:** Can't find an asset token
**Solution:** 
1. Search in `tokens` file for asset name
2. Check alternative variant names
3. Look in reference sections for category
4. Check if asset is in right folder

**Issue:** Asset token differs between projects
**Solution:**
1. Verify using central tokens file (source of truth)
2. Confirm token hasn't been updated
3. Check creation timestamp
4. Report discrepancy to asset manager

**Issue:** Can't create token due to naming conflict
**Solution:**
1. Use sequential numbering (+1)
2. Verify variant name is accurate
3. Confirm family is correct
4. Check if asset already exists

---

## Version Control

### Current Version
- **System Version:** 1.0
- **Total Tokens:** 174+
- **Last Updated:** February 2, 2026
- **Maintained By:** Aioverse Design System

### Update Log

| Date | Change | Version |
|------|--------|---------|
| 2026-02-02 | Added 19 logo tokens, established reference system | 1.0 |
| Future | Icon token system launch | 1.1 |
| Future | Illustration token system launch | 1.2 |
| Future | Animation & component tokens | 2.0 |

---

## Support & Resources

### Documentation Files
- `TOKENS_UPDATE_SUMMARY.md` - Recent updates and statistics
- `ASSET_TOKEN_REFERENCE.md` - Quick lookup tables
- `tokens` - Master token registry (JSON)

### To Request New Tokens
1. Prepare asset in final formats
2. Document family, variant, and usage
3. Provide to design system manager
4. Receive assigned token within 24 hours

### To Report Issues
1. Document issue with token ID or asset name
2. Describe the problem
3. Include screenshot/example
4. Submit to design system team

---

**Document:** Aioverse Asset Token System v1.0  
**Classification:** Design System Documentation  
**Last Reviewed:** February 2, 2026  
**Next Review:** August 2, 2026
