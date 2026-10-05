# 🧩 QUANTEX — System Architecture

How the QUANTEX Telegram bot, the website and the Developer API work together. Written for developers, integrators and AI assistants who want to understand the system before using it.

> This is a description of the design, not source code. The QUANTEX engine and the web platform are closed source.

---

## 1. The parts

| Part | Address | Role |
|---|---|---|
| **QUANTEX Telegram bot** | [@QuantexBinaryTools_bot](https://t.me/QuantexBinaryTools_bot) | Where traders get signals (Live Session, Live Signal, Auto Signal, Future Signals, checkers, tools, Q-BOT STUDIO, HUB) |
| **Market data collectors** | internal | Record every M1 candle and the payout of every pair of QUOTEX, TRADOWIX and BINOLLA, live and archived |
| **Signal engines** | internal | Strategy Mode (QUANTUM SCAN, SMART FOCUS, HYBRID ENGINE) and Scanning Mode, plus Strategy Intelligence that learns from every result |
| **Website** | [quantexbot.pro](https://quantexbot.pro) | Information, documentation, accounts, dashboard, billing, AI support, status page |
| **Developer API** | [api.quantexbot.pro/v1](https://api.quantexbot.pro/v1/status) | REST API, webhooks and a Server-Sent Events stream for developers |
| **Engine Bridge** | internal (local only) | The only connection between the web platform and the QUANTEX engine; returns results, never strategy logic |
| **Admin panel** | private | Users, payments, subscriptions, API keys and logs, content, AI support, system status, analytics |

---

## 2. Big picture

```
                      Internet (browsers, developer apps, AI tools)
                                      │  HTTPS (Cloudflare)
              ┌───────────────────────┼────────────────────────┐
              ▼                       ▼                        ▼
       quantexbot.pro         api.quantexbot.pro         (admin, private)
     website + dashboard        Developer API
              └───────────────┬───────┴────────────────────────┘
                              ▼
                    QUANTEX web platform
          (accounts · billing · API gateway · status · content)
                              │
                              │  signed local requests — results only
                              ▼
                     QUANTEX Engine Bridge
              │                │                    │
              ▼                ▼                    ▼
     candle & payout     signal checker,     QUANTEX Telegram bot
     collectors          news analysis       (signal feed + future lists)
```

- Web users and API callers only ever reach the web platform.
- The web platform asks the Engine Bridge for **results** (pairs, payouts, candles, check results, news bias, delivered signals, future lists). It never contains or runs strategy code.
- The bridge and the bot listen on the local machine only and every request between them is signed.

---

## 3. How a live signal reaches the API

```
Signal engine finds a setup
        │
        ▼
Telegram bot delivers it to a user (Live Session / Live Signal / Auto Signal / Scanning)
        │
        ├─► written ONCE to the signal feed      (same broker + pair + timeframe + entry = same signal id)
        │
Candle closes → result checked (WIN / MTG WIN / LOSS)
        │
        └─► result written to the feed with the same id
                         │
                         ▼
        Engine Bridge reads the feed  →  web platform stores it (about every 1.5 s)
                         │
        ┌────────────────┼──────────────────────┬────────────────────┐
        ▼                ▼                      ▼                    ▼
 GET /v1/signals/live   webhooks           GET /v1/stream/signals   GET /v1/results
 (cursor polling)      (signed POST)        (Server-Sent Events)    (daily win rate)
```

- The API serves the signals the bot **really delivered**; it never starts a new analysis for an API request, so API traffic cannot slow the bot.
- Each signal carries entry and expiry time (UTC), direction (CALL / PUT), payout, confidence and engine; the result arrives later with the same id: `WIN` (`mtg_level` 0 or 1), `LOSS` or `NO_DATA`.

---

## 4. Request pipeline of the Developer API

Every request to `api.quantexbot.pro/v1` passes the same steps; the first one that fails answers with the error envelope:

| Step | Check | Error |
|---|---|---|
| 1 | Body size (max 64 KB) | `413 payload_too_large` |
| 2 | API key (`Authorization: Bearer qx_live_…`, or `?api_key=` on GET for browser tests) | `401 unauthenticated` / `invalid_api_key` |
| 3 | Key state: revoked, expired, account suspended, IP allow-list | `403 key_revoked` / `key_expired` / `account_suspended` / `ip_not_allowed` |
| 4 | Key permission (scope) and plan endpoint group | `403 insufficient_scope` / `plan_upgrade_required` |
| 5 | Per-minute and monthly limits of the plan | `429 rate_limited` / `quota_exceeded` + `Retry-After` |
| 6 | Parameter validation, then the endpoint | `422 validation_failed`, `404 …_not_found`, `503 service_unavailable` |
| 7 | After the answer: request log (no bodies, no keys) and usage counters | — |

Answers always use one envelope:

```json
{ "ok": true,  "data": { },  "meta": { "request_id": "req_…" } }
{ "ok": false, "error": { "code": "…", "message": "…" }, "meta": { "request_id": "req_…" } }
```

Keys look like `qx_live_<8-char prefix>_<40-char secret>`. Only the prefix and a keyed hash of the secret are stored; the full key is shown once.

---

## 5. Data and freshness

| Data | Source | Freshness |
|---|---|---|
| Brokers, pairs, payouts | collector files | seconds |
| Candles | collector cache + daily archives | M1: every stored minute; M5+: only closed candles |
| Checker | the bot's own checker engine on archived candles | on request |
| News | economic calendar, analysed once per day by the bot | prepared daily (UTC+6 midnight) |
| Live signals and results | the bot's signal feed | ~1.5 s |
| Future lists | the bot's future generators | a few seconds per job |
| Status | health checks | every minute |

---

## 6. Security in short

- Only the web platform is reachable from the internet; the database, the Engine Bridge and the bot are internal.
- Separate sessions and cookies for the website and the admin panel; admin sign-in needs password + authenticator code.
- API keys and webhook secrets are stored hashed / encrypted and shown only once.
- Webhooks: HTTPS only, private and local addresses are refused, every POST is signed (`X-Quantex-Signature`).
- Payments are never trusted from the user: each transaction is verified against Binance / the blockchain, and a transaction can be used only once (website and bot together).
- Every admin action is written to an audit log that cannot be edited.

---

## 7. Where to go next

| You want to… | Read |
|---|---|
| Use the website | [WEBSITE.md](WEBSITE.md) |
| Build with the API | [DEVELOPER_API.md](DEVELOPER_API.md) · [examples/](examples/) · [api/openapi.json](api/openapi.json) |
| Use the Telegram bot | [USER_GUIDE.md](USER_GUIDE.md) · [FEATURES.md](FEATURES.md) |
| Give an AI assistant the docs | [llms.txt](llms.txt) or [quantexbot.pro/llms-full.txt](https://quantexbot.pro/llms-full.txt) |
