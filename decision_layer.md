# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-13T21:55:01.906973+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : HUMA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.520 | entrée 6.250 | trend 8.450 | rang 7.263
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : CTR-EUR | action LATENT_ACCELERATOR | opportunité 7.739 | entrée 5.400 | trend 8.900 | rang 7.379
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AZTEC-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.047 | entrée 6.750 | trend 8.950 | rang 7.707
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AZTEC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.707
2. CTR-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.379
3. SAFE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.326

## Accélération indépendante

- APE-EUR — BUILDING_ACCELERATION — score 5.517/10 — DETECTED_BUT_TOO_LATE
- KMNO-EUR — BUILDING_ACCELERATION — score 5.371/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ATH-EUR — MEMORY_24H — score mémoire 9.087/10 — sources ACCELERATION — MEMORY_ONLY
- AMP-EUR — MEMORY_DECAY_24_72H — score mémoire 8.413/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- STRK-EUR — MEMORY_DECAY_24_72H — score mémoire 8.075/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 7.892/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 7.867/10 — sources ACCELERATION — MEMORY_ONLY
- AZTEC-EUR — ACTIVE_NOW — score mémoire 7.707/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PROM-EUR — MEMORY_DECAY_24_72H — score mémoire 7.573/10 — sources ACCELERATION — MEMORY_ONLY
- RAD-EUR — MEMORY_DECAY_24_72H — score mémoire 7.419/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- CTR-EUR — ACTIVE_NOW — score mémoire 7.379/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CYBER-EUR — MEMORY_DECAY_24_72H — score mémoire 7.355/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- GNS-EUR +106.79% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZRC-EUR +37.66% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BAT-EUR +28.42% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CNPY-EUR +19.35% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- OP-EUR +19.26% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZK-EUR +12.23% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ICNT-EUR +11.13% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- KMNO-EUR +10.61% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DUSK-EUR +10.48% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- INJ-EUR +9.57% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
