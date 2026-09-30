# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-30T09:22:47.560159+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : CRV-EUR | action ACHETE_MAINTENANT | opportunité 8.967 | entrée 7.200 | trend 8.400 | rang 8.034
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SAND-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.563 | entrée 6.450 | trend 7.450 | rang 7.379
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : COW-EUR | action LATENT_ACCELERATOR | opportunité 7.521 | entrée 4.500 | trend 8.650 | rang 7.354
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : COMP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.558 | entrée 6.600 | trend 9.200 | rang 8.238
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. CRV-EUR — ACHETE_MAINTENANT — rank 8.034 — opportunité 8.967 — entrée 7.200 — trend 8.400
2. XLM-EUR — ACHETE_MAINTENANT — rank 7.894 — opportunité 8.373 — entrée 7.400 — trend 8.500
3. DOT-EUR — ACHETE_MAINTENANT — rank 7.835 — opportunité 8.840 — entrée 7.300 — trend 7.950
4. ICP-EUR — ACHETE_MAINTENANT — rank 7.830 — opportunité 7.826 — entrée 6.850 — trend 8.900
5. AXS-EUR — ACHETE_MAINTENANT — rank 7.595 — opportunité 8.065 — entrée 6.800 — trend 8.200

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. COMP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.238
2. CRV-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.034
3. XLM-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.894

## Accélération indépendante

- TRAC-EUR — CONFIRMED_ACCELERATION — score 8.971/10 — DETECTED_BUT_TOO_LATE
- DYDX-EUR — CONFIRMED_ACCELERATION — score 8.239/10 — DETECTED_BUT_TOO_LATE
- FTT-EUR — CONFIRMED_ACCELERATION — score 7.815/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZORA-EUR — CONFIRMED_ACCELERATION — score 6.928/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GIGA-EUR — BUILDING_ACCELERATION — score 6.024/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XAN-EUR — BUILDING_ACCELERATION — score 5.928/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BRETT-EUR — BUILDING_ACCELERATION — score 5.825/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PEAQ-EUR — BUILDING_ACCELERATION — score 5.656/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SAGA-EUR — BUILDING_ACCELERATION — score 5.625/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MANTRA-EUR — BUILDING_ACCELERATION — score 5.045/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CRV-EUR — ACTIVE_NOW — score mémoire 8.034/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- DOT-EUR — ACTIVE_NOW — score mémoire 7.835/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- TREAD-EUR — MEMORY_24H — score mémoire 9.983/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TRAC-EUR — ACTIVE_NOW — score mémoire 8.971/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SWELL-EUR — MEMORY_DECAY_24_72H — score mémoire 8.820/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WMTX-EUR — MEMORY_24H — score mémoire 8.460/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MOVR-EUR — MEMORY_24H — score mémoire 8.377/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.300/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DYDX-EUR — ACTIVE_NOW — score mémoire 8.239/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- COMP-EUR — ACTIVE_NOW — score mémoire 8.238/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- MOVR-EUR +98.79% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GTC-EUR +34.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GLMR-EUR +31.52% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +28.54% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PHA-EUR +25.34% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARK-EUR +19.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZBCN-EUR +15.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUMP-EUR +14.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 0G-EUR +14.04% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +13.94% — DETECTED_EARLY — couche NONE — action NONE

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
