# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T14:41:57.014877+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : JUP-EUR | action ACHETE_MAINTENANT | opportunité 9.318 | entrée 8.000 | trend 8.950 | rang 8.629
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : GRT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.753 | entrée 6.450 | trend 8.550 | rang 7.658
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : TIA-EUR | action LATENT_ACCELERATOR | opportunité 7.617 | entrée 4.500 | trend 8.400 | rang 7.308
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AXS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.283 | entrée 7.800 | trend 8.750 | rang 8.282
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. JUP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.629
2. AXS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.282
3. PYTH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.212

## Accélération indépendante

- MOVR-EUR — CONFIRMED_ACCELERATION — score 8.965/10 — DETECTED_BUT_TOO_LATE
- AERO-EUR — CONFIRMED_ACCELERATION — score 8.140/10 — DETECTED_BUT_TOO_LATE
- AXS-EUR — CONFIRMED_ACCELERATION — score 6.989/10 — DETECTED_BUT_TOO_LATE
- BIO-EUR — CONFIRMED_ACCELERATION — score 6.881/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- STO-EUR — CONFIRMED_ACCELERATION — score 6.796/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VET-EUR — CONFIRMED_ACCELERATION — score 6.610/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — CONFIRMED_ACCELERATION — score 6.537/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HAEDAL-EUR — BUILDING_ACCELERATION — score 6.352/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TREAD-EUR — BUILDING_ACCELERATION — score 6.207/10 — DETECTED_BUT_TOO_LATE
- GLMR-EUR — BUILDING_ACCELERATION — score 5.883/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- MOVR-EUR — ACTIVE_NOW — score mémoire 8.965/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- JUP-EUR — ACTIVE_NOW — score mémoire 8.629/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AXS-EUR — ACTIVE_NOW — score mémoire 8.282/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.212/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 8.179/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 8.140/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ICP-EUR — ACTIVE_NOW — score mémoire 8.071/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- OP-EUR — ACTIVE_NOW — score mémoire 8.044/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 8.042/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PHA-EUR +53.87% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- TREAD-EUR +41.02% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +25.54% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DBR-EUR +19.48% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +17.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +16.47% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHIP-EUR +16.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QNT-EUR +16.10% — DETECTED_EARLY — couche NONE — action NONE
- NIL-EUR +15.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XPL-EUR +14.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
