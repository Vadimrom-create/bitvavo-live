# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T23:48:05.793090+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : RENDER-EUR | action ACHETE_MAINTENANT | opportunité 9.024 | entrée 7.950 | trend 8.650 | rang 8.391
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ALT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.014 | entrée 5.950 | trend 8.750 | rang 7.713
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : 0G-EUR | action LATENT_ACCELERATOR | opportunité 7.979 | entrée 5.650 | trend 8.650 | rang 7.630
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ZK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.322 | entrée 6.500 | trend 8.950 | rang 8.424
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ZK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.424
2. RENDER-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.391
3. ALGO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.264

## Accélération indépendante

- POND-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- SSV-EUR — CONFIRMED_ACCELERATION — score 9.806/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — CONFIRMED_ACCELERATION — score 8.975/10 — DETECTED_BUT_TOO_LATE
- CELO-EUR — CONFIRMED_ACCELERATION — score 7.033/10 — DETECTED_BUT_TOO_LATE
- LPT-EUR — BUILDING_ACCELERATION — score 6.211/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RARE-EUR — BUILDING_ACCELERATION — score 5.824/10 — DETECTED_BUT_TOO_LATE
- ZEUS-EUR — BUILDING_ACCELERATION — score 5.766/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MLN-EUR — BUILDING_ACCELERATION — score 5.215/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- XPL-EUR — ACTIVE_NOW — score mémoire 8.071/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- POND-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SSV-EUR — ACTIVE_NOW — score mémoire 9.806/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — ACTIVE_NOW — score mémoire 8.975/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 8.667/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARK-EUR — MEMORY_24H — score mémoire 8.526/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZK-EUR — ACTIVE_NOW — score mémoire 8.424/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.391/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PHA-EUR +62.94% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- POND-EUR +47.67% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARK-EUR +31.18% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +23.81% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AERO-EUR +21.37% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SEI-EUR +19.49% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ENA-EUR +19.31% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUI-EUR +18.77% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WMTX-EUR +18.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +18.18% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
