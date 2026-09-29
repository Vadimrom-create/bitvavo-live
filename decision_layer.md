# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T03:57:06.247776+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : RUNE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.763 | entrée 6.250 | trend 8.150 | rang 7.411
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : 0G-EUR | action LATENT_ACCELERATOR | opportunité 7.660 | entrée 4.250 | trend 8.700 | rang 6.899
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LINK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.905 | entrée 6.500 | trend 8.900 | rang 7.809
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. LINK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.809
2. MIOTA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.770
3. SEI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.763

## Accélération indépendante

- ZRC-EUR — CONFIRMED_ACCELERATION — score 9.000/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- OSMO-EUR — CONFIRMED_ACCELERATION — score 7.990/10 — DETECTED_BUT_TOO_LATE
- GRASS-EUR — CONFIRMED_ACCELERATION — score 7.560/10 — DETECTED_BUT_TOO_LATE
- SSV-EUR — BUILDING_ACCELERATION — score 5.993/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- STRK-EUR — BUILDING_ACCELERATION — score 5.652/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NEO-EUR — BUILDING_ACCELERATION — score 5.301/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AVNT-EUR — BUILDING_ACCELERATION — score 5.115/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AUCTION-EUR — BUILDING_ACCELERATION — score 5.011/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MERL-EUR — BUILDING_ACCELERATION — score 4.988/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DEEP-EUR — BUILDING_ACCELERATION — score 4.791/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- PUFFER-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRC-EUR — ACTIVE_NOW — score mémoire 9.000/10 — sources ACCELERATION, V4 — WATCH_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.844/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.632/10 — sources ACCELERATION — MEMORY_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 8.100/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- OSMO-EUR — ACTIVE_NOW — score mémoire 7.990/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- AIXBT-EUR — MEMORY_24H — score mémoire 7.962/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 7.809/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- U-EUR — MEMORY_24H — score mémoire 7.773/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MIOTA-EUR — ACTIVE_NOW — score mémoire 7.770/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- NMR-EUR +45.99% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HBAR-EUR +24.46% — DETECTED_EARLY — couche NONE — action NONE
- CRV-EUR +17.51% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALGO-EUR +17.41% — DETECTED_EARLY — couche NONE — action NONE
- 0G-EUR +13.98% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MIOTA-EUR +8.40% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ARX-EUR +8.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IKA-EUR +8.00% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- XLM-EUR +7.68% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SYRUP-EUR +7.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
