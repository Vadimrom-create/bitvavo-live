# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-30T01:47:31.159297+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SUI-EUR | action ACHETE_MAINTENANT | opportunité 8.862 | entrée 7.150 | trend 7.900 | rang 7.928
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : HUMA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.128 | entrée 5.800 | trend 8.650 | rang 7.750
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BIO-EUR | action LATENT_ACCELERATOR | opportunité 8.412 | entrée 5.250 | trend 8.200 | rang 7.480
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ALGO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.387 | entrée 7.000 | trend 8.650 | rang 8.441
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. SUI-EUR — ACHETE_MAINTENANT — rank 7.928 — opportunité 8.862 — entrée 7.150 — trend 7.900
2. AVAX-EUR — ACHETE_MAINTENANT — rank 7.888 — opportunité 8.139 — entrée 7.150 — trend 8.700
3. ICP-EUR — ACHETE_MAINTENANT — rank 7.793 — opportunité 8.572 — entrée 6.850 — trend 9.200
4. RENDER-EUR — ACHETE_MAINTENANT — rank 7.529 — opportunité 8.003 — entrée 7.000 — trend 8.150
5. RAY-EUR — ACHETE_MAINTENANT — rank 6.706 — opportunité 8.038 — entrée 6.800 — trend 5.650

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ALGO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.441
2. SUI-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.928
3. SYRUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.903

## Accélération indépendante

- RON-EUR — CONFIRMED_ACCELERATION — score 6.668/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — BUILDING_ACCELERATION — score 6.251/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- QUID-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.866/10 — sources ACCELERATION — MEMORY_ONLY
- EDGE-EUR — MEMORY_24H — score mémoire 8.544/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ALGO-EUR — ACTIVE_NOW — score mémoire 8.441/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOLV-EUR — MEMORY_24H — score mémoire 8.017/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SUI-EUR — ACTIVE_NOW — score mémoire 7.928/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SYRUP-EUR — ACTIVE_NOW — score mémoire 7.903/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AVAX-EUR — ACTIVE_NOW — score mémoire 7.888/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZIG-EUR — MEMORY_24H — score mémoire 7.836/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SOON-EUR +40.23% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MOVR-EUR +35.45% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +31.41% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- POND-EUR +31.32% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GRASS-EUR +29.25% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PUMP-EUR +23.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +18.39% — DETECTED_EARLY — couche NONE — action NONE
- INIT-EUR +18.11% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- 0G-EUR +17.58% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MEW-EUR +16.35% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

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
