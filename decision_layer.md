# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T22:16:52.991610+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SYRUP-EUR | action ACHETE_MAINTENANT | opportunité 8.283 | entrée 7.150 | trend 9.000 | rang 8.091
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : C-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.561 | entrée 6.050 | trend 8.250 | rang 7.403
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : W-EUR | action LATENT_ACCELERATOR | opportunité 7.410 | entrée 4.500 | trend 8.400 | rang 7.213
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SKY-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.366 | entrée 6.350 | trend 9.000 | rang 8.020
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. SYRUP-EUR — ACHETE_MAINTENANT — rank 8.091 — opportunité 8.283 — entrée 7.150 — trend 9.000
2. ZRO-EUR — ACHETE_MAINTENANT — rank 7.687 — opportunité 8.350 — entrée 6.950 — trend 8.150
3. AAVE-EUR — ACHETE_MAINTENANT — rank 7.617 — opportunité 7.945 — entrée 8.100 — trend 8.900
4. XLM-EUR — ACHETE_MAINTENANT — rank 7.509 — opportunité 8.136 — entrée 7.350 — trend 7.700

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. SYRUP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.091
2. SKY-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.020
3. ROSE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.854

## Accélération indépendante

- PHA-EUR — CONFIRMED_ACCELERATION — score 9.363/10 — DETECTED_BUT_TOO_LATE
- ZBCN-EUR — CONFIRMED_ACCELERATION — score 7.651/10 — DETECTED_BUT_TOO_LATE
- MERL-EUR — CONFIRMED_ACCELERATION — score 6.931/10 — DETECTED_BUT_TOO_LATE
- GIGA-EUR — CONFIRMED_ACCELERATION — score 6.554/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LMWR-EUR — CONFIRMED_ACCELERATION — score 6.526/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GLMR-EUR — BUILDING_ACCELERATION — score 5.807/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LQTY-EUR — BUILDING_ACCELERATION — score 5.055/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- PHA-EUR — ACTIVE_NOW — score mémoire 9.363/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- POND-EUR — MEMORY_24H — score mémoire 9.160/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.866/10 — sources ACCELERATION — MEMORY_ONLY
- WMTX-EUR — MEMORY_24H — score mémoire 8.145/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SYRUP-EUR — ACTIVE_NOW — score mémoire 8.091/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SKY-EUR — ACTIVE_NOW — score mémoire 8.020/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MOVR-EUR — MEMORY_24H — score mémoire 8.020/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SOLV-EUR — MEMORY_24H — score mémoire 8.017/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- POND-EUR +33.07% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GRASS-EUR +30.30% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MOVR-EUR +23.80% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZBCN-EUR +22.85% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PHA-EUR +21.79% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 0G-EUR +21.70% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +18.82% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PUMP-EUR +18.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FUEL-EUR +15.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XDP-EUR +15.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
