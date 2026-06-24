# 🔮 QUANTEX-BOT v3 — Complete Feature Documentation

> **Official Telegram Bot**: [@QuantexBinaryTools_bot](https://t.me/QuantexBinaryTools_bot)  
> **Developer**: [@X_Akash_Owner](https://t.me/X_Akash_Owner)

---

## 📋 Feature Index

1. [Live Signal Engine](#1-live-signal-engine)
2. [AI-Assisted Live Signal System](#2-ai-assisted-live-signal-system)
3. [Live Signal Broadcast System](#3-live-signal-broadcast-system)
4. [Future Live Signal System](#4-future-live-signal-system)
5. [Signal Checker — Full Suite](#5-signal-checker--full-suite)
6. [MTG (Martingale) System](#6-mtg-martingale-system)
7. [Chart Generation](#7-chart-generation)
8. [Telegram Premium Integration](#8-telegram-premium-integration)
9. [Free Bots Mission](#9-free-bots-mission)
10. [Bot Builder](#10-bot-builder)
11. [Session Management](#11-session-management)
12. [Sleep Mode System](#12-sleep-mode-system)
13. [Scheduled Sessions](#13-scheduled-sessions)
14. [Partial Report System](#14-partial-report-system)
15. [Referral Program](#15-referral-program)
16. [Reviews & Ratings System](#16-reviews--ratings-system)
17. [License & Access System](#17-license--access-system)
18. [Admin Control Panel](#18-admin-control-panel)
19. [Points & Quota System](#19-points--quota-system)
20. [Database — PostgreSQL Backend](#20-database--postgresql-backend)
21. [Supported Markets & Pairs](#21-supported-markets--pairs)
22. [Multi-Platform Support](#22-multi-platform-support)

---

## 1. Live Signal Engine

The core of QUANTEX-BOT — a fully automated signal generation system using a **proprietary multi-factor analysis engine**.

### How Signals Are Generated

**Step 1 — Clock Sync**  
The bot synchronizes to the **5-minute candle clock**. Signals only generated at exact 5-minute boundaries.

**Step 2 — Data Fetch**  
Latest candle data fetched from the live market API for the selected pair.

**Step 3 — Proprietary Analysis Engine**  
QUANTEX-BOT runs its internal multi-factor analysis pipeline. Specific logic, parameters, and methods are proprietary.

**Step 4 — Confidence Scoring**  
Each signal is scored based on how many internal factors confirm the direction. Only signals reaching a high-confidence threshold are sent.

**Step 5 — Signal Delivered + Auto Result Check**  
High-confidence signal sent to Telegram. After candle closes, result automatically checked and delivered as WIN / LOSS / DOJI.

---

## 2. AI-Assisted Live Signal System

Every Live Signal goes through a dedicated **AI Confirmation Layer** before delivery.

### What the AI Does
- **Validates the signal setup** — reviews current market conditions
- **Calculates Support & Resistance levels** — key S/R zones included in signal
- **Fetches real-time payout data** — actual broker payout % before entry
- **Provides AI reasoning** — human-readable explanation of why the AI confirmed
- **Assigns AI Confidence Score** — rated confidence level for the setup
- **Fallback Logic** — if primary analysis produces no result, AI-assisted fallback generates a direction

### Signal Output Includes
```
📊 LIVE SIGNAL
━━━━━━━━━━━━━━━━━━━━
Pair         : EUR/USD OTC
Direction    : ⬆️ BUY (CALL)
Entry Time   : 14:35
Payout       : 87%
Support      : 1.0821
Resistance   : 1.0847
AI Confidence: HIGH
━━━━━━━━━━━━━━━━━━━━
🤖 Strong upward momentum confirmed
at support zone. Entry validated.
```

---

## 3. Live Signal Broadcast System

Send AI-confirmed signals automatically to your own **Telegram channel**.

### Setup Flow
1. Select a Telegram channel
2. Bot verifies **Post Messages** admin permission
3. Configure template, custom header, username
4. Session runs — signals sent to channel automatically

### Features
- **Manual Signal Mode** — manually trigger a signal for a specific pair
- **Auto Signal Mode** — bot scans all pairs and sends the strongest signal automatically
- **Multi-Template Support** — multiple message formats to choose from
- **Custom Header & Username** — fully personalize your signal messages
- **MTG in Broadcast** — recovery signals sent to channel automatically
- **Channel Permission Validation** — checks admin rights before starting
- **Owner Name Setting** — customize the name shown at bottom of each signal
- **Live Signal Quota** — free users get a set number of daily live signals; licensed users have unlimited access
- **Daily Remaining Display** — shows remaining signal quota for the day

---

## 4. Future Live Signal System

The **Future Live** system lets you paste a pre-planned signal list and have QUANTEX-BOT automatically send each signal to your channel at the exact scheduled time — with real result checking.

### How It Works

**Step 1 — Paste Signal List**  
Paste your planned signals in any format. All formats supported:
```
▢ 05:50 USDIDR ⇨OTC ☞ PUT
❒ USDCAD-OTC ☞ 05:53 ⊱ PUT
M1 EURUSD_OTC 06:00 BUY
```

**Step 2 — Select Chat/Channel**  
Choose where signals are sent (your DM or a channel).

**Step 3 — Select MTG Mode**  
Choose: MTG 1, MTG 2, or Non-MTG.

**Step 4 — Template Setup**  
Preview and customize the signal message template (header & username).

**Step 5 — Session Starts**  
Signals fire automatically at each scheduled time. Bot waits until the exact minute, sends the signal, waits for candle close, and auto-checks the result.

### Signal Status Tracking
During an active session:
- **View Signals** — see all remaining signals and their status
- **Next Signal Display** — shows upcoming pair and exact time
- **Live Countdown** — shows minutes until first signal fires
- **Completion Report** — full WIN/LOSS summary sent when all signals are processed
- **Stop Any Time** — stop the session with one tap

### Free Tier
Free users get **3 Future Live sessions** total. Licensed users have unlimited sessions.

---

## 5. Signal Checker — Full Suite

QUANTEX-BOT v3 features a completely rebuilt, **super-fast, 100% accurate** signal checking suite with multiple checker modes.

### ⚡ Super-Fast & 100% Accurate
- **Local candle cache system** — candle data stored locally for near-instant lookup
- **O(1) time index** — pre-built HH:MM → candle index map eliminates sequential searching
- **File-level cache** — JSON candle files cached in memory, only re-read when file changes
- **Archive + recent data** — checks both today's live data and historical archive files
- **100% accurate results** — direct candle close/open comparison, no estimation

### 🔍 Four Checker Modes

#### 1. OTC Checker
Standard binary options signal checker for OTC pairs.
- Paste signals → instant WIN/LOSS per signal
- Supports unlimited signals per check
- Real payout data per signal slot
- MTG result shown with superscript level (WIN¹, WIN², etc.)
- DOJI candles handled and displayed separately

#### 2. Blackout Checker *(New)*
A special checker mode for **Blackout-style signals** (signals with no direction).
- Determines direction automatically from the **previous candle** color
- Previous GREEN candle → expected direction: PUT
- Previous RED candle → expected direction: BUY
- DOJI previous candle → result shown as `[doji]`
- Checks entry candle + MTG steps against expected direction

#### 3. Whiteout Checker *(New)*
Similar to Blackout but uses the **same-direction** logic from the previous candle.
- Previous GREEN candle → expected direction: BUY
- Previous RED candle → expected direction: PUT
- All other logic identical to Blackout checker

#### 4. Custom Date Checker
Check signals for **any specific date**, not just today/yesterday.
- Enter any past date
- Bot fetches archived candle data for that date
- Full WIN/LOSS report for the chosen date
- Works across all three checker modes (OTC, Blackout, Whiteout)

### 📋 Checker Features (All Modes)
| Feature | Description |
|---|---|
| **Universal Signal Parser** | Parses signals from ANY source, ANY format — automatically |
| **Unicode Normalizer** | Converts fancy/bold/italic Unicode characters to standard ASCII before parsing |
| **Pair Alias Map** | Auto-normalizes 100+ pair name variants to canonical names |
| **OTC + Live Pair Support** | Supports 60+ OTC pairs and 30+ Live Forex pairs |
| **DOJI Detection** | DOJI candles detected and reported separately (not counted as WIN or LOSS) |
| **Payout Filter** | Filter signals below a set payout threshold — flagged with payout % |
| **BD Timezone** | Bangladesh timezone (UTC+6) for accurate time-based matching |
| **Today / Yesterday / Custom Date** | Check results for any date |
| **MTG Breakdown** | Shows exact MTG level for each WIN (WIN¹ = MTG1, WIN² = MTG2, etc.) |
| **Premium Emoji Output** | Results formatted with Telegram Premium animated emojis (if enabled) |
| **No-Data Handling** | Signals with no candle data reported as ❓ and excluded from win-rate |

### Output Report
```
▰▱▱ 𝚀𝚄𝙰𝙽𝚃𝙴𝚇 𝙱𝙾𝚃 𝙲𝙷𝙴𝙲𝙺𝙴𝚁 ▱▱▰
━━━━━━━━━━━ • ━━━━━━━━━━━
M1 EURUSD_OTC  14:35 BUY  ✅
M1 GBPUSD_OTC  15:00 SELL ✅¹
M1 AUDUSD_OTC  15:35 BUY  ✖️
M1 USDJPY_OTC  16:00 PUT  ⚖️ (doji)
━━━━━━━━━━━ • ━━━━━━━━━━━
🏆 Total : 4
✅ Win   : 2
✖️ Loss  : 1
```

---

## 6. MTG (Martingale) System

If the first signal results in a LOSS, QUANTEX-BOT activates a **Martingale recovery trade**.

- MTG 1 — one recovery step
- MTG 2 — two recovery steps (double recovery)
- Non-MTG — no recovery (single signal only)
- Results tracked as: WIN, WIN¹ (MTG1 win), WIN² (MTG2 win), LOSS
- In Future Live mode, MTG fires automatically at the next candle minute

---

## 7. Chart Generation

Every signal includes a professional candlestick chart.

### Signal Chart
- Recent candles with entry point marked
- Direction color coding (green = BUY, red = SELL)
- Proprietary indicator overlays
- Historical win-rate statistics

### Live Signal Chart
- Dedicated chart for Live Signal / channel broadcast mode
- Support & Resistance levels marked

### Result Chart
- WIN/LOSS result overlay
- MTG entries annotated
- DOJI candle shown in amber color

---

## 8. Telegram Premium Integration

Connect your Telegram account to unlock **Premium Emoji** signal formatting.

### How It Works
1. Tap **Premium** in the bot menu
2. Tap **Connect Telegram Account**
3. Secure browser-based login opens (WebApp)
4. Enter credentials and phone number
5. Enter verification code + optional 2FA
6. Connected — Premium mode active

### What It Unlocks
- Animated premium emojis in signal and checker outputs
- Signals sent via your own Telegram account
- Richer, more visually distinctive formatting

### Security
- Encrypted session storage with auto-reconnection
- 2FA fully supported
- Login tokens expire in 30 minutes if unused
- Admin can lock/unlock premium per user

---

## 9. Free Bots Mission

**"10 Powerful Premium Bots — 100% FREE"**

QUANTEX-BOT includes a dedicated **Free Bots** section where a collection of 10 premium-grade trading tools are being released step by step, completely free for all QUANTEX users.

### Currently Released
| Bot | Description |
|---|---|
| 🚀 **HUNTER X QUANTEX** | Advanced Live Signal Software — real-time signals, automatic result tracking, bad market filter, multi-pair analysis, unlimited daily sessions |
| 🐉 **DRAGON X QUANTEX** | Live OTC Signal Pro — 90%+ OTC accuracy, instant UP/DOWN signals, entry timer, high-confidence levels |
| 🖤 **BLACKOUT FUTURE AI** | Advanced Future Signal System — AI-powered engine, 80–95% accuracy, smart pair & time selection, real-time + historical data |

### Coming Soon (7 More)
Bots 4 through 10 are locked and will be released progressively. Follow [@Quantexbot1](https://t.me/Quantexbot1) to be notified when each new free bot drops.

> All free bots are accessible directly inside QUANTEX-BOT — no separate download or registration needed.

---

## 10. Bot Builder

**Coming Soon — Build Your Own Bot Without Any Coding**

The **Bot Builder** is an upcoming feature that will allow anyone — even with zero coding knowledge — to build and customize their own trading signal bot directly from QUANTEX-BOT.

### What It Will Do
- Step-by-step bot creation wizard inside Telegram
- No coding required — fully visual, button-based setup
- Customize signal format, branding, pairs, and settings
- Deploy the bot to your own Telegram channel
- Use it for personal trading or share it with your community
- Powered by QUANTEX's signal engine in the backend

> Currently shows "Coming Soon" in the bot. Full release date to be announced on [@Quantexbot1](https://t.me/Quantexbot1).

---

## 11. Session Management

QUANTEX-BOT handles multiple concurrent users with independent sessions.

### Session States
| State | Description |
|---|---|
| `IDLE` | User is at main menu |
| `RUNNING` | Active signal session in progress |
| `SETUP` | In configuration wizard |
| `PAUSED` | Paused (sleep mode) |
| `FLIVE_RUNNING` | Future Live session active |

### Configuration Options
1. **Chat** — DM or group/channel
2. **Username** — Broker username for tracking
3. **Mode** — Single pair or Auto (best signal from all)
4. **Market Type** — OTC or Live
5. **Trading Pairs** — Specific pairs or "All"
6. **Premium Mode** — Telegram Premium emojis (if connected)
7. **Charts** — Enable/disable signal and result charts
8. **Partial Reports** — Auto-report interval

---

## 12. Sleep Mode System

Bot automatically **pauses** during high-volatility hours.

- **Default window**: 7:00 PM → 10:00 PM daily
- All active sessions stopped; licensed users notified
- Bot resumes automatically at 10:00 PM with notification
- Admin can exempt specific users or disable entirely
- Custom sleep windows configurable

---

## 13. Scheduled Sessions

Auto-start sessions at specific times each week.

1. Select days (Mon–Sun, any combination)
2. Set start time and optional stop time
3. Bot fires session automatically with a pre-alert notification

---

## 14. Partial Report System

Real-time performance reports at configurable intervals.

Intervals: Every 5 / 10 / 15 / 30 / 60 minutes, or manual only.

```
📊 PARTIAL REPORT — 15:30
━━━━━━━━━━━━━━━━━━━━━━
Session: @username
Signals Sent : 6
✅ WIN        : 4
❌ LOSS       : 1
⚖️ DOJI       : 0
🔄 MTG WIN    : 1
━━━━━━━━━━━━━━━━━━━━━━
Win Rate     : 83.3%
```

---

## 15. Referral Program

Earn rewards by inviting others to QUANTEX-BOT.

- Each user gets a unique referral link
- Each verified referral is tracked
- Reaching milestones generates exclusive promo codes
- Dashboard shows total, pending, and confirmed referrals
- Admin can view and manage all referral activity

---

## 16. Reviews & Ratings System

Community-driven trust system.

- Users submit star ratings (1–5)
- Reviews verified against active accounts
- Bot displays current average rating publicly
- Total review count tracked
- Admin can view full review history

---

## 17. License & Access System

### License Types
| Type | Duration | Access |
|---|---|---|
| Monthly | 30 days | Full access |
| Quarterly | 90 days | Full access |
| Semi-Annual | 180 days | Full access |
| Lifetime | Permanent | Full access + VIP |

### Granular Permissions
Per-user feature permissions: `can_live`, `can_future`, `can_checker`.

### Promo Codes
- Admin-issued or earned via referral program
- Discounts or free trial access

Encrypted license keys tied to Telegram user ID — non-transferable.

---

## 18. Admin Control Panel

| Action | Function |
|---|---|
| Broadcast | Send to all or licensed users |
| Grant / Revoke License | Manage user access |
| Add / Set Points | Grant feature-use points |
| Set Unlimited Points | Unlimited access for a user |
| Set Live Quota | Control daily Live Signal limit |
| Pair On/Off | Enable/disable trading pairs globally |
| Maintenance Mode | Enable with custom message |
| Sleep Exempt | Exempt users from sleep mode |
| Premium Lock / Unlock | Control premium access per user |
| View All Users | Full user list with status |
| View Referrals | All referral activity |
| Manage Promos | Create and deactivate promo codes |
| Signal Stats | Market-wide signal performance stats |
| Broadcast Log | History of past broadcasts |
| Ban / Unban Users | Block specific users from the bot |

---

## 19. Points & Quota System

### Points (Free Feature Access)
- Admin grants points to users
- Each Future Signal or Signal Check use costs 1 point
- Licensed users have unlimited access
- Admin can set "unlimited points" per user

### Live Signal Quota
- Free users get a set number of daily live signals
- Quota visible in bot menu with remaining count
- Admin can increase quota per user
- Licensed users have unlimited daily signals

### Future Live Session Quota
- Free users get **3 Future Live sessions** total (lifetime)
- Licensed users have unlimited sessions

---

## 20. Database — PostgreSQL Backend

QUANTEX-BOT v3 uses **PostgreSQL** for all persistent storage.

All data is managed through a dedicated `db_postgres.py` module with connection pooling for efficient concurrent multi-user access.

### Data Managed
- User accounts, license data, permissions
- Signal history and market statistics
- Session configurations and schedules
- Referral tracking and promo codes
- Review and rating data
- Points, quotas, and limits
- Admin settings and ban lists
- Future Live session data
- Broadcast logs
- Favorite pair lists

---

## 21. Supported Markets & Pairs

- **OTC Forex** — 40+ major, minor, and exotic pairs (Quotex)
- **OTC Stocks** — Popular global stocks (FB, MSFT, BA, MCD, PFE, JNJ, AXP, INTC)
- **OTC Crypto** — Bitcoin, Ethereum, XRP, SOL, TON, BNB, and 20+ more
- **OTC Commodities** — Gold (XAUUSD), Silver (XAGUSD), US Crude, UK Brent
- **OTC Indices** — US, European, and Asian market indices
- **Live Forex** — 30+ major and minor Forex pairs

---

## 22. Multi-Platform Support

| Platform | Support |
|---|---|
| **Windows** | ✅ Full |
| **Linux** | ✅ Full |
| **macOS** | ✅ Full |
| **Android (Termux)** | ✅ Full |

Auto dependency installer handles all required packages on first run — zero manual setup.

---

## 📞 Support

- **Telegram**: [@X_Akash_Owner](https://t.me/X_Akash_Owner)
- **Email**: [quantexbotsupport@gmail.com](mailto:quantexbotsupport@gmail.com)
- **Channel**: [@Quantexbot1](https://t.me/Quantexbot1)
- **Bot**: [@QuantexBinaryTools_bot](https://t.me/QuantexBinaryTools_bot)
