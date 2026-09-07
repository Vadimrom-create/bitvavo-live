# Test plan before live trading

1. **API auth test** — DRY_RUN=true, AUTO_CANCEL_UNKNOWN_ORDERS=false. Confirm private balance endpoint works; do not publish balances.
2. **Inventory test** — list existing open orders and observe their operator/client IDs; do not cancel anything.
3. **WebSocket test** — confirm account channel subscription and receive order/fill events from a deliberately created harmless/manual test if needed.
4. **Approval dry-run** — ChatGPT writes one short-lived approved command after the user says yes; executor must classify entry as passive/immediately executable and reject it if market drift/spread guardrails fail.
5. **Security simulation** — inject a fake unknown event locally; verify SECURITY_FREEZE and email alert pipeline without touching Bitvavo.
6. **Small live entry** — explicit user approval, deliberately small stake; confirm exact clientOrderId/operatorId attribution and execution status.
7. **Protective exit test** — after verifying Bitvavo behavior for conditional orders and reserved funds, enable hard stop management.
8. **Production** — only then set DRY_RUN=false and AUTO_CANCEL_UNKNOWN_ORDERS=true, with MAX_ORDER_EUR initially capped well below the final 600 EUR ceiling.

No phase is skipped because the user intends to use 300-600 EUR positions later.
