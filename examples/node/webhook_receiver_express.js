// Receive QUANTEX webhooks and verify X-Quantex-Signature.
// npm install express · env QUANTEX_WEBHOOK_SECRET=whsec_…
const crypto = require('crypto');
const express = require('express');

const SECRET = process.env.QUANTEX_WEBHOOK_SECRET;
const app = express();

function verified(raw, header) {
  const parts = Object.fromEntries((header || '').split(',').map((p) => p.split('=')));
  const t = parts.t, v1 = parts.v1 || '';
  if (!/^\d+$/.test(t || '') || Math.abs(Date.now() / 1000 - Number(t)) > 300) return false;
  const expected = crypto.createHmac('sha256', SECRET).update(`${t}.`).update(raw).digest('hex');
  return v1.length === expected.length && crypto.timingSafeEqual(Buffer.from(expected), Buffer.from(v1));
}

// The signature is over the RAW body, so read it unparsed.
app.post('/quantex/webhook', express.raw({ type: 'application/json' }), (req, res) => {
  if (!verified(req.body, req.get('X-Quantex-Signature'))) return res.sendStatus(401);
  const event = JSON.parse(req.body.toString('utf8'));
  const s = event.data || {};
  if (event.type === 'signal.created') console.log('NEW', s.pair, s.timeframe, s.direction, s.entry_at);
  if (event.type === 'signal.result') console.log('RESULT', s.pair, s.result, 'mtg', s.mtg_level);
  res.sendStatus(200); // answer within 5 seconds
});

app.listen(8080, () => console.log('listening on :8080'));
