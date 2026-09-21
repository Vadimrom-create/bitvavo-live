# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T09:36:16.594747+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : INJ-EUR | action ACHETE_MAINTENANT | opportunité 9.311 | entrée 8.300 | trend 8.300 | rang 8.342
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ARX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.367 | entrée 5.900 | trend 8.900 | rang 8.197
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SENT-EUR | action LATENT_ACCELERATOR | opportunité 8.031 | entrée 4.500 | trend 8.700 | rang 7.452
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : WAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.664 | entrée 6.750 | trend 8.950 | rang 8.156
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. INJ-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.342
2. ARX-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 8.197
3. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.156

## Accélération indépendante

- PHA-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- BONK-EUR — CONFIRMED_ACCELERATION — score 8.784/10 — DETECTED_BUT_TOO_LATE
- SHELL-EUR — CONFIRMED_ACCELERATION — score 8.709/10 — DETECTED_BUT_TOO_LATE
- PONKE-EUR — CONFIRMED_ACCELERATION — score 8.317/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZAMA-EUR — CONFIRMED_ACCELERATION — score 8.219/10 — DETECTED_BUT_TOO_LATE
- WELL-EUR — CONFIRMED_ACCELERATION — score 7.629/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- METIS-EUR — CONFIRMED_ACCELERATION — score 7.334/10 — DETECTED_BUT_TOO_LATE
- AEVO-EUR — CONFIRMED_ACCELERATION — score 7.193/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SYN-EUR — CONFIRMED_ACCELERATION — score 6.881/10 — DETECTED_BUT_TOO_LATE
- ANKR-EUR — CONFIRMED_ACCELERATION — score 6.871/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- PEPE-EUR — ACTIVE_NOW — score mémoire 7.480/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- XPL-EUR — ACTIVE_NOW — score mémoire 6.896/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- PHA-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- EDGE-EUR — MEMORY_24H — score mémoire 9.925/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZETA-EUR — MEMORY_24H — score mémoire 9.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NOS-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BONK-EUR — ACTIVE_NOW — score mémoire 8.784/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- RON-EUR — MEMORY_24H — score mémoire 8.709/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SHELL-EUR — ACTIVE_NOW — score mémoire 8.709/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- MOCA-EUR — MEMORY_24H — score mémoire 8.589/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZETA-EUR +73.41% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PHA-EUR +56.36% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PTB-EUR +54.05% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NIL-EUR +38.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +32.40% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FTT-EUR +29.84% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- KMNO-EUR +28.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEAQ-EUR +27.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +25.15% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DRIFT-EUR +24.80% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
