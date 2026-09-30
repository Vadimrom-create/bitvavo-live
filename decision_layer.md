# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-30T02:02:56.983995+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : CRV-EUR | action ACHETE_MAINTENANT | opportunité 9.249 | entrée 7.500 | trend 8.050 | rang 8.089
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ROSE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.995 | entrée 5.850 | trend 8.400 | rang 7.954
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ALICE-EUR | action LATENT_ACCELERATOR | opportunité 7.460 | entrée 4.500 | trend 8.700 | rang 7.245
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ALGO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.195 | entrée 6.500 | trend 8.650 | rang 7.832
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. CRV-EUR — ACHETE_MAINTENANT — rank 8.089 — opportunité 9.249 — entrée 7.500 — trend 8.050
2. ICP-EUR — ACHETE_MAINTENANT — rank 7.783 — opportunité 8.636 — entrée 7.150 — trend 9.200
3. RENDER-EUR — ACHETE_MAINTENANT — rank 7.597 — opportunité 8.093 — entrée 7.000 — trend 8.150
4. SUI-EUR — ACHETE_MAINTENANT — rank 7.417 — opportunité 7.782 — entrée 6.900 — trend 7.900
5. SHIB-EUR — ACHETE_MAINTENANT — rank 7.014 — opportunité 8.369 — entrée 7.000 — trend 6.250

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. CRV-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.089
2. ROSE-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.954
3. ALGO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.832

## Accélération indépendante

- MEW-EUR — CONFIRMED_ACCELERATION — score 9.654/10 — DETECTED_BUT_TOO_LATE
- DYDX-EUR — BUILDING_ACCELERATION — score 5.997/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NIL-EUR — BUILDING_ACCELERATION — score 5.505/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LISTA-EUR — BUILDING_ACCELERATION — score 5.484/10 — DETECTED_BUT_TOO_LATE
- RECALL-EUR — BUILDING_ACCELERATION — score 5.114/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TOSHI-EUR — BUILDING_ACCELERATION — score 4.964/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WIF-EUR — BUILDING_ACCELERATION — score 4.847/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CRV-EUR — BUILDING_ACCELERATION — score 4.831/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CRV-EUR — ACTIVE_NOW — score mémoire 8.089/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- MEW-EUR — ACTIVE_NOW — score mémoire 9.654/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- QUID-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.866/10 — sources ACCELERATION — MEMORY_ONLY
- EDGE-EUR — MEMORY_24H — score mémoire 8.544/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SOLV-EUR — MEMORY_24H — score mémoire 8.017/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ROSE-EUR — ACTIVE_NOW — score mémoire 7.954/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZIG-EUR — MEMORY_24H — score mémoire 7.836/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ALGO-EUR — ACTIVE_NOW — score mémoire 7.832/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +36.77% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +33.58% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MOVR-EUR +32.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- POND-EUR +31.24% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GRASS-EUR +28.17% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MEW-EUR +24.68% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PUMP-EUR +23.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INIT-EUR +18.36% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PHA-EUR +18.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +17.89% — DETECTED_EARLY — couche NONE — action NONE

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
