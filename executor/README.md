# Bitvavo private executor / sentinel

This component is intentionally separated from the public scanner data path.

## Security model

- Bitvavo API key permissions: **View access + Trade digital assets only**.
- **Never enable Withdraw digital assets**, Internal Transfer, Administrative or subaccount-wide permissions.
- Bitvavo IP whitelist must contain only the fixed public IP of the private VM.
- API key and secret live only in `/etc/bitvavo-executor.env` on that VM (mode 0600).
- The service starts in `DRY_RUN=true` and `AUTO_CANCEL_UNKNOWN_ORDERS=false`.
- Every real order created by the executor uses one fixed `operatorId` plus a fresh private `clientOrderId` UUID.
- The account WebSocket listens to all `order` and `fill` events. Any event that does not match both the executor operator ID and its private registry is treated as an anomaly.
- On anomaly: `SECURITY_FREEZE` is set immediately. Once installation tests are complete, `AUTO_CANCEL_UNKNOWN_ORDERS=true` can also cancel an unknown open order immediately.
- A fill already executed cannot be canceled. The first production version freezes and alerts rather than automatically reversing an unknown fill.

## Approval model

`trade_approval.json` in the public scanner repo is only a relay for an explicit user approval in ChatGPT. It contains no API credentials. The executor independently checks that:

- the approval is fresh and unexpired;
- the market is a EUR market known by Bitvavo;
- order size is within `MAX_ORDER_EUR`;
- spread is within the configured limit;
- live mid-price has not drifted too far from the price shown when approval was requested;
- the requested entry is a limit order;
- no security freeze is active.

A fresh `clientOrderId` is generated locally on the VM immediately before submission and is never taken from the public approval file.

## Installation state

Phase 1 intentionally installs in observation/dry-run mode. Live trading is enabled only after:

1. the VM has a fixed IP;
2. the Bitvavo key is restricted by that IP and has no withdrawal permission;
3. private API authentication succeeds;
4. existing/manual orders have been inventoried so the sentinel does not accidentally cancel legitimate orders;
5. a dry-run ChatGPT approval is received and validated end-to-end;
6. a deliberately harmless/small live test is explicitly approved.

## Files that must never be committed

- API key
- API secret
- GitHub fine-grained token used by the VM to publish sanitized status/security events
- wallet balances / full private trade history
- `/var/lib/bitvavo-executor/state.json`

## Runtime

Systemd service: `bitvavo-executor.service`

Local private state: `/var/lib/bitvavo-executor/`

Sanitized public status, when a restricted GitHub status token is configured: `executor_status.json` and `security_event.json`.
