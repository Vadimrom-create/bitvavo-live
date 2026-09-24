# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T16:36:59.310315+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : XLM-EUR | action ACHETE_MAINTENANT | opportunité 9.098 | entrée 7.900 | trend 7.600 | rang 7.716
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : NEO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.792 | entrée 6.200 | trend 8.750 | rang 7.551
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : AERO-EUR | action LATENT_ACCELERATOR | opportunité 7.649 | entrée 4.500 | trend 8.700 | rang 7.306
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : BEAM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.520 | entrée 6.350 | trend 8.950 | rang 8.015
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. BEAM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.015
2. ICP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.980
3. GMT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.872

## Accélération indépendante

- ICX-EUR — CONFIRMED_ACCELERATION — score 9.834/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SAPIEN-EUR — CONFIRMED_ACCELERATION — score 8.581/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EDGE-EUR — CONFIRMED_ACCELERATION — score 8.463/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ALGO-EUR — CONFIRMED_ACCELERATION — score 8.225/10 — DETECTED_BUT_TOO_LATE
- AUCTION-EUR — CONFIRMED_ACCELERATION — score 7.715/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MAVIA-EUR — CONFIRMED_ACCELERATION — score 7.602/10 — DETECTED_BUT_TOO_LATE
- ENA-EUR — CONFIRMED_ACCELERATION — score 7.540/10 — DETECTED_BUT_TOO_LATE
- NEAR-EUR — CONFIRMED_ACCELERATION — score 7.256/10 — DETECTED_BUT_TOO_LATE
- EGLD-EUR — CONFIRMED_ACCELERATION — score 7.132/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZBCN-EUR — CONFIRMED_ACCELERATION — score 7.114/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- XLM-EUR — ACTIVE_NOW — score mémoire 7.716/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- AMP-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — ACTIVE_NOW — score mémoire 9.834/10 — sources ACCELERATION, V4 — WATCH_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- SAPIEN-EUR — ACTIVE_NOW — score mémoire 8.581/10 — sources ACCELERATION, V4 — WATCH_ONLY
- CNPY-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- POND-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- EDGE-EUR — ACTIVE_NOW — score mémoire 8.463/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- NOM-EUR +42.58% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- LSK-EUR +31.13% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ONDO-EUR +25.24% — DETECTED_EARLY — couche NONE — action NONE
- LTC-EUR +22.70% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +20.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEAQ-EUR +18.55% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PLUME-EUR +18.20% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +17.37% — DETECTED_EARLY — couche NONE — action NONE
- FET-EUR +17.11% — DETECTED_EARLY — couche NONE — action NONE
- XPL-EUR +17.03% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
