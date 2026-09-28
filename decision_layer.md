# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T14:58:51.293518+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : SEI-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.585 | entrée 6.050 | trend 8.600 | rang 7.310
  - Strong structure but imperfect current entry; prefer passive execution. High extension/chase reduces rank but does not erase the setup.
- **MEILLEUR_LATENT_ACCELERATOR** : AVNT-EUR | action LATENT_ACCELERATOR | opportunité 8.336 | entrée 5.550 | trend 7.400 | rang 7.405
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : KAS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.563 | entrée 6.050 | trend 8.300 | rang 7.893
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. KAS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.893
2. XDC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.808
3. W-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.670

## Accélération indépendante

- METIS-EUR — BUILDING_ACCELERATION — score 5.237/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SAGA-EUR — BUILDING_ACCELERATION — score 4.920/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FLOCK-EUR — BUILDING_ACCELERATION — score 4.805/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- WMTX-EUR — MEMORY_24H — score mémoire 9.914/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 9.434/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 9.209/10 — sources ACCELERATION — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.779/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.893/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FRAX-EUR — MEMORY_DECAY_24_72H — score mémoire 7.822/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XDC-EUR — ACTIVE_NOW — score mémoire 7.808/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MON-EUR — ACTIVE_NOW — score mémoire 7.701/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GRAM-EUR — MEMORY_24H — score mémoire 7.683/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- QNT-EUR +36.68% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HBAR-EUR +26.55% — DETECTED_EARLY — couche NONE — action NONE
- NMR-EUR +16.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AZTEC-EUR +12.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALGO-EUR +10.21% — DETECTED_EARLY — couche NONE — action NONE
- GRT-EUR +9.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IKA-EUR +9.37% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- XDC-EUR +8.92% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +8.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INIT-EUR +6.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
