# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T16:26:56.813650+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : XDC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.014 | entrée 5.800 | trend 9.000 | rang 7.862
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : NMR-EUR | action LATENT_ACCELERATOR | opportunité 7.482 | entrée 5.450 | trend 8.300 | rang 6.810
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PYTH-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.196 | entrée 6.200 | trend 8.650 | rang 7.804
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. XDC-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.862
2. PYTH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.804
3. RUNE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.757

## Accélération indépendante

- PUMP-EUR — CONFIRMED_ACCELERATION — score 8.750/10 — DETECTED_BUT_TOO_LATE
- BTT-EUR — CONFIRMED_ACCELERATION — score 8.582/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RECALL-EUR — CONFIRMED_ACCELERATION — score 8.403/10 — DETECTED_BUT_TOO_LATE
- AZTEC-EUR — CONFIRMED_ACCELERATION — score 8.383/10 — DETECTED_BUT_TOO_LATE
- QNT-EUR — CONFIRMED_ACCELERATION — score 7.239/10 — DETECTED_BUT_TOO_LATE
- MET-EUR — CONFIRMED_ACCELERATION — score 7.145/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PARTI-EUR — CONFIRMED_ACCELERATION — score 7.000/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- 0G-EUR — CONFIRMED_ACCELERATION — score 6.965/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- JTO-EUR — CONFIRMED_ACCELERATION — score 6.826/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VIRTUAL-EUR — CONFIRMED_ACCELERATION — score 6.823/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- IMU-EUR — MEMORY_24H — score mémoire 9.209/10 — sources ACCELERATION — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.779/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PUMP-EUR — ACTIVE_NOW — score mémoire 8.750/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- BTT-EUR — ACTIVE_NOW — score mémoire 8.582/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RECALL-EUR — ACTIVE_NOW — score mémoire 8.403/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AZTEC-EUR — ACTIVE_NOW — score mémoire 8.383/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY
- XDC-EUR — ACTIVE_NOW — score mémoire 7.862/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 7.804/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- HBAR-EUR +34.75% — DETECTED_EARLY — couche NONE — action NONE
- QNT-EUR +23.60% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AZTEC-EUR +21.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IKA-EUR +19.18% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ALGO-EUR +15.45% — DETECTED_EARLY — couche NONE — action NONE
- MON-EUR +13.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NMR-EUR +12.17% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PUMP-EUR +11.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRT-EUR +9.60% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MIOTA-EUR +8.67% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
