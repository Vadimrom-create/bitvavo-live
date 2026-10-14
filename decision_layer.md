# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-14T11:22:49.840444+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : FLUID-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.466 | entrée 6.000 | trend 8.550 | rang 7.278
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : STX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.794 | entrée 6.050 | trend 8.900 | rang 7.592
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. STX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.592
2. PYTH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.458
3. FLUID-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.278

## Accélération indépendante

- NES-EUR — CONFIRMED_ACCELERATION — score 9.532/10 — DETECTED_BUT_TOO_LATE
- DUSK-EUR — CONFIRMED_ACCELERATION — score 8.312/10 — DETECTED_BUT_TOO_LATE
- GLMR-EUR — BUILDING_ACCELERATION — score 5.243/10 — DETECTED_BUT_TOO_LATE
- AVA-EUR — BUILDING_ACCELERATION — score 5.072/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- NES-EUR — ACTIVE_NOW — score mémoire 9.532/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- DUSK-EUR — ACTIVE_NOW — score mémoire 8.312/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — MEMORY_24H — score mémoire 7.892/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 7.592/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CTR-EUR — MEMORY_24H — score mémoire 7.568/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RAD-EUR — MEMORY_24H — score mémoire 7.564/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 7.458/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 7.386/10 — sources ACCELERATION — MEMORY_ONLY
- FLUID-EUR — ACTIVE_NOW — score mémoire 7.278/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AZTEC-EUR — MEMORY_24H — score mémoire 7.261/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- GNS-EUR +85.74% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- WAL-EUR +41.87% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GLMR-EUR +20.71% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AVA-EUR +17.93% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZEUS-EUR +17.74% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NES-EUR +14.32% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DEEP-EUR +14.16% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PNT-EUR +13.86% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BAT-EUR +12.86% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AXL-EUR +11.37% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
