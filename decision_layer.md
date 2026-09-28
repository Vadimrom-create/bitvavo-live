# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T17:03:33.934139+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : XDC-EUR | action ACHETE_MAINTENANT | opportunité 8.665 | entrée 6.800 | trend 9.000 | rang 8.209
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : PEAQ-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.160 | entrée 6.400 | trend 7.550 | rang 7.235
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : IMX-EUR | action LATENT_ACCELERATOR | opportunité 7.695 | entrée 5.150 | trend 8.650 | rang 7.444
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : CRO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.221 | entrée 6.600 | trend 8.450 | rang 8.036
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. XDC-EUR — ACHETE_MAINTENANT — rank 8.209 — opportunité 8.665 — entrée 6.800 — trend 9.000

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. XDC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.209
2. CRO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.036
3. W-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.707

## Accélération indépendante

- ZEUS-EUR — CONFIRMED_ACCELERATION — score 8.844/10 — DETECTED_BUT_TOO_LATE
- WMTX-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — CONFIRMED_ACCELERATION — score 8.230/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZBT-EUR — BUILDING_ACCELERATION — score 5.201/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- IMU-EUR — MEMORY_24H — score mémoire 9.209/10 — sources ACCELERATION — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZEUS-EUR — ACTIVE_NOW — score mémoire 8.844/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — MEMORY_24H — score mémoire 8.779/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WMTX-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — WATCH_ONLY
- RECALL-EUR — MEMORY_24H — score mémoire 8.403/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — ACTIVE_NOW — score mémoire 8.230/10 — sources ACCELERATION, V4 — WATCH_ONLY
- XDC-EUR — ACTIVE_NOW — score mémoire 8.209/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY
- CRO-EUR — ACTIVE_NOW — score mémoire 8.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- HBAR-EUR +34.41% — DETECTED_EARLY — couche NONE — action NONE
- QNT-EUR +31.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IKA-EUR +15.55% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ALGO-EUR +13.33% — DETECTED_EARLY — couche NONE — action NONE
- NMR-EUR +12.64% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MON-EUR +11.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AZTEC-EUR +11.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUMP-EUR +9.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRT-EUR +9.07% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MIOTA-EUR +8.98% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
