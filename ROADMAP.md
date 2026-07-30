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
- [ ] Bots #4 through #10 — releasing progressively

### 🏗️ Bot Builder
- [x] Bot Builder button added to main menu
- [x] Full wizard — token verification, branding, module selection, template editing, button builder, review & deploy
- [x] Live deployment — real webhook registration, bot goes live instantly
- [x] My Bots management — start / stop / restart / delete
- [x] Early access released for INFINITY subscribers (1 bot per account)
- [ ] Public multi-bot release for all tiers — *in progress*

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

## 🔜 Phase 4 — Short Term

### Multiple Broker Support
- [ ] **Pocket Option** — full signal and broadcast support
- [ ] **Olymp Trade** — OTC and Live pair support
- [ ] **Binomo** — OTC support
- [ ] Broker selection in setup wizard

### Bot Builder — Public Release
- [ ] Open Bot Builder to all subscription tiers
- [ ] Multiple bots per account
- [ ] Nested multi-level menu builder
- [ ] Logo/banner upload & full theming

### Web Dashboard — Full Bot Management
- [ ] Manage deployed client bots from the browser
- [ ] Real-time signal display
- [ ] Session control from browser
- [ ] Mobile-responsive
- [ ] Telegram OAuth login

### Free Bots Mission — Phase 2
- [ ] Bot #4 release
- [ ] Bot #5 release
- [ ] Bot #6 release
- [ ] Bot #7 release
- [ ] Bot #8 release
- [ ] Bot #9 release
- [ ] Bot #10 release

---

## 🔮 Phase 5 — Medium Term

### Enhanced AI Capabilities
- [ ] Upgraded AI models for deeper analysis
- [ ] News Analysis Engine — monitor economic calendar
- [ ] News-Based Signals — triggered by news outcomes
- [ ] Sentiment Analysis — market sentiment scoring
- [ ] Pattern detection layer

### Advanced Signal Management
- [ ] Signal history archive per user
- [ ] Personal win-rate statistics dashboard
- [ ] Pair-specific and time-of-day performance tracking

---

## 🚀 Phase 6 — Long Term

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
| **v3.x** | Tiered subscriptions (STARTER/PLUS/INFINITY), Web Control dashboard, Admin Web Panel with role-based sub-admins, Bot Builder early access (live deployment) |
| **v3.0** | AI confirmation, Live broadcast, Future Live system, 4-mode checker suite (super-fast + 100% accurate), Free Bots (3 released), Bot Builder button, PostgreSQL, referrals, reviews, premium emojis |
| **v2.0** | Full bot manager, MTG, charts, sleep mode, scheduler, future engine, checker |
| **v1.x** | Core signal engine, basic Telegram integration |

---

## 💡 Feature Requests

- **Telegram**: [@X_Akash_Owner](https://t.me/X_Akash_Owner)
- **Channel**: [@Quantexbot1](https://t.me/Quantexbot1)
- **Community Group**: [t.me/quantexlounge](https://t.me/quantexlounge)
- **Email**: [quantexbotsupport@gmail.com](mailto:quantexbotsupport@gmail.com)

*Roadmap subject to change based on user feedback.*