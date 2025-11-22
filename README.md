# 2026 HCBS Conference Booth Selector

An interactive booth selection system designed to drive revenue growth through strategic scarcity and real-time FOMO (Fear of Missing Out) mechanics.

## 📊 Revenue Strategy

### Tier Allocation (Strategic Scarcity Model)

| Tier | Price | Booths | Type | Target | Last Year | Revenue |
|------|-------|--------|------|--------|-----------|---------|
| **Platinum** | $58,000 | 40 (20 sponsors) | Double 10×20 | 20 sponsors | 18 | $1,160,000 |
| **Diamond** | $48,000 | 0 planned | Single 10×8 | 0-2 sponsors | 0 | $0 |
| **Emerald** | $37,000 | 4 | Single 10×8 | 4 sponsors | 2 | $148,000 |
| **Sapphire** | $27,000 | 10 | Single 10×8 | 10 sponsors | 4 | $270,000 |
| **Ruby** | $16,250 | 16 | Single 10×8 | 16 sponsors | 16 | $260,000 |
| **Gold** | $13,000 | 14 | Single 10×8 | 14 sponsors | 23 | $182,000 |
| **Exhibitor** | $7,500 | 10 | Single 10×8 | 10 sponsors | 13 | $75,000 |
| **TOTAL** | | **94** | | | **76** | **$2,095,000** |

**Projected Revenue Increase: +$734,500 (+54%) from last year's $1,360,500**

### Strategic Insights

1. **Platinum Expansion** (18→20 sponsors): +$116,000
   - Premium double booths dominate the exhibit hall
   - 42% of all booth space allocated to top tier

2. **Gold Scarcity** (23→14 booths): -30% reduction
   - Forces upgrades to Sapphire ($14k more) or Ruby ($3,250 more)
   - Creates urgency and perceived value

3. **Emerald/Sapphire Push**: Combined growth from 6→14 booths
   - Emerald: 2→4 (+$74,000)
   - Sapphire: 4→10 (+$162,000)
   - Positioned as "accessible premium" tier

4. **Exhibitor Restriction** (13→10 booths): -23% reduction
   - Limited to worst foyer locations only (615-624)
   - Drives upgrades to Gold for better placement

## 🗺️ Booth Location Restrictions

### Foyer (24 booths)
- **601-603**: Gold tier (3 booths)
- **605-612**: Premium foyer - Sapphire/Emerald/Diamond/Platinum/Ruby only (8 booths)
- **613-614**: Gold tier (2 booths)
- **615-624**: Exhibitor ONLY (10 booths) - worst locations

### Main Exhibit Hall (70 booths)
- **Platinum**: 40 booths in pre-paired sets (best locations near entrances, food, stage)
- **Diamond**: Available throughout main hall (single booths)
- **Emerald**: Prime main hall locations only
- **Sapphire**: Main hall + premium foyer (605-612)
- **Ruby**: Main hall + premium foyer (605-612)
- **Gold**: Main hall + foyer gold sections (601-604, 613-614)

## 🚀 Key Features

### 1. **Live Scarcity Indicators**
- Real-time booth availability counters
- Color-coded urgency levels (green/yellow/red)
- "Only X spots left!" messaging

### 2. **FOMO Mechanics**
- Recent activity feed showing live reservations
- "X people viewing now" counter
- Urgency banners when booths are reserved
- Social proof displays

### 3. **Tier-Based Restrictions**
- Exhibitors can ONLY see booths 615-624
- Each tier has specific location allowances
- Visual indicators for unavailable booths

### 4. **Platinum Pre-Paired Sets**
20 premium double-booth sets automatically paired:
- Platinum sponsors select one set, automatically reserves both booths
- Best locations in main hall (near entrances, food, high traffic)

### 5. **Admin Panel**
- View all reservations
- Mark booths as "Taken" (confirmed/paid)
- Release reservations
- Export data to JSON
- Real-time updates

## 📱 How to Use

### For Sponsors

1. **Select Your Tier** - Click on your sponsorship level in the sidebar
2. **View Available Booths** - Color-coded map shows what's available for your tier
3. **Click to Reserve** - Select your preferred booth(s)
4. **Submit Information** - Fill in organization and contact details
5. **Confirmation** - Receive immediate confirmation (admin will follow up)

### For Administrators

1. **Access Admin Panel** - Click "Admin Panel" button (bottom right)
2. **Manage Reservations**:
   - Mark as "Taken" when payment confirmed
   - Release if needed
   - View all contact information
3. **Export Data** - Download JSON for integration with CRM/database
4. **Monitor Activity** - Track real-time selections

## 🔧 Technical Details

### Files
- `booth-selector.html` - Main interactive booth selector
- `monday-calendar.html` - Original conference calendar (separate tool)
- `README.md` - This documentation

### Data Storage
- Uses browser `localStorage` for persistence
- Export to JSON for backup/integration
- No server required (purely client-side)

### Customization

To adjust booth positions, edit the `getBoothPosition()` function:

```javascript
const positions = {
    601: { x: 5, y: 82 },  // x and y are percentages
    602: { x: 10, y: 82 },
    // ... add more booth coordinates
};
```

To modify tier allocation, update `TIER_CONFIG`:

```javascript
const TIER_CONFIG = {
    platinum: {
        name: 'Platinum',
        price: 58000,
        maxCount: 20,
        allowedBooths: 'main-hall-premium'
    },
    // ... modify tier settings
};
```

## 📈 Expected Outcomes

### Revenue Growth Drivers

1. **Scarcity Creates Urgency**: Limited Gold (14) and Exhibitor (10) spots force quick decisions
2. **Upgrade Incentives**:
   - Gold→Sapphire: +$14,000 for significantly better placement
   - Exhibitor→Gold: +$5,500 to escape worst locations
3. **Live FOMO**: Real-time activity feed drives competitive booking
4. **Premium Expansion**: 20 Platinum sponsors = +$116,000

### Conversion Strategy

| Current Tier | Target Upgrade | Price Difference | Value Proposition |
|--------------|----------------|------------------|-------------------|
| Gold (23→14) | → Sapphire | +$14,000 | Avoid being stuck in limited Gold spots |
| Ruby (16→16) | → Sapphire | +$10,750 | Move to premium foyer (605-612) |
| Exhibitor (13→10) | → Gold | +$5,500 | Escape worst foyer locations |
| Emerald (2→4) | → Platinum | +$21,000 | Double the visibility, worth the jump |

## 🎯 Success Metrics

**Conservative Goal**: 94 booths × average $22,287 = **$2,095,000**
**Stretch Goal**: If we sell 2 Diamond sponsors: **$2,191,000** (+$831,500 from last year)

### Key Performance Indicators
- Booth selection conversion rate
- Time to reserve after viewing
- Upgrade rate from lower tiers
- Premium tier (Sapphire+) fill rate

## 💡 Future Enhancements

1. **Backend Integration**: Connect to Monday.com or CRM
2. **Email Notifications**: Auto-send confirmations
3. **Payment Processing**: Direct Stripe/PayPal integration
4. **Actual Floor Plan**: Overlay on real venue blueprint image
5. **Mobile Optimization**: Touch-friendly booth selection
6. **Multi-language Support**: Spanish, French, etc.
7. **Analytics Dashboard**: Track views, clicks, conversion funnel

## 📞 Support

For questions or technical issues:
- Check the Admin Panel for reservation status
- Export data regularly for backup
- Contact conference team for tier adjustments

---

**Last Updated**: November 22, 2025
**Conference Date**: August 2026
**Venue**: HCBS Conference Center
