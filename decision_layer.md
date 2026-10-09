# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-09T09:12:09.807367+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : IMX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.402 | entrée 5.900 | trend 8.200 | rang 7.006
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : JUP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.733 | entrée 7.100 | trend 8.900 | rang 7.536
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. JUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.536
2. BAT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.494
3. PARTI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.362

## Accélération indépendante

- W-EUR — CONFIRMED_ACCELERATION — score 8.700/10 — DETECTED_BUT_TOO_LATE
- AGI-EUR — CONFIRMED_ACCELERATION — score 8.443/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AIOZ-EUR — CONFIRMED_ACCELERATION — score 7.911/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GIGA-EUR — CONFIRMED_ACCELERATION — score 6.657/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZKJ-EUR — BUILDING_ACCELERATION — score 6.132/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KAIA-EUR — BUILDING_ACCELERATION — score 6.000/10 — DETECTED_BUT_TOO_LATE
- PYTH-EUR — BUILDING_ACCELERATION — score 5.650/10 — DETECTED_BUT_TOO_LATE
- GWEI-EUR — BUILDING_ACCELERATION — score 5.444/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LSK-EUR — BUILDING_ACCELERATION — score 5.388/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DEEP-EUR — BUILDING_ACCELERATION — score 5.335/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ZEUS-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 8.700/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AMP-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- AGI-EUR — ACTIVE_NOW — score mémoire 8.443/10 — sources ACCELERATION — WATCH_ONLY
- GLMR-EUR — MEMORY_24H — score mémoire 8.432/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 8.425/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SCR-EUR — MEMORY_24H — score mémoire 8.302/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GTC-EUR — MEMORY_24H — score mémoire 8.274/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SXT-EUR — MEMORY_24H — score mémoire 8.096/10 — sources ACCELERATION — MEMORY_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.911/10 — sources ACCELERATION, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- OGN-EUR +47.57% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- STRK-EUR +43.91% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RLC-EUR +36.87% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- KAIA-EUR +34.56% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DRV-EUR +21.05% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZRC-EUR +17.57% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AMP-EUR +15.32% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PYTH-EUR +14.57% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MAGIC-EUR +13.36% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GTC-EUR +12.87% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
