# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T11:00:38.735311+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ONDO-EUR | action ACHETE_MAINTENANT | opportunité 9.129 | entrée 8.400 | trend 8.150 | rang 8.138
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : MIOTA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.166 | entrée 6.250 | trend 7.350 | rang 7.186
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ACH-EUR | action LATENT_ACCELERATOR | opportunité 8.007 | entrée 5.500 | trend 9.000 | rang 7.722
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MERL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.574 | entrée 7.350 | trend 9.200 | rang 8.287
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.287
2. ONDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.138
3. RUNE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.995

## Accélération indépendante

- IMX-EUR — CONFIRMED_ACCELERATION — score 9.317/10 — DETECTED_BUT_TOO_LATE
- PHA-EUR — CONFIRMED_ACCELERATION — score 9.074/10 — DETECTED_BUT_TOO_LATE
- SEI-EUR — CONFIRMED_ACCELERATION — score 8.603/10 — DETECTED_BUT_TOO_LATE
- SPX-EUR — CONFIRMED_ACCELERATION — score 6.604/10 — DETECTED_BUT_TOO_LATE
- ARB-EUR — CONFIRMED_ACCELERATION — score 6.523/10 — DETECTED_BUT_TOO_LATE
- ZAMA-EUR — BUILDING_ACCELERATION — score 6.232/10 — DETECTED_BUT_TOO_LATE
- BLUR-EUR — BUILDING_ACCELERATION — score 6.127/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CELR-EUR — BUILDING_ACCELERATION — score 5.736/10 — DETECTED_BUT_TOO_LATE
- PTB-EUR — BUILDING_ACCELERATION — score 5.697/10 — DETECTED_BUT_TOO_LATE
- XPL-EUR — BUILDING_ACCELERATION — score 5.684/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ONDO-EUR — ACTIVE_NOW — score mémoire 8.138/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- EDGE-EUR — MEMORY_24H — score mémoire 9.925/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 9.488/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RLC-EUR — MEMORY_24H — score mémoire 9.465/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMX-EUR — ACTIVE_NOW — score mémoire 9.317/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CHIP-EUR — MEMORY_24H — score mémoire 9.309/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 9.074/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- NOS-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SEI-EUR — ACTIVE_NOW — score mémoire 8.603/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- MOCA-EUR — MEMORY_24H — score mémoire 8.589/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- PHA-EUR +84.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZETA-EUR +73.04% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PTB-EUR +55.46% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NIL-EUR +36.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SEI-EUR +33.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +29.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEAQ-EUR +25.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +24.31% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SUI-EUR +23.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SAGA-EUR +22.98% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
