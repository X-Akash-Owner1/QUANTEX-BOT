# 13 · Q-BOT STUDIO — Build Your Own Signal Bot

[⬅ Back to the User Guide](../USER_GUIDE.md)

**Q-BOT STUDIO** lets you create **your own branded Telegram signal bot** that runs on the QUANTEX engine. No coding and no server: you give a bot token, choose templates and features, and tap **DEPLOY**.

| Plan | Bots you can run |
|---|---|
| 🆓 FREE | 0 |
| 🟢 STARTER | 1 |
| 💎 PLUS | 3 |
| 👑 INFINITY | 10 |

**Templates included:** 5 Welcome + 5 About + 5 Help = **15 ready-made message templates**, plus 26 menu features in 6 groups (24 selectable now, 2 coming soon), button renaming and colours, signal templates and chart branding.

---

## 13.1 Studio home

Tap **Q-BOT STUDIO** on the main menu. The home screen shows **SYSTEM STATUS**: bots used / limit, running bots, your plan and access.

| Button | What it does |
|---|---|
| **CREATE** | Starts the 8-step wizard to build a new bot |
| **MYBOTS** | Lists your bots (🟢 running / 🔴 stopped) to manage them |
| **ANALYTICS** | Users, active today, actions today and total actions for each bot (**PREV / NEXT** between bots) |
| **SUBSCRIBE** | Your Studio plan, bots used and the bot limit of every plan, with **UPGRADE** |
| **HELP** | Step-by-step Studio help |
| **Back** | Main menu |

> If the Studio is under maintenance you see **⚠️ UNDER MAINTENANCE** until the admin turns it back on.
> If your plan's limit is reached, **CREATE** shows **🔒 Bot limit reached** with **UPGRADE** and **MYBOTS**.

---

## 13.2 Before you start: get a bot token

1. Open **@BotFather** in Telegram and send **`/newbot`**.
2. Choose a display name and a username ending in **`bot`** (e.g. `MySignalsBot`).
3. BotFather sends a **token** like `1234567890:AAEabc...xyz`. Copy it.

⚠️ Never share your token with anyone else.

---

## 13.3 CREATE — the 8 steps

### Step 1 / 8 — BOT TOKEN
Paste the full token. The bot checks it (**🔍 CHECKING BOT TOKEN… ▰▰▰**) and deletes your message for safety.

- Wrong format or invalid token: **❌ INVALID BOT TOKEN** (send it again).
- Token already used by another user: revoke it in BotFather, generate a new one and try again.

### Step 2 / 8 — BOT VERIFIED + BRAND NAME
Shows your bot's name, @username and ID. Send your **brand name** (max **32** characters). The brand name **replaces "QUANTEX" everywhere** in your bot: menus, welcome message, signal and result cards, chart titles, watermarks and partial reports. To keep the bot's current name, simply send that name.

### Step 3 / 8 — SUPPORT ACCOUNT
The Telegram account your users contact. It is used on every Support / Contact Owner button.

| Button | What it does |
|---|---|
| *(send `@username`)* | Sets that account (5+ characters, letters/numbers/underscore) |
| **USE MY PROFILE USERNAME** | Uses your own Telegram username |
| **SKIP** | Uses your own account |
| **Back** | Back to Step 2 |

### Step 4 / 8 — WELCOME MESSAGE (5 templates)
The message users see on `/start`.

| Template | Style |
|---|---|
| **TEMPLATE 01** | Clean & Professional |
| **TEMPLATE 02** | Modern & Premium |
| **TEMPLATE 03** | AI & Futuristic |
| **TEMPLATE 04** | Luxury & Elite |
| **TEMPLATE 05** | Bold & Powerful |

Tap a template → a **preview** with your brand name appears → **CONFIRM** to apply it, or **BACK** to choose another.

### Step 5 / 8 — ABOUT MESSAGE (5 templates)
Shown when users tap **ABOUT**: **1 PROFESSIONAL** (clean & professional), **2 AI STYLE** (modern & tech), **3 PREMIUM** (luxury & elegant), **4 SMART** (short & powerful), **5 TEMPLATE 05**. Preview → **CONFIRM** / **BACK**.

