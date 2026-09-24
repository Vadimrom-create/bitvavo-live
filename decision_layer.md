# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T22:00:59.673116+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ADA-EUR | action ACHETE_MAINTENANT | opportunité 9.284 | entrée 8.050 | trend 8.150 | rang 8.382
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : NEO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.762 | entrée 6.000 | trend 8.750 | rang 7.624
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BAT-EUR | action LATENT_ACCELERATOR | opportunité 7.571 | entrée 4.500 | trend 8.650 | rang 7.377
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ALGO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.248 | entrée 6.750 | trend 8.200 | rang 8.180
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ADA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.382
2. ICP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.322
3. ALGO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.180

## Accélération indépendante

- PEAQ-EUR — CONFIRMED_ACCELERATION — score 9.037/10 — DETECTED_BUT_TOO_LATE
- U-EUR — BUILDING_ACCELERATION — score 6.112/10 — DETECTED_BUT_TOO_LATE
- BILL-EUR — BUILDING_ACCELERATION — score 5.441/10 — DETECTED_BUT_TOO_LATE
- CVX-EUR — BUILDING_ACCELERATION — score 5.333/10 — DETECTED_BUT_TOO_LATE
- SAGA-EUR — BUILDING_ACCELERATION — score 5.295/10 — DETECTED_BUT_TOO_LATE
- SYN-EUR — BUILDING_ACCELERATION — score 5.202/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MOODENG-EUR — BUILDING_ACCELERATION — score 4.789/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- PEAQ-EUR — ACTIVE_NOW — score mémoire 9.037/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- ADA-EUR — ACTIVE_NOW — score mémoire 8.382/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.322/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- DYM-EUR — MEMORY_24H — score mémoire 8.195/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ALGO-EUR — ACTIVE_NOW — score mémoire 8.180/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.072/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- BEAM-EUR — ACTIVE_NOW — score mémoire 8.020/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- XAI-EUR +34.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEAQ-EUR +29.31% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ONDO-EUR +27.36% — DETECTED_EARLY — couche NONE — action NONE
- LSK-EUR +27.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QNT-EUR +26.26% — DETECTED_EARLY — couche NONE — action NONE
- XPL-EUR +26.11% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- TREAD-EUR +24.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +24.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +20.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LTC-EUR +16.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
