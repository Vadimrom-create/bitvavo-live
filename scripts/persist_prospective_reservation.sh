#!/usr/bin/env bash
# Executed under the single prospective workflow lock, before any market capture.
set -euo pipefail
git config user.name 'bitvavo-live-bot'
git config user.email 'actions@users.noreply.github.com'
git add prospective_collection_state.json prospective_collection_health.json prospective_wakeup_receipts
if git diff --cached --quiet; then exit 0; fi
git commit -m "Reserve prospective window / record wakeup ${GITHUB_RUN_ID}_${GITHUB_RUN_ATTEMPT}"
for attempt in 1 2 3 4 5 6; do
  git fetch origin main
  if ! git rebase origin/main; then
    git rebase --abort || true
    echo 'Reservation conflict: refusing an unreserved collection.' >&2
    exit 1
  fi
  if git push origin HEAD:main; then exit 0; fi
  sleep $((attempt * 2))
done
exit 1
