# ❓ QUANTEX-BOT — Frequently Asked Questions (FAQ)

> **Bot**: [@QuantexBinaryTools_bot](https://t.me/QuantexBinaryTools_bot) | **Support**: [@X_Akash_Owner](https://t.me/X_Akash_Owner)

---

## 📌 General

### What is QUANTEX-BOT?
QUANTEX-BOT is an automated binary options trading signal system on Telegram. It uses a proprietary multi-factor analysis engine combined with AI confirmation to deliver high-confidence BUY/CALL or SELL/PUT signals with real-time charts, payout data, and automatic result tracking.

### What's new in v3?
v3 adds: AI-confirmed Live Signals with S/R levels and payout, Live Signal Broadcast (Manual & Auto), Future Live Signal System, a completely rebuilt 4-mode super-fast 100% accurate checker suite (OTC + Blackout + Whiteout + Custom Date), Free Bots Mission (10 premium bots, free), Bot Builder (coming soon), Telegram Premium emoji integration, referral program, reviews system, and a PostgreSQL database backend.

### What broker should I use?
Currently optimized for **Quotex**. Multiple broker support is coming soon.

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
**3 sessions total** (lifetime). Licensed users have unlimited sessions.

---

## 🔍 Signal Checker

### What is the Checker Suite?
QUANTEX-BOT v3 includes **4 checker modes**:
- **OTC Checker** — standard WIN/LOSS check for normal signals
- **Blackout Checker** — direction-free signals checked using reverse previous-candle logic
- **Whiteout Checker** — direction-free signals checked using follow previous-candle logic
- **Custom Date Checker** — check signals for any specific past date

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

## 🤖 Free Bots Mission

### What is the Free Bots Mission?
QUANTEX is releasing **10 premium trading bots completely free** to all users, one by one. Each bot is independent and has its own unique features.

### Which free bots are available now?
- **Bot #1: HUNTER X QUANTEX** — Live signal software with bad market filter
- **Bot #2: DRAGON X QUANTEX** — OTC Signal Pro with entry timer
- **Bot #3: BLACKOUT FUTURE AI** — AI-powered future signal system (80–95% accuracy)
- Bots #4–10: coming soon

### How do I access the free bots?
Inside QUANTEX-BOT → **Free Bots** menu → select any available bot. No separate login or signup required.

---

## 🏗️ Bot Builder

### What is the Bot Builder?
An upcoming feature (currently "Coming Soon") that will let anyone build their own custom trading signal bot directly from QUANTEX-BOT — no coding required. You set it up through a button-based wizard and deploy it to your own channel.

### When will Bot Builder be released?
Follow [@Quantexbot1](https://t.me/Quantexbot1) for the release announcement.

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

## 💰 Pricing & License

| Plan | Price |
|---|---|
| 1 Month | $30 |
| 3 Months | $80 |
| 6 Months | $140 |
| Lifetime | $300 |

Contact [@X_Akash_Owner](https://t.me/X_Akash_Owner) to purchase.

**Promo codes** available — follow [@Quantexbot1](https://t.me/Quantexbot1) or earn via referrals.

---

## 💤 Sleep Mode

Bot auto-pauses **7:00 PM – 10:00 PM** daily. High volatility during this period makes signals unreliable. Bot resumes automatically at 10:00 PM and notifies all licensed users.

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
- 🤖 **Bot**: [@QuantexBinaryTools_bot](https://t.me/QuantexBinaryTools_bot)
