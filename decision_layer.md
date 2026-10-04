# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-04T08:39:39.451463+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 8.523 | entrée 7.650 | trend 9.200 | rang 8.201
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : GALA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.641 | entrée 6.000 | trend 8.900 | rang 7.422
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MAGIC-EUR | action LATENT_ACCELERATOR | opportunité 7.724 | entrée 5.400 | trend 8.450 | rang 7.303
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : FLUID-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.774 | entrée 5.850 | trend 9.200 | rang 7.641
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AAVE-EUR — ACHETE_MAINTENANT — rank 8.201 — opportunité 8.523 — entrée 7.650 — trend 9.200

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.201
2. FLUID-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.641
3. GALA-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.422

## Accélération indépendante

- GROVE-EUR — CONFIRMED_ACCELERATION — score 7.045/10 — DETECTED_BUT_TOO_LATE
- RUNE-EUR — CONFIRMED_ACCELERATION — score 6.577/10 — DETECTED_BUT_TOO_LATE
- BEAM-EUR — BUILDING_ACCELERATION — score 6.443/10 — DETECTED_BUT_TOO_LATE
- BIGTIME-EUR — BUILDING_ACCELERATION — score 5.978/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GMT-EUR — BUILDING_ACCELERATION — score 5.869/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GNO-EUR — BUILDING_ACCELERATION — score 5.307/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZKJ-EUR — BUILDING_ACCELERATION — score 5.212/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AKT-EUR — BUILDING_ACCELERATION — score 5.066/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- WIN-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.201/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ARK-EUR — MEMORY_24H — score mémoire 8.048/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ATH-EUR — MEMORY_24H — score mémoire 7.764/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FLUID-EUR — ACTIVE_NOW — score mémoire 7.641/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SKY-EUR — ACTIVE_NOW — score mémoire 7.634/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FLOCK-EUR — MEMORY_DECAY_24_72H — score mémoire 7.529/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOVE-EUR — MEMORY_DECAY_24_72H — score mémoire 7.524/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GALA-EUR — ACTIVE_NOW — score mémoire 7.422/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZEUS-EUR — MEMORY_DECAY_24_72H — score mémoire 7.419/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- BEAM-EUR +37.57% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GLMR-EUR +34.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +27.65% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TREAD-EUR +26.83% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- STRK-EUR +25.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FUN-EUR +20.81% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ATH-EUR +16.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AKT-EUR +16.13% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PUMP-EUR +15.58% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZAMA-EUR +14.14% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
