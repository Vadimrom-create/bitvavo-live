# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T06:09:00.234869+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : GMT-EUR | action ACHETE_MAINTENANT | opportunité 8.729 | entrée 7.450 | trend 8.250 | rang 8.114
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : THE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.783 | entrée 6.050 | trend 8.200 | rang 7.766
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : CAKE-EUR | action LATENT_ACCELERATOR | opportunité 7.801 | entrée 5.400 | trend 8.950 | rang 7.697
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : TIA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.197 | entrée 6.750 | trend 8.150 | rang 8.215
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. TIA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.215
2. GMT-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.114
3. SEI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.097

## Accélération indépendante

- SAGA-EUR — CONFIRMED_ACCELERATION — score 8.681/10 — DETECTED_BUT_TOO_LATE
- WMTX-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- ZETA-EUR — CONFIRMED_ACCELERATION — score 6.819/10 — DETECTED_BUT_TOO_LATE
- U-EUR — BUILDING_ACCELERATION — score 6.093/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IMU-EUR — BUILDING_ACCELERATION — score 5.793/10 — DETECTED_BUT_TOO_LATE
- ZRO-EUR — BUILDING_ACCELERATION — score 5.485/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ICX-EUR — MEMORY_24H — score mémoire 9.235/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- UP-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.742/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SAGA-EUR — ACTIVE_NOW — score mémoire 8.681/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PHA-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WMTX-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- WAXP-EUR — MEMORY_24H — score mémoire 8.311/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- QNT-EUR +35.39% — DETECTED_EARLY — couche NONE — action NONE
- TREAD-EUR +32.48% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- XPL-EUR +28.78% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ONDO-EUR +23.95% — DETECTED_EARLY — couche NONE — action NONE
- PEAQ-EUR +22.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +20.44% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARK-EUR +19.94% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DBR-EUR +19.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FET-EUR +16.53% — DETECTED_EARLY — couche NONE — action NONE
- PHA-EUR +15.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
