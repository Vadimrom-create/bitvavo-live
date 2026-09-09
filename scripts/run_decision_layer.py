#!/usr/bin/env python3
"""Run Decision Layer V1 after the frozen scanner pipeline.

Reads the newest immutable scan journal, writes a latest public decision report
and an append-only per-scan decision journal. It never changes V3/V4 output,
alert_candidates.json, proposed_orders.json or any execution path.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

# Direct execution from scripts/ puts that directory, not the repository root,
# on sys.path. Add the root explicitly so research.* imports are reliable in CI.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.common import atomic_json, read_json, utc
from research.decision_layer import BUCKETS, decide


def newest_scan() -> Path:
    paths = sorted(Path("history").glob("*/*.json.gz"))
    if not paths:
        raise RuntimeError("NO_SCAN_JOURNAL_FOR_DECISION_LAYER")
    return paths[-1]


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
    scan_path = newest_scan()
    scan = read_json(scan_path)
    result = decide(scan["observations"])
    payload = {
        **result,
        "scan_id": scan["scan_id"],
        "scan_at_utc": scan["scan_at_utc"],
        "generated_at_utc": utc(),
        "source_journal": str(scan_path),
    }
    atomic_json("decision_layer.json", payload)
    Path("decision_layer.md").write_text(render(payload), encoding="utf-8")

    journal_path = Path("decision_history") / scan["scan_at_utc"][:10] / f"{scan['scan_id']}.json.gz"
    if journal_path.exists():
        previous = read_json(journal_path)
        old = {k: v for k, v in previous.items() if k != "generated_at_utc"}
        new = {k: v for k, v in payload.items() if k != "generated_at_utc"}
        if old != new:
            raise RuntimeError("DECISION_JOURNAL_IMMUTABILITY_VIOLATION")
    else:
        atomic_json(journal_path, payload)

    print(json.dumps({
        "decision_layer": payload["policy"],
        "scan_id": payload["scan_id"],
        "top": [r["market"] for r in payload["top_actionable"]],
        "production_orders_enabled": payload["principles"]["production_orders_enabled"],
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
