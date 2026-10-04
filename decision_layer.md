# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-04T12:20:20.006947+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : HUMA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.613 | entrée 6.450 | trend 8.950 | rang 7.526
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ILV-EUR | action LATENT_ACCELERATOR | opportunité 7.525 | entrée 5.600 | trend 8.700 | rang 7.292
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : FLUID-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.991 | entrée 6.600 | trend 9.200 | rang 7.814
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. FLUID-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.814
2. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.539
3. SKY-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.530

## Accélération indépendante

- BAT-EUR — CONFIRMED_ACCELERATION — score 7.727/10 — DETECTED_BUT_TOO_LATE
- LUMIA-EUR — BUILDING_ACCELERATION — score 5.964/10 — DETECTED_BUT_TOO_LATE
- MOCA-EUR — BUILDING_ACCELERATION — score 4.970/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- WIN-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FLUID-EUR — ACTIVE_NOW — score mémoire 7.814/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- BAT-EUR — ACTIVE_NOW — score mémoire 7.727/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ARK-EUR — MEMORY_DECAY_24_72H — score mémoire 7.549/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.539/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SKY-EUR — ACTIVE_NOW — score mémoire 7.530/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HUMA-EUR — ACTIVE_NOW — score mémoire 7.526/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PUMP-EUR — ACTIVE_NOW — score mémoire 7.331/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- IMX-EUR — MEMORY_24H — score mémoire 7.323/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GALA-EUR — ACTIVE_NOW — score mémoire 7.317/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- BEAM-EUR +33.10% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TREAD-EUR +31.03% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- STRK-EUR +25.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +23.26% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NOS-EUR +19.26% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NOM-EUR +15.41% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BAT-EUR +14.62% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AXS-EUR +13.67% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FUN-EUR +13.44% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AKT-EUR +12.85% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
