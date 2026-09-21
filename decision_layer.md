# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T09:42:37.705624+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : INJ-EUR | action ACHETE_MAINTENANT | opportunité 9.288 | entrée 8.150 | trend 8.300 | rang 8.313
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ARX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.367 | entrée 5.900 | trend 8.900 | rang 8.197
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : COW-EUR | action LATENT_ACCELERATOR | opportunité 8.189 | entrée 4.500 | trend 8.950 | rang 7.638
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AIOZ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.184 | entrée 7.350 | trend 8.850 | rang 8.222
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. INJ-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.313
2. AIOZ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.222
3. ARX-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 8.197

## Accélération indépendante

- PORTAL-EUR — CONFIRMED_ACCELERATION — score 9.136/10 — DETECTED_BUT_TOO_LATE
- ZAMA-EUR — CONFIRMED_ACCELERATION — score 9.107/10 — DETECTED_BUT_TOO_LATE
- PHA-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- METIS-EUR — CONFIRMED_ACCELERATION — score 7.675/10 — DETECTED_BUT_TOO_LATE
- CTC-EUR — CONFIRMED_ACCELERATION — score 7.528/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DOGE-EUR — CONFIRMED_ACCELERATION — score 7.274/10 — DETECTED_BUT_TOO_LATE
- PEOPLE-EUR — CONFIRMED_ACCELERATION — score 7.271/10 — DETECTED_BUT_TOO_LATE
- LAPTOP-EUR — CONFIRMED_ACCELERATION — score 7.269/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BONK-EUR — CONFIRMED_ACCELERATION — score 6.972/10 — DETECTED_BUT_TOO_LATE
- PENGU-EUR — CONFIRMED_ACCELERATION — score 6.557/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EIGEN-EUR — ACTIVE_NOW — score mémoire 7.710/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- LINK-EUR — ACTIVE_NOW — score mémoire 7.378/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- EDGE-EUR — MEMORY_24H — score mémoire 9.925/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PORTAL-EUR — ACTIVE_NOW — score mémoire 9.136/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ZAMA-EUR — ACTIVE_NOW — score mémoire 9.107/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ZETA-EUR — MEMORY_24H — score mémoire 9.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NOS-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RON-EUR — MEMORY_24H — score mémoire 8.709/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SHELL-EUR — MEMORY_24H — score mémoire 8.709/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MOCA-EUR — MEMORY_24H — score mémoire 8.589/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZETA-EUR +72.37% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PTB-EUR +54.95% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PHA-EUR +50.75% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +38.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +30.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +28.86% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +28.31% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEAQ-EUR +27.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +24.32% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DRIFT-EUR +23.81% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
