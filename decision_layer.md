# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T09:22:03.492241+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : DOT-EUR | action ACHETE_MAINTENANT | opportunité 9.238 | entrée 7.450 | trend 8.000 | rang 8.081
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ETHFI-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.616 | entrée 6.100 | trend 8.550 | rang 7.910
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : WAL-EUR | action LATENT_ACCELERATOR | opportunité 8.062 | entrée 4.500 | trend 8.950 | rang 7.583
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PENDLE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.724 | entrée 6.350 | trend 8.950 | rang 8.135
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. PENDLE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.135
2. DOT-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.081
3. ALGO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.039

## Accélération indépendante

- EDGE-EUR — CONFIRMED_ACCELERATION — score 9.925/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- UNI-EUR — CONFIRMED_ACCELERATION — score 8.751/10 — DETECTED_BUT_TOO_LATE
- RON-EUR — CONFIRMED_ACCELERATION — score 8.709/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WIN-EUR — CONFIRMED_ACCELERATION — score 8.139/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PTB-EUR — CONFIRMED_ACCELERATION — score 7.806/10 — DETECTED_BUT_TOO_LATE
- XMN-EUR — CONFIRMED_ACCELERATION — score 7.639/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CRO-EUR — CONFIRMED_ACCELERATION — score 7.629/10 — DETECTED_BUT_TOO_LATE
- PHA-EUR — CONFIRMED_ACCELERATION — score 7.625/10 — DETECTED_BUT_TOO_LATE
- A-EUR — CONFIRMED_ACCELERATION — score 6.729/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FLOCK-EUR — CONFIRMED_ACCELERATION — score 6.673/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PEPE-EUR — ACTIVE_NOW — score mémoire 7.580/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- XLM-EUR — ACTIVE_NOW — score mémoire 7.304/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- EDGE-EUR — ACTIVE_NOW — score mémoire 9.925/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 9.245/10 — sources ACCELERATION — MEMORY_ONLY
- ZETA-EUR — MEMORY_24H — score mémoire 9.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 9.049/10 — sources ACCELERATION — MEMORY_ONLY
- NOS-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- UNI-EUR — ACTIVE_NOW — score mémoire 8.751/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- RON-EUR — ACTIVE_NOW — score mémoire 8.709/10 — sources ACCELERATION, V4 — WATCH_ONLY
- MOCA-EUR — MEMORY_24H — score mémoire 8.589/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZETA-EUR +74.67% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PTB-EUR +60.77% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NIL-EUR +34.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +33.02% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +29.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +29.39% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PHA-EUR +28.41% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEAQ-EUR +26.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +24.85% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUI-EUR +22.45% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
