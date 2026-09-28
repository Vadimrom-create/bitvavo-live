# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T17:24:30.677728+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : XDC-EUR | action ACHETE_MAINTENANT | opportunité 8.740 | entrée 7.100 | trend 9.000 | rang 8.190
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : NMR-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.546 | entrée 6.650 | trend 8.450 | rang 7.062
  - Strong structure but imperfect current entry; prefer passive execution. High extension/chase reduces rank but does not erase the setup.
- **MEILLEUR_LATENT_ACCELERATOR** : IMX-EUR | action LATENT_ACCELERATOR | opportunité 7.471 | entrée 4.950 | trend 8.650 | rang 7.328
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MIOTA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.774 | entrée 6.200 | trend 9.200 | rang 8.120
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. XDC-EUR — ACHETE_MAINTENANT — rank 8.190 — opportunité 8.740 — entrée 7.100 — trend 9.000

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. XDC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.190
2. MIOTA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.120
3. LINK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.834

## Accélération indépendante

- SWEAT-EUR — CONFIRMED_ACCELERATION — score 7.366/10 — DETECTED_BUT_TOO_LATE
- PEOPLE-EUR — CONFIRMED_ACCELERATION — score 6.878/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GMX-EUR — CONFIRMED_ACCELERATION — score 6.729/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DIA-EUR — BUILDING_ACCELERATION — score 6.222/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WIN-EUR — BUILDING_ACCELERATION — score 6.166/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SKY-EUR — BUILDING_ACCELERATION — score 5.838/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CVX-EUR — BUILDING_ACCELERATION — score 5.736/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IKA-EUR — BUILDING_ACCELERATION — score 5.610/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BRETT-EUR — BUILDING_ACCELERATION — score 5.497/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LMWR-EUR — BUILDING_ACCELERATION — score 5.199/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- IMU-EUR — MEMORY_24H — score mémoire 9.209/10 — sources ACCELERATION — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.844/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.779/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WMTX-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RECALL-EUR — MEMORY_24H — score mémoire 8.403/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 8.230/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XDC-EUR — ACTIVE_NOW — score mémoire 8.190/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MIOTA-EUR — ACTIVE_NOW — score mémoire 8.120/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- HBAR-EUR +35.93% — DETECTED_EARLY — couche NONE — action NONE
- QNT-EUR +33.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALGO-EUR +15.64% — DETECTED_EARLY — couche NONE — action NONE
- IKA-EUR +13.11% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- NMR-EUR +11.79% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MIOTA-EUR +10.90% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MON-EUR +10.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUMP-EUR +9.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LINK-EUR +8.71% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRT-EUR +8.63% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
