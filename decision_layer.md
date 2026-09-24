# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T17:58:28.879909+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAIKO-EUR | action ACHETE_MAINTENANT | opportunité 7.824 | entrée 7.200 | trend 7.900 | rang 7.413
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AERO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.795 | entrée 6.250 | trend 8.700 | rang 7.702
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : TRB-EUR | action LATENT_ACCELERATOR | opportunité 8.279 | entrée 5.600 | trend 8.700 | rang 7.328
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ICP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.029 | entrée 6.800 | trend 9.200 | rang 8.030
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ICP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.030
2. GMT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.966
3. DATAIP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.788

## Accélération indépendante

- MLN-EUR — CONFIRMED_ACCELERATION — score 9.991/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PIXEL-EUR — CONFIRMED_ACCELERATION — score 8.951/10 — DETECTED_BUT_TOO_LATE
- XAI-EUR — CONFIRMED_ACCELERATION — score 8.446/10 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — CONFIRMED_ACCELERATION — score 7.485/10 — DETECTED_BUT_TOO_LATE
- ALICE-EUR — CONFIRMED_ACCELERATION — score 6.828/10 — DETECTED_BUT_TOO_LATE
- ZIG-EUR — CONFIRMED_ACCELERATION — score 6.781/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZKJ-EUR — CONFIRMED_ACCELERATION — score 6.738/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PORTAL-EUR — BUILDING_ACCELERATION — score 6.097/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CYBER-EUR — BUILDING_ACCELERATION — score 5.893/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RON-EUR — BUILDING_ACCELERATION — score 5.503/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- MLN-EUR — ACTIVE_NOW — score mémoire 9.991/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PIXEL-EUR — ACTIVE_NOW — score mémoire 8.951/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 8.892/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- UP-EUR — MEMORY_24H — score mémoire 8.796/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- 2Z-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CNPY-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- EDGE-EUR — MEMORY_24H — score mémoire 8.463/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XAI-EUR — ACTIVE_NOW — score mémoire 8.446/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- XAI-EUR +55.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOM-EUR +33.81% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- LSK-EUR +33.23% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ONDO-EUR +25.64% — DETECTED_EARLY — couche NONE — action NONE
- ARX-EUR +20.39% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +19.67% — DETECTED_EARLY — couche NONE — action NONE
- LTC-EUR +19.09% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEAQ-EUR +18.92% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +18.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PLUME-EUR +17.32% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
