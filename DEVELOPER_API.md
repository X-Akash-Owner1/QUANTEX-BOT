<div align="center">

# 🔌 QUANTEX Developer API

**Market data, live signals, results, future signals, the signal checker and economic news — as a REST API for your own apps and Telegram bots.**

[![Website](https://img.shields.io/badge/Website-quantexbot.pro-2f6bff?style=flat-square)](https://quantexbot.pro)
[![API Docs](https://img.shields.io/badge/API%20Docs-quantexbot.pro%2Fdocs%2Fapi-8b5cf6?style=flat-square)](https://quantexbot.pro/docs/api)
[![Base URL](https://img.shields.io/badge/Base%20URL-api.quantexbot.pro%2Fv1-00b894?style=flat-square)](https://api.quantexbot.pro/v1/status)
[![OpenAPI](https://img.shields.io/badge/OpenAPI-3.1-6BA539?style=flat-square&logo=openapiinitiative&logoColor=white)](https://api.quantexbot.pro/v1/openapi.json)
[![Status](https://img.shields.io/badge/Status-quantexbot.pro%2Fstatus-00ff88?style=flat-square)](https://quantexbot.pro/status)

</div>

---

## 🧭 At a glance

| | |
|---|---|
| **Base URL** | `https://api.quantexbot.pro/v1` |
| **Format** | JSON over HTTPS, always `{"ok", "data" \| "error", "meta"}` |
| **Authentication** | `Authorization: Bearer qx_live_…` (keys are created in [Dashboard → API keys](https://quantexbot.pro/dashboard/api/keys)) |
| **Get a key** | [Create an account](https://quantexbot.pro/register) → verify email → Dashboard → API keys (free Developer plan included) |
| **Plans** | Developer (free), Starter, Pro, Business — see [Plans](#plans) and [quantexbot.pro/pricing](https://quantexbot.pro/pricing) |
| **Machine-readable** | [OpenAPI 3.1](https://api.quantexbot.pro/v1/openapi.json) · [llms.txt](https://quantexbot.pro/llms.txt) · [full Markdown](https://quantexbot.pro/docs/api.md) · copy in this repo: [`api/openapi.json`](api/openapi.json) |
| **Live status** | [quantexbot.pro/status](https://quantexbot.pro/status) · JSON: [`GET /v1/status`](https://api.quantexbot.pro/v1/status) (no key) |
| **Code examples** | [`examples/`](examples/) — Python, Node.js, PHP, JavaScript |

### What you can build

- 📡 **Your own signal channel or bot** — receive every signal the QUANTEX bot delivers (entry time, expiry, direction, payout, confidence) and its WIN / LOSS result, by polling, **webhooks** or a **live stream**.
- 📊 **Dashboards and analytics** — payouts of every pair, OHLC candles (M1 → H4), daily win rates.
- 🔍 **Result checking** — send a signal list, get WIN / LOSS / NO_DATA with martingale steps.
- 🔮 **Future signal lists** — the same generators as the bot's Future Signal (OTC, Live, Blackout, Whiteout).
- 📰 **News trading** — the economic calendar with the expected direction and the pairs to trade.

### Endpoints

| Method | Path | What it does | Group |
|---|---|---|---|
| GET | `/v1/status` | API, data feed, bot and payment status + incidents (no key) | public |
| GET | `/v1/account` | Your plan, limits, usage and the key in use | account |
| GET | `/v1/usage` | Requests per day and per endpoint | account |
| GET | `/v1/brokers` | QUOTEX, TRADOWIX, BINOLLA and whether their feed is live | markets |
| GET | `/v1/pairs` | Pairs of a broker: OTC / Live, category, open now, payout | markets |
| GET | `/v1/payouts` | Current payout % of every pair | payouts |
| GET | `/v1/candles` | OHLC candles M1–H4 (closed candles only), activity volume, payout | candles |
| POST | `/v1/checker` | WIN / LOSS / NO_DATA of a signal list with MTG | checker |
| GET | `/v1/news` | Economic events with bias, confidence and pairs | news |
| GET | `/v1/signals/live` | Live signals + results, cursor polling | signals |
| GET | `/v1/signals/{id}` | One signal with its result | signals |
| GET | `/v1/results` | A day's settled signals + win rate | signals |
| POST | `/v1/future` | Start a future signal list (async, 202) | future |
| GET | `/v1/jobs/{id}` | The future list job and its result | future |
| GET | `/v1/stream/signals` | Server-Sent Events stream of signals and results | stream |
| GET | `/v1/openapi.json` | This API as OpenAPI 3.1 (no key) | public |
| — | Webhooks | `signal.created` / `signal.result` POSTed to your HTTPS server, signed | webhooks |

### Contents

- [Introduction](#introduction) · [Quick start](#quick-start) · [Testing in the browser](#testing-in-the-browser) · [Authentication](#authentication) · [API keys](#api-keys)
- [Base URL and versioning](#base-url-and-versioning) · [Response format](#response-format) · [Rate limits](#rate-limits) · [Examples](#examples) · [Telegram bot integration](#telegram-bot-integration)
- [Live signals and results](#live-signals-and-results) · [Webhooks](#webhooks) · [Signal stream](#signal-stream-server-sent-events) · [Future signals](#future-signals) · [Usage guide](#usage-guide)
- [Endpoint reference](#endpoint-reference) · [Error codes](#error-codes) · [Plans](#plans)

---

## Introduction

The QUANTEX Developer API gives your apps and Telegram bots the same market data QUANTEX uses: the brokers and their OTC / Live pairs, current payouts, candles, the live signals the bot delivers with their results, future signal lists, the signal checker and the economic news calendar. Every endpoint, parameter and example is listed in the **Endpoint reference** below.

> Binary options trading carries high risk. Data from the API is analysis, not a guarantee.

## Quick start

1. [Create an account](https://quantexbot.pro/register) and confirm your email address.
2. Open **Dashboard → API keys**, create a key and copy it (it is shown only once).
3. Make your first request:

```bash
curl "https://api.quantexbot.pro/v1/pairs?broker=quotex&market=otc&open=true" \
  -H "Authorization: Bearer qx_live_YOUR_KEY"
```

The answer is JSON:

```json
{"ok": true, "data": [{"symbol": "EURUSD_otc", "name": "EUR/USD (OTC)", "market": "otc", "category": "currency", "open": true, "payout": 87, "updated_at": "2026-10-05T10:00:00Z"}], "meta": {"request_id": "req_…", "broker": "quotex", "count": 1}}
```

## Testing in the browser

A browser address bar cannot send headers, so for a quick test of a **GET** endpoint you can put the key in the address instead (`api_key=`). Paste the address into the browser and press Enter — the answer is shown as readable JSON:

```
https://api.quantexbot.pro/v1/pairs?broker=quotex&market=otc&open=true&api_key=qx_live_YOUR_KEY
```

More addresses to try:

```
https://api.quantexbot.pro/v1/payouts?broker=quotex&min=85&api_key=qx_live_YOUR_KEY
https://api.quantexbot.pro/v1/news?impact=high&days=1&api_key=qx_live_YOUR_KEY
https://api.quantexbot.pro/v1/account?api_key=qx_live_YOUR_KEY
```

- Works for **GET** requests only. `POST /v1/checker` needs the header (use the Python or Node.js example, or a tool such as Postman).
- A key in an address is saved in the browser history and can appear in logs. Use a **separate test key** with only the permissions it needs, and never put `api_key=` in apps, bots or shared links — send the header there.
- `https://api.quantexbot.pro/v1/status` needs no key at all.

## Authentication

Send your API key in the `Authorization` header of every request:

```
Authorization: Bearer qx_live_<prefix>_<secret>
```

`GET /v1/status` and `GET /v1/openapi.json` need no key. Never put a key in front-end code, a public repository, a chat or a screenshot — anyone with the key can use your quota.

## API keys

- Create and manage keys in **Dashboard → API keys**. The number of keys depends on your plan.
- **Permissions:** give each key only what it needs (for example `markets:read`, `payouts:read`, `checker:run`).
- **Allowed IP addresses:** optionally limit a key to your server's IP addresses or ranges.
- **Expiry:** optionally let a key expire after 30, 90, 180 or 365 days.
- **New secret:** replaces the secret and keeps the settings; the old secret stops working at once.
- **Revoke:** stops a key for good. If a key ever leaks, revoke it and create a new one.

QUANTEX stores only a hash of each key, so a lost key cannot be shown again — create a new one.

## Base URL and versioning

```
https://api.quantexbot.pro/v1
```

The version is part of the path. A change that would break existing code gets a new version (`/v2`) and `/v1` keeps working for a while. Times are always UTC (ISO 8601, e.g. `2026-10-05T10:00:00Z`).

## Response format

Every response is JSON with the same envelope.

A successful response:

```json
{"ok": true, "data": {}, "meta": {"request_id": "req_…"}}
```

An error response:

```json
{"ok": false, "error": {"code": "validation_failed", "message": "Some parameters are invalid.", "fields": {"pair": ["The pair field is required."]}}, "meta": {"request_id": "req_…"}}
```

Always check `ok` first. When `ok` is `false`, `error.code` tells you what went wrong. Quote `meta.request_id` (also in the `X-Request-Id` header) when you contact support. All error codes are listed in the reference below.

## Rate limits

Each plan has a number of requests per minute and per month for the whole account (all keys together). See the [pricing](https://quantexbot.pro/pricing) page for the plans.

Every answer tells you where you stand:

| Header | Meaning |
|---|---|
| `X-RateLimit-Limit` | requests allowed per minute |
| `X-RateLimit-Remaining` | requests left this minute |
| `X-Quota-Limit` | requests allowed this month |
| `X-Quota-Remaining` | requests left this month (resets on the 1st, UTC) |

When a limit is reached the API answers `429` (`rate_limited` or `quota_exceeded`) with a `Retry-After` header in seconds. Wait that long before trying again. Data is cached for a few seconds, so asking for the same thing more often than every 5–10 seconds only uses quota.

## Examples

Python (requests):

```python
import requests

API = "https://api.quantexbot.pro/v1"
HEADERS = {"Authorization": "Bearer qx_live_YOUR_KEY"}

r = requests.get(f"{API}/payouts", params={"broker": "quotex", "market": "otc", "min": 85}, headers=HEADERS, timeout=15)
body = r.json()
if body["ok"]:
    for pair in body["data"]:
        print(pair["name"], pair["payout"], "%")
else:
    print("Error:", body["error"]["code"], body["error"]["message"])
```

Node.js (18+):

```javascript
const API = "https://api.quantexbot.pro/v1";
const res = await fetch(`${API}/checker`, {
  method: "POST",
  headers: { "Authorization": "Bearer qx_live_YOUR_KEY", "Content-Type": "application/json" },
  body: JSON.stringify({ broker: "quotex", mtg: 1, date: "today", timezone: 6, text: "M1 EURUSD-OTC 14:05 CALL\nM1 GBPUSD-OTC 14:20 PUT" }),
});
const body = await res.json();
if (body.ok) console.log(body.data.summary);
else console.error(body.error.code, body.error.message);
```

PHP:

```php
<?php
$ch = curl_init('https://api.quantexbot.pro/v1/news?impact=high&days=1');
curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER => true, CURLOPT_HTTPHEADER => ['Authorization: Bearer qx_live_YOUR_KEY'], CURLOPT_TIMEOUT => 15]);
$body = json_decode(curl_exec($ch), true);
foreach ($body['ok'] ? $body['data']['events'] : [] as $event) {
    echo $event['time'], ' ', $event['currency'], ' ', $event['title'], ' → ', $event['bias'] ?? 'no bias', PHP_EOL;
}
```

## Telegram bot integration

A small Python bot that posts the best-paying open OTC pairs to your Telegram channel every 10 minutes. Make your bot an admin of the channel first.

```python
import time
import requests

QX_KEY = "qx_live_YOUR_KEY"              # Dashboard → API keys (permission: payouts:read)
BOT_TOKEN = "123456:ABC..."              # from @BotFather
CHANNEL = "@your_channel"

def best_pairs():
    r = requests.get("https://api.quantexbot.pro/v1/payouts",
                     params={"broker": "quotex", "market": "otc", "min": 85},
                     headers={"Authorization": f"Bearer {QX_KEY}"}, timeout=15)
    body = r.json()
    if not body["ok"]:
        raise RuntimeError(body["error"]["message"])
    return [p for p in body["data"] if p["open"]][:10]

while True:
    try:
        lines = [f"{p['name']} — {p['payout']}%" for p in best_pairs()]
        text = "Top OTC payouts now:\n" + "\n".join(lines) if lines else "No pair pays 85%+ right now."
        requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                      json={"chat_id": CHANNEL, "text": text}, timeout=15)
    except Exception as exc:
        print("skipped:", exc)
    time.sleep(600)
```

The same pattern works for the checker: collect your signals during the day, send them to `POST /v1/checker` in the evening and post the summary.

## Live signals and results

The live signals are the signals the QUANTEX bot really delivers to its Telegram users (Live Session, Auto Signal, Live Signal), each setup **once**, with its result after expiry. The API never starts a new analysis for a request, so polling is fast.

Poll every 2–5 seconds and pass the cursor of the last answer:

```bash
curl "https://api.quantexbot.pro/v1/signals/live?since=0&broker=quotex&tf=M1" \
  -H "Authorization: Bearer qx_live_YOUR_KEY"
```

- `active` — signals waiting for entry or running.
- `events` — `signal.created` (a new signal) and `signal.result` (its result), oldest first. Remember `next_cursor` and send it as `since` next time.
- Every signal has `entry_at` and `expiry_at` (UTC), `direction` (`CALL` / `PUT`), `payout`, `confidence` and `engine`. The result arrives later with the **same id**: `WIN` (`mtg_level` 0 = direct, 1 = after one martingale step), `LOSS` (also after one step) or `NO_DATA`.
- `GET /v1/signals/{id}` returns one signal; `GET /v1/results?date=YYYY-MM-DD` returns a day's settled signals with wins, losses and the win rate (30 days back).

A Python loop that posts each new signal to your Telegram channel:

```python
import time, requests

QX = {"Authorization": "Bearer qx_live_YOUR_KEY"}       # permission: signals:read
BOT, CHANNEL = "123456:ABC...", "@your_channel"
cursor = None

while True:
    params = {"broker": "quotex"} | ({"since": cursor} if cursor is not None else {})
    body = requests.get("https://api.quantexbot.pro/v1/signals/live", params=params, headers=QX, timeout=15).json()
    if body["ok"]:
        if cursor is not None:                                   # skip the history on the first call
            for ev in body["data"]["events"]:
                s = ev["signal"]
                text = (f"{s['pair']} {s['timeframe']} {s['direction']} at {s['entry_at'][11:16]} UTC"
                        if ev["type"] == "signal.created" else f"{s['pair']}: {s['result']}")
                requests.post(f"https://api.telegram.org/bot{BOT}/sendMessage", json={"chat_id": CHANNEL, "text": text}, timeout=15)
        cursor = body["data"]["next_cursor"]
    time.sleep(3)
```

## Webhooks

Instead of polling, let QUANTEX call your server: **Dashboard → API → Webhooks** → add your `https://` address. Each new `signal.created` and `signal.result` is POSTed within seconds as JSON `{"id", "type", "created_at", "data": {signal}}`.

- Check the header `X-Quantex-Signature: t=<unix time>,v1=<hex>`: HMAC-SHA256 of `"<t>.<raw body>"` with your webhook secret (shown once when you create it). Refuse requests older than 5 minutes.
- Answer with any 2xx status within 5 seconds. A failed delivery is tried again after 1, 5 and 30 minutes; after 10 deliveries in a row failed the webhook is turned off and you get an email.
- `X-Quantex-Event` holds the event type and `X-Quantex-Delivery` a delivery id (the same on every retry). Use **Send test** to try your endpoint.

## Signal stream (Server-Sent Events)

`GET /v1/stream/signals` keeps the connection open and sends every event the moment it arrives (`id:` is the cursor, `event:` the type, `data:` the event JSON). After 5 minutes the server ends the stream with `event: reconnect`; reconnect with the `Last-Event-ID` header and nothing is missed. At most 2 open streams per account.

```bash
curl -N "https://api.quantexbot.pro/v1/stream/signals?broker=quotex" -H "Authorization: Bearer qx_live_YOUR_KEY"
```

## Future signals

`POST /v1/future` makes a future signal list with the same generators as the bot's **Future Signal** (OTC, Live, Blackout, Whiteout). It answers `202` with a job at once; ask `GET /v1/jobs/{id}` every few seconds until `status` is `done` (or `failed` with the reason).

```bash
curl -X POST "https://api.quantexbot.pro/v1/future" \
  -H "Authorization: Bearer qx_live_YOUR_KEY" -H "Content-Type: application/json" \
  -d '{"mode": "otc", "start": "18:00", "end": "22:00", "timezone": 6, "system": 1, "strategy": 1, "pairs": ["EURUSD_otc", "USDJPY_otc"]}'
```

## Usage guide

- **Dashboard → API overview** shows your plan, limits and today's activity; **API usage** shows requests per day and per endpoint; **API logs** lists every request of the last 90 days (request bodies and keys are never stored).
- **My APIs** shows which endpoint groups your plan includes. Endpoints outside your plan answer `403 plan_upgrade_required`; upgrade in **Billing → Upgrade plan**.
- Live signals, results and future lists need the **signals:read** / **future:generate** permissions on the key; webhooks and the stream are in the Pro and Business plans.
- Questions? Visit the [contact](https://quantexbot.pro/contact) page; news about the API is posted on the [main channel](https://t.me/bdtraderpro).

## Endpoint reference

Every answer is JSON: `{"ok": true, "data": …, "meta": {"request_id": "req_…"}}` or `{"ok": false, "error": {"code", "message"}, "meta": {…}}`. Send the key as `Authorization: Bearer qx_live_…` (or `?api_key=` on GET, for quick tests in a browser).

### `GET /v1/status`

Status of the API, data feeds, Telegram bot and payments, and open incidents (the same as quantexbot.pro/status). status: operational, degraded, partial_outage, major_outage or maintenance; each component: operational, degraded, down or unknown. No key needed.

- No API key needed.

Example `data`:

```json
{
    "status": "operational",
    "api_version": "v1",
    "server_time": "2026-10-05T10:00:00Z",
    "components": {
        "api": "operational",
        "market_data": "operational",
        "website": "operational",
        "telegram_bot": "operational",
        "payments": "operational"
    },
    "incidents": [],
    "page": "https://quantexbot.pro/status"
}
```

### `GET /v1/account`

Your plan, its limits, what you used and the key in use.

- Key permission (scope): `account:read` · endpoint group: `account` · plans: Developer, Starter, Pro, Business

Example `data`:

```json
{
    "plan": {
        "key": "starter",
        "name": "Starter",
        "expires_at": "2026-11-04T10:00:00Z"
    },
    "limits": {
        "requests_per_minute": 60,
        "requests_per_month": 100000,
        "api_keys": 2
    },
    "usage": {
        "month": 1520,
        "month_remaining": 98480,
        "resets_at": "2026-11-01T00:00:00Z"
    },
    "groups": [
        "markets",
        "payouts",
        "news",
        "account",
        "checker"
    ],
    "key": {
        "name": "My bot",
        "prefix": "Ab12Cd34",
        "scopes": [
            "markets:read",
            "checker:run"
        ]
    }
}
```

### `GET /v1/usage`

Requests per day and per endpoint.

- Key permission (scope): `account:read` · endpoint group: `account` · plans: Developer, Starter, Pro, Business

| parameter | in | type | required | description |
|---|---|---|---|---|
| `days` | query | integer | no | Number of days, 1-90. Default: 30. |

Example `data`:

```json
{
    "days": [
        {
            "date": "2026-10-05",
            "requests": 320,
            "errors": 2
        }
    ],
    "endpoints": [
        {
            "endpoint": "pairs",
            "requests": 210,
            "errors": 0
        }
    ]
}
```

### `GET /v1/brokers`

Supported brokers and whether their data feed is live.

- Key permission (scope): `markets:read` · endpoint group: `markets` · plans: Developer, Starter, Pro, Business

Example `data`:

```json
[
    {
        "id": "quotex",
        "name": "QUOTEX",
        "status": "operational",
        "pairs": 92,
        "open_pairs": 61,
        "markets": [
            "live",
            "otc"
        ],
        "updated_at": "2026-10-05T10:00:00Z"
    }
]
```

### `GET /v1/pairs`

Pairs of a broker: OTC or Live, category, open now, current payout.

- Key permission (scope): `markets:read` · endpoint group: `markets` · plans: Developer, Starter, Pro, Business

| parameter | in | type | required | description |
|---|---|---|---|---|
| `broker` | query | string | no | Broker: quotex, tradowix or binolla. One of: quotex, tradowix, binolla. Default: quotex. |
| `market` | query | string | no | otc, live or all. One of: all, otc, live. Default: all. |
| `open` | query | boolean | no | true = only pairs that are open now. Default: false. |

Example `data`:

```json
[
    {
        "symbol": "EURUSD_otc",
        "name": "EUR/USD (OTC)",
        "market": "otc",
        "category": "currency",
        "open": true,
        "payout": 87,
        "updated_at": "2026-10-05T10:00:00Z"
    }
]
```

### `GET /v1/payouts`

Current payout % of every pair, highest first.

- Key permission (scope): `payouts:read` · endpoint group: `payouts` · plans: Developer, Starter, Pro, Business

| parameter | in | type | required | description |
|---|---|---|---|---|
| `broker` | query | string | no | Broker: quotex, tradowix or binolla. One of: quotex, tradowix, binolla. Default: quotex. |
| `market` | query | string | no | otc, live or all. One of: all, otc, live. Default: all. |
| `min` | query | integer | no | Only pairs paying at least this % (0-100). Default: 0. |

Example `data`:

```json
[
    {
        "symbol": "BTCUSD_otc",
        "name": "BTC/USD (OTC)",
        "market": "otc",
        "payout": 92,
        "open": true,
        "updated_at": "2026-10-05T10:00:00Z"
    }
]
```

### `GET /v1/candles`

OHLC candles (UTC), oldest first. M1 gives every stored minute (only closed minutes are stored). M5 and higher give only closed candles: the running candle is left out until its period has ended (at 12:23 the newest M5 candle is the one of 12:15; 12:20 arrives complete after 12:25). Without date: the most recent candles; with date: that UTC day (within your plan's history). Brokers give no real volume, so volume is an activity score: the candle's range (60 %) and body (40 %) against the average of the 20 candles before it, x100 (100 = normal, 0 when fewer than 20 earlier candles). payout = the broker's payout % when the candle opened.

- Key permission (scope): `candles:read` · endpoint group: `candles` · plans: Pro, Business

| parameter | in | type | required | description |
|---|---|---|---|---|
| `broker` | query | string | no | Broker: quotex, tradowix or binolla. One of: quotex, tradowix, binolla. Default: quotex. |
| `pair` | query | string | yes | Pair symbol from /v1/pairs, e.g. EURUSD_otc. |
| `tf` | query | string | no | Timeframe. One of: M1, M5, M15, M30, H1, H4. Default: M1. |
| `limit` | query | integer | no | Number of candles, 1-1000 (newest last). Default: 100. |
| `date` | query | string | no | UTC day, YYYY-MM-DD. |

Example `data`:

```json
{
    "broker": "quotex",
    "symbol": "EURUSD_otc",
    "timeframe": "M1",
    "candles": [
        {
            "time": "2026-10-05T07:27:00Z",
            "chart_open": true,
            "epoch": 1791185220,
            "open": 17800.91,
            "high": 17801.26,
            "low": 17799.7,
            "close": 17800.03,
            "payout": 89,
            "volume": 87
        },
        {
            "time": "2026-10-05T07:28:00Z",
            "chart_open": true,
            "epoch": 1791185280,
            "open": 17800.03,
            "high": 17800.08,
            "low": 17798.43,
            "close": 17798.6,
            "payout": 89,
            "volume": 124
        }
    ]
}
```

### `POST /v1/checker`

Check a signal list: WIN / LOSS / NO_DATA for each signal, with martingale (MTG) steps.

- Key permission (scope): `checker:run` · endpoint group: `checker` · plans: Starter, Pro, Business

JSON body:

| field | type | required | description |
|---|---|---|---|
| `broker` | string | no | quotex, tradowix or binolla (default quotex). |
| `signals` | array | no | Up to 200 objects: {"pair":"EURUSD_otc","time":"14:05","direction":"BUY","timeframe":"M1"}. Direction BUY/CALL or PUT/SELL. |
| `text` | string | no | Or paste a list in the bot format, one per line: "M1 EURUSD-OTC 14:05 CALL". |
| `mtg` | integer | no | Martingale steps 0-3 (default 1). |
| `date` | string | no | today, yesterday or YYYY-MM-DD (last 30 days). |
| `timezone` | number | no | UTC offset of the signal times in hours, e.g. 6 or -3 (default 6). |

Example `data`:

```json
{
    "broker": "quotex",
    "date": "2026-10-05",
    "timezone": 6,
    "mtg": 1,
    "results": [
        {
            "pair": "EURUSD_otc",
            "time": "14:05",
            "direction": "BUY",
            "timeframe": "M1",
            "result": "WIN",
            "mtg_level": 0,
            "payout": 87
        }
    ],
    "summary": {
        "total": 1,
        "wins": 1,
        "losses": 0,
        "no_data": 0,
        "win_rate": 100,
        "mtg_breakdown": [
            1,
            0
        ]
    },
    "rejected": []
}
```

### `GET /v1/news`

Upcoming economic events with the expected direction (bias) and the pairs to trade. The direction combines forecast vs previous, how the market reacted to past releases of the same event, the trend and AI; unclear news is skipped, and a currency / pair never gets two directions at the same minute. days=1 is the rest of today (in your timezone), 2 adds tomorrow, 3 the day after.

- Key permission (scope): `news:read` · endpoint group: `news` · plans: Developer, Starter, Pro, Business

| parameter | in | type | required | description |
|---|---|---|---|---|
| `days` | query | integer | no | 1-3 days ahead. Default: 1. |
| `impact` | query | string | no | high, medium, low or all. One of: all, high, medium, low. Default: all. |
| `currency` | query | string | no | Comma-separated currencies, e.g. USD,EUR. |
| `timezone` | query | number | no | UTC offset used for "today" (default 6). Default: 6. |

Example `data`:

```json
{
    "events": [
        {
            "time": "2026-10-05T12:30:00Z",
            "currency": "USD",
            "impact": "high",
            "title": "CPI m/m",
            "forecast": "0.4%",
            "previous": "0.2%",
            "bias": "bullish",
            "confidence": 78,
            "bias_source": "analysis",
            "factors": {
                "fundamental": 0.66,
                "history": 0.6,
                "technical": 0.21
            },
            "pairs_up": [
                "USDJPY"
            ],
            "pairs_down": [
                "EURUSD"
            ]
        }
    ],
    "skipped": 1,
    "reason": null,
    "source": "ForexFactory economic calendar + QUANTEX analysis"
}
```

### `GET /v1/signals/live`

Live signals the QUANTEX bot delivered, and their results. active = signals waiting for entry or running. events = signal.created and signal.result, oldest first; ask again with since=next_cursor (every 2-5 s) to get only new events. Without since: the latest events. A signal has its entry and expiry time (UTC), so your own bot can post it at once; its result arrives later with the same id. result: WIN (mtg_level 0 = direct, 1 = after one martingale step), LOSS (also after one martingale step) or NO_DATA.

- Key permission (scope): `signals:read` · endpoint group: `signals` · plans: Starter, Pro, Business

| parameter | in | type | required | description |
|---|---|---|---|---|
| `since` | query | integer | no | Cursor from next_cursor of the last answer. |
| `limit` | query | integer | no | Events per answer, 1-500. Default: 100. |
| `broker` | query | string | no | Broker(s), comma-separated: quotex, tradowix, binolla. Empty = all. |
| `market` | query | string | no | otc, live or all. One of: all, otc, live. Default: all. |
| `tf` | query | string | no | Timeframe(s), comma-separated, e.g. M1,M5. Empty = all. |
| `pair` | query | string | no | Pair(s), comma-separated, e.g. EURUSD_otc. Empty = all. |

Example `data`:

```json
{
    "active": [],
    "events": [
        {
            "cursor": 1042,
            "type": "signal.result",
            "created_at": "2026-10-05T10:32:09Z",
            "signal": {
                "id": "sig_3f9a1c0d2b7e4a6f8c11",
                "broker": "quotex",
                "pair": "EURUSD_otc",
                "market": "otc",
                "timeframe": "M1",
                "direction": "CALL",
                "entry_at": "2026-10-05T10:31:00Z",
                "expiry_at": "2026-10-05T10:32:00Z",
                "entry_epoch": 1791196260,
                "payout": 87,
                "confidence": 82,
                "engine": "hybrid",
                "status": "settled",
                "result": "WIN",
                "mtg_level": 0,
                "result_at": "2026-10-05T10:32:09Z"
            }
        }
    ],
    "next_cursor": 1042
}
```

### `GET /v1/signals/{id}`

One signal by id, with its result when it is known (status pending, running or settled).

- Key permission (scope): `signals:read` · endpoint group: `signals` · plans: Starter, Pro, Business

| parameter | in | type | required | description |
|---|---|---|---|---|
| `id` | path | string | yes | Signal id (sig_…). |

Example `data`:

```json
{
    "id": "sig_3f9a1c0d2b7e4a6f8c11",
    "broker": "quotex",
    "pair": "EURUSD_otc",
    "market": "otc",
    "timeframe": "M1",
    "direction": "CALL",
    "entry_at": "2026-10-05T10:31:00Z",
    "expiry_at": "2026-10-05T10:32:00Z",
    "entry_epoch": 1791196260,
    "payout": 87,
    "confidence": 82,
    "engine": "hybrid",
    "status": "settled",
    "result": "WIN",
    "mtg_level": 0,
    "result_at": "2026-10-05T10:32:09Z"
}
```

### `GET /v1/results`

Settled signals of one UTC day with a summary: wins, mtg_wins (won after one martingale step), losses, win_rate (with one martingale step) and win_rate_no_mtg. Up to 30 days back.

- Key permission (scope): `signals:read` · endpoint group: `signals` · plans: Starter, Pro, Business

| parameter | in | type | required | description |
|---|---|---|---|---|
| `date` | query | string | no | UTC day, YYYY-MM-DD (default today). |
| `limit` | query | integer | no | Signals in the list, 1-1000. Default: 500. |
| `broker` | query | string | no | Broker(s), comma-separated: quotex, tradowix, binolla. Empty = all. |
| `market` | query | string | no | otc, live or all. One of: all, otc, live. Default: all. |
| `tf` | query | string | no | Timeframe(s), comma-separated, e.g. M1,M5. Empty = all. |
| `pair` | query | string | no | Pair(s), comma-separated, e.g. EURUSD_otc. Empty = all. |

Example `data`:

```json
{
    "date": "2026-10-05",
    "summary": {
        "total": 48,
        "wins": 33,
        "mtg_wins": 9,
        "losses": 5,
        "no_data": 1,
        "win_rate": 89.36,
        "win_rate_no_mtg": 70.21
    },
    "results": [
        {
            "id": "sig_3f9a1c0d2b7e4a6f8c11",
            "broker": "quotex",
            "pair": "EURUSD_otc",
            "market": "otc",
            "timeframe": "M1",
            "direction": "CALL",
            "entry_at": "2026-10-05T10:31:00Z",
            "expiry_at": "2026-10-05T10:32:00Z",
            "entry_epoch": 1791196260,
            "payout": 87,
            "confidence": 82,
            "engine": "hybrid",
            "status": "settled",
            "result": "WIN",
            "mtg_level": 0,
            "result_at": "2026-10-05T10:32:09Z"
        }
    ]
}
```

### `POST /v1/future`

Make a future signal list with the QUANTEX future generators (the same as the bot's Future Signal). Answers 202 with a job at once; the list is usually ready in a few seconds: GET /v1/jobs/{id}. Times are in the timezone you send.

- Key permission (scope): `future:generate` · endpoint group: `future` · plans: Starter, Pro, Business
- Success status: 202

JSON body:

| field | type | required | description |
|---|---|---|---|
| `mode` | string | no | otc (default), live, blackout or whiteout (blackout / whiteout give times without a direction). |
| `broker` | string | no | quotex (default), tradowix or binolla. |
| `start` | string | no | From HH:MM (default 00:00), in your timezone. |
| `end` | string | no | To HH:MM (default 23:59), in your timezone. |
| `timezone` | number | no | UTC offset in hours, e.g. 6 or -3 (default 6). |
| `system` | integer | no | Gap between signals: 1 = LITE (2 min), 2 = PRO (5 min), 3 = ULTRA (7 min), 4 = HYBRID (2/5/7). |
| `strategy` | integer | no | 1 PRECISION (up trends, CALL), 2 COUNTER (down trends, PUT), 3 DYNAMIC, 4 ADAPTIVE (mixed). |
| `quantity` | integer | no | Maximum signals: 1 = 15, 2 = 30 (default), 3 = all. |
| `pairs` | array | no | Pairs to use, e.g. ["EURUSD_otc","USDJPY_otc"]. Empty = every open pair. |

Example `data`:

```json
{
    "id": "9d2c4b1e-7a3f-4c58-9e0a-2b6d8f1c3a47",
    "type": "future",
    "status": "queued",
    "created_at": "2026-10-05T10:00:00Z",
    "finished_at": null,
    "params": {
        "mode": "otc",
        "broker": "quotex",
        "start": "18:00",
        "end": "22:00",
        "timezone": 6,
        "system": 1,
        "strategy": 1,
        "quantity": 2,
        "pairs": []
    },
    "poll": "https://api.quantexbot.pro/v1/jobs/9d2c4b1e-7a3f-4c58-9e0a-2b6d8f1c3a47"
}
```

### `GET /v1/jobs/{id}`

State of a future list job: queued, running, done (result.signals) or failed (error). Jobs are kept 7 days.

- Key permission (scope): `future:generate` · endpoint group: `future` · plans: Starter, Pro, Business

| parameter | in | type | required | description |
|---|---|---|---|---|
| `id` | path | string | yes | Job id from POST /v1/future. |

Example `data`:

```json
{
    "id": "9d2c4b1e-7a3f-4c58-9e0a-2b6d8f1c3a47",
    "type": "future",
    "status": "done",
    "created_at": "2026-10-05T10:00:00Z",
    "finished_at": "2026-10-05T10:00:04Z",
    "params": {
        "mode": "otc",
        "timezone": 6
    },
    "result": {
        "mode": "otc",
        "broker": "quotex",
        "timezone": 6,
        "date": "2026-10-05",
        "timeframe": "M1",
        "system": "Q-BOT LITE",
        "strategy": "PRECISION",
        "pairs_scanned": 41,
        "reason": null,
        "signals": [
            {
                "pair": "EURUSD_otc",
                "time": "18:05",
                "time_utc": "2026-10-05T12:05:00Z",
                "direction": "CALL"
            }
        ]
    }
}
```

### `GET /v1/stream/signals`

Server-Sent Events: every new signal.created / signal.result the moment it arrives (id = cursor). The stream closes after 5 minutes with event "reconnect"; reconnect with the Last-Event-ID header (EventSource does this by itself) so nothing is missed. At most 2 open streams per account.

- Key permission (scope): `signals:read` · endpoint group: `stream` · plans: Pro, Business
- Content type: `text/event-stream`

| parameter | in | type | required | description |
|---|---|---|---|---|
| `since` | query | integer | no | Start after this cursor (default: only new events). |
| `broker` | query | string | no | Broker(s), comma-separated: quotex, tradowix, binolla. Empty = all. |
| `market` | query | string | no | otc, live or all. One of: all, otc, live. Default: all. |
| `tf` | query | string | no | Timeframe(s), comma-separated, e.g. M1,M5. Empty = all. |
| `pair` | query | string | no | Pair(s), comma-separated, e.g. EURUSD_otc. Empty = all. |

### `GET /v1/openapi.json`

This API described as an OpenAPI 3.1 file. No key needed.

- No API key needed.

## Error codes

| code | HTTP | meaning |
|---|---|---|
| `unauthenticated` | 401 | No API key was sent. |
| `invalid_api_key` | 401 | The API key is not valid. |
| `key_revoked` | 403 | The key was revoked. |
| `key_expired` | 403 | The key has expired. |
| `account_suspended` | 403 | The account is suspended. |
| `ip_not_allowed` | 403 | The request came from an IP address that is not on the key's list. |
| `insufficient_scope` | 403 | The key does not have the permission this endpoint needs (error.required_scope). |
| `plan_upgrade_required` | 403 | Your plan does not include this endpoint group (error.required_group). |
| `history_limit` | 403 | The requested date is older than your plan's candle history. |
| `not_found` | 404 | The endpoint does not exist. |
| `pair_not_found` | 404 | The pair is not available at this broker. |
| `signal_not_found` | 404 | No signal with this id. |
| `job_not_found` | 404 | No job with this id for your account. |
| `method_not_allowed` | 405 | Wrong HTTP method for this endpoint. |
| `payload_too_large` | 413 | The request body is larger than 64 KB. |
| `validation_failed` | 422 | Some parameters are invalid (error.fields lists them). |
| `rate_limited` | 429 | Too many requests this minute (Retry-After header). |
| `quota_exceeded` | 429 | The monthly quota is used up (error.resets_at). |
| `too_many_jobs` | 429 | Too many future lists in progress for this account; wait for one to finish. |
| `too_many_streams` | 429 | Too many open signal streams for this account. |
| `internal_error` | 500 | Server problem; quote meta.request_id to support. |
| `service_unavailable` | 503 | Market data is temporarily unavailable (Retry-After header). |
| `busy` | 503 | The data service is busy; retry in a few seconds. |

## Plans

| plan | price (USDT / month) | requests / minute | requests / month | keys | webhooks | endpoint groups |
|---|---|---|---|---|---|---|
| Developer | 0 | 10 | 3,000 | 1 | 0 | markets, payouts, news, account |
| Starter | 29 | 60 | 100,000 | 2 | 0 | markets, payouts, news, account, checker, signals, future |
| Pro | 79 | 300 | 1,000,000 | 5 | 3 | markets, payouts, news, account, checker, signals, future, candles, webhooks, stream |
| Business | 199 | 1000 | 5,000,000 | 20 | 10 | markets, payouts, news, account, checker, signals, future, candles, webhooks, stream |

Binary options trading carries high risk. Data from the API is analysis, not a guarantee.

---

> Prices and limits above are the defaults; the current list is always on [quantexbot.pro/pricing](https://quantexbot.pro/pricing). This file is generated from the same endpoint catalog the API itself uses, so it matches the live API. The live version of this page: [quantexbot.pro/docs/api](https://quantexbot.pro/docs/api).
