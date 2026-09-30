# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-30T02:43:10.687281+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : HUMA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.967 | entrée 6.000 | trend 8.650 | rang 7.667
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ROSE-EUR | action LATENT_ACCELERATOR | opportunité 7.577 | entrée 4.700 | trend 8.400 | rang 7.219
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ICP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.801 | entrée 6.450 | trend 9.200 | rang 8.003
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ICP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.003
2. LTC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.969
3. HBAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.903

## Accélération indépendante

- TREAD-EUR — BUILDING_ACCELERATION — score 5.666/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARX-EUR — BUILDING_ACCELERATION — score 5.180/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOON-EUR — BUILDING_ACCELERATION — score 5.035/10 — DETECTED_BUT_TOO_LATE
- HMSTR-EUR — BUILDING_ACCELERATION — score 4.811/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- QUID-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.866/10 — sources ACCELERATION — MEMORY_ONLY
- SOLV-EUR — MEMORY_24H — score mémoire 8.017/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.003/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LTC-EUR — ACTIVE_NOW — score mémoire 7.969/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HBAR-EUR — ACTIVE_NOW — score mémoire 7.903/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GTC-EUR — MEMORY_24H — score mémoire 7.830/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEAQ-EUR — ACTIVE_NOW — score mémoire 7.829/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 7.707/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SOON-EUR +35.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +32.05% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- POND-EUR +30.58% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MOVR-EUR +27.29% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PUMP-EUR +25.25% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +24.94% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MEW-EUR +23.10% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- INIT-EUR +19.13% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZBCN-EUR +17.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ETHFI-EUR +15.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
