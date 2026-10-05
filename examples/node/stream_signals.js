// Read the QUANTEX signal stream (Server-Sent Events) and reconnect without missing events.
// Node 18+ (built-in fetch) · env QUANTEX_API_KEY (Pro or Business plan, permission signals:read)
const URL = 'https://api.quantexbot.pro/v1/stream/signals?broker=quotex';
let lastId = null;

async function connect() {
  const headers = { Authorization: `Bearer ${process.env.QUANTEX_API_KEY}`, Accept: 'text/event-stream' };
  if (lastId) headers['Last-Event-ID'] = lastId;          // continue after the last event we saw
  const res = await fetch(URL, { headers });
  if (!res.ok) throw new Error(`HTTP ${res.status}: ${await res.text()}`);

  const decoder = new TextDecoder();
  let buffer = '';
  for await (const chunk of res.body) {
    buffer += decoder.decode(chunk, { stream: true });
    let end;
    while ((end = buffer.indexOf('\n\n')) !== -1) {
      const block = buffer.slice(0, end);
      buffer = buffer.slice(end + 2);
      const msg = { event: 'message', data: '' };
      for (const line of block.split('\n')) {
        if (line.startsWith(':')) continue;                // keep-alive comment
        const [field, ...rest] = line.split(':');
        const value = rest.join(':').replace(/^ /, '');
        if (field === 'id') lastId = value;
        if (field === 'event') msg.event = value;
        if (field === 'data') msg.data += value;
      }
      if (msg.event === 'signal.created' || msg.event === 'signal.result') {
        const { signal } = JSON.parse(msg.data);
        console.log(msg.event, signal.pair, signal.direction, signal.entry_at, signal.result || '');
      }
    }
  }
}

(async function run() {
  for (;;) {
    try { await connect(); } catch (e) { console.error(e.message); }
    await new Promise((r) => setTimeout(r, 3000));         // the server closes every 5 min: reconnect
  }
})();
