# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-17T19:14:16.641804+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : DUSK-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.844 | entrée 5.850 | trend 8.550 | rang 7.120
  - Strong structure but imperfect current entry; prefer passive execution. High extension/chase reduces rank but does not erase the setup.
- **MEILLEUR_LATENT_ACCELERATOR** : METIS-EUR | action LATENT_ACCELERATOR | opportunité 7.544 | entrée 5.050 | trend 8.300 | rang 7.124
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : INJ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.145 | entrée 6.450 | trend 8.900 | rang 7.648
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.648
2. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.199
3. METIS-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.124

## Accélération indépendante

- OGN-EUR — BUILDING_ACCELERATION — score 6.337/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — BUILDING_ACCELERATION — score 5.892/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- APE-EUR — BUILDING_ACCELERATION — score 5.074/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GALA-EUR — BUILDING_ACCELERATION — score 5.014/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LSK-EUR — BUILDING_ACCELERATION — score 4.987/10 — DETECTED_BUT_TOO_LATE
- ZORA-EUR — BUILDING_ACCELERATION — score 4.963/10 — DETECTED_BUT_TOO_LATE
- FUEL-EUR — BUILDING_ACCELERATION — score 4.848/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- EPIC-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- AXL-EUR — MEMORY_24H — score mémoire 9.132/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 8.833/10 — sources ACCELERATION — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.245/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GTC-EUR — MEMORY_24H — score mémoire 7.849/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICNT-EUR — MEMORY_24H — score mémoire 7.720/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CPOOL-EUR — MEMORY_24H — score mémoire 7.716/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 7.667/10 — sources ACCELERATION — MEMORY_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 7.648/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.199/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ICNT-EUR +36.55% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AVA-EUR +35.14% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GTC-EUR +16.01% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SAND-EUR +15.07% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ALT-EUR +13.87% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZEUS-EUR +13.36% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- EPIC-EUR +12.77% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LSK-EUR +10.16% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BTT-EUR +9.58% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GNS-EUR +9.26% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
