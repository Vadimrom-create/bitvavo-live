# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T00:42:34.919755+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ALGO-EUR | action ACHETE_MAINTENANT | opportunité 9.318 | entrée 7.100 | trend 8.500 | rang 8.312
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : CAKE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.803 | entrée 6.150 | trend 8.950 | rang 7.778
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BEAM-EUR | action LATENT_ACCELERATOR | opportunité 7.832 | entrée 5.300 | trend 8.900 | rang 7.642
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SEI-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.885 | entrée 7.200 | trend 8.350 | rang 8.042
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ALGO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.312
2. XLM-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.238
3. RENDER-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.151

## Accélération indépendante

- ARK-EUR — CONFIRMED_ACCELERATION — score 8.892/10 — DETECTED_BUT_TOO_LATE
- WAXP-EUR — CONFIRMED_ACCELERATION — score 7.686/10 — DETECTED_BUT_TOO_LATE
- QKC-EUR — CONFIRMED_ACCELERATION — score 7.675/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BIGTIME-EUR — BUILDING_ACCELERATION — score 6.275/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZIG-EUR — BUILDING_ACCELERATION — score 6.098/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MANTRA-EUR — BUILDING_ACCELERATION — score 5.767/10 — DETECTED_BUT_TOO_LATE
- ANKR-EUR — BUILDING_ACCELERATION — score 5.349/10 — DETECTED_BUT_TOO_LATE
- GMT-EUR — BUILDING_ACCELERATION — score 5.238/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IMU-EUR — BUILDING_ACCELERATION — score 4.966/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- XLM-EUR — ACTIVE_NOW — score mémoire 8.238/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- DATAIP-EUR — ACTIVE_NOW — score mémoire 7.382/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- WMTX-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- SYN-EUR — MEMORY_24H — score mémoire 9.107/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEAQ-EUR — MEMORY_24H — score mémoire 9.037/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- ARK-EUR — ACTIVE_NOW — score mémoire 8.892/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ALGO-EUR — ACTIVE_NOW — score mémoire 8.312/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +63.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +30.83% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ONDO-EUR +28.02% — DETECTED_EARLY — couche NONE — action NONE
- QNT-EUR +27.75% — DETECTED_EARLY — couche NONE — action NONE
- XPL-EUR +26.77% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- TREAD-EUR +24.32% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- XAI-EUR +20.59% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DBR-EUR +19.92% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEAQ-EUR +19.28% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FET-EUR +18.52% — DETECTED_EARLY — couche NONE — action NONE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
