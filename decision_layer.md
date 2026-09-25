# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T10:36:18.915658+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : VET-EUR | action ACHETE_MAINTENANT | opportunité 8.145 | entrée 7.400 | trend 8.400 | rang 7.787
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : DYM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.348 | entrée 6.000 | trend 8.450 | rang 7.692
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : RED-EUR | action LATENT_ACCELERATOR | opportunité 8.539 | entrée 5.700 | trend 8.950 | rang 7.928
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LTC-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.160 | entrée 6.250 | trend 8.900 | rang 7.937
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LTC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.937
2. RED-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.928
3. JUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.915

## Accélération indépendante

- WMTX-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- CHIP-EUR — CONFIRMED_ACCELERATION — score 7.647/10 — DETECTED_BUT_TOO_LATE
- FUEL-EUR — CONFIRMED_ACCELERATION — score 7.240/10 — DETECTED_BUT_TOO_LATE
- REZ-EUR — CONFIRMED_ACCELERATION — score 7.228/10 — DETECTED_BUT_TOO_LATE
- ZBCN-EUR — CONFIRMED_ACCELERATION — score 7.194/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NIL-EUR — CONFIRMED_ACCELERATION — score 6.500/10 — DETECTED_BUT_TOO_LATE
- GTC-EUR — BUILDING_ACCELERATION — score 6.270/10 — DETECTED_BUT_TOO_LATE
- DYM-EUR — BUILDING_ACCELERATION — score 6.072/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HUMA-EUR — BUILDING_ACCELERATION — score 5.356/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ACU-EUR — BUILDING_ACCELERATION — score 5.218/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GLMR-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WMTX-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- CSPR-EUR — MEMORY_24H — score mémoire 8.374/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.253/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 7.937/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RED-EUR — ACTIVE_NOW — score mémoire 7.928/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- JUP-EUR — ACTIVE_NOW — score mémoire 7.915/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- QNT-EUR +40.24% — DETECTED_EARLY — couche NONE — action NONE
- TREAD-EUR +33.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ONDO-EUR +31.68% — DETECTED_EARLY — couche NONE — action NONE
- XPL-EUR +31.53% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARK-EUR +29.36% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PHA-EUR +26.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FET-EUR +23.17% — DETECTED_EARLY — couche NONE — action NONE
- PEAQ-EUR +20.60% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHIP-EUR +19.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- JTO-EUR +19.90% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
