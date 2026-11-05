# Solaire — Frozen 24h exit and risk audit, 11 October 2026

Research-only. Draft PR #163, issue #134. No production, order, private wallet or trading-rule changes.

## Provenance

Same 75 machine BUY_SENT alerts, 44 EUR markets, selected by timestamp before outcomes. Alert time window: 2026-10-08 19:17:40 UTC through 2026-10-10 19:07:40 UTC; complete 24h horizon checked at 2026-10-11 19:17:40 UTC.

Public data sources are archival CI artifacts, expiring after 7/14 days:
- Original market capture run: https://github.com/Vadimrom-create/bitvavo-live/actions/runs/38167319461 (artifact 11712443325)
- Original machine-book pairing: https://github.com/Vadimrom-create/bitvavo-live/actions/runs/38166530515 (artifact 11712357334)
- Frozen comparison and marked-equity risk: https://github.com/Vadimrom-create/bitvavo-live/actions/runs/38168762021 (artifact 11713430176)
- Candle market source SHA-256: 6df783e699ae28ae63d791223000c4c5f11e1a660025521093154fba98b557d6
- 42 offline tests, plus repository general tests, economic tests and archive checks, all PASS at 6d5b85e3487f6a0eee651dd0d75d624a3fe2101a.
- The frozen script scripts/audit_frozen_exit_execution.py verifies source hashes, original alert window and comparable cohort; it does not fetch any newer prices.

## Modeled 2300 EUR portfolio, 100 EUR orders, 10 max simultaneous

| Execution valuation method | Trades modeled | Final net modeled PnL | Portfolio rejections | Indicative max drawdown at last traded close |
|---|---:|---:|---:|---:|
| Strict closed 5m candles | Not determined | NULL | NULL | NULL |
| Flat zero-trade path, sale at previous print by 24h | 29 | -7.49218582 EUR | 24 | 53.561458 EUR |
| Flat zero-trade path, exit first actual print after 24h | 28 | -2.71025322 EUR | 25 | 53.561458 EUR |

ALL are research proxies, NOT Bitvavo fills or executable exit profits. Real wallet PnL and real liquidation drawdown remain NULL. Simulated fee 0.25% plus adverse slippage 0.10%, each side. Exits at printed prices do not prove liquidity for a 100 EUR sell. Strict method has 48 censored and cannot measure net profit.

Next-real-print exits release modeled cash 5-70 minutes after horizon. Difference of +4.78193260 EUR relative to legacy valuation is mostly because an RLC-EUR model trade losing -5.59521994 EUR is excluded by capital occupancy; the same 28 trades actually deteriorate by -0.81328733 EUR on rerating their exits. This is an allocation/timing effect, not evidence of a better strategy.

Legacy 29-trade cohort: 9 winners, 20 losers, 15 horizon exits, 9 modeled stops, 5 target exits. Total modeled fees 14.48131322 EUR. Next-print cohort: 10 winners, 18 losers, 15 delayed horizon exits, 8 modeled stops, 5 targets. Fees 13.99329489 EUR.

With 10 x 100 EUR positions, only 1000 EUR maximum could be deployed out of 2300 EUR. Time-weighted average modeled allocation across the alert window plus 24-hour horizon was about 641 EUR (27.9%). The last-trade-price mark-to-market drawdown of 53.561458 EUR is indicative and could materially understate the cost of immediate liquidation. No real executable drawdown has been computed.

## GO/STOP decision and blockers

NO GO for a live strategy. The data are one recent retrospective period, and the selected alerts are production BUY_SENT, not matching frozen V4 or R2 policy cohorts.

Priority is proof of executable exit depth, spreads, stop gap, latency and genuine fills; a private exchange ledger must never be uploaded to public GitHub. Next compare V4, R2 and a simple benchmark on exactly the same opportunity timestamps, portfolio constraints and independently prospective period. ChatGPT data export will help attribute prior human decisions but is not required for these technical tests.

No trading thresholds, exits, orders, live workflow, VPS, alert rules, production files or secrets changed.
