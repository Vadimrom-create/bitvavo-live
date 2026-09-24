# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T03:00:55.374578+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : EIGEN-EUR | action ACHETE_MAINTENANT | opportunité 8.682 | entrée 6.800 | trend 7.300 | rang 7.451
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : WIF-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.098 | entrée 6.550 | trend 7.450 | rang 6.823
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : NEO-EUR | action LATENT_ACCELERATOR | opportunité 8.401 | entrée 5.750 | trend 7.350 | rang 7.205
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : INJ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.171 | entrée 7.300 | trend 7.800 | rang 7.825
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.825
2. BONK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.771
3. PLUME-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.761

## Accélération indépendante

- WIF-EUR — CONFIRMED_ACCELERATION — score 7.143/10 — DETECTED_BUT_TOO_LATE
- PEAQ-EUR — CONFIRMED_ACCELERATION — score 6.630/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- JASMY-EUR — BUILDING_ACCELERATION — score 6.038/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ORCA-EUR — BUILDING_ACCELERATION — score 5.973/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MANTRA-EUR — BUILDING_ACCELERATION — score 5.915/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FARTCOIN-EUR — BUILDING_ACCELERATION — score 5.563/10 — DETECTED_BUT_TOO_LATE
- LTC-EUR — BUILDING_ACCELERATION — score 5.545/10 — DETECTED_BUT_TOO_LATE
- ETC-EUR — BUILDING_ACCELERATION — score 5.247/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RARE-EUR — BUILDING_ACCELERATION — score 5.157/10 — DETECTED_BUT_TOO_LATE
- ALICE-EUR — BUILDING_ACCELERATION — score 5.155/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EIGEN-EUR — ACTIVE_NOW — score mémoire 7.451/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- IMU-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- TRIA-EUR — MEMORY_24H — score mémoire 9.929/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- IKA-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TRAC-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NOM-EUR — MEMORY_24H — score mémoire 8.393/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZBCN-EUR — MEMORY_24H — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 7.825/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- NOM-EUR +36.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +35.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +19.50% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CPOOL-EUR +14.81% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +11.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DBR-EUR +11.30% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RAY-EUR +9.47% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IMU-EUR +9.12% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOSO-EUR +8.99% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- KMNO-EUR +8.83% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
