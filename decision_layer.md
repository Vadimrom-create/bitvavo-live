# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T03:55:43.784041+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 8.086 | entrée 6.800 | trend 8.300 | rang 7.222
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ARB-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.420 | entrée 6.150 | trend 7.500 | rang 7.551
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : 0G-EUR | action LATENT_ACCELERATOR | opportunité 7.984 | entrée 5.150 | trend 8.650 | rang 7.465
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PLUME-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.575 | entrée 6.950 | trend 8.700 | rang 8.023
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. PLUME-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.023
2. ETC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.865
3. DRIFT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.856

## Accélération indépendante

- IQ-EUR — CONFIRMED_ACCELERATION — score 6.755/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NOM-EUR — BUILDING_ACCELERATION — score 5.679/10 — DETECTED_BUT_TOO_LATE
- THE-EUR — BUILDING_ACCELERATION — score 5.064/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ETC-EUR — ACTIVE_NOW — score mémoire 7.865/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- LTC-EUR — ACTIVE_NOW — score mémoire 7.222/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- IMU-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- TRIA-EUR — MEMORY_24H — score mémoire 9.929/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TRAC-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZBCN-EUR — MEMORY_24H — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PLUME-EUR — ACTIVE_NOW — score mémoire 8.023/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- DRIFT-EUR — ACTIVE_NOW — score mémoire 7.856/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- NOM-EUR +37.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +35.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DBR-EUR +14.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SAGA-EUR +14.61% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LSK-EUR +12.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CPOOL-EUR +11.95% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOSO-EUR +9.60% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- KMNO-EUR +7.49% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +6.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IKA-EUR +6.55% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
