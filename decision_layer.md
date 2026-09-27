# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T15:46:14.877562+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : TRUST-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.115 | entrée 6.150 | trend 9.000 | rang 7.858
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BIGTIME-EUR | action LATENT_ACCELERATOR | opportunité 7.901 | entrée 5.750 | trend 8.900 | rang 7.769
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : TAIKO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.372 | entrée 6.800 | trend 8.650 | rang 8.302
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. TAIKO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.302
2. BAT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.252
3. AVNT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.149

## Accélération indépendante

- SOON-EUR — CONFIRMED_ACCELERATION — score 9.214/10 — DETECTED_BUT_TOO_LATE
- TAIKO-EUR — CONFIRMED_ACCELERATION — score 6.521/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ADX-EUR — BUILDING_ACCELERATION — score 6.280/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- INX-EUR — BUILDING_ACCELERATION — score 6.011/10 — DETECTED_BUT_TOO_LATE
- BAT-EUR — BUILDING_ACCELERATION — score 6.007/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- METIS-EUR — BUILDING_ACCELERATION — score 5.996/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- SOON-EUR — ACTIVE_NOW — score mémoire 9.214/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- MMT-EUR — MEMORY_24H — score mémoire 9.122/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GROVE-EUR — MEMORY_24H — score mémoire 8.518/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TAIKO-EUR — ACTIVE_NOW — score mémoire 8.302/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AXL-EUR — ACTIVE_NOW — score mémoire 8.252/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- BAT-EUR — ACTIVE_NOW — score mémoire 8.252/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AVNT-EUR — ACTIVE_NOW — score mémoire 8.149/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- DRIFT-EUR — ACTIVE_NOW — score mémoire 8.135/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GRAM-EUR — ACTIVE_NOW — score mémoire 8.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- QNT-EUR +54.18% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +53.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +39.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GLMR-EUR +30.86% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARX-EUR +27.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AUDIO-EUR +23.73% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- W-EUR +20.19% — DETECTED_EARLY — couche NONE — action NONE
- AGI-EUR +18.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +16.19% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INX-EUR +15.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
