# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T22:29:17.658441+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 9.085 | entrée 7.800 | trend 8.650 | rang 8.359
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ZK-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.500 | entrée 5.850 | trend 8.950 | rang 8.044
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : GRT-EUR | action LATENT_ACCELERATOR | opportunité 8.037 | entrée 5.550 | trend 8.850 | rang 7.619
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PYTH-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.433 | entrée 7.850 | trend 9.200 | rang 8.652
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. PYTH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.652
2. LTC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.359
3. PLUME-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.243

## Accélération indépendante

- WMTX-EUR — CONFIRMED_ACCELERATION — score 7.594/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TREAD-EUR — CONFIRMED_ACCELERATION — score 7.357/10 — DETECTED_BUT_TOO_LATE
- PYTH-EUR — CONFIRMED_ACCELERATION — score 7.169/10 — DETECTED_BUT_TOO_LATE
- CHIP-EUR — CONFIRMED_ACCELERATION — score 7.075/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AVNT-EUR — CONFIRMED_ACCELERATION — score 6.594/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LMWR-EUR — BUILDING_ACCELERATION — score 6.063/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ROSE-EUR — BUILDING_ACCELERATION — score 5.750/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CETUS-EUR — BUILDING_ACCELERATION — score 5.449/10 — DETECTED_BUT_TOO_LATE
- POPCAT-EUR — BUILDING_ACCELERATION — score 5.411/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SENT-EUR — BUILDING_ACCELERATION — score 5.387/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PHA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 8.667/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.652/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LTC-EUR — ACTIVE_NOW — score mémoire 8.359/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PLUME-EUR — ACTIVE_NOW — score mémoire 8.243/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- HFT-EUR — MEMORY_24H — score mémoire 8.111/10 — sources ACCELERATION — MEMORY_ONLY
- MANA-EUR — ACTIVE_NOW — score mémoire 8.106/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 8.094/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- DATAIP-EUR — ACTIVE_NOW — score mémoire 8.075/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PHA-EUR +83.86% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ARK-EUR +23.34% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AERO-EUR +22.16% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +21.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SEI-EUR +20.65% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUI-EUR +18.72% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DEEP-EUR +18.24% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ENA-EUR +17.64% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +16.18% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +16.11% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
