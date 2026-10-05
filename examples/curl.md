# cURL — one request per endpoint

```bash
export QX="Authorization: Bearer $QUANTEX_API_KEY"
API=https://api.quantexbot.pro/v1

# Public (no key)
curl "$API/status"
curl "$API/openapi.json"

# Account
curl -H "$QX" "$API/account"
curl -H "$QX" "$API/usage?days=7"

# Markets
curl -H "$QX" "$API/brokers"
curl -H "$QX" "$API/pairs?broker=quotex&market=otc&open=true"
curl -H "$QX" "$API/payouts?broker=tradowix&min=85"
curl -H "$QX" "$API/candles?broker=quotex&pair=EURUSD_otc&tf=M5&limit=50"

# Checker
curl -X POST -H "$QX" -H "Content-Type: application/json" "$API/checker" \
  -d '{"broker":"quotex","mtg":1,"date":"today","timezone":6,"signals":[{"pair":"EURUSD_otc","time":"14:05","direction":"CALL","timeframe":"M1"}]}'

# News
curl -H "$QX" "$API/news?days=1&impact=high"

# Live signals and results
curl -H "$QX" "$API/signals/live?broker=quotex"            # latest events + next_cursor
curl -H "$QX" "$API/signals/live?since=1042"               # only what is new after cursor 1042
curl -H "$QX" "$API/signals/sig_3f9a1c0d2b7e4a6f8c11"
curl -H "$QX" "$API/results?date=2026-10-05&broker=quotex"

# Future list (async)
curl -X POST -H "$QX" -H "Content-Type: application/json" "$API/future" \
  -d '{"mode":"otc","start":"18:00","end":"22:00","timezone":6,"system":1,"strategy":1,"quantity":2}'
curl -H "$QX" "$API/jobs/<job id from the answer>"

# Stream (Server-Sent Events) — keep the connection open
curl -N -H "$QX" "$API/stream/signals?broker=quotex"
```

In a browser address bar (GET only, for quick tests): add `api_key=qx_live_…` to the address, e.g.
`https://api.quantexbot.pro/v1/pairs?broker=quotex&api_key=qx_live_YOUR_KEY`. Use a separate test key with few permissions.
