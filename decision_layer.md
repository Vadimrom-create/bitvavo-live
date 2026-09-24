# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T17:10:41.088330+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : XLM-EUR | action ACHETE_MAINTENANT | opportunité 8.920 | entrée 7.200 | trend 7.600 | rang 7.708
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : EIGEN-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.867 | entrée 6.400 | trend 8.650 | rang 7.596
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : 0G-EUR | action LATENT_ACCELERATOR | opportunité 7.842 | entrée 4.500 | trend 8.650 | rang 7.428
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : KMNO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.017 | entrée 6.850 | trend 8.550 | rang 8.125
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. KMNO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.125
2. AERO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.950
3. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.936

## Accélération indépendante

- TREAD-EUR — CONFIRMED_ACCELERATION — score 8.594/10 — DETECTED_BUT_TOO_LATE
- XAI-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- WMTX-EUR — CONFIRMED_ACCELERATION — score 7.500/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IKA-EUR — CONFIRMED_ACCELERATION — score 7.364/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAI-EUR — BUILDING_ACCELERATION — score 6.030/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LUMIA-EUR — BUILDING_ACCELERATION — score 5.933/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — BUILDING_ACCELERATION — score 5.880/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRAC-EUR — BUILDING_ACCELERATION — score 5.749/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WCT-EUR — BUILDING_ACCELERATION — score 5.675/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PEAQ-EUR — BUILDING_ACCELERATION — score 5.619/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- AMP-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- TREAD-EUR — ACTIVE_NOW — score mémoire 8.594/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- 2Z-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CNPY-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- POND-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XAI-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- MLN-EUR — MEMORY_24H — score mémoire 8.477/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- EDGE-EUR — MEMORY_24H — score mémoire 8.463/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- NOM-EUR +42.01% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- LSK-EUR +35.50% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ONDO-EUR +25.51% — DETECTED_EARLY — couche NONE — action NONE
- LTC-EUR +23.63% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +23.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QNT-EUR +20.24% — DETECTED_EARLY — couche NONE — action NONE
- PEAQ-EUR +19.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARX-EUR +19.84% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PLUME-EUR +18.26% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XAI-EUR +17.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
