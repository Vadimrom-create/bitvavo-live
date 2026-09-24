# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T01:54:01.791999+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : RENDER-EUR | action ACHETE_MAINTENANT | opportunité 7.576 | entrée 7.150 | trend 7.650 | rang 7.286
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ZIG-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.924 | entrée 5.950 | trend 7.850 | rang 7.170
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : 0G-EUR | action LATENT_ACCELERATOR | opportunité 7.453 | entrée 4.950 | trend 8.400 | rang 7.226
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : KMNO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.304 | entrée 6.600 | trend 8.300 | rang 8.024
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. KMNO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.024
2. PEAQ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.877
3. ZRO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.814

## Accélération indépendante

- IMU-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- CHR-EUR — CONFIRMED_ACCELERATION — score 8.520/10 — DETECTED_BUT_TOO_LATE
- EPIC-EUR — CONFIRMED_ACCELERATION — score 6.970/10 — DETECTED_BUT_TOO_LATE
- LIGHTER-EUR — BUILDING_ACCELERATION — score 5.827/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRC-EUR — BUILDING_ACCELERATION — score 5.762/10 — DETECTED_BUT_TOO_LATE
- API3-EUR — BUILDING_ACCELERATION — score 5.391/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BEL-EUR — BUILDING_ACCELERATION — score 5.214/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARX-EUR — BUILDING_ACCELERATION — score 5.141/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- IMU-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- TRIA-EUR — MEMORY_24H — score mémoire 9.929/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- IKA-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CHR-EUR — ACTIVE_NOW — score mémoire 8.520/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- NOM-EUR — MEMORY_24H — score mémoire 8.393/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZBCN-EUR — MEMORY_24H — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- KMNO-EUR — ACTIVE_NOW — score mémoire 8.024/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PEAQ-EUR — ACTIVE_NOW — score mémoire 7.877/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- NIL-EUR +44.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOM-EUR +42.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IMU-EUR +22.15% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SAGA-EUR +18.25% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DBR-EUR +16.88% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- CPOOL-EUR +16.06% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- UP-EUR +15.75% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- LSK-EUR +11.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +10.78% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CAP-EUR +10.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
