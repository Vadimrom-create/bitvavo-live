# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T22:58:50.318547+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : ROSE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.521 | entrée 5.950 | trend 8.950 | rang 8.096
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : GALA-EUR | action LATENT_ACCELERATOR | opportunité 8.869 | entrée 5.350 | trend 8.700 | rang 8.094
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AAVE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.620 | entrée 6.500 | trend 9.000 | rang 8.225
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.225
2. RENDER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.161
3. ROSE-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 8.096

## Accélération indépendante

- AIXBT-EUR — CONFIRMED_ACCELERATION — score 9.605/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- QNT-EUR — CONFIRMED_ACCELERATION — score 8.429/10 — DETECTED_BUT_TOO_LATE
- IMX-EUR — CONFIRMED_ACCELERATION — score 8.274/10 — DETECTED_BUT_TOO_LATE
- ACH-EUR — CONFIRMED_ACCELERATION — score 7.893/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WOO-EUR — CONFIRMED_ACCELERATION — score 7.008/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GLMR-EUR — BUILDING_ACCELERATION — score 6.079/10 — DETECTED_BUT_TOO_LATE
- RARE-EUR — BUILDING_ACCELERATION — score 6.026/10 — DETECTED_BUT_TOO_LATE
- WMTX-EUR — BUILDING_ACCELERATION — score 4.795/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- AIXBT-EUR — ACTIVE_NOW — score mémoire 9.605/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.458/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- QNT-EUR — ACTIVE_NOW — score mémoire 8.429/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- IMX-EUR — ACTIVE_NOW — score mémoire 8.274/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.225/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 8.170/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.161/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- QNT-EUR +125.76% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +42.66% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INX-EUR +33.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRT-EUR +25.98% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +21.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- W-EUR +19.73% — DETECTED_EARLY — couche NONE — action NONE
- PUMP-EUR +16.31% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +15.31% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- AUDIO-EUR +14.29% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IMX-EUR +14.27% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
