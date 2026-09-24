# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T12:07:50.386729+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ONDO-EUR | action ACHETE_MAINTENANT | opportunité 8.659 | entrée 6.800 | trend 7.600 | rang 7.727
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : COMP-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.637 | entrée 5.800 | trend 8.500 | rang 7.509
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : XTZ-EUR | action LATENT_ACCELERATOR | opportunité 7.471 | entrée 5.050 | trend 7.550 | rang 6.821
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LTC-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.330 | entrée 6.700 | trend 9.200 | rang 8.144
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LTC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.144
2. JUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.949
3. PLUME-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.861

## Accélération indépendante

- ONDO-EUR — CONFIRMED_ACCELERATION — score 9.156/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PHA-EUR — CONFIRMED_ACCELERATION — score 7.785/10 — DETECTED_BUT_TOO_LATE
- RED-EUR — BUILDING_ACCELERATION — score 6.186/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZIG-EUR — BUILDING_ACCELERATION — score 5.498/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ONDO-EUR — ACTIVE_NOW — score mémoire 9.156/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ZRC-EUR — MEMORY_24H — score mémoire 9.712/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PROM-EUR — MEMORY_24H — score mémoire 9.590/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FLOCK-EUR — MEMORY_24H — score mémoire 9.446/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 8.917/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CNPY-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- C98-EUR — MEMORY_24H — score mémoire 8.347/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 8.144/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- EDGE-EUR — MEMORY_24H — score mémoire 7.950/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- NOM-EUR +39.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +30.16% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- LSK-EUR +26.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARX-EUR +15.48% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CVC-EUR +13.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IMU-EUR +13.40% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PHA-EUR +8.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOSO-EUR +8.68% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- CNPY-EUR +8.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LTC-EUR +6.58% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
