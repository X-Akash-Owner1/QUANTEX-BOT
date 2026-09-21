# 🔮 QUANTEX-BOT v4 — Complete Feature Documentation

> **Official Telegram Bot**: [@QuantexBinaryTools_bot](https://t.me/QuantexBinaryTools_bot)  
> **Developer**: [@X_Akash_Owner](https://t.me/X_Akash_Owner)

---

## 📋 Feature Index

1. [Live Signal Engine](#1-live-signal-engine)
2. [AI-Assisted Live Signal System](#2-ai-assisted-live-signal-system)
3. [Live Signal Broadcast System](#3-live-signal-broadcast-system)
4. [Future Live Signal System](#4-future-live-signal-system)
5. [Signal Checker — Full Suite](#5-signal-checker--full-suite)
6. [News Signal System](#6-news-signal-system)
7. [Signal Tools](#7-signal-tools)
8. [MTG (Martingale) System](#8-mtg-martingale-system)
9. [Chart Generation](#9-chart-generation)
10. [Telegram Premium Integration](#10-telegram-premium-integration)
11. [Free Bots Mission](#11-free-bots-mission)
12. [Bot Builder](#12-bot-builder)
13. [Auto Payment System](#13-auto-payment-system)
14. [Session Management](#14-session-management)
15. [Sleep Mode System](#15-sleep-mode-system)
16. [Scheduled Sessions](#16-scheduled-sessions)
17. [Partial Report System](#17-partial-report-system)
18. [Referral Program](#18-referral-program)
19. [Reviews & Ratings System](#19-reviews--ratings-system)
20. [Subscription & Access System](#20-subscription--access-system)
21. [Admin Control Panel](#21-admin-control-panel)
22. [Points & Quota System](#22-points--quota-system)
23. [Database — PostgreSQL Backend](#23-database--postgresql-backend)
24. [Supported Markets & Pairs](#24-supported-markets--pairs)
25. [Multi-Platform Support](#25-multi-platform-support)
26. [Web Control Dashboard](#26-web-control-dashboard)
27. [Session Log Viewer](#27-session-log-viewer)
28. [Strategy Intelligence Dashboard](#28-strategy-intelligence-dashboard)

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

### 🧠 Machine Learning Signal Engine

QUANTEX-BOT's signal engine is powered by an adaptive **machine learning-based analysis system** that continuously learns from real market results:

| Feature | Description |
|---|---|
| **3 Analyzer Engines** | QUANTUM SCAN (Dynamic MTF + Structure), SMART FOCUS (Best Quality Market Analyzer), HYBRID ENGINE (MTF + Structure + Trap, Score 75+) |
| **20+ Analysis Modules** | Each signal passes through independent modules: Trend Continuation, Break of Structure, Change of Character, Engulfing Reversal, MACD Cross, RSI Divergence, Bollinger Breakout, Pin Bar, MTF Confluence, VWAP Reversion, Ichimoku, Fibonacci Pullback, Candlestick Patterns, Supertrend+PSAR, CCI Extreme, Multi-Indicator Confluence, Tweezer Reversal, Three Black Crows, and more |
| **Multi-Timeframe Analysis** | M1, M2, M3, M5, M10, M15 timeframe support with real clock-boundary aggregation |
| **Auto Strategy Optimization** | Strategies are continuously trained on live signal results — per-pair, per-timeframe parameter overrides applied automatically |
| **Self-Healing Performance** | When a strategy underperforms, the system detects it and automatically adjusts — performance improves continuously over time |
| **Strategy Intelligence Dashboard** | Admin browser dashboard showing real-time strategy performance, win rates, and auto-optimization status per pair and timeframe |
| **Score-Based Filtering** | Every signal scored by multiple independent engines; only signals meeting the minimum confidence threshold (79+) are delivered |
| **Weighted Module System** | Module performance weights updated based on historical results — stronger-performing modules carry more influence |

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
- **Live Signal Quota** — every tier has its own daily live-signal limit; INFINITY subscribers have unlimited access
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
Free users get **3 Future Live sessions** total. Subscribed users have unlimited sessions.

---

## 5. Signal Checker — Full Suite

QUANTEX-BOT v4 features a completely rebuilt, **super-fast, 100% accurate** signal checking suite with five checker modes.

### ⚡ Super-Fast & 100% Accurate
- **Local candle cache system** — candle data stored locally for near-instant lookup
- **O(1) time index** — pre-built HH:MM → candle index map eliminates sequential searching
- **File-level cache** — JSON candle files cached in memory, only re-read when file changes
- **Archive + recent data** — checks both today's live data and historical archive files
- **100% accurate results** — direct candle close/open comparison, no estimation

### 🔍 Five Checker Modes

#### 1. Live Checker *(New in v4.0)*
Signal checker for **real/live market pairs** — identical accuracy and feature set as OTC Checker but applied to live forex pairs.
- Paste live market signals → instant WIN/LOSS per signal
- Full MTG breakdown and DOJI detection
- Premium emoji formatted output

#### 2. OTC Checker
Standard binary options signal checker for OTC pairs.
- Paste signals → instant WIN/LOSS per signal
- Supports unlimited signals per check
- Real payout data per signal slot
- MTG result shown with superscript level (WIN¹, WIN², etc.)
- DOJI candles handled and displayed separately

#### 3. Blackout Checker
A special checker mode for **Blackout-style signals** (signals with no direction).
- Determines direction automatically from the **previous candle** color
- Previous GREEN candle → expected direction: PUT
- Previous RED candle → expected direction: BUY
- DOJI previous candle → result shown as `[doji]`
- Checks entry candle + MTG steps against expected direction

#### 4. Whiteout Checker
Similar to Blackout but uses the **same-direction** logic from the previous candle.
- Previous GREEN candle → expected direction: BUY
- Previous RED candle → expected direction: PUT
- All other logic identical to Blackout checker

#### 5. Custom Date Checker
Check signals for **any specific date**, not just today/yesterday.
- Enter any past date
- Bot fetches archived candle data for that date
- Full WIN/LOSS report for the chosen date
- Works across all checker modes (OTC, Live, Blackout, Whiteout)

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

## 6. News Signal System

*(New in v4.0)* — AI-powered trading signals derived from the Forex Factory **economic calendar**.

### How It Works

**Step 1 — Calendar Fetch**  
QUANTEX-BOT pulls live economic event data from the Forex Factory JSON feed. No Selenium, no scraping — reliable structured data.

**Step 2 — Filter Events**  
Events are filtered by:
- **Impact Level** — HIGH, MEDIUM, LOW, or All
- **Day Range** — events for the next 1, 2, or 3 days ahead
- **Currency** — only currencies relevant to your selected trading pairs

**Step 3 — AI Direction Analysis**  
Each event is sent to the Gemini AI model, which assigns:
- **BULLISH** or **BEARISH** bias for the event currency
- **Confidence score** (60–95%)
- **Rationale** — 1–2 sentence explanation

**Step 4 — Heuristic Blend**  
If AI analysis is unavailable, a built-in heuristic engine derives bias from `forecast vs previous` (with inversion logic for unemployment, jobless claims, etc.).

**Step 5 — Technical Structure Blend**  
A lightweight 30-day technical read (trend + momentum) is blended with the fundamental bias. Agreement boosts confidence; disagreement reduces it.

**Step 6 — CALL/PUT Pair Mapping**  
The currency bias is automatically mapped to CALL and PUT recommendations across all your selected pairs:
- Currency BULLISH → CALL on base pairs, PUT on quote pairs
- Currency BEARISH → PUT on base pairs, CALL on quote pairs

### Supported Pairs — 29 Pairs
```
EUR/USD · GBP/USD · USD/JPY · USD/CHF · AUD/USD · USD/CAD · NZD/USD
EUR/GBP · EUR/JPY · EUR/CHF · EUR/AUD · EUR/CAD · EUR/NZD
GBP/JPY · GBP/CHF · GBP/AUD · GBP/CAD · GBP/NZD
AUD/JPY · AUD/CHF · AUD/CAD · AUD/NZD
CAD/JPY · CAD/CHF · CHF/JPY
NZD/JPY · NZD/CHF · NZD/CAD
XAU/USD
```

### Features
- Caches analysis results per event — first user pays the AI cost, everyone else gets it instantly
- Analysis expires after the event's release time to ensure freshness
- Formatted with premium emoji signal cards
- Available as a standalone module in the main bot and as a selectable module in Bot Builder

---

## 7. Signal Tools

*(New in v4.0)* — A set of utility tools to reformat, adjust, and analyze signal lists.

### 🗂️ Signal Formatter
Paste any signal list in any format — the Formatter normalizes and rebuilds it into a clean, standardized card layout.
- Supports all common signal formats (any source)
- Useful for re-sharing or archiving signal lists cleanly

### 🔄 Swap C/P
Paste a signal list → every **CALL** becomes **PUT** and every **PUT** becomes **CALL** — instantly. Useful for reversing a strategy direction.

### 🌐 TZ Converter
Paste signal entry times in one timezone → receive them converted to any other timezone. Supports all standard UTC offsets.

### 📊 Market Filters
Shows which live markets are currently in **stable, tradeable conditions** right now — helping you avoid choppy or low-volatility pairs before entering a session.

---

## 8. MTG (Martingale) System

If the first signal results in a LOSS, QUANTEX-BOT activates a **Martingale recovery trade**.

- MTG 1 — one recovery step
- MTG 2 — two recovery steps (double recovery)
- Non-MTG — no recovery (single signal only)
- Results tracked as: WIN, WIN¹ (MTG1 win), WIN² (MTG2 win), LOSS
- In Future Live mode, MTG fires automatically at the next candle minute

---

## 9. Chart Generation

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

## 10. Telegram Premium Integration

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

## 11. Free Bots Mission

**"10 Powerful Premium Bots — 100% FREE"**

QUANTEX-BOT includes a dedicated **Free Bots** section where a collection of 10 premium-grade trading tools are being released step by step, completely free for all QUANTEX users.

### Currently Released
| Bot | Description |
|---|---|
| 🚀 **HUNTER X QUANTEX** | Advanced Live Signal Software — real-time signals, automatic result tracking, bad market filter, multi-pair analysis, unlimited daily sessions |
| 🐉 **DRAGON X QUANTEX** | Live OTC Signal Pro — 90%+ OTC accuracy, instant UP/DOWN signals, entry timer, high-confidence levels |
| 🖤 **BLACKOUT FUTURE AI** | Advanced Future Signal System — AI-powered engine, 80–95% accuracy, smart pair & time selection, real-time + historical data |
| ⚡ **STORM X QUANTEX** | Premium trading bot — details coming soon |
| 👻 **PHANTOM X QUANTEX** | Premium trading bot — details coming soon |

### Coming Soon (5 More)
Bots #6–10 are locked and will be released progressively. Follow [@Quantexbot1](https://t.me/Quantexbot1) to be notified when each new free bot drops.

> All free bots are accessible directly inside QUANTEX-BOT — no separate download or registration needed.

---

## 12. Bot Builder

**PLUS & INFINITY Subscribers — Build Your Own Bot Without Any Coding**

The **Bot Builder** lets anyone — even with zero coding knowledge — build, customize, and deploy their own white-label trading signal bot directly from QUANTEX-BOT.

### Plan Limits
| Plan | Max Bots |
|---|---|
| 🆓 FREE | 0 (not available) |
| 🟢 STARTER | 1 bot |
| 💎 PLUS | **3 bots** |
| 👑 INFINITY | **10 bots** |

### What It Does
- Step-by-step bot creation wizard inside Telegram — paste your @BotFather token and go
- No coding required — fully visual, button-based setup
- Customize display name, description, welcome message, support/community links, theme, and language
- Choose which modules appear in your bot — all modules available:
  - **Core**: Live Session, Schedule, Settings
  - **Checkers**: Live Checker, OTC Checker, Blackout Checker, Whiteout Checker
  - **Future Signals**: OTC Market FS, Live Market FS, Blackout FS, Whiteout FS, Future Live
  - **Signals**: Live Signal, Live Payouts, News Signal
  - **Tools**: Formatter, Market Filters, Swap C/P, TZ Converter
  - **User**: Profile, Referral, Upgrade, About, Reviews, Help
- **Custom AI Prompt** — set a custom AI instruction used by your bot's AI confirmation layer
- **Notification Template** — customize the default announcement text in your Child Admin Panel
- Customize your bot's core message templates (signal titles, result titles, checker headers, etc.)
- One-tap **Deploy** — your bot goes live immediately with a working webhook
- Manage your bot anytime — start, stop, restart, or delete from **My Bots**
- **Child Admin Panel** — full admin panel for managing your deployed bot's users (ban, license, points, broadcast)
- **Session Log Viewer** — view real-time diagnostic logs for active sessions in your deployed bot
- Powered by QUANTEX's signal engine in the backend

---

## 13. Auto Payment System

*(New in v4.0)* — Subscribe to any plan **instantly and automatically**, directly inside the bot — no need to contact the owner manually.

### Supported Payment Methods

| Method | Details |
|---|---|
| **Binance Pay** | Binance Pay ID: **1133439955** — instant transfer via Binance app |
| **TRC20 USDT** | USDT on the TRON network — wallet address provided in-bot |
| **BEP20 USDT** | USDT on the BNB Smart Chain — wallet address provided in-bot |

### How It Works
1. Tap **🪄 Upgrade** inside the bot
2. Select your plan (STARTER, PLUS, or INFINITY)
3. Choose your payment method (Binance Pay, TRC20, or BEP20)
4. Send the exact USDT amount to the provided address/ID
5. Bot automatically verifies the payment via API
6. Subscription is activated instantly — no manual approval needed

### Payment Rules
- **60-minute expiry window** — payment must be completed within 60 minutes of initiating the request
- **Amount tolerance** — minor blockchain/fee differences handled automatically
- **Auto-verification** — Binance Pay verified via Binance API; on-chain USDT verified via TronGrid (TRC20) and BSC RPC (BEP20)
- You can always contact [@X_Akash_Owner](https://t.me/X_Akash_Owner) for manual activation if preferred

---

## 14. Session Management

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
1. **Broker** — Quotex or Tradowix
2. **Chat** — DM or group/channel
3. **Username** — Broker username for tracking
4. **Mode** — Single pair or Auto (best signal from all)
5. **Market Type** — OTC or Live
6. **Trading Pairs** — Specific pairs or "All"
7. **Premium Mode** — Telegram Premium emojis (if connected)
8. **Charts** — Enable/disable signal and result charts
9. **Partial Reports** — Auto-report interval

---

## 15. Sleep Mode System

Bot automatically **pauses** during high-volatility hours.

- **Default window**: 7:00 PM → 10:00 PM daily
- All active sessions stopped; subscribed users notified
- Bot resumes automatically at 10:00 PM with notification
- Admin can exempt specific users or disable entirely
- Custom sleep windows configurable

---

## 16. Scheduled Sessions

Auto-start sessions at specific times each week.

1. Select days (Mon–Sun, any combination)
2. Set start time and optional stop time
3. Bot fires session automatically with a pre-alert notification

---

## 17. Partial Report System

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

## 18. Referral Program

Earn rewards by inviting others to QUANTEX-BOT.

- Each user gets a unique referral link
- Each verified referral is tracked
- Reaching milestones generates exclusive promo codes
- Dashboard shows total, pending, and confirmed referrals
- Admin can view and manage all referral activity

---

## 19. Reviews & Ratings System

Community-driven trust system.

- Users submit star ratings (1–5)
- Reviews verified against active accounts
- Bot displays current average rating publicly
- Total review count tracked
- Admin can view full review history

---

## 20. Subscription & Access System

### Subscription Tiers
| Tier | Price | Access Level |
|---|---|---|
| 🆓 FREE | $0 | Limited daily usage |
| 🟢 STARTER | $18/month | Higher usage limits, premium templates, 1 bot in Bot Builder |
| 💎 PLUS | $32/month | 10× usage, full template customization, Web Control, Bot Builder (3 bots) |
| 👑 INFINITY | $49/month | Unlimited usage, Bot Builder (10 bots), full control |

Subscriptions can be activated for any duration (custom days or permanent) at any tier — the tier determines *what* you can access, the duration determines *how long*.

### Purchase Options
- **Auto Payment** — instant self-serve activation via Binance Pay, TRC20 USDT, or BEP20 USDT
- **Manual** — contact [@X_Akash_Owner](https://t.me/X_Akash_Owner) directly

### Granular Permissions
Per-user feature permissions and daily-usage limits are enforced automatically based on subscription tier.

### Promo Codes
- Admin-issued or earned via referral program
- Discounts or free trial access

Subscriptions are tied to your Telegram user ID — non-transferable.

---

## 21. Admin Control Panel

Available to the bot owner and delegated sub-admins via Telegram commands and a browser-based Web Admin Panel.

> Details of admin controls are not publicly disclosed.



---

## 22. Points & Quota System

### Points (Free Trial Access)
- Admin grants bonus points to users
- Each Future Signal or Signal Check use can cost 1 point for free-trial access
- Subscribed users use their tier's daily quota instead
- Admin can set "unlimited points" per user

### Daily Signal Quotas (Tier-Based)
- Every tier (FREE, STARTER, PLUS, INFINITY) has its own daily Future Signal and Live Signal allowance
- Quota only counts signals actually delivered to you — quiet scan cycles that find nothing don't use your quota
- Quota remaining is shown live in your profile and in Web Control
- INFINITY subscribers have unlimited daily signals

### Future Live Session Quota
- Free users get a limited number of Future Live sessions
- Subscribed users have unlimited sessions

---

## 23. Database — PostgreSQL Backend

QUANTEX-BOT v4 uses **PostgreSQL** for all persistent storage.

All data is managed through a dedicated `db_postgres.py` module with connection pooling for efficient concurrent multi-user access.

### Data Managed
- User accounts, subscription data, permissions
- Signal history and market statistics
- Session configurations and schedules
- Referral tracking and promo codes
- Review and rating data
- Points, quotas, and limits
- Admin settings and ban lists
- Future Live session data
- Broadcast logs
- Favorite pair lists
- News signal analysis cache (per-event, expires at release time)
- Bot Builder (studio) data — bots, features, labels, texts, users, licenses, quotas
- Session log entries (per active session, in-memory)

---

## 24. Supported Markets & Pairs

### Quotex — Supported Pairs
- **OTC Forex** — 55+ major, minor, and exotic pairs
- **OTC Crypto** — Bitcoin (BTC), Ethereum (ETH), XRP, SOL, TON, BNB, BCH, DOT, ETC, ZEC, ATO, AVA, AXS, DAS, LIN, LTC, TRU and more
- **OTC Commodities** — Gold (XAUUSD), Silver (XAGUSD), US Crude, UK Brent
- **Live Forex** — 29 major and minor pairs: AUDCAD, AUDCHF, AUDJPY, AUDUSD, AXJAUD, CADJPY, CHFJPY, EURAUD, EURCAD, EURCHF, EURGBP, EURJPY, EURUSD, F40EUR, FTSGBP, GBPAUD, GBPCAD, GBPCHF, GBPJPY, GBPUSD, HSIHKD, IBXEUR, JPXJPY, STXEUR, USDCAD, USDCHF, USDJPY, XAUUSD

### Tradowix — Supported Pairs
**100+ pairs across all categories:**

**OTC Forex (major/minor/exotic):**
AUDCAD_otc, AUDCHF_otc, AUDJPY_otc (also AUDJPY live), AUDNZD_otc, AUDUSD_otc (also AUDUSD live), CADCHF_otc, CADJPY_otc, CHFJPY_otc, EURAUD_otc (also EURAUD live), EURCAD_otc (also EURCAD live), EURCHF_otc (also EURCHF live), EURGBP_otc (also EURGBP live), EURJPY_otc (also EURJPY live), EURNZD_otc, EURSGD_otc, EURUSD_otc (also EURUSD live), GBPAUD_otc, GBPCAD_otc, GBPCHF_otc, GBPJPY_otc (also GBPJPY live), GBPNZD_otc, GBPUSD_otc (also GBPUSD live), NZDCAD_otc, NZDCHF_otc, NZDJPY_otc, NZDUSD_otc, USDARS_otc, USDBDT_otc, USDBRL_otc, USDCAD_otc (also USDCAD live), USDCHF_otc (also USDCHF live), USDCOP_otc, USDDZD_otc, USDEGP_otc, USDIDR_otc, USDINR_otc, USDJPY_otc (also USDJPY live), USDMXN_otc, USDNGN_otc, USDPHP_otc, USDPKR_otc, USDTRY_otc, USDZAR_otc

**OTC Crypto:**
APTUSD_otc, ARBUSD_otc, ATOMUSD_otc, AVAXUSD_otc, AXSUSD_otc, BCHUSD_otc, BNBUSD_otc, BTCUSD_otc (also BTCUSD live), COPPERUSD_otc, DASHUSD_otc, DOGEUSD_otc, DOTUSD_otc, ETCUSD_otc, ETHUSD_otc (also ETHUSD live), GALAUSD_otc, LINKUSD_otc, LTCUSD_otc, MANAUSD_otc, MELANIAUSD_otc, OAIA_otc, SOLUSD_otc, TIAUSD_otc, TONUSD_otc, TRUMPUSD_otc, TRXUSD_otc, WIFUSD_otc, XRPUSD_otc

**OTC Stocks:**
AAPL_otc, AMD_otc, AMZN_otc, ANTH_otc, AXP_otc, BA_otc, DIS_otc, GOOG_otc, GS_otc, INTC_otc, JNJ_otc, JPM_otc, KO_otc, MCD_otc, META_otc, MSFT_otc, NFLX_otc, NKE_otc, NVDA_otc, PFE_otc, TSLA_otc, V_otc, WMT_otc, XOM_otc

**OTC Commodities:**
BCOUSD_otc (Brent), WTIUSD_otc (WTI/US Crude), XAGUSD_otc, XAUUSD_otc, XPDUSD_otc (Palladium), XPTUSD_otc (Platinum)

---

## 25. Multi-Platform Support

| Platform | Support |
|---|---|
| **Windows** | ✅ Full |
| **Linux** | ✅ Full |
| **macOS** | ✅ Full |
| **Android (Termux)** | ✅ Full |

Auto dependency installer handles all required packages on first run — zero manual setup.

---

## 26. Web Control Dashboard

A browser-based control panel for your account, available directly inside Telegram as a **Mini App** — no separate website login required, it opens using your existing Telegram session.

### Who Can Access It
| Tier | Access Level |
|---|---|
| 🆓 FREE / 🟢 STARTER | View-only — profile, plan status, and pricing |
| 💎 PLUS / 👑 INFINITY | Full control — every feature below |

### What You Can Do
- **Live Profile** — see your current plan, daily signal credits used/remaining, and referral stats in real time
- **Timezone Management** — set the clock offset for every signal type from one screen, with instant live preview
- **Template Customization** — visually edit your Live Session and Live Signal message templates (titles, chart labels, watermark, footer)
- **Referral Sharing** — copy or share your referral link with one tap
- **Upgrade / Pricing** — see all subscription tiers and a direct link to purchase or change plans

### Security
- Authenticated using Telegram's own signed session data — no separate password to create or remember
- All changes sync instantly with the bot itself

---

## 27. Session Log Viewer

*(New in v4.0)* — A real-time **diagnostic log** for every active live signal session.

### What It Tracks
Every event in the signal loop is logged in real time:
- **Scan** — each pair scanned (pair name + timestamp)
- **Signal** — every signal generated (pair, direction, time)
- **Reject** — pairs that failed the confidence filter (with reason)
- **Info** — general session events (start, stop, resume)

### Storage Design
- Implemented in `session_log_store.py` — a lightweight shared in-memory module
- Log is scoped to **one active session per user** — automatically cleared when the session stops
- Signal entries are **never evicted** for the session's lifetime (complete history guaranteed)
- General log entries capped at 20,000 entries to prevent unbounded memory growth

### Access
- Accessible from the **Web Control Dashboard** and from **Bot Builder's Child Admin Panel**
- Reopening the log page shows the full accumulated history without missing entries
- Available to both the main bot owner and to Bot Builder child bot owners

---

## 28. Strategy Intelligence Dashboard

*(New in v4.0)* — A **browser-based strategy analysis tool** hosted at `/strategy_intelligence` in the web panel.

- Visual strategy intelligence interface for reviewing market conditions and signal setups
- Accessible from the Web Control / Admin Panel
- No coding required — browser-based, opens from a Telegram Mini App link
- Real-time strategy performance, win rates, and auto-optimization status per pair and timeframe

### How Strategy Intelligence Works

- **Live Training**: Every signal result (WIN/LOSS/DOJI) is logged with the full strategy configuration snapshot used to generate it
- **Per-Pair, Per-Timeframe Learning**: Each combination of pair + timeframe develops its own optimized parameter profile over time
- **Auto-Recovery**: When a strategy's win rate drops below threshold, the system automatically adjusts parameters — the engine self-heals without manual intervention
- **Continuous Improvement**: The longer the bot runs, the smarter it gets — performance increases naturally as the ML engine accumulates more signal data
- **Admin Visibility**: Real-time dashboard shows strategy performance across all pairs, timeframes, and analyzer types

---

## 📞 Support

- **Telegram**: [@X_Akash_Owner](https://t.me/X_Akash_Owner)
- **Email**: [quantexbotsupport@gmail.com](mailto:quantexbotsupport@gmail.com)
- **Channel**: [@Quantexbot1](https://t.me/Quantexbot1)
- **Community Group**: [t.me/quantexlounge](https://t.me/quantexlounge)
- **Bot**: [@QuantexBinaryTools_bot](https://t.me/QuantexBinaryTools_bot)