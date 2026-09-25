# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T07:14:29.876068+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAIKO-EUR | action ACHETE_MAINTENANT | opportunité 9.162 | entrée 7.150 | trend 7.950 | rang 8.064
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : GRT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.532 | entrée 6.000 | trend 8.300 | rang 7.413
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : PYTH-EUR | action LATENT_ACCELERATOR | opportunité 7.607 | entrée 4.500 | trend 8.650 | rang 7.367
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : INJ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.166 | entrée 6.550 | trend 7.900 | rang 8.086
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.086
2. JUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.075
3. TAIKO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.064

## Accélération indépendante

- MOVR-EUR — CONFIRMED_ACCELERATION — score 7.865/10 — DETECTED_BUT_TOO_LATE
- QNT-EUR — CONFIRMED_ACCELERATION — score 7.635/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — BUILDING_ACCELERATION — score 4.916/10 — DETECTED_BUT_TOO_LATE
- EDGE-EUR — BUILDING_ACCELERATION — score 4.856/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- UP-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- SAGA-EUR — MEMORY_24H — score mémoire 8.681/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- WMTX-EUR — MEMORY_24H — score mémoire 8.143/10 — sources ACCELERATION — MEMORY_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 8.086/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 8.075/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TAIKO-EUR — ACTIVE_NOW — score mémoire 8.064/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 8.044/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +43.13% — DETECTED_EARLY — couche NONE — action NONE
- TREAD-EUR +40.69% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- XPL-EUR +31.10% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ONDO-EUR +27.31% — DETECTED_EARLY — couche NONE — action NONE
- PHA-EUR +22.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +18.47% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARK-EUR +18.47% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEAQ-EUR +17.97% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DBR-EUR +16.54% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AXS-EUR +15.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
