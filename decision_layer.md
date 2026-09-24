# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T12:52:55.892520+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : FET-EUR | action ACHETE_MAINTENANT | opportunité 8.727 | entrée 7.350 | trend 7.650 | rang 7.828
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : PLUME-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.491 | entrée 5.850 | trend 8.650 | rang 7.502
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ZETA-EUR | action LATENT_ACCELERATOR | opportunité 7.642 | entrée 5.700 | trend 7.450 | rang 6.609
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LTC-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.332 | entrée 6.550 | trend 9.200 | rang 8.124
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LTC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.124
2. FET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.828
3. ETC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.759

## Accélération indépendante

- PEAQ-EUR — CONFIRMED_ACCELERATION — score 8.354/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FTT-EUR — CONFIRMED_ACCELERATION — score 8.174/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NES-EUR — CONFIRMED_ACCELERATION — score 7.085/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARKM-EUR — CONFIRMED_ACCELERATION — score 6.714/10 — DETECTED_BUT_TOO_LATE
- ARK-EUR — BUILDING_ACCELERATION — score 5.658/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KAITO-EUR — BUILDING_ACCELERATION — score 5.290/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LSK-EUR — BUILDING_ACCELERATION — score 5.107/10 — DETECTED_BUT_TOO_LATE
- INIT-EUR — BUILDING_ACCELERATION — score 4.975/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- QNT-EUR — ACTIVE_NOW — score mémoire 7.670/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- AMP-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FLOCK-EUR — MEMORY_24H — score mémoire 9.446/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 8.917/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CNPY-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEAQ-EUR — ACTIVE_NOW — score mémoire 8.354/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- C98-EUR — MEMORY_24H — score mémoire 8.347/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FTT-EUR — ACTIVE_NOW — score mémoire 8.174/10 — sources ACCELERATION, V4 — WATCH_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 8.124/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- NOM-EUR +36.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +29.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +25.26% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARX-EUR +16.76% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PHA-EUR +9.97% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEAQ-EUR +8.83% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARK-EUR +8.31% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOSO-EUR +8.30% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- IMU-EUR +8.07% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CVC-EUR +7.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
