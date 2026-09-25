# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T02:01:11.626587+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LINK-EUR | action ACHETE_MAINTENANT | opportunité 9.101 | entrée 7.800 | trend 7.350 | rang 7.880
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : CAKE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.911 | entrée 6.100 | trend 8.950 | rang 7.833
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : COMP-EUR | action LATENT_ACCELERATOR | opportunité 7.494 | entrée 5.550 | trend 8.750 | rang 7.503
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : NEAR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.056 | entrée 7.150 | trend 8.500 | rang 7.846
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LINK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.880
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.846
3. CAKE-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.833

## Accélération indépendante

- SYN-EUR — BUILDING_ACCELERATION — score 6.229/10 — DETECTED_BUT_TOO_LATE
- PEAQ-EUR — BUILDING_ACCELERATION — score 5.803/10 — DETECTED_BUT_TOO_LATE
- HOME-EUR — BUILDING_ACCELERATION — score 5.615/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WMTX-EUR — BUILDING_ACCELERATION — score 5.588/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PTB-EUR — BUILDING_ACCELERATION — score 5.448/10 — DETECTED_BUT_TOO_LATE
- EDGE-EUR — BUILDING_ACCELERATION — score 5.430/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CRO-EUR — BUILDING_ACCELERATION — score 5.376/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KAIA-EUR — BUILDING_ACCELERATION — score 5.009/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TREAD-EUR — BUILDING_ACCELERATION — score 4.914/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- QKC-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- ARK-EUR — MEMORY_24H — score mémoire 8.892/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.169/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 8.082/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 7.880/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- OGN-EUR — MEMORY_24H — score mémoire 7.854/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NEAR-EUR — ACTIVE_NOW — score mémoire 7.846/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +56.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ONDO-EUR +28.67% — DETECTED_EARLY — couche NONE — action NONE
- QNT-EUR +28.59% — DETECTED_EARLY — couche NONE — action NONE
- TREAD-EUR +27.16% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- XPL-EUR +26.25% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- DYM-EUR +21.32% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEAQ-EUR +20.77% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DBR-EUR +18.14% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARK-EUR +15.62% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FET-EUR +15.57% — DETECTED_EARLY — couche NONE — action NONE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
