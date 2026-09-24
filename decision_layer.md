# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T16:54:04.560589+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : EIGEN-EUR | action ACHETE_MAINTENANT | opportunité 8.277 | entrée 7.250 | trend 8.650 | rang 7.816
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : A-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.924 | entrée 6.100 | trend 8.600 | rang 7.487
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : 0G-EUR | action LATENT_ACCELERATOR | opportunité 7.842 | entrée 4.500 | trend 8.650 | rang 7.418
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : KMNO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.063 | entrée 6.850 | trend 8.550 | rang 8.163
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. KMNO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.163
2. BEAM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.116
3. ICP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.098

## Accélération indépendante

- 2Z-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- MLN-EUR — CONFIRMED_ACCELERATION — score 8.477/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MOG-EUR — CONFIRMED_ACCELERATION — score 7.283/10 — DETECTED_BUT_TOO_LATE
- STRK-EUR — BUILDING_ACCELERATION — score 6.423/10 — DETECTED_BUT_TOO_LATE
- SAPIEN-EUR — BUILDING_ACCELERATION — score 6.101/10 — DETECTED_BUT_TOO_LATE
- WIN-EUR — BUILDING_ACCELERATION — score 5.783/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- QKC-EUR — BUILDING_ACCELERATION — score 5.105/10 — DETECTED_BUT_TOO_LATE
- ZKP-EUR — BUILDING_ACCELERATION — score 5.000/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RPL-EUR — BUILDING_ACCELERATION — score 4.983/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- QUID-EUR — BUILDING_ACCELERATION — score 4.883/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- XLM-EUR — ACTIVE_NOW — score mémoire 7.764/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- AMP-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 9.834/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- 2Z-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CNPY-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- POND-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MLN-EUR — ACTIVE_NOW — score mémoire 8.477/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- EDGE-EUR — MEMORY_24H — score mémoire 8.463/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- NOM-EUR +43.56% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- LSK-EUR +33.30% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ONDO-EUR +25.48% — DETECTED_EARLY — couche NONE — action NONE
- LTC-EUR +23.02% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +21.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARX-EUR +20.37% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +19.43% — DETECTED_EARLY — couche NONE — action NONE
- PLUME-EUR +18.40% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEAQ-EUR +17.56% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XPL-EUR +16.91% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
