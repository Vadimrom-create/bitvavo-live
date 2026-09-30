# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-30T04:24:33.761085+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : WLD-EUR | action ACHETE_MAINTENANT | opportunité 8.737 | entrée 7.400 | trend 7.900 | rang 7.953
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AZTEC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.583 | entrée 6.700 | trend 7.500 | rang 7.410
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ALICE-EUR | action LATENT_ACCELERATOR | opportunité 8.252 | entrée 5.650 | trend 8.550 | rang 7.747
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SYRUP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.719 | entrée 6.250 | trend 8.450 | rang 8.043
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. WLD-EUR — ACHETE_MAINTENANT — rank 7.953 — opportunité 8.737 — entrée 7.400 — trend 7.900
2. RENDER-EUR — ACHETE_MAINTENANT — rank 7.832 — opportunité 8.417 — entrée 7.750 — trend 7.950

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. SYRUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.043
2. ALGO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.957
3. WLD-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.953

## Accélération indépendante

- ICX-EUR — CONFIRMED_ACCELERATION — score 9.062/10 — DETECTED_BUT_TOO_LATE
- QUID-EUR — CONFIRMED_ACCELERATION — score 8.702/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- 0G-EUR — CONFIRMED_ACCELERATION — score 8.250/10 — DETECTED_BUT_TOO_LATE
- NOM-EUR — CONFIRMED_ACCELERATION — score 7.520/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BABY-EUR — CONFIRMED_ACCELERATION — score 6.608/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRO-EUR — CONFIRMED_ACCELERATION — score 6.593/10 — DETECTED_BUT_TOO_LATE
- WOO-EUR — BUILDING_ACCELERATION — score 6.267/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- 2Z-EUR — BUILDING_ACCELERATION — score 6.075/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EPIC-EUR — BUILDING_ACCELERATION — score 5.865/10 — DETECTED_BUT_TOO_LATE
- CAKE-EUR — BUILDING_ACCELERATION — score 5.396/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- DEEP-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZBCN-EUR — MEMORY_24H — score mémoire 9.934/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — ACTIVE_NOW — score mémoire 9.062/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.866/10 — sources ACCELERATION — MEMORY_ONLY
- QUID-EUR — ACTIVE_NOW — score mémoire 8.702/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- POND-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- 0G-EUR — ACTIVE_NOW — score mémoire 8.250/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SYRUP-EUR — ACTIVE_NOW — score mémoire 8.043/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOLV-EUR — MEMORY_24H — score mémoire 8.017/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SOON-EUR +37.62% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- POND-EUR +35.97% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MOVR-EUR +35.32% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZBCN-EUR +28.97% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MEW-EUR +20.71% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRO-EUR +18.98% — DETECTED_EARLY — couche NONE — action NONE
- QNT-EUR +18.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUMP-EUR +18.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INIT-EUR +17.24% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- 0G-EUR +14.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
