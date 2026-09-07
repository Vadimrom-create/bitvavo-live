# Setup checklist — user actions only

The executor code, approval relay, dry-run guardrails, account sentinel, sanitized status channel and security-event email bridge are prepared by ChatGPT.

The remaining user-only steps are intentionally limited to account/security actions ChatGPT cannot perform:

1. Create a small always-on Linux VM with a fixed public IPv4 address.
2. Create a Bitvavo API key restricted to that exact IP with only **View access + Trade digital assets**. Do **not** enable Withdraw, Internal Transfer, Administrative or Include all subaccounts.
3. Create a GitHub fine-grained personal access token limited to repository `Vadimrom-create/bitvavo-live` with **Contents: Read and write** only. This token lets the private VM publish sanitized status/security-event files; it gives no Bitvavo access.
4. Paste those three secrets (Bitvavo key, Bitvavo secret, restricted GitHub token) into `/etc/bitvavo-executor.env` on the VM. Never paste them into ChatGPT.

After that ChatGPT can handle repository-side configuration and the executor remains in DRY_RUN until explicit end-to-end validation.
