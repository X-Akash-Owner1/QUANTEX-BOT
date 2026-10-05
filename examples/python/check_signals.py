"""Check a signal list with the QUANTEX checker (WIN / LOSS / NO_DATA, martingale steps).

Needs: pip install requests · Env: QUANTEX_API_KEY (permission checker:run)
"""
import os

import requests

LIST = """
M1 EURUSD-OTC 14:05 CALL
M1 USDJPY-OTC 14:12 PUT
M1 GBPUSD-OTC 14:20 CALL
"""

r = requests.post(
    "https://api.quantexbot.pro/v1/checker",
    headers={"Authorization": f"Bearer {os.environ['QUANTEX_API_KEY']}"},
    json={"broker": "quotex", "text": LIST, "mtg": 1, "date": "today", "timezone": 6},
    timeout=30,
)
body = r.json()
if not body["ok"]:
    raise SystemExit(f"{body['error']['code']}: {body['error']['message']}")
for row in body["data"]["results"]:
    print(f"{row['pair']:<14} {row['time']} {row['direction']:<4} → {row['result']} (MTG {row['mtg_level']})")
s = body["data"]["summary"]
print(f"\n{s['wins']} wins / {s['losses']} losses · win rate {s['win_rate']}%")
