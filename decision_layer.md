# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T17:28:39.377090+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : BONK-EUR | action ACHETE_MAINTENANT | opportunité 9.186 | entrée 7.400 | trend 8.100 | rang 8.023
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : NEO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.650 | entrée 6.200 | trend 8.750 | rang 7.546
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : EIGEN-EUR | action LATENT_ACCELERATOR | opportunité 7.743 | entrée 4.500 | trend 8.650 | rang 7.369
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ICP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.306 | entrée 6.800 | trend 9.200 | rang 8.093
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ICP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.093
2. BONK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.023
3. TAIKO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.923

## Accélération indépendante

- TREAD-EUR — CONFIRMED_ACCELERATION — score 8.892/10 — DETECTED_BUT_TOO_LATE
- UP-EUR — CONFIRMED_ACCELERATION — score 8.796/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MOCA-EUR — CONFIRMED_ACCELERATION — score 8.534/10 — DETECTED_BUT_TOO_LATE
- MOG-EUR — CONFIRMED_ACCELERATION — score 7.137/10 — DETECTED_BUT_TOO_LATE
- IMU-EUR — CONFIRMED_ACCELERATION — score 6.697/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PROM-EUR — BUILDING_ACCELERATION — score 6.321/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XAI-EUR — BUILDING_ACCELERATION — score 5.235/10 — DETECTED_BUT_TOO_LATE
- XPL-EUR — BUILDING_ACCELERATION — score 5.229/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PENDLE-EUR — BUILDING_ACCELERATION — score 5.079/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BTT-EUR — BUILDING_ACCELERATION — score 4.953/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- TREAD-EUR — ACTIVE_NOW — score mémoire 8.892/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- UP-EUR — ACTIVE_NOW — score mémoire 8.796/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MOCA-EUR — ACTIVE_NOW — score mémoire 8.534/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- 2Z-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CNPY-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MLN-EUR — MEMORY_24H — score mémoire 8.477/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- EDGE-EUR — MEMORY_24H — score mémoire 8.463/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- NOM-EUR +40.00% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- LSK-EUR +34.21% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ONDO-EUR +26.31% — DETECTED_EARLY — couche NONE — action NONE
- LTC-EUR +22.18% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +22.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +20.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEAQ-EUR +20.41% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +20.31% — DETECTED_EARLY — couche NONE — action NONE
- ARX-EUR +19.66% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PLUME-EUR +18.29% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
