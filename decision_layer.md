# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T15:43:34.615814+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : XDC-EUR | action ACHETE_MAINTENANT | opportunité 8.355 | entrée 6.900 | trend 9.000 | rang 8.054
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SEI-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.688 | entrée 6.250 | trend 8.600 | rang 7.337
  - Strong structure but imperfect current entry; prefer passive execution. High extension/chase reduces rank but does not erase the setup.
- **MEILLEUR_LATENT_ACCELERATOR** : ZRO-EUR | action LATENT_ACCELERATOR | opportunité 8.018 | entrée 5.500 | trend 7.550 | rang 7.066
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MIOTA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.975 | entrée 7.050 | trend 8.550 | rang 7.770
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. XDC-EUR — ACHETE_MAINTENANT — rank 8.054 — opportunité 8.355 — entrée 6.900 — trend 9.000
2. ALGO-EUR — ACHETE_MAINTENANT — rank 7.370 — opportunité 8.084 — entrée 6.850 — trend 8.900

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. XDC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.054
2. MIOTA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.770
3. LINK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.673

## Accélération indépendante

- ZRO-EUR — CONFIRMED_ACCELERATION — score 9.578/10 — DETECTED_BUT_TOO_LATE
- U-EUR — CONFIRMED_ACCELERATION — score 7.773/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — CONFIRMED_ACCELERATION — score 7.606/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CVX-EUR — CONFIRMED_ACCELERATION — score 6.918/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HBAR-EUR — BUILDING_ACCELERATION — score 6.463/10 — DETECTED_BUT_TOO_LATE
- GRT-EUR — BUILDING_ACCELERATION — score 6.462/10 — DETECTED_BUT_TOO_LATE
- IKA-EUR — BUILDING_ACCELERATION — score 5.886/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HFT-EUR — BUILDING_ACCELERATION — score 5.513/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KITE-EUR — BUILDING_ACCELERATION — score 5.513/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BOME-EUR — BUILDING_ACCELERATION — score 5.245/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ZRO-EUR — ACTIVE_NOW — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- BTT-EUR — MEMORY_24H — score mémoire 9.434/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 9.209/10 — sources ACCELERATION — MEMORY_ONLY
- SOON-EUR — MEMORY_24H — score mémoire 9.150/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.779/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY
- XDC-EUR — ACTIVE_NOW — score mémoire 8.054/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- U-EUR — ACTIVE_NOW — score mémoire 7.773/10 — sources ACCELERATION, V4 — WATCH_ONLY
- MIOTA-EUR — ACTIVE_NOW — score mémoire 7.770/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FRAX-EUR — MEMORY_DECAY_24_72H — score mémoire 7.691/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- HBAR-EUR +32.09% — DETECTED_EARLY — couche NONE — action NONE
- QNT-EUR +22.46% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IKA-EUR +15.56% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- AZTEC-EUR +14.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALGO-EUR +13.80% — DETECTED_EARLY — couche NONE — action NONE
- NMR-EUR +13.02% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRT-EUR +11.50% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MON-EUR +9.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XDC-EUR +8.55% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MIOTA-EUR +7.27% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
