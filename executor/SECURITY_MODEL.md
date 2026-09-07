# Security boundaries

## What a stolen Bitvavo key can and cannot do

The production key must have View + Trade only, with Withdraw disabled. A stolen key can still trade and therefore cause losses, but cannot use Bitvavo withdrawal endpoints when the key lacks the withdrawal permission. The IP whitelist adds a second barrier: Bitvavo accepts the key only from the VM's fixed IP.

## Sentinel attribution

Every executor order uses:

- fixed `operatorId = 26090701` (configurable); and
- a fresh UUID `clientOrderId` generated locally on the private VM.

Bitvavo account WebSocket `order` and `fill` events return both fields. The sentinel compares both with its local authorization registry. A matching operator ID alone is not enough.

## Unknown activity response

1. Set `SECURITY_FREEZE` immediately.
2. Stop new strategy orders.
3. Publish a sanitized security event to GitHub so the existing Gmail alert infrastructure can notify the user.
4. Once installation observation is complete, unknown still-open orders can be canceled automatically.
5. Already executed fills cannot be canceled. Automatic reversal is deliberately disabled in the first production phase because an incorrect reversal can compound losses.

## GitHub compromise containment

The public approval relay is not trusted blindly. The executor rejects stale, oversized, non-EUR, non-limit or badly priced approvals and re-checks live Bitvavo bid/ask and spread before execution. The private Bitvavo secret is never stored in GitHub.

The optional GitHub token on the VM is fine-grained and limited to Contents read/write on one repository. Compromising that token gives no direct access to Bitvavo.
