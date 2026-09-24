# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T02:11:27.487386+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : BEAM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.513 | entrée 5.800 | trend 7.850 | rang 7.142
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : 0G-EUR | action LATENT_ACCELERATOR | opportunité 7.450 | entrée 4.950 | trend 8.400 | rang 7.285
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SOL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.110 | entrée 6.700 | trend 7.650 | rang 7.989
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.989
2. GRT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.770
3. UNI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.769

## Accélération indépendante

- TRAC-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- BTT-EUR — BUILDING_ACCELERATION — score 5.027/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- IMU-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- TRIA-EUR — MEMORY_24H — score mémoire 9.929/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- IKA-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TRAC-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- NOM-EUR — MEMORY_24H — score mémoire 8.393/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZBCN-EUR — MEMORY_24H — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SOL-EUR — ACTIVE_NOW — score mémoire 7.989/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GRT-EUR — ACTIVE_NOW — score mémoire 7.770/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- NIL-EUR +45.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOM-EUR +41.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +19.50% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LSK-EUR +14.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CPOOL-EUR +14.09% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DBR-EUR +13.39% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- ZRO-EUR +12.56% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CAP-EUR +11.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IMU-EUR +10.01% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- RAY-EUR +7.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
