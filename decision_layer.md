# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T14:29:06.130788+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LINK-EUR | action ACHETE_MAINTENANT | opportunité 9.422 | entrée 8.400 | trend 8.750 | rang 8.581
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : LDO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.037 | entrée 6.100 | trend 8.650 | rang 7.704
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : 0G-EUR | action LATENT_ACCELERATOR | opportunité 8.068 | entrée 5.000 | trend 8.950 | rang 7.773
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : WAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.382 | entrée 6.350 | trend 8.950 | rang 8.066
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LINK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.581
2. EIGEN-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.515
3. FORM-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.238

## Accélération indépendante

- ESP-EUR — CONFIRMED_ACCELERATION — score 8.598/10 — DETECTED_BUT_TOO_LATE
- EDGE-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- AMP-EUR — CONFIRMED_ACCELERATION — score 6.999/10 — DETECTED_BUT_TOO_LATE
- ETHFI-EUR — BUILDING_ACCELERATION — score 6.038/10 — DETECTED_BUT_TOO_LATE
- HUMA-EUR — BUILDING_ACCELERATION — score 5.653/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AVNT-EUR — BUILDING_ACCELERATION — score 5.573/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — BUILDING_ACCELERATION — score 4.930/10 — DETECTED_BUT_TOO_LATE
- ACE-EUR — BUILDING_ACCELERATION — score 4.795/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- XMN-EUR — MEMORY_24H — score mémoire 9.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RAD-EUR — MEMORY_24H — score mémoire 9.291/10 — sources ACCELERATION — MEMORY_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ESP-EUR — ACTIVE_NOW — score mémoire 8.598/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LINK-EUR — ACTIVE_NOW — score mémoire 8.581/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ACT-EUR — MEMORY_24H — score mémoire 8.555/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- EIGEN-EUR — ACTIVE_NOW — score mémoire 8.515/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — MEMORY_24H — score mémoire 8.515/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- POND-EUR +135.29% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +74.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +48.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +36.01% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- 2Z-EUR +31.23% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARK-EUR +22.11% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- KMNO-EUR +19.39% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PROM-EUR +16.71% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- AERO-EUR +14.75% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KAS-EUR +14.27% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
