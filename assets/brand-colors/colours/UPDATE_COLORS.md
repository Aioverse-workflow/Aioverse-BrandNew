# Colour Palette Update Guide

## Master Configuration File

The `colours-config.json` file is the **single source of truth** for all colour hex codes in the Aioverse brand system.

### How to Update Colours

1. **Edit `colours-config.json`**
   - Locate the colour you want to update
   - Change only the `hex` value (e.g., `"#0066CC"` → `"#0099FF"`)
   - The RGB value will need to be calculated and updated manually

2. **Propagate Changes**
   - Update the `COLOUR_PALETTE.md` table with the new hex code
   - Update the CSS Variables section in `COLOUR_PALETTE.md`
   - Update the `cssVariables` section in `colours-config.json` to match

### RGB Conversion Tool

To convert hex to RGB:
- Use online converters like https://www.rapidtables.com/convert/color/hex-to-rgb.html
- Or use this formula: Split hex into pairs (e.g., #0066CC → 00, 66, CC) and convert to decimal

### File Structure

```
colours/
├── colours-config.json          ← Edit hex codes HERE
├── COLOUR_PALETTE.md            ← Update from config
├── UPDATE_COLORS.md             ← This file
└── (future: colour-swatches.html, accessibility-matrix.md)
```

### Quick Reference: What Changes When You Update a Hex Code

| File | Section | Update Required |
|---|---|---|
| `colours-config.json` | `palette.[category][]` | ✅ Yes - update hex value |
| `colours-config.json` | `cssVariables.variables` | ✅ Yes - update matching variable |
| `COLOUR_PALETTE.md` | Primary/Secondary/Functional/Neutral table | ✅ Yes - update Hex Code column |
| `COLOUR_PALETTE.md` | Visual Reference Guide | ✅ Yes - update colour block comment |
| `COLOUR_PALETTE.md` | CSS Variables Reference | ✅ Yes - update CSS value |

### Example: Updating "Brand Blue"

**Before:**
```json
{
  "name": "Brand Blue",
  "hex": "#0066CC",
  "rgb": "rgb(0, 102, 204)",
  "usage": "Primary CTA, Headers, Brand Elements"
}
```

**After changing to #0099FF:**
```json
{
  "name": "Brand Blue",
  "hex": "#0099FF",
  "rgb": "rgb(0, 153, 255)",
  "usage": "Primary CTA, Headers, Brand Elements"
}
```

Then update in `COLOUR_PALETTE.md`:
- Table row: `#0099FF` and `rgb(0, 153, 255)`
- CSS: `--color-brand-blue: #0099FF;`

---

## Future Automation

This JSON structure is ready for:
- **Build scripts** that auto-generate CSS/SCSS from `colours-config.json`
- **Design tool exports** (Figma, Adobe XD integration)
- **Web demo generators** that pull from this config
- **Accessibility checkers** that validate contrast ratios automatically
