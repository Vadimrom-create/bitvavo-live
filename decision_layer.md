# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T13:10:18.082574+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ARB-EUR | action ACHETE_MAINTENANT | opportunité 9.063 | entrée 7.650 | trend 7.500 | rang 8.013
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : RENDER-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.784 | entrée 6.750 | trend 8.200 | rang 7.431
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : PLUME-EUR | action LATENT_ACCELERATOR | opportunité 7.579 | entrée 4.500 | trend 8.650 | rang 7.320
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LTC-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.027 | entrée 8.400 | trend 9.200 | rang 8.535
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LTC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.535
2. ARB-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.013
3. FET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.010

## Accélération indépendante

- HUMA-EUR — CONFIRMED_ACCELERATION — score 8.807/10 — DETECTED_BUT_TOO_LATE
- COTI-EUR — CONFIRMED_ACCELERATION — score 7.594/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FET-EUR — CONFIRMED_ACCELERATION — score 7.557/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZAMA-EUR — CONFIRMED_ACCELERATION — score 7.512/10 — DETECTED_BUT_TOO_LATE
- LTC-EUR — CONFIRMED_ACCELERATION — score 7.026/10 — DETECTED_BUT_TOO_LATE
- RAY-EUR — CONFIRMED_ACCELERATION — score 6.634/10 — DETECTED_BUT_TOO_LATE
- PEAQ-EUR — CONFIRMED_ACCELERATION — score 6.623/10 — DETECTED_BUT_TOO_LATE
- SXT-EUR — CONFIRMED_ACCELERATION — score 6.526/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAI-EUR — BUILDING_ACCELERATION — score 6.254/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICP-EUR — BUILDING_ACCELERATION — score 6.103/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- FET-EUR — ACTIVE_NOW — score mémoire 8.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ICP-EUR — ACTIVE_NOW — score mémoire 7.453/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- AMP-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FLOCK-EUR — MEMORY_24H — score mémoire 9.446/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 8.917/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HUMA-EUR — ACTIVE_NOW — score mémoire 8.807/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- LTC-EUR — ACTIVE_NOW — score mémoire 8.535/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CNPY-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- C98-EUR — MEMORY_24H — score mémoire 8.347/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- NIL-EUR +39.69% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- NOM-EUR +37.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +26.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARX-EUR +18.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IMU-EUR +12.54% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PEAQ-EUR +11.73% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LTC-EUR +10.64% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INIT-EUR +9.01% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SOSO-EUR +8.30% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- ARK-EUR +8.05% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
