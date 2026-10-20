# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-20T21:00:38.946747+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : ALT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.781 | entrée 6.000 | trend 8.950 | rang 7.297
  - Strong structure but imperfect current entry; prefer passive execution. High extension/chase reduces rank but does not erase the setup.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : BEAM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.333 | entrée 5.950 | trend 8.750 | rang 7.235
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ALT-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.297
2. BEAM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.235
3. CTR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.880

## Accélération indépendante

- IOST-EUR — CONFIRMED_ACCELERATION — score 7.706/10 — DETECTED_BUT_TOO_LATE
- BRETT-EUR — CONFIRMED_ACCELERATION — score 6.503/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZIG-EUR — BUILDING_ACCELERATION — score 6.196/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- OP-EUR — BUILDING_ACCELERATION — score 5.957/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CTC-EUR — BUILDING_ACCELERATION — score 5.588/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- REZ-EUR — BUILDING_ACCELERATION — score 5.519/10 — DETECTED_BUT_TOO_LATE
- MON-EUR — BUILDING_ACCELERATION — score 5.317/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SYRUP-EUR — BUILDING_ACCELERATION — score 5.157/10 — DETECTED_BUT_TOO_LATE
- ZRX-EUR — BUILDING_ACCELERATION — score 5.024/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GNS-EUR — MEMORY_24H — score mémoire 9.505/10 — sources ACCELERATION — MEMORY_ONLY
- POND-EUR — MEMORY_24H — score mémoire 8.833/10 — sources ACCELERATION — MEMORY_ONLY
- IOST-EUR — ACTIVE_NOW — score mémoire 7.706/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- WHUF-EUR — MEMORY_24H — score mémoire 7.643/10 — sources ACCELERATION — MEMORY_ONLY
- AVA-EUR — MEMORY_24H — score mémoire 7.332/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ALT-EUR — ACTIVE_NOW — score mémoire 7.297/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- BEAM-EUR — ACTIVE_NOW — score mémoire 7.235/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 7.132/10 — sources V4 — DETECTED_BUT_TOO_LATE
- AMP-EUR — MEMORY_24H — score mémoire 7.109/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- METIS-EUR — MEMORY_24H — score mémoire 6.932/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- IOST-EUR +42.14% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- COMP-EUR +22.04% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GNS-EUR +18.19% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- REZ-EUR +18.09% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICNT-EUR +17.77% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- WLD-EUR +14.75% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- USELESS-EUR +13.30% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- KERNEL-EUR +13.21% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PEPE-EUR +11.74% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ALT-EUR +11.39% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
