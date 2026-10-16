# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-16T14:14:53.272336+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : DUSK-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.462 | entrée 5.900 | trend 8.500 | rang 7.161
  - Strong structure but imperfect current entry; prefer passive execution. High extension/chase reduces rank but does not erase the setup.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DODO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.663 | entrée 5.500 | trend 8.700 | rang 7.353
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. DODO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.353
2. DUSK-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.161
3. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.045

## Accélération indépendante

- ICNT-EUR — BUILDING_ACCELERATION — score 6.051/10 — DETECTED_BUT_TOO_LATE
- CAP-EUR — BUILDING_ACCELERATION — score 5.733/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- APE-EUR — BUILDING_ACCELERATION — score 5.276/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- GNS-EUR — MEMORY_24H — score mémoire 9.754/10 — sources ACCELERATION — MEMORY_ONLY
- ETHFI-EUR — MEMORY_24H — score mémoire 9.389/10 — sources ACCELERATION — MEMORY_ONLY
- BANANA-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION — MEMORY_ONLY
- BREV-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION — MEMORY_ONLY
- COW-EUR — MEMORY_24H — score mémoire 8.909/10 — sources ACCELERATION — MEMORY_ONLY
- ZRO-EUR — MEMORY_24H — score mémoire 8.832/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HOME-EUR — MEMORY_24H — score mémoire 8.559/10 — sources ACCELERATION — MEMORY_ONLY
- IRYS-EUR — MEMORY_24H — score mémoire 8.481/10 — sources ACCELERATION — MEMORY_ONLY
- BAT-EUR — MEMORY_24H — score mémoire 8.396/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TURBO-EUR — MEMORY_24H — score mémoire 8.332/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- POND-EUR +46.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TIA-EUR +28.63% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICNT-EUR +24.07% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- INJ-EUR +23.60% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NPC-EUR +20.91% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DRV-EUR +16.12% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BAT-EUR +14.76% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZRO-EUR +14.37% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- APE-EUR +14.17% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- KMNO-EUR +13.86% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
