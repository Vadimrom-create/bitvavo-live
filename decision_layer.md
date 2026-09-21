# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T01:54:36.280617+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAO-EUR | action ACHETE_MAINTENANT | opportunité 7.750 | entrée 7.650 | trend 8.250 | rang 7.609
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : MERL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.589 | entrée 6.350 | trend 8.650 | rang 7.606
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ARX-EUR | action LATENT_ACCELERATOR | opportunité 7.852 | entrée 5.400 | trend 8.900 | rang 7.652
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : WAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.071 | entrée 6.050 | trend 9.200 | rang 7.944
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.944
2. KAS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.851
3. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.798

## Accélération indépendante

- PTB-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- LSK-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PEAQ-EUR — CONFIRMED_ACCELERATION — score 6.744/10 — DETECTED_BUT_TOO_LATE
- LIGHTER-EUR — CONFIRMED_ACCELERATION — score 6.590/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- G-EUR — BUILDING_ACCELERATION — score 6.402/10 — DETECTED_BUT_TOO_LATE
- XTZ-EUR — BUILDING_ACCELERATION — score 6.325/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PROVE-EUR — BUILDING_ACCELERATION — score 5.574/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XYO-EUR — BUILDING_ACCELERATION — score 4.801/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- XPL-EUR — ACTIVE_NOW — score mémoire 5.932/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- PTB-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ICX-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.883/10 — sources ACCELERATION — MEMORY_ONLY
- LSK-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.376/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- UP-EUR — MEMORY_24H — score mémoire 8.113/10 — sources ACCELERATION — MEMORY_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.944/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.851/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 7.798/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PTB-EUR +60.17% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +42.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +29.00% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NIL-EUR +23.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +23.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +20.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +17.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- VVV-EUR +16.75% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- S-EUR +15.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEAQ-EUR +15.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
