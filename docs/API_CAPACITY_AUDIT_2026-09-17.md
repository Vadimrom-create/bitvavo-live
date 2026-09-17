# Public API capacity measurement

Start checkpoint: `3544673e22418d6e9835722275f0a74ff8606d02`.

The opt-in `scripts/audit_api_capacity.py` runs the same corrected-inputs
pipeline. It must run in an expendable checkout: the ordinary pipeline writes
scan outputs there. It invokes no publisher, pilot lifecycle, email or private
endpoint. Production workflows and the monitoring pin are unchanged.

Only the read-only CI public smoke job uses the observer. Its sidecar
`runtime/capacity-audit.json.gz` records public GET attempt timestamps, endpoint
parameters, response status and rate-limit headers, duration, configured
timeout, thread identity, pacing waits, logical-call IDs and cache-only reads.
Request bodies and authentication headers are never logged; returned public
market payloads remain in the existing replay artifact.

The observer calls the unchanged PublicClient implementation and preserves its
cache, pace, retry and deadline behavior. No trading policy imports it. One new
attempt is charged its documented weight even if it fails (conservative when
the server never received it). Rolling windows are (t-60,t], based on client
request starts; they are not the exchange's reset windows. Analyze reset headers
separately. Pacing sums are thread-seconds, not wall-clock delay. Appends' measured
cost excludes Python wrapper overhead and is not a full overhead benchmark.

Official weights checked 2026-09-17: candles 1; ticker/24h without market 25,
with market 1; ticker/price and ticker/book 1; per-market book 1; trades 5;
markets and time 1. Sources: https://docs.bitvavo.com/docs/rate-limits/ and
https://docs.bitvavo.com/docs/rest-api/get-candlestick-data/ plus endpoint pages.

The audit distinguishes market visibility, native OHLCV continuity and
strategy-grade trading_data_valid. No missing candle is synthesized and no
quality rule is relaxed. Actual scenario results belong to the identified
measurement artifact; successful instrumentation tests alone demonstrate no
capacity margin. Real private monitoring remains PENDING PRIVATE CONFIGURATION.

Validation: seven observer tests cover weighted rolling boundaries, cache
identity, successful and failing header capture, retries, timeouts, deadline
rejection before network, restoration of patched functions and rejection of
private authentication. The existing full test suites and real V4 replay remain
CI gates. No isolation/publication correction is part of this commit.
