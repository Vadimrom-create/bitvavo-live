# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T09:23:12.527327+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : PYTH-EUR | action ACHETE_MAINTENANT | opportunité 8.001 | entrée 7.350 | trend 8.900 | rang 7.727
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : IMX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.296 | entrée 5.800 | trend 8.500 | rang 7.627
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : RED-EUR | action LATENT_ACCELERATOR | opportunité 7.989 | entrée 5.450 | trend 8.950 | rang 7.681
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : BEAM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.760 | entrée 6.700 | trend 8.900 | rang 8.033
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. BEAM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.033
2. COMP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.941
3. KMNO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.786

## Accélération indépendante

- SAGA-EUR — CONFIRMED_ACCELERATION — score 8.706/10 — DETECTED_BUT_TOO_LATE
- WAXP-EUR — CONFIRMED_ACCELERATION — score 8.248/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARK-EUR — CONFIRMED_ACCELERATION — score 8.161/10 — DETECTED_BUT_TOO_LATE
- AVA-EUR — CONFIRMED_ACCELERATION — score 7.155/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RON-EUR — CONFIRMED_ACCELERATION — score 6.852/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — CONFIRMED_ACCELERATION — score 6.500/10 — DETECTED_BUT_TOO_LATE
- ILV-EUR — BUILDING_ACCELERATION — score 6.371/10 — DETECTED_BUT_TOO_LATE
- KITE-EUR — BUILDING_ACCELERATION — score 6.285/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VVV-EUR — BUILDING_ACCELERATION — score 6.249/10 — DETECTED_BUT_TOO_LATE
- AMP-EUR — BUILDING_ACCELERATION — score 6.080/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- SEI-EUR — ACTIVE_NOW — score mémoire 6.418/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XPL-EUR — MEMORY_24H — score mémoire 8.847/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SAGA-EUR — ACTIVE_NOW — score mémoire 8.706/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- WMTX-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 8.374/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 8.264/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- WAXP-EUR — ACTIVE_NOW — score mémoire 8.248/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ARK-EUR — ACTIVE_NOW — score mémoire 8.161/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- TREAD-EUR +45.04% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- QNT-EUR +38.68% — DETECTED_EARLY — couche NONE — action NONE
- ARK-EUR +34.22% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XPL-EUR +33.79% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ONDO-EUR +29.41% — DETECTED_EARLY — couche NONE — action NONE
- PHA-EUR +24.25% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FUEL-EUR +23.59% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- FET-EUR +20.45% — DETECTED_EARLY — couche NONE — action NONE
- PEAQ-EUR +19.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XAI-EUR +19.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
