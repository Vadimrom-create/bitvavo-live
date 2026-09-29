# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T14:43:52.444942+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : WLD-EUR | action ACHETE_MAINTENANT | opportunité 9.239 | entrée 7.600 | trend 7.950 | rang 8.207
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : MIOTA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.253 | entrée 5.900 | trend 8.900 | rang 7.942
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : XDC-EUR | action LATENT_ACCELERATOR | opportunité 7.471 | entrée 4.500 | trend 8.700 | rang 7.349
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : GALA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.432 | entrée 7.500 | trend 9.000 | rang 8.464
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. WLD-EUR — ACHETE_MAINTENANT — rank 8.207 — opportunité 9.239 — entrée 7.600 — trend 7.950
2. XPL-EUR — ACHETE_MAINTENANT — rank 7.809 — opportunité 9.005 — entrée 7.400 — trend 7.250
3. NEAR-EUR — ACHETE_MAINTENANT — rank 7.727 — opportunité 9.093 — entrée 7.600 — trend 7.500
4. EIGEN-EUR — ACHETE_MAINTENANT — rank 7.582 — opportunité 8.052 — entrée 7.200 — trend 7.850

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. GALA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.464
2. XLM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.289
3. COMP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.273

## Accélération indépendante

- ZRO-EUR — CONFIRMED_ACCELERATION — score 8.634/10 — DETECTED_BUT_TOO_LATE
- BIO-EUR — CONFIRMED_ACCELERATION — score 8.562/10 — DETECTED_BUT_TOO_LATE
- PROM-EUR — CONFIRMED_ACCELERATION — score 8.146/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POND-EUR — CONFIRMED_ACCELERATION — score 7.454/10 — DETECTED_BUT_TOO_LATE
- ALICE-EUR — CONFIRMED_ACCELERATION — score 7.220/10 — DETECTED_BUT_TOO_LATE
- OP-EUR — CONFIRMED_ACCELERATION — score 6.590/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BOME-EUR — BUILDING_ACCELERATION — score 6.439/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MLN-EUR — BUILDING_ACCELERATION — score 6.299/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PONKE-EUR — BUILDING_ACCELERATION — score 6.172/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ETHFI-EUR — BUILDING_ACCELERATION — score 6.130/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- WLD-EUR — ACTIVE_NOW — score mémoire 8.207/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- NEAR-EUR — ACTIVE_NOW — score mémoire 7.727/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- GIGA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- USELESS-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.836/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 8.690/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRO-EUR — ACTIVE_NOW — score mémoire 8.634/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- 0G-EUR +44.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- POND-EUR +42.74% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZBCN-EUR +30.75% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CRV-EUR +24.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CELO-EUR +20.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AAVE-EUR +20.49% — DETECTED_EARLY — couche NONE — action NONE
- GRASS-EUR +19.06% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ETHFI-EUR +19.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYRUP-EUR +17.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICP-EUR +17.83% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
