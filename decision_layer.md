# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T19:48:16.619403+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : VET-EUR | action ACHETE_MAINTENANT | opportunité 9.341 | entrée 8.200 | trend 8.450 | rang 8.368
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : COW-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.788 | entrée 6.750 | trend 8.900 | rang 7.821
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MERL-EUR | action LATENT_ACCELERATOR | opportunité 7.803 | entrée 5.300 | trend 8.900 | rang 7.669
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : TAO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.169 | entrée 7.400 | trend 8.050 | rang 8.083
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.368
2. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.083
3. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.042

## Accélération indépendante

- PTB-EUR — CONFIRMED_ACCELERATION — score 9.534/10 — DETECTED_BUT_TOO_LATE
- ZKJ-EUR — CONFIRMED_ACCELERATION — score 9.182/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EPIC-EUR — CONFIRMED_ACCELERATION — score 8.748/10 — DETECTED_BUT_TOO_LATE
- ZEUS-EUR — CONFIRMED_ACCELERATION — score 7.632/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TREAD-EUR — CONFIRMED_ACCELERATION — score 6.862/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- JASMY-EUR — BUILDING_ACCELERATION — score 5.840/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CC-EUR — BUILDING_ACCELERATION — score 5.266/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SAGA-EUR — BUILDING_ACCELERATION — score 5.173/10 — DETECTED_BUT_TOO_LATE
- IMU-EUR — BUILDING_ACCELERATION — score 5.152/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HNT-EUR — BUILDING_ACCELERATION — score 4.857/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- VET-EUR — ACTIVE_NOW — score mémoire 8.368/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- RON-EUR — MEMORY_24H — score mémoire 9.938/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PTB-EUR — ACTIVE_NOW — score mémoire 9.534/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ZKJ-EUR — ACTIVE_NOW — score mémoire 9.182/10 — sources ACCELERATION, V4 — WATCH_ONLY
- THQ-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACU-EUR — MEMORY_24H — score mémoire 9.053/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- EPIC-EUR — ACTIVE_NOW — score mémoire 8.748/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LUMIA-EUR — MEMORY_24H — score mémoire 8.655/10 — sources ACCELERATION — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ICX-EUR +122.44% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRC-EUR +114.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZETA-EUR +57.07% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PHA-EUR +39.81% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AIOZ-EUR +37.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FORM-EUR +37.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PTB-EUR +35.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SWELL-EUR +29.48% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOS-EUR +24.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEPE-EUR +23.70% — DETECTED_EARLY — couche NONE — action NONE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
