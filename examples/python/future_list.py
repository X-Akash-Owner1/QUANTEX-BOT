"""Make a future signal list (async job) and print it.

Needs: pip install requests · Env: QUANTEX_API_KEY (permission future:generate)
"""
import os
import time

import requests

API = "https://api.quantexbot.pro/v1"
HEADERS = {"Authorization": f"Bearer {os.environ['QUANTEX_API_KEY']}"}

job = requests.post(f"{API}/future", headers=HEADERS, timeout=20, json={
    "mode": "otc",            # otc | live | blackout | whiteout
    "broker": "quotex",
    "start": "18:00", "end": "22:00", "timezone": 6,
    "system": 1,              # 1 LITE (2 min gap) · 2 PRO (5) · 3 ULTRA (7) · 4 HYBRID
    "strategy": 1,            # 1 PRECISION · 2 COUNTER · 3 DYNAMIC · 4 ADAPTIVE
    "quantity": 2,            # 1 = max 15 · 2 = max 30 · 3 = all
    "pairs": [],              # empty = every open pair
}).json()
if not job["ok"]:
    raise SystemExit(job["error"]["message"])
job_id = job["data"]["id"]

while True:
    time.sleep(3)
    state = requests.get(f"{API}/jobs/{job_id}", headers=HEADERS, timeout=20).json()["data"]
    if state["status"] in ("done", "failed"):
        break

if state["status"] == "failed":
    raise SystemExit(state["error"]["message"])
result = state["result"]
print(f"{result['mode'].upper()} FS · {result['date']} · UTC{result['timezone']:+g}")
for s in result["signals"]:
    print(f"M1 {s['pair']} {s['time']} {s['direction'] or ''}")
