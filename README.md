# 2026 HCBS Sponsorships - Floor Plan

Interactive floor plan showing booth sponsorships for the 2026 HCBS conference.

## Live Site

Your floor plan is hosted on GitHub Pages at:
**https://advancingstateshcbs.github.io/2026HCBSSponsorships/**

The site deploys automatically when you push to the branch. You can view deployment status in the "Actions" tab of your repository.

## Features

- Interactive convention center floor plan layout
- Real-time sponsor data from Monday.com
- Color-coded booth status (Available, Taken, Pending)
- Filter by sponsorship level
- Click booths to view sponsor details
- All booth numbers and venue sections (KENT, ESSEX, HARBORSIDE FOYER)

## Firebase Deployment

To deploy to Firebase Hosting:

1. **Login to Firebase:**
   ```bash
   firebase login
   ```

2. **Create/Select Firebase Project:**
   ```bash
   firebase projects:create hcbs-sponsorships-2026
   # OR if project exists:
   firebase use hcbs-sponsorships-2026
   ```

3. **Deploy:**
   ```bash
   firebase deploy
   ```

4. **Access your site at:**
   ```
   https://hcbs-sponsorships-2026.web.app
   ```

## Configuration

When you first open the page, configure the following in the settings panel:

- **Monday.com API Token**: Your Monday.com API authentication token
- **Board ID**: The ID of your Monday.com board
- **Booth Column**: Column ID containing booth numbers (default: `text`)
- **Status Column**: Column ID containing status (default: `status`)
- **Sponsorship Column**: Column ID containing sponsorship levels (default: `color_mkwgq36e`)

Configuration is saved in your browser's localStorage.

## Local Development

Simply open `monday-calendar.html` in a web browser to test locally.

## Booth Layout

The floor plan includes:
- **100 series**: KENT section booths
- **200 series**: Center-left booths
- **300 series**: Center booths
- **400 series**: Center-right booths
- **500 series**: ESSEX section booths
- **600 series**: HARBORSIDE FOYER booths

## Support

For issues or questions, please contact the repository maintainers.
