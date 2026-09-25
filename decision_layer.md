# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T15:21:52.418893+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : JUP-EUR | action ACHETE_MAINTENANT | opportunité 8.414 | entrée 7.300 | trend 8.950 | rang 8.021
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : BEAM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.094 | entrée 6.000 | trend 8.900 | rang 7.794
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ALT-EUR | action LATENT_ACCELERATOR | opportunité 8.038 | entrée 5.450 | trend 8.550 | rang 7.611
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PYTH-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.010 | entrée 6.900 | trend 9.200 | rang 8.266
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. PYTH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.266
2. ICP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.039
3. JUP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.021

## Accélération indépendante

- RARE-EUR — CONFIRMED_ACCELERATION — score 9.175/10 — DETECTED_BUT_TOO_LATE
- MOVR-EUR — CONFIRMED_ACCELERATION — score 8.882/10 — DETECTED_BUT_TOO_LATE
- REQ-EUR — CONFIRMED_ACCELERATION — score 8.033/10 — DETECTED_BUT_TOO_LATE
- JTO-EUR — CONFIRMED_ACCELERATION — score 7.512/10 — DETECTED_BUT_TOO_LATE
- EDGE-EUR — CONFIRMED_ACCELERATION — score 7.475/10 — DETECTED_BUT_TOO_LATE
- JUP-EUR — CONFIRMED_ACCELERATION — score 7.382/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- C98-EUR — CONFIRMED_ACCELERATION — score 7.084/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PYTH-EUR — BUILDING_ACCELERATION — score 6.139/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GALA-EUR — BUILDING_ACCELERATION — score 5.531/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DUSK-EUR — BUILDING_ACCELERATION — score 5.300/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- JUP-EUR — ACTIVE_NOW — score mémoire 8.021/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- LDO-EUR — ACTIVE_NOW — score mémoire 7.808/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- RARE-EUR — ACTIVE_NOW — score mémoire 9.175/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- MOVR-EUR — ACTIVE_NOW — score mémoire 8.882/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.266/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.039/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- REQ-EUR — ACTIVE_NOW — score mémoire 8.033/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.986/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- OP-EUR — ACTIVE_NOW — score mémoire 7.929/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PHA-EUR +55.21% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- TREAD-EUR +44.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +26.26% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MOVR-EUR +23.20% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +21.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QNT-EUR +19.20% — DETECTED_EARLY — couche NONE — action NONE
- KMNO-EUR +18.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +17.64% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +17.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +17.29% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
