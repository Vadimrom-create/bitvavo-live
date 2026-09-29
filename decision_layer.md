# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T14:22:31.581765+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : GALA-EUR | action ACHETE_MAINTENANT | opportunité 8.792 | entrée 6.800 | trend 9.000 | rang 8.212
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ZRO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.273 | entrée 5.900 | trend 8.400 | rang 7.582
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : CRO-EUR | action LATENT_ACCELERATOR | opportunité 7.462 | entrée 5.700 | trend 8.800 | rang 7.524
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LINK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.090 | entrée 6.500 | trend 9.200 | rang 8.053
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. GALA-EUR — ACHETE_MAINTENANT — rank 8.212 — opportunité 8.792 — entrée 6.800 — trend 9.000
2. NEAR-EUR — ACHETE_MAINTENANT — rank 7.630 — opportunité 8.705 — entrée 7.650 — trend 7.300

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. GALA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.212
2. LINK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.053
3. XLM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.020

## Accélération indépendante

- NOS-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- SCR-EUR — BUILDING_ACCELERATION — score 6.408/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IMU-EUR — BUILDING_ACCELERATION — score 5.743/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- 0G-EUR — BUILDING_ACCELERATION — score 5.734/10 — DETECTED_BUT_TOO_LATE
- POND-EUR — BUILDING_ACCELERATION — score 5.555/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- NEAR-EUR — ACTIVE_NOW — score mémoire 7.630/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- GIGA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- USELESS-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.836/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 8.690/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BONK-EUR — MEMORY_24H — score mémoire 8.619/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.582/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- 0G-EUR +44.02% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- POND-EUR +36.99% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZBCN-EUR +25.58% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CELO-EUR +22.48% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CRV-EUR +20.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYRUP-EUR +18.11% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AAVE-EUR +17.17% — DETECTED_EARLY — couche NONE — action NONE
- GRASS-EUR +16.88% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ICP-EUR +16.73% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CVX-EUR +14.69% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
