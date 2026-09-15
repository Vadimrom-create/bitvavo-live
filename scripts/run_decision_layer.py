#!/usr/bin/env python3
"""Run Decision Layer V1 after the frozen scanner pipeline.

Reads the explicitly identified immutable scan journal, writes a public report
and an append-only per-scan decision journal. It never changes V3/V4 output,
alert_candidates.json, proposed_orders.json or any execution path.
"""
from __future__ import annotations

import sys
from pathlib import Path

# Direct execution from scripts/ puts that directory, not the repository root,
# on sys.path. Add the root explicitly so research.* imports are reliable in CI.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.common import read_json
from research.decision_layer import BUCKETS


def render(payload: dict) -> str:
    lines = [
        "# Decision Layer V1 — shadow",
        "",
        f"Scan : {payload['scan_at_utc']}",
        f"Policy : {payload['policy']} au-dessus de {payload['frozen_scanner_policy']}",
        "",
        "Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.",
        "Entry est un indicateur de timing, pas un veto structurel.",
        "",
        "## Quatre lectures obligatoires",
        "",
    ]
    for bucket in BUCKETS:
        row = payload["bucket_winners"].get(bucket)
        if not row:
            lines.append(f"- **{bucket}** : aucun candidat matériel")
            continue
        lines.append(
            f"- **{bucket}** : {row['market']} | action {row['action']} | "
            f"opportunité {row['opportunity_score']:.3f} | entrée {row['entry_score']:.3f} | "
            f"trend {row['trend_score']:.3f} | rang {row['rank_score']:.3f}"
        )
        lines.append(f"  - {row['reason']}")
    lines += ["", "## Top cross-sectionnel", ""]
    if not payload["top_actionable"]:
        lines.append("Aucun candidat ne remplit actuellement un bucket décisionnel.")
    else:
        for idx, row in enumerate(payload["top_actionable"], 1):
            lines.append(
                f"{idx}. {row['market']} — {row['bucket']} — {row['action']} — "
                f"rank {row['rank_score']:.3f}"
            )
    lines += [
        "",
        "## Garde-fous",
        "",
        "- Veto uniquement pour défauts structurels de données/exécution.",
        "- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.",
        "- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.",
        "- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    from scripts.run_shadow import run
    current = read_json("runtime/current_scan.json")
    if not current:
        raise RuntimeError("EXPLICIT_CURRENT_SCAN_REQUIRED")
    run(current["journal"], current["scan_id"], "v1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
