# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T15:23:12.640715+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : IMX-EUR | action LATENT_ACCELERATOR | opportunité 7.613 | entrée 4.950 | trend 8.450 | rang 7.378
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : XDC-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.946 | entrée 6.850 | trend 9.000 | rang 7.899
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. XDC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.899
2. MIOTA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.676
3. KAS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.420

## Accélération indépendante

- SOON-EUR — CONFIRMED_ACCELERATION — score 9.150/10 — DETECTED_BUT_TOO_LATE
- PUFFER-EUR — CONFIRMED_ACCELERATION — score 7.479/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IKA-EUR — CONFIRMED_ACCELERATION — score 6.594/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DGB-EUR — BUILDING_ACCELERATION — score 6.478/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WMTX-EUR — BUILDING_ACCELERATION — score 5.735/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- JUP-EUR — BUILDING_ACCELERATION — score 5.464/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FLOCK-EUR — BUILDING_ACCELERATION — score 5.396/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZKJ-EUR — BUILDING_ACCELERATION — score 5.273/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HEI-EUR — BUILDING_ACCELERATION — score 5.237/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARX-EUR — BUILDING_ACCELERATION — score 5.163/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- BTT-EUR — MEMORY_24H — score mémoire 9.434/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 9.209/10 — sources ACCELERATION — MEMORY_ONLY
- SOON-EUR — ACTIVE_NOW — score mémoire 9.150/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — MEMORY_24H — score mémoire 8.779/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY
- XDC-EUR — ACTIVE_NOW — score mémoire 7.899/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FRAX-EUR — MEMORY_DECAY_24_72H — score mémoire 7.751/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MIOTA-EUR — ACTIVE_NOW — score mémoire 7.676/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XLM-EUR — MEMORY_24H — score mémoire 7.592/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 7.582/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +32.30% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HBAR-EUR +24.66% — DETECTED_EARLY — couche NONE — action NONE
- SOON-EUR +18.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NMR-EUR +17.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AZTEC-EUR +13.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALGO-EUR +11.76% — DETECTED_EARLY — couche NONE — action NONE
- IKA-EUR +11.38% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- GRT-EUR +8.42% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MIOTA-EUR +7.92% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MON-EUR +7.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
