# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T18:23:52.971519+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : EIGEN-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.506 | entrée 6.150 | trend 8.450 | rang 7.473
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : COMP-EUR | action LATENT_ACCELERATOR | opportunité 7.826 | entrée 5.550 | trend 9.000 | rang 7.450
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : GMT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.082 | entrée 6.950 | trend 9.000 | rang 7.902
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. GMT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.902
2. ICP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.853
3. PYTH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.645

## Accélération indépendante

- ICX-EUR — CONFIRMED_ACCELERATION — score 8.429/10 — DETECTED_BUT_TOO_LATE
- U-EUR — CONFIRMED_ACCELERATION — score 7.974/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TREAD-EUR — BUILDING_ACCELERATION — score 6.418/10 — DETECTED_BUT_TOO_LATE
- RAY-EUR — BUILDING_ACCELERATION — score 6.397/10 — DETECTED_BUT_TOO_LATE
- LINK-EUR — BUILDING_ACCELERATION — score 5.715/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VVV-EUR — BUILDING_ACCELERATION — score 5.548/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IMU-EUR — BUILDING_ACCELERATION — score 5.498/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ONT-EUR — BUILDING_ACCELERATION — score 5.481/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAI-EUR — BUILDING_ACCELERATION — score 5.405/10 — DETECTED_BUT_TOO_LATE
- DGB-EUR — BUILDING_ACCELERATION — score 5.227/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- UP-EUR — MEMORY_24H — score mémoire 8.796/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- 2Z-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CNPY-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- EDGE-EUR — MEMORY_24H — score mémoire 8.463/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XAI-EUR — MEMORY_24H — score mémoire 8.446/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — ACTIVE_NOW — score mémoire 8.429/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — ACTIVE_NOW — score mémoire 7.974/10 — sources ACCELERATION, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- XAI-EUR +51.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +33.48% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- NOM-EUR +28.29% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ONDO-EUR +23.14% — DETECTED_EARLY — couche NONE — action NONE
- PEAQ-EUR +20.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +19.67% — DETECTED_EARLY — couche NONE — action NONE
- LTC-EUR +19.23% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +18.32% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PLUME-EUR +17.86% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARX-EUR +16.84% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
