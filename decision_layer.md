# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T11:42:37.272764+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LINK-EUR | action ACHETE_MAINTENANT | opportunité 8.693 | entrée 7.950 | trend 9.200 | rang 8.379
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : CC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.897 | entrée 5.950 | trend 7.300 | rang 7.555
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MIOTA-EUR | action LATENT_ACCELERATOR | opportunité 7.813 | entrée 5.200 | trend 8.900 | rang 7.627
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : XLM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.387 | entrée 7.850 | trend 8.650 | rang 8.465
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. LINK-EUR — ACHETE_MAINTENANT — rank 8.379 — opportunité 8.693 — entrée 7.950 — trend 9.200
2. ALGO-EUR — ACHETE_MAINTENANT — rank 8.116 — opportunité 8.508 — entrée 7.000 — trend 8.900
3. XDC-EUR — ACHETE_MAINTENANT — rank 7.814 — opportunité 8.164 — entrée 7.100 — trend 8.750
4. NEAR-EUR — ACHETE_MAINTENANT — rank 7.708 — opportunité 8.724 — entrée 7.600 — trend 7.300
5. ICP-EUR — ACHETE_MAINTENANT — rank 7.701 — opportunité 8.513 — entrée 7.050 — trend 9.000
6. XPL-EUR — ACHETE_MAINTENANT — rank 7.439 — opportunité 8.880 — entrée 7.500 — trend 6.650

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. XLM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.465
2. LINK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.379
3. RUNE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.248

## Accélération indépendante

- EDEN-EUR — CONFIRMED_ACCELERATION — score 8.870/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NIL-EUR — CONFIRMED_ACCELERATION — score 8.201/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WMTX-EUR — CONFIRMED_ACCELERATION — score 8.145/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — CONFIRMED_ACCELERATION — score 8.036/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FUEL-EUR — CONFIRMED_ACCELERATION — score 7.293/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ILV-EUR — CONFIRMED_ACCELERATION — score 7.073/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FLUID-EUR — CONFIRMED_ACCELERATION — score 6.541/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TREAD-EUR — BUILDING_ACCELERATION — score 6.441/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CELO-EUR — BUILDING_ACCELERATION — score 6.278/10 — DETECTED_BUT_TOO_LATE
- PEAQ-EUR — BUILDING_ACCELERATION — score 5.917/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GIGA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- EDEN-EUR — ACTIVE_NOW — score mémoire 8.870/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.836/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 8.690/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.632/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.582/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZBCN-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- POND-EUR +56.73% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CELO-EUR +28.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 0G-EUR +28.64% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +21.25% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SYRUP-EUR +19.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CRV-EUR +18.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZBCN-EUR +18.46% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- AAVE-EUR +15.58% — DETECTED_EARLY — couche NONE — action NONE
- CVX-EUR +15.40% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- INIT-EUR +14.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
