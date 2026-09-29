# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T21:56:29.343312+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ZRO-EUR | action ACHETE_MAINTENANT | opportunité 8.854 | entrée 6.950 | trend 8.150 | rang 7.902
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SKY-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.970 | entrée 5.800 | trend 9.000 | rang 7.797
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ARX-EUR | action LATENT_ACCELERATOR | opportunité 8.336 | entrée 5.650 | trend 8.250 | rang 7.708
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SYRUP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.791 | entrée 7.250 | trend 9.000 | rang 8.335
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ZRO-EUR — ACHETE_MAINTENANT — rank 7.902 — opportunité 8.854 — entrée 6.950 — trend 8.150
2. AAVE-EUR — ACHETE_MAINTENANT — rank 7.696 — opportunité 8.295 — entrée 8.050 — trend 8.900

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. SYRUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.335
2. ETHFI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.008
3. LINK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.937

## Accélération indépendante

- SYRUP-EUR — BUILDING_ACCELERATION — score 5.269/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRB-EUR — BUILDING_ACCELERATION — score 5.249/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ZRO-EUR — ACTIVE_NOW — score mémoire 7.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- GIGA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- POND-EUR — MEMORY_24H — score mémoire 9.160/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.866/10 — sources ACCELERATION — MEMORY_ONLY
- SYRUP-EUR — ACTIVE_NOW — score mémoire 8.335/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WMTX-EUR — MEMORY_24H — score mémoire 8.145/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MOVR-EUR — MEMORY_24H — score mémoire 8.020/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SOLV-EUR — MEMORY_24H — score mémoire 8.017/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- POND-EUR +29.36% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GRASS-EUR +28.44% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MOVR-EUR +27.08% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- 0G-EUR +21.92% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +19.15% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZBCN-EUR +18.21% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PUMP-EUR +17.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +15.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICP-EUR +15.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AAVE-EUR +14.36% — DETECTED_EARLY — couche NONE — action NONE

## Gestion des positions détenues

Policy : STAGED_10_20_RUNNER_V1
- +10% : prise partielle 35%.
- +20% : seconde prise 35%.
- Runner conservé : 30%.
- Revue coût d'opportunité après 72 h ; sortie seulement avant la première partielle, proche/sous le PRU et avec momentum 15m affaibli.
- Pas de stop serré mécaniquement après une petite hausse ; le stop reste lié à l'invalidation structurelle.

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
