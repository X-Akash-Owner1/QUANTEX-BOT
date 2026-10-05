<?php
// QUANTEX webhook receiver for any PHP host. Set QUANTEX_WEBHOOK_SECRET (whsec_…) in the environment.

$secret = getenv('QUANTEX_WEBHOOK_SECRET');
$raw = file_get_contents('php://input');
$t = $v1 = null;
foreach (explode(',', $_SERVER['HTTP_X_QUANTEX_SIGNATURE'] ?? '') as $part) {
    [$k, $v] = array_pad(explode('=', $part, 2), 2, '');
    if ($k === 't') { $t = $v; } elseif ($k === 'v1') { $v1 = $v; }
}
$ok = $t !== null && ctype_digit($t) && abs(time() - (int) $t) < 300
    && hash_equals(hash_hmac('sha256', $t.'.'.$raw, $secret), (string) $v1);
if (! $ok) {
    http_response_code(401);
    exit;
}

$event = json_decode($raw, true);
$s = $event['data'] ?? [];
if ($event['type'] === 'signal.created') {
    error_log("NEW {$s['pair']} {$s['timeframe']} {$s['direction']} {$s['entry_at']}");
} elseif ($event['type'] === 'signal.result') {
    error_log("RESULT {$s['pair']} {$s['result']} mtg {$s['mtg_level']}");
}
http_response_code(200); // answer within 5 seconds
