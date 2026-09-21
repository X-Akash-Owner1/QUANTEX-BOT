# 🗺️ QUANTEX-BOT — Development Roadmap

> **Official Bot**: [@QuantexBinaryTools_bot](https://t.me/QuantexBinaryTools_bot)  
> **Developer**: [@X_Akash_Owner](https://t.me/X_Akash_Owner)

---

## ✅ v1.x — Foundation
- [x] Core signal engine
- [x] Basic Telegram bot integration
- [x] OTC pair support

---

## ✅ v2.0 — Full Bot System
- [x] Multi-user Telegram Bot Manager
- [x] Signal Result Auto-Checker
- [x] MTG (Martingale) Recovery System
- [x] Candlestick Chart Generation
- [x] Backtest Statistics
- [x] Session Management
- [x] Sleep Mode
- [x] Scheduled Sessions
- [x] Partial Performance Reports
- [x] License Key System
- [x] Promo Code System
- [x] Admin Control Panel
- [x] Points System
- [x] Signal Checker Engine
- [x] Future Signal Engine
- [x] Multi-Platform Support
- [x] Quotex OTC + Live support
- [x] Telegram WebApp Login Server

---

## ✅ v3.0 — AI + Live Broadcast + Checker Suite + Free Bots

### 🤖 AI Integration
- [x] AI Signal Confirmation on every Live Signal
- [x] AI Reasoning Output
- [x] Support & Resistance auto-calculation
- [x] Real-Time Payout Display per signal
- [x] AI Confidence Score
- [x] AI Fallback direction when primary analysis fails

### 📡 Live Signal Broadcast
- [x] Channel Broadcasting (Manual & Auto modes)
- [x] Multi-Template Signal Formatting
- [x] Custom Header & Username branding
- [x] MTG in channel broadcast
- [x] Channel permission validation
- [x] Free tier daily signal quota
- [x] Daily quota remaining display
- [x] Live Signal Chart (dedicated)

### ⏱ Future Live Signal System
- [x] Paste any signal list — all formats parsed automatically
- [x] Signals auto-fire at exact scheduled time
- [x] Automatic WIN/LOSS/DOJI result check per signal
- [x] MTG 1 & MTG 2 support in Future Live
- [x] View Signals dashboard (remaining + next signal)
- [x] Session status display with countdown
- [x] Stop session any time
- [x] Full session completion summary
- [x] Free tier: 3 sessions lifetime
- [x] Custom header & username (licensed users)
- [x] Template preview before starting

### 🔍 Signal Checker — 4-Mode Suite
- [x] **OTC Checker** — standard checker rebuilt, super-fast & 100% accurate
- [x] **Blackout Checker** — direction-free signals, reverse previous-candle logic
- [x] **Whiteout Checker** — direction-free signals, follow previous-candle logic
- [x] **Custom Date Checker** — check any specific past date
- [x] O(1) local candle index lookup (pre-built HH:MM map)
- [x] Local candle file cache (near-instant, no API calls needed)
- [x] Archive candle data support (yesterday and custom dates)
- [x] Unicode normalizer (handles bold/italic/fancy Telegram text)
- [x] DOJI detection and separate reporting
- [x] Payout filter per signal (flag low-payout signals)
- [x] MTG breakdown with superscript level
- [x] BD timezone (UTC+6) accurate time matching
- [x] 100+ pair alias normalization
- [x] 60+ OTC + 30+ Live pair support
- [x] Premium emoji formatted output

### 🤖 Free Bots Mission
- [x] Free Bots section added to main menu
- [x] **HUNTER X QUANTEX** — Bot #1 released
- [x] **DRAGON X QUANTEX** — Bot #2 released
- [x] **BLACKOUT FUTURE AI** — Bot #3 released
- [x] **STORM X QUANTEX** — Bot #4 released
- [x] **PHANTOM X QUANTEX** — Bot #5 released
- [ ] Bots #6 through #10 — releasing progressively

### 🏗️ Bot Builder
- [x] Bot Builder button added to main menu
- [x] Full wizard — token verification, branding, module selection, template editing, button builder, review & deploy
- [x] Live deployment — real webhook registration, bot goes live instantly
- [x] My Bots management — start / stop / restart / delete
- [x] Early access released for INFINITY subscribers (1 bot per account)

### 💎 Telegram Premium Integration
- [x] User-account sender (own Telegram account)
- [x] Premium animated emojis in signals and checker
- [x] Secure browser WebApp login (2FA supported)
- [x] Premium lock/unlock per user (admin)
- [x] Token expiry (30 min for unused tokens)

### 👥 Community Features
- [x] Referral Program with unique per-user link
- [x] Referral milestone tracking
- [x] Promo code generation from referrals
- [x] Reviews & Ratings (star system + public average)

### 🗄️ Infrastructure
- [x] PostgreSQL database (upgraded from SQLite)
- [x] Connection pooling for concurrent users
- [x] Granular permissions (can_live, can_future, can_checker)
- [x] Ban cache & subscription cache (fast per-request checks)
- [x] Broadcast log history
- [x] Live payout menu (real-time % for all pairs)
- [x] Favorite pair list management

---

## ✅ v3.x — Tiered Subscriptions + Web Control

### 💳 Tiered Subscription System
- [x] Replaced flat license pricing with FREE / STARTER / PLUS / INFINITY tiers
- [x] Per-tier daily usage limits for Future Signal & Live Signal
- [x] Quota now counts only signals actually delivered, not scan attempts
- [x] "Upgrade" menu with live pricing and one-tap purchase link
- [x] Admin tools to grant/change any tier and duration, with instant user notification

### 🌐 Web Control Dashboard
- [x] Telegram Mini App — opens instantly using existing Telegram session
- [x] Live profile view (plan, credits, referral stats)
- [x] Timezone management for every signal type
- [x] Full template customization (Live Session & Live Signal)
- [x] One-tap referral link sharing
- [x] Gated to PLUS & INFINITY — FREE/STARTER see a view-only + upgrade prompt

### 🛠️ Admin Web Panel
- [x] Full user search & management from the browser
- [x] Licensed / expired subscriber views with in-place tier & duration editing
- [x] Role-based sub-admin presets (Co-Owner, Moderator, Sales, Support, Broadcaster)
- [x] Pair enable/disable toggle list
- [x] Promo code management, points, premium lock, broadcast

---

## ✅ v4.0 — Multi-Broker + Auto Payment + News Signal + Tools + Bot Builder Expansion

### 🏢 Multi-Broker Support
- [x] **Tradowix broker** — fully supported alongside Quotex
- [x] Broker selection in setup wizard
- [x] Per-broker pair support (OTC + Live)
- [x] Admin broker enable/disable toggle (Quotex, Tradowix)

### 💳 Auto Payment System
- [x] Binance Pay integration (ID: 1133439955) — auto-verified via Binance API
- [x] TRC20 USDT wallet — auto-verified via TronGrid API
- [x] BEP20 USDT wallet — auto-verified via BSC RPC
- [x] 60-minute payment expiry window
- [x] Amount tolerance for minor blockchain fee differences
- [x] Instant subscription activation — no manual approval needed
- [x] Self-serve flow entirely inside the bot

### 📰 News Signal System
- [x] Forex Factory economic calendar JSON feed integration
- [x] AI-powered direction analysis via Gemini (BULLISH / BEARISH / NEUTRAL)
- [x] Heuristic fallback (forecast vs previous, with inversion for negative metrics)
- [x] 30-day technical structure blend (trend + momentum)
- [x] Per-event analysis caching (expires at release time)
- [x] Filter by impact: HIGH / MEDIUM / LOW / All
- [x] Filter by days ahead: 1, 2, or 3 days
- [x] 29 supported pairs (major forex + XAU/USD)
- [x] Automatic CALL/PUT pair mapping from currency bias
- [x] Premium emoji formatted signal cards
- [x] Available as a standalone module and in Bot Builder

### 🔍 Signal Checker — 5th Mode Added
- [x] **Live Checker** — new checker mode for real/live market pairs
- [x] Full feature parity with OTC Checker (MTG, DOJI, payout filter, premium emoji)

### ⏱ Future Signal Modes — Expanded
- [x] **Live Market FS** — future signal sessions for live market pairs
- [x] **Blackout FS** — future signal sessions for blackout-style signals
- [x] **Whiteout FS** — future signal sessions for whiteout-style signals

### 🛠️ Signal Tools (New Category)
- [x] **Signal Formatter** — reformat any signal list into a clean card layout
- [x] **Swap C/P** — flip all CALL/PUT directions in a pasted signal list
- [x] **TZ Converter** — convert signal entry times to any other timezone
- [x] **Market Filters** — show which markets are currently stable

### 🏗️ Bot Builder — Major Expansion
- [x] PLUS plan: up to **3 bots** per account (previously 1)
- [x] INFINITY plan: up to **10 bots** per account (previously 1)
- [x] **Custom AI Prompt** per child bot — extra instruction for AI confirmation
- [x] **Notification Template** — customize default announcement text in Child Admin
- [x] **Child Admin Panel** — full admin panel for each deployed child bot
- [x] **Session Log Viewer** — real-time diagnostic log for sessions in child bots
- [x] All new modules selectable in Bot Builder (News Signal, Live Checker, Live FS, Blackout FS, Whiteout FS, Formatter, Market Filters, Swap C/P, TZ Converter)

### 📋 Session Log Store
- [x] `session_log_store.py` — shared in-memory session log module
- [x] Tracks scan / signal / reject / info events per session
- [x] Signal entries guaranteed never evicted (complete history)
- [x] General log capped at 20,000 entries
- [x] Web-based session log viewer (`session_log.html`)

### 🧠 Strategy Intelligence
- [x] `strategy_intelligence.html` — browser-based strategy intelligence dashboard
- [x] Accessible from Web Control / Admin Panel

---

## 🔜 Phase 5 — Short Term

### Multiple Broker Support — Phase 2
- [ ] **Pocket Option** — full signal and broadcast support
- [ ] **Olymp Trade** — OTC and Live pair support
- [ ] **Binomo** — OTC support

### Bot Builder — Full Public Release
- [ ] Open Bot Builder to STARTER tier
- [ ] Nested multi-level menu builder
- [ ] Logo/banner upload & full theming

### Free Bots Mission — Phase 2
- [ ] Bot #6 release
- [ ] Bot #7 release
- [ ] Bot #8 release
- [ ] Bot #9 release
- [ ] Bot #10 release

---

## 🔮 Phase 6 — Medium Term

### Enhanced AI Capabilities
- [ ] Upgraded AI models for deeper analysis
- [ ] Sentiment Analysis — market sentiment scoring
- [ ] Pattern detection layer

### Advanced Signal Management
- [ ] Signal history archive per user
- [ ] Personal win-rate statistics dashboard
- [ ] Pair-specific and time-of-day performance tracking

---

## 🚀 Phase 7 — Long Term

### Auto Trading System
- [ ] Quotex API direct trade execution
- [ ] Pocket Option API integration
- [ ] Risk management engine (auto stake sizing)
- [ ] Drawdown protection (auto-stop on daily loss limit)
- [ ] Auto compounding

### Mobile Application
- [ ] Native Android app
- [ ] Native iOS app
- [ ] Push notifications for signals

### Multi-Language Support
- [ ] Bengali (বাংলা)
- [ ] Arabic (عربي)
- [ ] Spanish (Español)
- [ ] Hindi (हिंदी)
- [ ] Indonesian (Bahasa Indonesia)

---

## 📊 Version History

| Version | Highlights |
|---|---|
| **v4.0** | Tradowix broker support, Auto Payment (Binance Pay/TRC20/BEP20), News Signal System (Forex Factory + AI), Live Checker (5th checker mode), Signal Tools (Formatter/Swap C/P/TZ Converter/Market Filters), new Future Signal modes (Live/Blackout/Whiteout FS), Bot Builder expanded (PLUS: 3 bots, INFINITY: 10 bots; Custom AI Prompt; Child Admin Panel; Session Log Viewer), Strategy Intelligence dashboard |
| **v3.x** | Tiered subscriptions (STARTER/PLUS/INFINITY), Web Control dashboard, Admin Web Panel with role-based sub-admins, Bot Builder early access (live deployment) |
| **v3.0** | AI confirmation, Live broadcast, Future Live system, 4-mode checker suite (super-fast + 100% accurate), Free Bots (5 released), Bot Builder button, PostgreSQL, referrals, reviews, premium emojis |
| **v2.0** | Full bot manager, MTG, charts, sleep mode, scheduler, future engine, checker |
| **v1.x** | Core signal engine, basic Telegram integration |

---

## 💡 Feature Requests

- **Telegram**: [@X_Akash_Owner](https://t.me/X_Akash_Owner)
- **Channel**: [@Quantexbot1](https://t.me/Quantexbot1)
- **Community Group**: [t.me/quantexlounge](https://t.me/quantexlounge)
- **Email**: [quantexbotsupport@gmail.com](mailto:quantexbotsupport@gmail.com)

*Roadmap subject to change based on user feedback.*