### Step 6 / 8 — HELP MESSAGE (5 templates)
Shown on the **HELP** button: **TEMPLATE 01 – 05**. Preview → **CONFIRM** / **BACK**.

### Step 7 / 8 — SELECT FEATURES
Every feature you select becomes a **button in your bot's main menu**. Unselected features stay hidden. A progress bar shows `selected / 26`.

| Button | What it does |
|---|---|
| **CORE n/3** · **CHECKERS n/4** · **FUTURE SIGNALS n/5** · **SIGNALS n/3** · **TOOLS n/4** · **USER n/7** | Opens that group |
| **SELECTALL** / **CLEARALL** | Select or clear everything |
| **NEXT** | Go to Step 8 |

Inside a group: tap a feature to tick ✅ / untick ▫️, **Select Group**, **Clear Group**, **DONE**.

| Group | Features |
|---|---|
| **CORE** | START LIVE SESSION · SCHEDULE SESSION · SETTINGS |
| **CHECKERS** | LIVE CHECKER · OTC CHECKER · BLACKOUT CHECKER · WHITEOUT CHECKER |
| **FUTURE SIGNALS** | OTC MARKET FS · LIVE MARKET FS · BLACKOUT FS · WHITEOUT FS · FUTURE LIVE |
| **SIGNALS** | LIVE SIGNAL · LIVE PAYOUTS · NEWS SIGNAL |
| **TOOLS** | FORMATTER · MARKET FILTERS · SWAP C/P · TZ CONVERTER |
| **USER** | MY PROFILE · UPGRADE · ABOUT · REVIEWS · HELP · 🔒 REFERRAL *(coming soon)* · 🔒 OTHERS *(coming soon)* |

### Step 8 / 8 — CHANNEL MEMBERSHIP (Force Join)
Do users have to join your channel before using the bot?

| Button | What it does |
|---|---|
| **ENABLE** | Set your channel: first add your bot as an **admin** of the channel, then send `@yourchannel`, a `https://t.me/yourchannel` link, or **forward a post** (for private channels) |
| **SKIP** | No force join (you can enable it later) |

With Force Join ON, non-members see a **JOIN** card instead of the menu, and users who leave are asked to rejoin.

### REVIEW & DEPLOY
Shows bot, @username, brand, support, active features, welcome template and force-join status.

| Button | What it does |
|---|---|
| **DEPLOY** | Registers the token, applies everything and **starts your bot** |
| **FEATURES** / **WELCOME** / **FORCEJOIN** | Go back and change that part |
| **Back** | Back to Step 8 |

**✅ YOUR BOT IS LIVE** shows your bot link. Open it and send `/start`: you will see your custom menu. Button: **MYBOTS**.

---

## 13.4 MY BOTS — manage a bot

Tap a bot in **MYBOTS**. The detail screen shows status (RUNNING / STOPPED), title, number of features, users (total / active today), deploy date and any error.

| Button | What it does |
|---|---|
| **START BOT** / **STOP BOT** | Turns the bot on or off |
| **CUSTOMIZE** | Opens all customisation options (below) |
| **CHANGE TOKEN** | Send a new BotFather token (e.g. after revoking the old one) |
| **ANALYTICS** | Total users, active today, actions today/total, signals today/total |
| **DELETE BOT** | Asks for **CONFIRM**. Stops the bot and erases its features, branding, wording and analytics. The Telegram bot itself stays in your BotFather account. **Cannot be undone** |
| **Back** | Back to My Bots |

### CUSTOMIZE

The screen summarises brand, support, welcome template, number of changed template fields and force-join status. **All changes apply from the very next message.**

