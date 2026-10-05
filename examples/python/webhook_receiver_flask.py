"""Receive QUANTEX webhooks (signal.created / signal.result / ping) and verify the signature.

Needs: pip install flask · Env: QUANTEX_WEBHOOK_SECRET (whsec_…, shown once when you add the webhook)
Run behind HTTPS (QUANTEX only sends to https:// addresses).
"""
import hashlib
import hmac
import json
import os
import time

from flask import Flask, abort, request

SECRET = os.environ["QUANTEX_WEBHOOK_SECRET"].encode()
app = Flask(__name__)
seen = set()                       # delivery ids already handled (retries reuse the same id)


def verified(raw: bytes, header: str) -> bool:
    parts = dict(p.split("=", 1) for p in header.split(",") if "=" in p)
    t, v1 = parts.get("t", ""), parts.get("v1", "")
    if not t.isdigit() or abs(time.time() - int(t)) > 300:
        return False
    expected = hmac.new(SECRET, t.encode() + b"." + raw, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, v1)


@app.post("/quantex/webhook")
def webhook():
    raw = request.get_data()
    if not verified(raw, request.headers.get("X-Quantex-Signature", "")):
        abort(401)
    delivery = request.headers.get("X-Quantex-Delivery", "")
    if delivery in seen:
        return "", 200               # already handled
    seen.add(delivery)
    event = json.loads(raw)
    if event["type"] == "signal.created":
        s = event["data"]
        print("NEW", s["pair"], s["timeframe"], s["direction"], "entry", s["entry_at"])
    elif event["type"] == "signal.result":
        s = event["data"]
        print("RESULT", s["pair"], s["result"], "mtg", s["mtg_level"])
    return "", 200                   # answer 2xx within 5 seconds; do slow work later


if __name__ == "__main__":
    app.run(port=8080)
