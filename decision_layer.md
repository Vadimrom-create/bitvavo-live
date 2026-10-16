# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-16T04:56:20.881396+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : METIS-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.579 | entrée 6.400 | trend 8.650 | rang 7.273
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DUSK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.936 | entrée 6.450 | trend 8.550 | rang 7.432
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. DUSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.432
2. METIS-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.273
3. PYTH-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.204

## Accélération indépendante

- ICNT-EUR — CONFIRMED_ACCELERATION — score 7.822/10 — DETECTED_BUT_TOO_LATE
- PROMPT-EUR — CONFIRMED_ACCELERATION — score 6.542/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FORM-EUR — BUILDING_ACCELERATION — score 5.884/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GMX-EUR — BUILDING_ACCELERATION — score 5.054/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DUSK-EUR — BUILDING_ACCELERATION — score 4.922/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- GNS-EUR — MEMORY_24H — score mémoire 9.754/10 — sources ACCELERATION — MEMORY_ONLY
- ETHFI-EUR — MEMORY_24H — score mémoire 9.389/10 — sources ACCELERATION — MEMORY_ONLY
- MAGIC-EUR — MEMORY_24H — score mémoire 9.346/10 — sources ACCELERATION — MEMORY_ONLY
- BANANA-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION — MEMORY_ONLY
- BREV-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION — MEMORY_ONLY
- COW-EUR — MEMORY_24H — score mémoire 8.909/10 — sources ACCELERATION — MEMORY_ONLY
- ZRO-EUR — MEMORY_24H — score mémoire 8.832/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HOME-EUR — MEMORY_24H — score mémoire 8.559/10 — sources ACCELERATION — MEMORY_ONLY
- IRYS-EUR — MEMORY_24H — score mémoire 8.481/10 — sources ACCELERATION — MEMORY_ONLY
- BAT-EUR — MEMORY_24H — score mémoire 8.396/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- POND-EUR +30.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICNT-EUR +28.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INJ-EUR +22.87% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZRO-EUR +20.27% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AVA-EUR +17.64% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +14.01% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- INIT-EUR +13.79% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TIA-EUR +13.71% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- KMNO-EUR +13.50% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZAMA-EUR +13.31% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
