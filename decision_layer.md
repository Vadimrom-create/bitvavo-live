# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T20:40:16.765908+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAIKO-EUR | action ACHETE_MAINTENANT | opportunité 8.823 | entrée 6.800 | trend 8.200 | rang 7.968
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : PYTH-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.272 | entrée 5.800 | trend 8.900 | rang 7.873
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : NEO-EUR | action LATENT_ACCELERATOR | opportunité 7.668 | entrée 5.750 | trend 8.750 | rang 7.545
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : BEAM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.336 | entrée 6.200 | trend 8.950 | rang 8.499
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. BEAM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.499
2. SEI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.406
3. KMNO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.059

## Accélération indépendante

- MIRA-EUR — CONFIRMED_ACCELERATION — score 8.635/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LSK-EUR — CONFIRMED_ACCELERATION — score 7.787/10 — DETECTED_BUT_TOO_LATE
- WMTX-EUR — BUILDING_ACCELERATION — score 6.277/10 — DETECTED_BUT_TOO_LATE
- CSPR-EUR — BUILDING_ACCELERATION — score 5.995/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SNX-EUR — BUILDING_ACCELERATION — score 5.373/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KMNO-EUR — BUILDING_ACCELERATION — score 5.044/10 — DETECTED_BUT_TOO_LATE
- EDGE-EUR — BUILDING_ACCELERATION — score 4.851/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- MIRA-EUR — ACTIVE_NOW — score mémoire 8.635/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BEAM-EUR — ACTIVE_NOW — score mémoire 8.499/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SEI-EUR — ACTIVE_NOW — score mémoire 8.406/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- KMNO-EUR — ACTIVE_NOW — score mémoire 8.059/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- TAIKO-EUR — ACTIVE_NOW — score mémoire 7.968/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 7.873/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +45.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XAI-EUR +40.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ONDO-EUR +23.28% — DETECTED_EARLY — couche NONE — action NONE
- TREAD-EUR +22.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QNT-EUR +22.30% — DETECTED_EARLY — couche NONE — action NONE
- XPL-EUR +21.10% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARK-EUR +20.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PLUME-EUR +19.26% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEAQ-EUR +18.34% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +17.31% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
