# Deploy Instructions

## Step 1: Enable GitHub Pages

1. Go to your repository: https://github.com/ADvancingStatesHCBS/2026HCBSSponsorships
2. Click **Settings** (top menu)
3. Click **Pages** (left sidebar)
4. Under "Source", select: **Deploy from a branch**
5. Under "Branch", select: `claude/conference-booth-selector-014AvBBSGUx1A4n3WFkwBhah` and folder `/root`
6. Click **Save**

**Your site will be live at:**
```
https://advancingstates.github.io/2026HCBSSponsorships/booth-selector.html
```

(GitHub will take 2-3 minutes to build and deploy)

## Step 2: Add Real-Time Updates (Optional but Recommended)

For live multi-user updates (FOMO effect), you need a backend. Two options:

### Option A: Firebase (Recommended - Free & Easy)
1. Go to https://console.firebase.google.com/
2. Create new project "HCBS-Booth-Selector"
3. Add a Web App
4. Copy your Firebase config
5. I'll integrate it into the HTML file

### Option B: For Now - LocalStorage Only
The current version saves to browser localStorage (single-user only). Once you set up Firebase, I'll add the real-time sync.

## Current Features (No Backend Required)
- ✅ Interactive booth selection
- ✅ Tier-based filtering
- ✅ Reservation form
- ✅ Admin panel
- ✅ Data persists in browser
- ✅ Export to JSON

## Next: Add Firebase for Real-Time Updates
Once your Firebase project is ready, send me the config and I'll add:
- Real-time booth availability across all users
- Live "Someone just booked!" notifications
- Viewer count tracking
- Activity feed syncing