| Button | What you can change |
|---|---|
| **WELCOME** | Pick another of the 5 Welcome templates (preview → confirm) or **RESET** to default |
| **ABOUT** | Pick one of the About templates or write your own About text; **RESET** |
| **HELP** | Pick one of the 5 Help templates |
| **SUPPORT** | Send a new support `@username` |
| **BRAND** | Send a new title (max 32). It replaces "QUANTEX" in every place you have not customised yourself |
| **BUTTONS** | Rename any menu button (max 30 characters, emojis allowed, e.g. `🔥 VIP SIGNAL`) and set its colour **Green / Blue / Red**. **RESET** restores a button or all buttons. The button keeps doing the same job |
| **FEATURES** | Tick / untick features by group, then **SAVE**. Changes reach the bot immediately |
| **TEMPLATES** | Signal templates for **Live Session**, **Live Signal** and **Checker & Future Signal**: Signal Title, Result Title, Chart Title, Chart Watermark, Username, Partial Title, Partial Footer (and Checker / Future titles). Each shows default, current and max length. **RESET** per field or per template |
| **MESSAGES** | Other texts: Home footer note, Signal title, Result title, Partial title, Checker title, Profile title, Pricing title, **Custom AI prompt** (an extra instruction for this bot's AI confirmation) and **Notification template** (default announcement text). 2–80 characters each |
| **CHART** | Chart title and watermark for Live Session and Live Signal charts, so screenshots carry your name |
| **FORCEJOIN** | **SETUP** / **CHANGE** the channel and **Turn ON / Turn OFF**. Keep the bot an admin there, or the check stops working |
| **EMOJI:ON / EMOJI:OFF** | Turn premium (animated) emojis in your bot's messages on or off |
| **STUDIO CONTROL** | Opens the **Creator Panel** web app: Overview, Brand, Features, Texts and Buttons tabs with a **Live Preview**, then **Publish** |

---

## 13.5 Your bot's ADMIN PANEL

Inside **your own bot**, you (the owner) are the admin. Send **`/admin`** there.

**🛠 ADMIN PANEL** shows users (total / today), licensed users, banned users, actions today and the access mode.

| Button | What it does |
|---|---|
| **ADMIN WEB** | Opens the full web admin (Overview, Users, Limits, Logs, Bot Control) |
| **USERS** | Everyone who used your bot (15 per page, **PREV / NEXT**) with their IDs and last activity |
| **LICENSES** | List of licensed users with tier and days left. **LICENSE** to add one |
| **BROADCAST** | Send a message (HTML allowed) to all non-banned users. You get a report: sent / failed |
| **BANNED** | List of banned users |
| **STATS** | Users, active today, actions today, signals today, actions total |
| **Access: OPEN / LICENSED** | **OPEN** = anyone may use the bot (as FREE tier). **LICENSED** = only users you licensed. Tap to switch |
| **LOGS** | Last 25 events of your bot |
| **GUIDE** | List of admin commands |

### Giving licences to your users
Tap **LICENSE** and send `user_id days [tier]`:

| Example | Result |
|---|---|
| `123456789 30` | 30 days, INFINITY tier (default) |
| `123456789 7 plus` | 7 days on PLUS |
| `123456789 permanent` | Never expires |

The user is notified (*"🎉 You've been given access"*). Tiers: `free · starter · plus · infinity`.

### Admin commands (inside your bot)

| Command | What it does |
|---|---|
| `/admin` | Open the panel |
| `/stats` | Users, activity, licences |
| `/users` | Everyone who used your bot |
| `/broadcast` | Message everyone (or reply to a message with it) |
| `/ban <id>` · `/unban <id>` · `/banlist` | Ban management |
| `/addlicense <id> <days> [tier]` · `/addlicense <id> permanent` | Give a licence |
| `/removelicense <id>` · `/checklicense <id>` · `/licensedusers` | Licence management |
| `/access open` · `/access licensed` | Who may use the bot |

### ADMIN WEB extras

| Tab | What you can do |
|---|---|
| **Overview** | Total users, licensed, banned, today |
| **Users** | Search users, **Grant License** (days + plan), **Remove License**, **Ban / Unban** |
| **Limits** | Set daily **Live** and **Future** limits for each tier of your bot (`-1` = unlimited), **Save**, and **Reset All User Limits** |
| **Logs** | Full live log viewer |
| **Bot Control** | Bot status and **Start / Stop**, **Access Mode** (Open · Everyone / Licensed Only), **Send Announcement** |

Everything here belongs to your bot only: its users, licences, bans and limits. As the owner you are never limited inside your own bot. Group Live Signal (`/start_live_signal`) is also controlled by you in your bot (see [Chapter 4](04-live-signal.md#d--group-live-signal-for-bot-owners)).

[⬅ Free Bots](12-free-bots.md) · [Back to the User Guide](../USER_GUIDE.md)
