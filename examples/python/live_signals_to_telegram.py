"""Post every new QUANTEX live signal and its result to your Telegram channel.

Needs: pip install requests
Env:   QUANTEX_API_KEY (permission signals:read), TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL (e.g. @your_channel)
The bot must be an admin of the channel.
"""
import os
import time

import requests

API = "https://api.quantexbot.pro/v1"
HEADERS = {"Authorization": f"Bearer {os.environ['QUANTEX_API_KEY']}"}
BOT = os.environ["TELEGRAM_BOT_TOKEN"]
CHANNEL = os.environ["TELEGRAM_CHANNEL"]
FILTERS = {"broker": "quotex", "tf": "M1"}          # remove to get every broker / timeframe


def send(text: str) -> None:
    requests.post(f"https://api.telegram.org/bot{BOT}/sendMessage",
                  json={"chat_id": CHANNEL, "text": text}, timeout=15)


def describe(event: dict) -> str:
    s = event["signal"]
    if event["type"] == "signal.created":
        arrow = "🟢 CALL" if s["direction"] == "CALL" else "🔴 PUT"
        return (f"{s['pair']} · {s['timeframe']} · {arrow}\n"
                f"Entry {s['entry_at'][11:16]} UTC · payout {s['payout']}% · confidence {s['confidence']}%")
    mtg = " (MTG)" if s.get("mtg_level") else ""
    return f"{s['pair']} {s['entry_at'][11:16]} UTC → {s['result']}{mtg}"


def main() -> None:
    cursor = None
    while True:
        params = dict(FILTERS)
        if cursor is not None:
            params["since"] = cursor
        try:
            r = requests.get(f"{API}/signals/live", params=params, headers=HEADERS, timeout=15)
            body = r.json()
            if not body["ok"]:
                print("API:", body["error"]["code"], body["error"]["message"])
                time.sleep(int(r.headers.get("Retry-After", 10)))
                continue
            data = body["data"]
            if cursor is not None:                     # first call: only remember where we are
                for event in data["events"]:
                    send(describe(event))
            cursor = data["next_cursor"]
        except requests.RequestException as exc:
            print("network:", exc)
        time.sleep(3)


if __name__ == "__main__":
    main()
