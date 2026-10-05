# 🧪 QUANTEX Developer API — code examples

Small, complete programs you can copy. Put your key in the environment variable `QUANTEX_API_KEY` (create it in [Dashboard → API keys](https://quantexbot.pro/dashboard/api/keys)); never write a key into code you share.

| File | Language | What it shows | Plan |
|---|---|---|---|
| [curl.md](curl.md) | shell | One request per endpoint | any |
| [python/live_signals_to_telegram.py](python/live_signals_to_telegram.py) | Python | Poll `/v1/signals/live` with a cursor and post each signal and result to your Telegram channel | Starter+ |
| [python/check_signals.py](python/check_signals.py) | Python | Check a signal list with `POST /v1/checker` | Starter+ |
| [python/future_list.py](python/future_list.py) | Python | `POST /v1/future`, then wait for `GET /v1/jobs/{id}` | Starter+ |
| [python/webhook_receiver_flask.py](python/webhook_receiver_flask.py) | Python | Receive webhooks and verify `X-Quantex-Signature` | Pro+ |
| [node/webhook_receiver_express.js](node/webhook_receiver_express.js) | Node.js | The same webhook receiver in Express | Pro+ |
| [node/stream_signals.js](node/stream_signals.js) | Node.js | Read the Server-Sent Events stream `/v1/stream/signals`, reconnect with `Last-Event-ID` | Pro+ |
| [php/webhook_receiver.php](php/webhook_receiver.php) | PHP | Webhook receiver for any PHP host | Pro+ |

Full documentation: [../DEVELOPER_API.md](../DEVELOPER_API.md) · OpenAPI: [../api/openapi.json](../api/openapi.json)
