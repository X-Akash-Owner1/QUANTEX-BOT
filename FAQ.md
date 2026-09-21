# ❓ QUANTEX-BOT — Frequently Asked Questions (FAQ)

> **Bot**: [@QuantexBinaryTools_bot](https://t.me/QuantexBinaryTools_bot) | **Support**: [@X_Akash_Owner](https://t.me/X_Akash_Owner)

---

## 📌 General

### What is QUANTEX-BOT?
QUANTEX-BOT is an automated binary options trading signal system on Telegram. It uses a proprietary multi-factor analysis engine combined with AI confirmation to deliver high-confidence BUY/CALL or SELL/PUT signals with real-time charts, payout data, and automatic result tracking.

### What's new in v4.0?
v4.0 adds: **Tradowix broker** support (alongside Quotex); an **Auto Payment system** (Binance Pay, TRC20 USDT, BEP20 USDT — subscribe instantly without contacting the owner); a **News Signal system** powered by the Forex Factory economic calendar and Gemini AI; a **Live Checker** (5th checker mode for real market pairs); **Signal Tools** (Formatter, Swap C/P, TZ Converter, Market Filters); new **Future Signal modes** (Live FS, Blackout FS, Whiteout FS); **Bot Builder expanded** (PLUS: 3 bots, INFINITY: 10 bots; custom AI prompt; notification template; Child Admin Panel); a **Session Log Viewer**; a **Strategy Intelligence Dashboard** with auto-optimization and ML-based continuous training; a **Machine Learning Signal Engine** with 3 analyzer engines and 20+ independent modules; and **5 Free Bots** now released (HUNTER, DRAGON, BLACKOUT FUTURE AI, STORM, PHANTOM).

### What broker should I use?
QUANTEX-BOT currently supports two brokers: **Quotex** and **Tradowix**. Both are fully supported with OTC and Live pair signals. Select your preferred broker in the setup wizard.

---

## 📡 Signals & Accuracy

### How accurate are signals?
Depends on market conditions. During strong trends: 70–85% win rate is common. During sideways markets: bot sends fewer signals to maintain quality. During high-volatility hours: bot enters sleep mode automatically.

### How often does the bot send signals?
At **5-minute clock boundaries**. Only when all internal factors align — frequency varies by market conditions.

### What is a DOJI result?
A DOJI candle means the open and close price are equal (no movement). QUANTEX-BOT detects these and reports them separately — they are not counted as WIN or LOSS in your win-rate.

---

## 🤖 AI Signal Confirmation

### What does AI confirmation add?
In Live Signal mode, every signal is additionally validated by an AI model that checks market conditions, calculates support/resistance levels, fetches real-time payout data, and provides a written reason. This is an extra quality layer on top of the base signal engine.

### Can the AI reject a signal?
Yes. If the AI determines the setup is not strong enough, it overrides and blocks the signal from being sent.

### What is "Support & Resistance" in the signal?
Key price levels automatically calculated and included in every Live Signal. Support = price floor. Resistance = price ceiling. They give context for the trade entry.

---

## ⏱ Future Live Signal System

### What is Future Live?
You paste a pre-planned signal list and QUANTEX-BOT automatically sends each signal to your channel at the exact scheduled time, waits for the candle to close, checks the result, and sends WIN/LOSS — all fully automated.

### What signal formats does Future Live accept?
Any format — the universal parser handles everything:
```
▢ 05:50 USDIDR ⇨OTC ☞ PUT
M1 EURUSD_OTC 06:00 BUY
USDCAD-OTC 05:53 PUT
```

### How many Future Live sessions do free users get?
**3 sessions total** (lifetime) for free users. Subscribed users have unlimited sessions.

---

## 🔍 Signal Checker

### What is the Checker Suite?
QUANTEX-BOT v4 includes **5 checker modes**:
- **Live Checker** *(New)* — WIN/LOSS check for real/live market signals
- **OTC Checker** — standard WIN/LOSS check for OTC signals
- **Blackout Checker** — direction-free signals checked using reverse previous-candle logic
- **Whiteout Checker** — direction-free signals checked using follow previous-candle logic
- **Custom Date Checker** — check signals for any specific past date

### What is the Live Checker?
The Live Checker works exactly like the OTC Checker, but for **real (live) market pairs** instead of OTC pairs. Paste your live market signals and receive instant WIN/LOSS/DOJI results.

### What makes the checker "super-fast & 100% accurate"?
The checker uses a **local candle cache** with a pre-built time index for O(1) lookups — no external API calls needed. Candle data is compared directly (open vs close), not estimated. Results are exact.

### What is the Blackout Checker?
For signals that have no direction. The checker looks at the **previous candle** — if it was GREEN, expected direction is PUT; if RED, expected direction is BUY. Then it checks the entry candle against that expected direction.

### What is the Whiteout Checker?
Same as Blackout but logic is reversed — previous GREEN → expected BUY; previous RED → expected PUT.

### What is the Payout Filter?
Set a minimum payout threshold (e.g., 80%). Signals below that threshold are flagged with their actual payout % so you can decide whether to skip them.

### What is the Custom Date Checker?
Check signals for any past date — not just today or yesterday. Bot fetches archived candle data for the chosen date.

---

## 📰 News Signal System

### What is the News Signal?
The News Signal system generates trading signals based on the **Forex Factory economic calendar**. It fetches upcoming economic events (e.g. NFP, CPI, interest rate decisions), analyzes the expected impact using Gemini AI, and produces CALL/PUT recommendations for each of your selected pairs.

### How does it determine direction?
In three layers:
1. **Heuristic** — compares `forecast vs previous` for the event, with inversion logic for negative metrics (e.g. unemployment rate)
2. **AI Analysis** — Gemini AI provides BULLISH/BEARISH/NEUTRAL bias with a confidence score and rationale
3. **Technical Blend** — a 30-day technical structure read (trend + momentum) is blended with the fundamental bias to adjust confidence up or down

### Which pairs are supported by News Signal?
29 pairs: all major forex pairs (EUR, GBP, USD, JPY, CHF, CAD, AUD, NZD combinations) plus XAU/USD.

### Can I filter by news impact level?
Yes — you can filter events by **HIGH**, **MEDIUM**, **LOW**, or show **All** impacts.

### How many days ahead can I see?
1, 2, or 3 days ahead from the current time.

### Is the AI re-run for every user requesting the same event?
No — analysis results are **cached per event** (keyed by title + currency + exact release time). The first user requesting an event pays the AI cost; everyone else requesting the same event within its window gets the cached result instantly. Cache expires after the event's release time.

---

## 🛠️ Signal Tools

### What are the Signal Tools?
Four utility tools for working with signal lists, accessible from the main menu:

- **Signal Formatter** — paste any signal list, receive it reformatted into a clean, standardized card layout
- **Swap C/P** — paste a signal list, every CALL becomes PUT and vice versa (useful for reversing strategies)
- **TZ Converter** — paste signals, enter source and target timezone → receive time-converted signals
- **Market Filters** — shows which live markets are currently stable and tradeable

### Who can use the Signal Tools?
All users — the tools are available to FREE, STARTER, PLUS, and INFINITY subscribers.

---

## 💳 Auto Payment

### What is the Auto Payment system?
A self-serve subscription system that lets you activate your plan **instantly inside the bot**, without contacting the owner. Supported methods: **Binance Pay**, **TRC20 USDT**, and **BEP20 USDT**.

### How does it work?
1. Tap **Upgrade** inside the bot
2. Select your plan (STARTER, PLUS, or INFINITY)
3. Choose a payment method
4. Send the exact USDT amount to the provided address/ID
5. Bot verifies payment automatically and activates your subscription immediately

### How long do I have to complete payment?
**60 minutes** from the time you initiate the request. After that, the request expires and you can start a new one.

### Is manual payment still available?
Yes — you can always contact [@X_Akash_Owner](https://t.me/X_Akash_Owner) directly if you prefer manual activation.

---

## 🧠 Machine Learning Engine

### Does QUANTEX-BOT use machine learning?
Yes. The signal engine includes an adaptive ML-based analysis system with **3 distinct analyzer engines** and **20+ independent analysis modules**. Every signal result (WIN/LOSS/DOJI) is logged and used to continuously train and optimize the engine's per-pair, per-timeframe parameters.

| Analyzer Engine | Description |
|---|---|
| **QUANTUM SCAN** | Dynamic MTF + Structure + Practical Signals |
| **SMART FOCUS** | Best Quality Market Analyzer |
| **HYBRID ENGINE** | MTF + Structure + Trap detection, Score 75+ |

### What are the 20+ analysis modules?
Each signal passes through independent modules including: Trend Continuation, Break of Structure, Change of Character, Engulfing Reversal, MACD Cross, RSI Divergence, Bollinger Breakout, Pin Bar, MTF Confluence, VWAP Reversion, Ichimoku Confluence, Fibonacci Pullback, Candlestick Patterns (Harami, Morning/Evening Star, Tweezer, Three Black Crows), Supertrend + PSAR, CCI Extreme Reversal, and Multi-Indicator Confluence. Only signals where multiple independent modules agree are delivered.

### Does the bot get better over time?
Yes. The **Strategy Intelligence** system automatically learns from every WIN, LOSS, and DOJI result. Per-pair, per-timeframe parameter profiles are continuously updated. When a strategy underperforms on a specific pair or timeframe, the system detects it and self-corrects — the longer the bot runs, the smarter it becomes.

### What is Strategy Intelligence?
A browser-based admin dashboard showing real-time strategy performance, win rates per pair and timeframe, and the auto-optimization status of each analyzer engine. Strategies are continuously trained and self-healing **without any manual intervention**.

### What is the minimum signal confidence threshold?
Only signals scoring **79 or higher** on the internal confidence scale are delivered. Signals below this threshold are silently discarded. The scoring is weighted — stronger modules that have historically performed well carry more influence.

---

## 🤖 Free Bots Mission

### What is the Free Bots Mission?
QUANTEX is releasing **10 premium trading bots completely free** to all users, one by one. Each bot is independent and has its own unique features.

### Which free bots are available now?
- **Bot #1: HUNTER X QUANTEX** — Live signal software with bad market filter
- **Bot #2: DRAGON X QUANTEX** — OTC Signal Pro with entry timer
- **Bot #3: BLACKOUT FUTURE AI** — AI-powered future signal system (80–95% accuracy)
- **Bot #4: STORM X QUANTEX** — Premium trading bot (details coming soon)
- **Bot #5: PHANTOM X QUANTEX** — Premium trading bot (details coming soon)
- Bots #6–10: coming soon

### How do I access the free bots?
Inside QUANTEX-BOT → **Free Bots** menu → select any available bot. No separate login or signup required.

---

## 🏗️ Bot Builder

### What is the Bot Builder?
A feature that lets you build your own custom, white-label trading signal bot directly from QUANTEX-BOT — no coding required. You set it up through a button-based wizard (token, branding, modules, templates) and deploy it with one tap.

### Who can use it?
Available to **PLUS and INFINITY** subscribers.

| Plan | Max Bots |
|---|---|
| 💎 PLUS | 3 bots |
| 👑 INFINITY | 10 bots |

### What's new in Bot Builder v4.0?
- **Custom AI Prompt** — set a custom instruction that your bot's AI confirmation layer uses
- **Notification Template** — customize the default announcement text in your Child Admin Panel
- **Child Admin Panel** — full admin panel to manage users of your deployed bot
- **Session Log Viewer** — real-time diagnostic log for active sessions in your bot
- All new modules now selectable: News Signal, Live Checker, Live FS, Blackout FS, Whiteout FS, Formatter, Market Filters, Swap C/P, TZ Converter

### When will it be available to STARTER users?
Follow [@Quantexbot1](https://t.me/Quantexbot1) for the announcement.

---

## 🏢 Brokers

### Which brokers are supported?
**Quotex** and **Tradowix** are both fully supported. Both provide OTC and Live Forex signal support.

### Are more brokers coming?
Yes — Pocket Option, Olymp Trade, Binomo, and others are planned. Follow [@Quantexbot1](https://t.me/Quantexbot1) for updates.

---

## 💎 Telegram Premium Mode

### What is Premium Mode?
Connects your own Telegram account so signals are sent with Telegram **Premium animated emojis** for a more visually distinctive format in the checker and signal outputs.

### Do I need Telegram Premium?
Yes, Premium animated emojis are only displayed correctly to users with an active Telegram Premium subscription.

### Is it safe to connect my account?
Yes. Login is handled through a secure browser WebApp. Session is encrypted. 2FA is fully supported. Login tokens expire in 30 minutes if unused.

---

## 🔄 MTG (Martingale)

### What MTG levels are available?
- **Non-MTG** — single signal only
- **MTG 1** — one recovery step
- **MTG 2** — two recovery steps

### Is MTG automatic?
In Live Signal mode, the bot sends the MTG analysis/signal. In Future Live mode, MTG fires automatically at the next candle. Whether you place the actual trade is your choice.

---

## 👥 Referral Program

### How does it work?
Go to **Referral** in the bot → get your unique link → share it. Each verified signup earns you referral credit. Reaching milestones generates exclusive promo codes.

---

## 💰 Pricing & Subscriptions

| Plan | Price |
|---|---|
| 🆓 FREE | $0 |
| 🟢 STARTER | $18 / month |
| 💎 PLUS ⭐ Most Popular | $32 / month |
| 👑 INFINITY | $49 / month |

Tap **🪄 Upgrade** inside the bot to subscribe instantly via **Auto Payment** (Binance Pay, TRC20 USDT, BEP20 USDT), or contact [@X_Akash_Owner](https://t.me/X_Akash_Owner) for manual activation.

**Promo codes** available — follow [@Quantexbot1](https://t.me/Quantexbot1) or earn via referrals.

---

## 🌐 Web Control

### What is Web Control?
A browser-based dashboard that opens directly inside Telegram (as a Mini App). It shows your live profile, plan, and signal credits, and lets PLUS/INFINITY subscribers manage timezone settings and message templates without typing commands.

### Do I need to create a separate account for Web Control?
No — it opens using your existing Telegram session automatically. Nothing extra to set up.

### Can FREE or STARTER users open Web Control?
Yes — you can view your profile and the subscription plans, with a prompt to upgrade for full control access.

---

## 📋 Session Log Viewer

### What is the Session Log Viewer?
A real-time diagnostic log that records every event in your active live signal session — which pairs were scanned, which signals were generated, which were rejected and why. Accessible from the Web Control dashboard and from Bot Builder's Child Admin Panel.

### Does closing the log page lose my data?
No — the log keeps running in the background regardless of whether the page is open. Reopening the page shows the full accumulated history.

---

## 🔒 Trust & Safety

### Is QUANTEX-BOT a scam?
No. QUANTEX-BOT has an active **public community group** — [t.me/quantexlounge](https://t.me/quantexlounge) — where users share real results, both wins and losses, openly. A bot with poor performance couldn't survive that kind of open scrutiny for long. The product is actively maintained and transparently run.

### Can I be sure the bot performs well before paying?
We recommend **backtesting** the signals in demo mode first, so you can verify performance yourself before subscribing or trading real funds. Binary options trading carries real risk, and no signal service — including this one — can promise a 100% win rate.

### Is it safe to connect my Telegram account (Premium Mode)?
Yes. The connection is handled through a secure, encrypted login flow. Your credentials are never exposed or shared, and are stored safely for the sole purpose of verifying your account and enabling Telegram Premium emoji formatting.

---

## 💤 Sleep Mode

Bot auto-pauses **7:00 PM – 10:00 PM** daily. High volatility during this period makes signals unreliable. Bot resumes automatically at 10:00 PM and notifies all subscribed users.

---

## ⚠️ Risk Disclaimer

Binary options trading carries high risk. QUANTEX-BOT provides signals to assist your decisions — it does not guarantee profits. Only trade with money you can afford to lose.

**Recommended money management:**
- 1–5% of balance per trade maximum
- Set a daily loss limit
- Never chase losses with bigger stakes

---

## 📞 Support

- 💬 **Telegram**: [@X_Akash_Owner](https://t.me/X_Akash_Owner)
- 📧 **Email**: [quantexbotsupport@gmail.com](mailto:quantexbotsupport@gmail.com)
- 📢 **Channel**: [@Quantexbot1](https://t.me/Quantexbot1)
- 👥 **Community Group**: [t.me/quantexlounge](https://t.me/quantexlounge)
- 🤖 **Bot**: [@QuantexBinaryTools_bot](https://t.me/QuantexBinaryTools_bot)
