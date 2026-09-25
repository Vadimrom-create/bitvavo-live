# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T04:41:59.597911+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : INJ-EUR | action ACHETE_MAINTENANT | opportunité 8.579 | entrée 6.950 | trend 7.900 | rang 7.799
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : TAIKO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.924 | entrée 6.100 | trend 7.450 | rang 7.596
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BEAM-EUR | action LATENT_ACCELERATOR | opportunité 7.722 | entrée 5.350 | trend 8.650 | rang 7.548
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : CAKE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.421 | entrée 6.150 | trend 8.950 | rang 8.515
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. CAKE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.515
2. LTC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.371
3. PYTH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.808

## Accélération indépendante

- WMTX-EUR — CONFIRMED_ACCELERATION — score 8.409/10 — DETECTED_BUT_TOO_LATE
- MOVR-EUR — CONFIRMED_ACCELERATION — score 8.391/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XAI-EUR — CONFIRMED_ACCELERATION — score 6.612/10 — DETECTED_BUT_TOO_LATE
- CFG-EUR — BUILDING_ACCELERATION — score 6.302/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — BUILDING_ACCELERATION — score 6.202/10 — DETECTED_BUT_TOO_LATE
- VVV-EUR — BUILDING_ACCELERATION — score 6.117/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RON-EUR — BUILDING_ACCELERATION — score 5.935/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DIA-EUR — BUILDING_ACCELERATION — score 5.419/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ETHFI-EUR — BUILDING_ACCELERATION — score 4.947/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NIL-EUR — BUILDING_ACCELERATION — score 4.894/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- QKC-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- UP-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.742/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 8.515/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WMTX-EUR — ACTIVE_NOW — score mémoire 8.409/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- MOVR-EUR — ACTIVE_NOW — score mémoire 8.391/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 8.371/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- QNT-EUR +36.77% — DETECTED_EARLY — couche NONE — action NONE
- TREAD-EUR +32.20% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ONDO-EUR +27.96% — DETECTED_EARLY — couche NONE — action NONE
- XPL-EUR +27.20% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PEAQ-EUR +22.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +22.82% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- XAI-EUR +17.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FET-EUR +16.34% — DETECTED_EARLY — couche NONE — action NONE
- TAI-EUR +14.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DBR-EUR +14.47% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
