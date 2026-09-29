# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T15:26:34.213200+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : WLD-EUR | action ACHETE_MAINTENANT | opportunité 8.736 | entrée 7.050 | trend 7.950 | rang 7.830
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : RUNE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.714 | entrée 5.800 | trend 8.400 | rang 7.508
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : JASMY-EUR | action LATENT_ACCELERATOR | opportunité 8.006 | entrée 5.200 | trend 9.000 | rang 7.695
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LINK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.072 | entrée 6.100 | trend 9.200 | rang 7.997
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. WLD-EUR — ACHETE_MAINTENANT — rank 7.830 — opportunité 8.736 — entrée 7.050 — trend 7.950

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. LINK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.997
2. ALGO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.926
3. GALA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.831

## Accélération indépendante

- NOS-EUR — CONFIRMED_ACCELERATION — score 6.785/10 — DETECTED_BUT_TOO_LATE
- OSMO-EUR — BUILDING_ACCELERATION — score 6.494/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRO-EUR — BUILDING_ACCELERATION — score 4.797/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- GIGA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- USELESS-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.836/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 8.690/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.582/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FUEL-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.185/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- 0G-EUR +37.42% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- POND-EUR +34.70% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZBCN-EUR +24.35% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CRV-EUR +23.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +22.76% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INIT-EUR +20.49% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- AAVE-EUR +17.87% — DETECTED_EARLY — couche NONE — action NONE
- CELO-EUR +17.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYRUP-EUR +15.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICP-EUR +14.19% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
