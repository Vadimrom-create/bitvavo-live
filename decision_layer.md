# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T15:23:49.784881+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : INJ-EUR | action ACHETE_MAINTENANT | opportunité 7.950 | entrée 7.350 | trend 8.300 | rang 7.523
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : CAKE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.563 | entrée 6.700 | trend 7.550 | rang 7.599
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : RED-EUR | action LATENT_ACCELERATOR | opportunité 7.663 | entrée 4.500 | trend 8.650 | rang 7.322
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PYTH-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.761 | entrée 6.700 | trend 8.650 | rang 7.846
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. PYTH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.846
2. BEAM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.767
3. STX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.720

## Accélération indépendante

- XAI-EUR — CONFIRMED_ACCELERATION — score 9.433/10 — DETECTED_BUT_TOO_LATE
- ZAMA-EUR — CONFIRMED_ACCELERATION — score 9.405/10 — DETECTED_BUT_TOO_LATE
- NOS-EUR — CONFIRMED_ACCELERATION — score 8.744/10 — DETECTED_BUT_TOO_LATE
- HFT-EUR — CONFIRMED_ACCELERATION — score 8.258/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CTK-EUR — CONFIRMED_ACCELERATION — score 7.454/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PYTH-EUR — CONFIRMED_ACCELERATION — score 7.289/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VELO-EUR — CONFIRMED_ACCELERATION — score 7.205/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AVA-EUR — CONFIRMED_ACCELERATION — score 7.160/10 — DETECTED_BUT_TOO_LATE
- POND-EUR — CONFIRMED_ACCELERATION — score 6.983/10 — DETECTED_BUT_TOO_LATE
- ONDO-EUR — CONFIRMED_ACCELERATION — score 6.648/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ADA-EUR — ACTIVE_NOW — score mémoire 7.256/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- AMP-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FLOCK-EUR — MEMORY_24H — score mémoire 9.446/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XAI-EUR — ACTIVE_NOW — score mémoire 9.433/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ZAMA-EUR — ACTIVE_NOW — score mémoire 9.405/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- NOS-EUR — ACTIVE_NOW — score mémoire 8.744/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- 2Z-EUR — MEMORY_24H — score mémoire 8.723/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CNPY-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- NOM-EUR +35.27% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- LSK-EUR +23.66% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ONDO-EUR +22.98% — DETECTED_EARLY — couche NONE — action NONE
- LTC-EUR +20.78% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +18.16% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PEAQ-EUR +15.49% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARX-EUR +14.37% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ETC-EUR +12.53% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PLUME-EUR +12.23% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CAT-EUR +11.58% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
