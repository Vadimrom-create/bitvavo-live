# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T20:57:57.958185+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : PYTH-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.994 | entrée 6.100 | trend 8.900 | rang 7.779
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : NEO-EUR | action LATENT_ACCELERATOR | opportunité 7.987 | entrée 5.550 | trend 8.750 | rang 7.658
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AERO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.795 | entrée 6.650 | trend 8.400 | rang 8.108
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. AERO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.108
2. ICP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.936
3. SEI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.915

## Accélération indépendante

- BTT-EUR — CONFIRMED_ACCELERATION — score 7.272/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CSPR-EUR — CONFIRMED_ACCELERATION — score 6.663/10 — DETECTED_BUT_TOO_LATE
- TAI-EUR — BUILDING_ACCELERATION — score 6.406/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SYRUP-EUR — BUILDING_ACCELERATION — score 5.985/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BICO-EUR — BUILDING_ACCELERATION — score 5.667/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARK-EUR — BUILDING_ACCELERATION — score 5.371/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — BUILDING_ACCELERATION — score 5.365/10 — DETECTED_BUT_TOO_LATE
- DEEP-EUR — BUILDING_ACCELERATION — score 5.099/10 — DETECTED_BUT_TOO_LATE
- XMN-EUR — BUILDING_ACCELERATION — score 4.937/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 8.108/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.936/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SEI-EUR — ACTIVE_NOW — score mémoire 7.915/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- OGN-EUR — MEMORY_24H — score mémoire 7.854/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- KMNO-EUR — ACTIVE_NOW — score mémoire 7.812/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LSK-EUR — MEMORY_24H — score mémoire 7.787/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 7.779/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +39.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XAI-EUR +37.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +25.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ONDO-EUR +24.37% — DETECTED_EARLY — couche NONE — action NONE
- QNT-EUR +23.38% — DETECTED_EARLY — couche NONE — action NONE
- XPL-EUR +21.21% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PEAQ-EUR +20.47% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARK-EUR +20.28% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PLUME-EUR +18.63% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +18.15% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
