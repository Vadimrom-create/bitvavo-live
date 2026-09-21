# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T09:54:48.265332+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : INJ-EUR | action ACHETE_MAINTENANT | opportunité 9.259 | entrée 7.700 | trend 8.300 | rang 8.239
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : PENDLE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.455 | entrée 6.100 | trend 8.950 | rang 7.910
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ATH-EUR | action LATENT_ACCELERATOR | opportunité 8.032 | entrée 5.500 | trend 8.450 | rang 7.459
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MERL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.593 | entrée 6.700 | trend 9.200 | rang 8.147
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. INJ-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.239
2. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.147
3. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.083

## Accélération indépendante

- TAI-EUR — CONFIRMED_ACCELERATION — score 9.488/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SYN-EUR — CONFIRMED_ACCELERATION — score 8.602/10 — DETECTED_BUT_TOO_LATE
- SWEAT-EUR — CONFIRMED_ACCELERATION — score 6.711/10 — DETECTED_BUT_TOO_LATE
- ANKR-EUR — CONFIRMED_ACCELERATION — score 6.673/10 — DETECTED_BUT_TOO_LATE
- RLC-EUR — BUILDING_ACCELERATION — score 6.383/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AIOZ-EUR — BUILDING_ACCELERATION — score 6.016/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — BUILDING_ACCELERATION — score 5.872/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZAMA-EUR — BUILDING_ACCELERATION — score 5.807/10 — DETECTED_BUT_TOO_LATE
- PEAQ-EUR — BUILDING_ACCELERATION — score 5.638/10 — DETECTED_BUT_TOO_LATE
- AGI-EUR — BUILDING_ACCELERATION — score 5.197/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- STX-EUR — ACTIVE_NOW — score mémoire 7.735/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- LINK-EUR — ACTIVE_NOW — score mémoire 6.957/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- EDGE-EUR — MEMORY_24H — score mémoire 9.925/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TAI-EUR — ACTIVE_NOW — score mémoire 9.488/10 — sources ACCELERATION, V4 — WATCH_ONLY
- ZETA-EUR — MEMORY_24H — score mémoire 9.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NOS-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SYN-EUR — ACTIVE_NOW — score mémoire 8.602/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- MOCA-EUR — MEMORY_24H — score mémoire 8.589/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PHA-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 8.457/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZETA-EUR +71.86% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PTB-EUR +57.19% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PHA-EUR +48.99% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +40.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +31.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +31.23% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +27.47% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEAQ-EUR +27.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VVV-EUR +23.49% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DRIFT-EUR +22.69% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
