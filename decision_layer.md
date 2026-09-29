# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T15:02:27.825202+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : WLD-EUR | action ACHETE_MAINTENANT | opportunité 8.960 | entrée 7.600 | trend 7.950 | rang 7.973
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : MIOTA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.116 | entrée 6.150 | trend 8.900 | rang 7.868
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : JASMY-EUR | action LATENT_ACCELERATOR | opportunité 8.420 | entrée 5.650 | trend 9.000 | rang 7.884
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ALGO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.434 | entrée 6.050 | trend 8.900 | rang 7.984
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. WLD-EUR — ACHETE_MAINTENANT — rank 7.973 — opportunité 8.960 — entrée 7.600 — trend 7.950
2. XPL-EUR — ACHETE_MAINTENANT — rank 7.662 — opportunité 8.874 — entrée 7.200 — trend 7.250
3. EIGEN-EUR — ACHETE_MAINTENANT — rank 7.439 — opportunité 7.839 — entrée 6.950 — trend 7.850

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ALGO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.984
2. WLD-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.973
3. GALA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.965

## Accélération indépendante

- FUEL-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- XDP-EUR — CONFIRMED_ACCELERATION — score 6.945/10 — DETECTED_BUT_TOO_LATE
- ZIG-EUR — CONFIRMED_ACCELERATION — score 6.729/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CRV-EUR — BUILDING_ACCELERATION — score 5.751/10 — DETECTED_BUT_TOO_LATE
- SOON-EUR — BUILDING_ACCELERATION — score 5.718/10 — DETECTED_BUT_TOO_LATE
- FIL-EUR — BUILDING_ACCELERATION — score 5.688/10 — DETECTED_BUT_TOO_LATE
- THQ-EUR — BUILDING_ACCELERATION — score 5.487/10 — DETECTED_BUT_TOO_LATE
- AGI-EUR — BUILDING_ACCELERATION — score 5.325/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VELO-EUR — BUILDING_ACCELERATION — score 5.289/10 — DETECTED_BUT_TOO_LATE
- YB-EUR — BUILDING_ACCELERATION — score 5.045/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- GIGA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- USELESS-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.836/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 8.690/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.582/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FUEL-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — MEMORY_24H — score mémoire 8.185/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- 0G-EUR +43.04% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- POND-EUR +33.90% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZBCN-EUR +28.86% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CRV-EUR +25.38% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +21.11% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INIT-EUR +20.11% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- AAVE-EUR +19.69% — DETECTED_EARLY — couche NONE — action NONE
- CELO-EUR +19.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ETHFI-EUR +18.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALICE-EUR +18.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
