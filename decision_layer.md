# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-30T06:54:11.783398+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : AAVE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.052 | entrée 6.300 | trend 8.700 | rang 7.832
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : COMP-EUR | action LATENT_ACCELERATOR | opportunité 8.220 | entrée 5.750 | trend 9.200 | rang 8.023
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ICP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.349 | entrée 7.450 | trend 9.200 | rang 8.287
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ICP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.287
2. XDC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.084
3. COMP-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 8.023

## Accélération indépendante

- WMTX-EUR — CONFIRMED_ACCELERATION — score 8.460/10 — DETECTED_BUT_TOO_LATE
- PHA-EUR — CONFIRMED_ACCELERATION — score 7.994/10 — DETECTED_BUT_TOO_LATE
- ARK-EUR — BUILDING_ACCELERATION — score 6.404/10 — DETECTED_BUT_TOO_LATE
- RARE-EUR — BUILDING_ACCELERATION — score 5.306/10 — DETECTED_BUT_TOO_LATE
- ROSE-EUR — BUILDING_ACCELERATION — score 4.975/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PUNDIX-EUR — BUILDING_ACCELERATION — score 4.880/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- TREAD-EUR — MEMORY_24H — score mémoire 9.983/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOVR-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WMTX-EUR — ACTIVE_NOW — score mémoire 8.460/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- AGI-EUR — MEMORY_24H — score mémoire 8.300/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.287/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XDC-EUR — ACTIVE_NOW — score mémoire 8.084/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- COMP-EUR — ACTIVE_NOW — score mémoire 8.023/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOLV-EUR — MEMORY_24H — score mémoire 8.017/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 7.994/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- MOVR-EUR +57.86% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +40.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARK-EUR +20.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- POND-EUR +20.79% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +18.99% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZBCN-EUR +18.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QNT-EUR +17.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUMP-EUR +17.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +16.35% — DETECTED_EARLY — couche NONE — action NONE
- MEW-EUR +15.47% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

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
