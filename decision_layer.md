# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-04T13:14:43.938473+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : ILV-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.322 | entrée 5.800 | trend 8.700 | rang 7.833
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : GALA-EUR | action LATENT_ACCELERATOR | opportunité 8.216 | entrée 4.950 | trend 8.700 | rang 7.685
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HUMA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.987 | entrée 7.150 | trend 8.950 | rang 7.897
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. HUMA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.897
2. FLUID-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.894
3. ILV-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.833

## Accélération indépendante

- MAGIC-EUR — BUILDING_ACCELERATION — score 6.149/10 — DETECTED_BUT_TOO_LATE
- DGB-EUR — BUILDING_ACCELERATION — score 5.987/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POND-EUR — BUILDING_ACCELERATION — score 5.258/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- FIDA-EUR — MEMORY_24H — score mémoire 9.160/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HUMA-EUR — ACTIVE_NOW — score mémoire 7.897/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FLUID-EUR — ACTIVE_NOW — score mémoire 7.894/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ILV-EUR — ACTIVE_NOW — score mémoire 7.833/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.767/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PUMP-EUR — ACTIVE_NOW — score mémoire 7.757/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GALA-EUR — ACTIVE_NOW — score mémoire 7.685/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SKY-EUR — ACTIVE_NOW — score mémoire 7.610/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ATH-EUR — ACTIVE_NOW — score mémoire 7.498/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- TREAD-EUR +31.41% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BEAM-EUR +28.56% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- STRK-EUR +25.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +23.30% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NOS-EUR +16.41% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AKT-EUR +15.21% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NOM-EUR +13.61% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AXS-EUR +13.47% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BAT-EUR +12.96% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FUN-EUR +12.02% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
