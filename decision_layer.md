# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T04:00:35.503609+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : BEAM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.775 | entrée 6.000 | trend 8.650 | rang 7.651
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : DEEP-EUR | action LATENT_ACCELERATOR | opportunité 8.004 | entrée 5.350 | trend 8.600 | rang 7.130
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : CAKE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.381 | entrée 6.650 | trend 8.950 | rang 8.025
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. CAKE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.025
2. LTC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.812
3. JUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.691

## Accélération indépendante

- U-EUR — CONFIRMED_ACCELERATION — score 8.051/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WMTX-EUR — CONFIRMED_ACCELERATION — score 6.761/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARK-EUR — CONFIRMED_ACCELERATION — score 6.515/10 — DETECTED_BUT_TOO_LATE
- SWELL-EUR — BUILDING_ACCELERATION — score 6.156/10 — DETECTED_BUT_TOO_LATE
- EDGE-EUR — BUILDING_ACCELERATION — score 5.902/10 — DETECTED_BUT_TOO_LATE
- SAGA-EUR — BUILDING_ACCELERATION — score 5.819/10 — DETECTED_BUT_TOO_LATE
- TAI-EUR — BUILDING_ACCELERATION — score 5.793/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- QNT-EUR — BUILDING_ACCELERATION — score 5.174/10 — DETECTED_BUT_TOO_LATE
- WAL-EUR — BUILDING_ACCELERATION — score 5.125/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CROSS-EUR — BUILDING_ACCELERATION — score 4.842/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- QKC-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- UP-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — ACTIVE_NOW — score mémoire 8.051/10 — sources ACCELERATION, V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 8.025/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HBAR-EUR — MEMORY_24H — score mémoire 7.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BOB-EUR — MEMORY_24H — score mémoire 7.875/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- OGN-EUR — MEMORY_24H — score mémoire 7.854/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- QNT-EUR +32.19% — DETECTED_EARLY — couche NONE — action NONE
- XPL-EUR +28.94% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- TREAD-EUR +28.77% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ONDO-EUR +25.49% — DETECTED_EARLY — couche NONE — action NONE
- EDGE-EUR +23.32% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PEAQ-EUR +23.04% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARK-EUR +19.58% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XAI-EUR +14.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FET-EUR +13.99% — DETECTED_EARLY — couche NONE — action NONE
- TAI-EUR +13.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
