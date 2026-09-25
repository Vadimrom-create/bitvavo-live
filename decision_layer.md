# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T10:52:33.619122+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : VET-EUR | action ACHETE_MAINTENANT | opportunité 8.905 | entrée 7.200 | trend 8.400 | rang 8.081
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : RED-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.102 | entrée 5.900 | trend 8.950 | rang 8.236
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : 0G-EUR | action LATENT_ACCELERATOR | opportunité 7.961 | entrée 5.650 | trend 8.650 | rang 7.566
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : BONK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.268 | entrée 7.050 | trend 8.200 | rang 8.222
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. RED-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 8.236
2. BONK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.222
3. JUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.202

## Accélération indépendante

- ARK-EUR — CONFIRMED_ACCELERATION — score 8.839/10 — DETECTED_BUT_TOO_LATE
- ZRO-EUR — CONFIRMED_ACCELERATION — score 6.876/10 — DETECTED_BUT_TOO_LATE
- SQD-EUR — CONFIRMED_ACCELERATION — score 6.816/10 — DETECTED_BUT_TOO_LATE
- ZEN-EUR — CONFIRMED_ACCELERATION — score 6.551/10 — DETECTED_BUT_TOO_LATE
- IMU-EUR — BUILDING_ACCELERATION — score 6.375/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WAXP-EUR — BUILDING_ACCELERATION — score 6.186/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SNX-EUR — BUILDING_ACCELERATION — score 6.043/10 — DETECTED_BUT_TOO_LATE
- HUMA-EUR — BUILDING_ACCELERATION — score 5.955/10 — DETECTED_BUT_TOO_LATE
- CHILLGUY-EUR — BUILDING_ACCELERATION — score 5.792/10 — DETECTED_BUT_TOO_LATE
- VELO-EUR — BUILDING_ACCELERATION — score 5.715/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GLMR-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARK-EUR — ACTIVE_NOW — score mémoire 8.839/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- TAI-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 8.374/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.253/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RED-EUR — ACTIVE_NOW — score mémoire 8.236/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- BONK-EUR — ACTIVE_NOW — score mémoire 8.222/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 8.202/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- QNT-EUR +35.78% — DETECTED_EARLY — couche NONE — action NONE
- ARK-EUR +34.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +30.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ONDO-EUR +29.20% — DETECTED_EARLY — couche NONE — action NONE
- XPL-EUR +28.55% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PHA-EUR +28.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- JTO-EUR +20.88% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- FET-EUR +20.06% — DETECTED_EARLY — couche NONE — action NONE
- CHIP-EUR +19.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEAQ-EUR +19.56% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
