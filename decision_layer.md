# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T16:51:14.534289+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : RENDER-EUR | action ACHETE_MAINTENANT | opportunité 8.458 | entrée 7.300 | trend 9.000 | rang 8.154
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : YGG-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.457 | entrée 6.050 | trend 8.000 | rang 7.673
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BEAM-EUR | action LATENT_ACCELERATOR | opportunité 8.285 | entrée 5.100 | trend 8.900 | rang 7.744
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : COMP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.994 | entrée 5.800 | trend 8.750 | rang 8.201
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. COMP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.201
2. RENDER-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.154
3. JUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.144

## Accélération indépendante

- ZRC-EUR — CONFIRMED_ACCELERATION — score 9.898/10 — DETECTED_BUT_TOO_LATE
- CETUS-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- PHA-EUR — CONFIRMED_ACCELERATION — score 7.573/10 — DETECTED_BUT_TOO_LATE
- MLN-EUR — BUILDING_ACCELERATION — score 6.319/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- STO-EUR — BUILDING_ACCELERATION — score 6.011/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRAC-EUR — BUILDING_ACCELERATION — score 5.727/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AERO-EUR — BUILDING_ACCELERATION — score 5.660/10 — DETECTED_BUT_TOO_LATE
- MERL-EUR — BUILDING_ACCELERATION — score 5.201/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GWEI-EUR — BUILDING_ACCELERATION — score 5.093/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — BUILDING_ACCELERATION — score 5.032/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ZRC-EUR — ACTIVE_NOW — score mémoire 9.898/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CETUS-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- COMP-EUR — ACTIVE_NOW — score mémoire 8.201/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.154/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 8.144/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AXS-EUR — ACTIVE_NOW — score mémoire 8.097/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- REQ-EUR — MEMORY_24H — score mémoire 8.033/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_DECAY_24_72H — score mémoire 8.007/10 — sources ACCELERATION — MEMORY_ONLY
- HUMA-EUR — MEMORY_24H — score mémoire 7.999/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- PHA-EUR +56.32% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- TREAD-EUR +27.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +25.84% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +25.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +19.93% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +19.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +18.56% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AERO-EUR +17.98% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SPK-EUR +17.27% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +16.28% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
