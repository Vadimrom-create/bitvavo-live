# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-30T00:47:19.599700+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ICP-EUR | action ACHETE_MAINTENANT | opportunité 8.414 | entrée 7.450 | trend 9.200 | rang 7.947
  - V4 buy-ready with acceptable current entry; no structural veto. High extension/chase is retained as risk context, not an automatic veto.
- **MEILLEURE_LIMITE_PASSIVE** : COMP-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.885 | entrée 5.950 | trend 8.650 | rang 7.635
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : DEEP-EUR | action LATENT_ACCELERATOR | opportunité 7.563 | entrée 5.750 | trend 8.150 | rang 7.304
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SYRUP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.280 | entrée 6.500 | trend 9.000 | rang 8.036
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ICP-EUR — ACHETE_MAINTENANT — rank 7.947 — opportunité 8.414 — entrée 7.450 — trend 9.200

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. SYRUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.036
2. ICP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.947
3. ALICE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.821

## Accélération indépendante

- ZRO-EUR — CONFIRMED_ACCELERATION — score 8.323/10 — DETECTED_BUT_TOO_LATE
- SYRUP-EUR — CONFIRMED_ACCELERATION — score 6.804/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LIGHTER-EUR — BUILDING_ACCELERATION — score 6.352/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NEAR-EUR — BUILDING_ACCELERATION — score 6.066/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FOLD-EUR — BUILDING_ACCELERATION — score 5.431/10 — DETECTED_BUT_TOO_LATE
- SQD-EUR — BUILDING_ACCELERATION — score 5.135/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- JUP-EUR — BUILDING_ACCELERATION — score 4.830/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICP-EUR — BUILDING_ACCELERATION — score 4.799/10 — DETECTED_BUT_TOO_LATE
- POWR-EUR — BUILDING_ACCELERATION — score 4.777/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- QUID-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.866/10 — sources ACCELERATION — MEMORY_ONLY
- MEW-EUR — MEMORY_24H — score mémoire 8.720/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- EDGE-EUR — MEMORY_24H — score mémoire 8.544/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TOSHI-EUR — MEMORY_24H — score mémoire 8.433/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRO-EUR — ACTIVE_NOW — score mémoire 8.323/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SYRUP-EUR — ACTIVE_NOW — score mémoire 8.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOLV-EUR — MEMORY_24H — score mémoire 8.017/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.947/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- SOON-EUR +41.86% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MOVR-EUR +31.77% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- POND-EUR +31.06% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GRASS-EUR +24.68% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +18.20% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PUMP-EUR +17.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +17.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TRIA-EUR +15.87% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ZBCN-EUR +15.44% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- INIT-EUR +15.39% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

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
