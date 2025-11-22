# HCBS Venue Map - Loveable Integration Guide

## 📋 Overview

This JSON file (`venue-map.json`) contains a complete, structured representation of the 2026 HCBS venue map with 90+ clickable booths.

## 🎯 Features

- **90 Main Hall Booths** - 10 columns × 9 rows of 10' booths
- **3 Premium 16' Booths** - Larger orange booths
- **19 Foyer Booths** - Curved arrangement with tier restrictions
- **5 Exit Markers** - Non-clickable location markers
- **Dance Stage** - Central non-clickable stage area

## 🎨 Tier System

### All Tiers (Blue/Purple)
- Available to all sponsorship levels
- Colors: `#58b0e2` (blue), `#7b68a6` (purple)
- **Booths:** 101-245, 409-417

### Exhibitor Only (Green/Light Blue)
- Reserved for exhibitor tier
- Colors: `#5a9367` (green), `#7eb8bb` (light blue)
- **Booths:** 401-406

### Gold Tier (Gold/Yellow)
- Available to all, likely for gold sponsors
- Color: `#daa520`
- **Booths:** 407-408, 418-419

### Premium 16' (Orange)
- Larger booths, available to all
- Color: `#ff8c42`
- **Booths:** 301-303

## 📝 Editing Booth Numbers

In the JSON file, find the booth you want to edit:

```json
{
  "id": "L1-1",
  "number": "101",  // ← Change this number
  "tier": "all",
  "size": "10'",
  "x": 210,
  "y": 60,
  "color": 0
}
```

### Numbering Scheme (Default)
- **Main Hall Left:** 101-145
- **Main Hall Right:** 201-245
- **Premium 16' Booths:** 301-303
- **Foyer:** 401-419

## 🚀 Using with Loveable

### Option 1: Direct Import
1. Go to [Loveable.dev](https://loveable.dev)
2. Create a new project
3. Import `venue-map.json`
4. Loveable will generate a beautiful, interactive venue map

### Option 2: Component Prompt
Copy this prompt into Loveable:

```
Create an interactive venue map using the data from venue-map.json with these features:

1. Responsive grid layout showing the main exhibit hall
2. Clickable booth components with hover effects
3. Color-coded tiers (blue/purple for all, green/lightblue for exhibitor, gold for gold tier, orange for premium)
4. Selected state highlighting (red border when clicked)
5. Booth detail panel showing: booth number, tier, size, availability
6. Filter buttons to show/hide booths by tier
7. Search functionality by booth number
8. Zoom and pan controls for the map
9. Dance stage in the center (non-clickable)
10. Red exit markers
11. Curved foyer section at the bottom
12. Modern, clean UI with gradients and shadows

Use Tailwind CSS and shadcn/ui components. Make it mobile-responsive.
```

## 🎨 Color Reference

```javascript
// Theme Colors
Primary: #006273
Secondary: #3a8297
Accent: #58b0e2
Background: linear-gradient(135deg, #006273 0%, #3a8297 50%, #58b0e2 100%)

// Booth Colors
All Tiers Blue: #58b0e2
All Tiers Purple: #7b68a6
Exhibitor Green: #5a9367
Exhibitor Light Blue: #7eb8bb
Gold: #daa520
Premium Orange: #ff8c42
Exit Red: #dc3545
```

## 📐 Layout Specifications

- **Standard Booth:** 50px × 50px (10')
- **Premium Booth:** 80px × 30px (16')
- **Dance Stage:** 200px × 150px
- **Main Hall:** 1000px × 550px
- **Grid Spacing:** 5px between booths

## 🔧 JSON Structure

```javascript
venueMap
├── title & subtitle
├── layout (dimensions, stage position)
├── boothSizes (standard & large)
├── tiers (all, exhibitor, gold, premium)
├── exits (5 locations)
└── booths
    ├── mainHall
    │   ├── leftSection (L1-L5, 45 booths)
    │   ├── rightSection (R1-R5, 45 booths)
    │   └── premiumBooths (3 booths)
    └── foyer (19 booths with rotation)
```

## ✨ Interactive Features to Implement

When using with Loveable, request these features:

1. **Click to Select** - Highlight booth with red border
2. **Hover Effects** - Gold border and shadow on hover
3. **Tier Filtering** - Toggle visibility by sponsorship tier
4. **Search** - Find booth by number
5. **Availability Status** - Mark as available/taken/pending
6. **Sponsor Assignment** - Assign sponsor to booth
7. **Export** - Download booth assignments as CSV/PDF
8. **Mobile Responsive** - Touch-friendly on tablets

## 📱 Recommended Loveable Prompt

```
Build a modern, interactive venue map dashboard using this JSON data:

Components needed:
- VenueMapCanvas: Main SVG/Canvas area with booth grid
- BoothCard: Individual clickable booth component
- ControlPanel: Filters, search, legend
- DetailsSidebar: Selected booth information
- TierLegend: Color-coded tier key
- ExportButton: Download booth assignments

Features:
- Click booth to select (red highlight)
- Hover for preview (gold highlight)
- Filter by tier checkboxes
- Search by booth number
- Zoom/pan controls
- Responsive grid layout
- Modern glassmorphism design
- Smooth animations

Tech stack: React, TypeScript, Tailwind, shadcn/ui
```

## 🎯 Quick Start

1. Upload `venue-map.json` to Loveable
2. Use the prompt above
3. Customize booth numbers in the JSON
4. Deploy and share!

---

**Need help?** The JSON is fully documented with comments and follows a clean, hierarchical structure perfect for Loveable's AI generation.
