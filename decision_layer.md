# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T21:47:59.934712+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ICP-EUR | action ACHETE_MAINTENANT | opportunité 8.814 | entrée 6.850 | trend 9.000 | rang 8.276
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : NEO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.906 | entrée 6.000 | trend 8.750 | rang 7.691
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : EIGEN-EUR | action LATENT_ACCELERATOR | opportunité 7.695 | entrée 5.750 | trend 8.450 | rang 7.512
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PYTH-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.264 | entrée 6.750 | trend 8.900 | rang 7.984
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ICP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.276
2. ADA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.172
3. PYTH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.984

## Accélération indépendante

- CHIP-EUR — CONFIRMED_ACCELERATION — score 9.136/10 — DETECTED_BUT_TOO_LATE
- SAGA-EUR — BUILDING_ACCELERATION — score 6.000/10 — DETECTED_BUT_TOO_LATE
- XPL-EUR — BUILDING_ACCELERATION — score 5.491/10 — DETECTED_BUT_TOO_LATE
- PEAQ-EUR — BUILDING_ACCELERATION — score 5.027/10 — DETECTED_BUT_TOO_LATE
- LMWR-EUR — BUILDING_ACCELERATION — score 4.997/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CHIP-EUR — ACTIVE_NOW — score mémoire 9.136/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.276/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- DYM-EUR — MEMORY_24H — score mémoire 8.195/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ADA-EUR — ACTIVE_NOW — score mémoire 8.172/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 7.984/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- BEAM-EUR — ACTIVE_NOW — score mémoire 7.983/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- OGN-EUR — MEMORY_24H — score mémoire 7.854/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- XAI-EUR +33.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEAQ-EUR +27.46% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ONDO-EUR +26.90% — DETECTED_EARLY — couche NONE — action NONE
- LSK-EUR +26.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XPL-EUR +25.43% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- QNT-EUR +25.34% — DETECTED_EARLY — couche NONE — action NONE
- TREAD-EUR +23.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +22.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +21.72% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHIP-EUR +18.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
