# ChatGPT -> executor approval contract

ChatGPT must never write an approval merely because a scanner says BUY_READY. An approval is written only after a specific recommendation has been shown to the user and the user explicitly authorizes that exact trade.

Example relay payload:

```json
{
  "version": 1,
  "approval": {
    "id": "uuid",
    "status": "APPROVED_BY_USER",
    "created_at_utc": "2026-09-07T10:00:00+00:00",
    "expires_at_utc": "2026-09-07T10:10:00+00:00",
    "market": "EXAMPLE-EUR",
    "side": "buy",
    "order_type": "limit",
    "stake_eur": 400,
    "reference_price": "0.1234",
    "limit_price": "0.1228",
    "stop_loss": {
      "trigger_price": "0.1160",
      "reason": "structural invalidation"
    },
    "take_profit": {
      "tp1_price": "0.1350",
      "tp1_fraction": 0.6,
      "runner_target_price": "0.1450"
    }
  }
}
```

Before submission the VM independently checks current best bid/ask, spread, price drift, market metadata, amount rounding, expiry, maximum order size and security-freeze state.

Phase 1 is limit-buy only. Live sell/protection management is enabled only after dry-run and small-value testing.
