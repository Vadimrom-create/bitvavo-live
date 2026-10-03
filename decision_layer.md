# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-03T07:55:53.729594+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 8.629 | entrée 7.150 | trend 8.900 | rang 8.249
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AXS-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.600 | entrée 5.850 | trend 8.400 | rang 7.462
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : IMX-EUR | action LATENT_ACCELERATOR | opportunité 8.133 | entrée 5.200 | trend 9.200 | rang 7.806
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : FLUID-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.454 | entrée 6.800 | trend 8.950 | rang 8.005
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AAVE-EUR — ACHETE_MAINTENANT — rank 8.249 — opportunité 8.629 — entrée 7.150 — trend 8.900

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.249
2. FLUID-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.005
3. IMX-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.806

## Accélération indépendante

- GLMR-EUR — CONFIRMED_ACCELERATION — score 9.409/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FOLD-EUR — CONFIRMED_ACCELERATION — score 8.607/10 — DETECTED_BUT_TOO_LATE
- FLOCK-EUR — CONFIRMED_ACCELERATION — score 7.645/10 — DETECTED_BUT_TOO_LATE
- XDP-EUR — CONFIRMED_ACCELERATION — score 7.502/10 — DETECTED_BUT_TOO_LATE
- SWEAT-EUR — CONFIRMED_ACCELERATION — score 6.946/10 — DETECTED_BUT_TOO_LATE
- MOVR-EUR — CONFIRMED_ACCELERATION — score 6.692/10 — DETECTED_BUT_TOO_LATE
- SAND-EUR — BUILDING_ACCELERATION — score 5.897/10 — DETECTED_BUT_TOO_LATE
- MERL-EUR — BUILDING_ACCELERATION — score 5.318/10 — DETECTED_BUT_TOO_LATE
- XAN-EUR — BUILDING_ACCELERATION — score 4.805/10 — DETECTED_BUT_TOO_LATE
- AUDIO-EUR — BUILDING_ACCELERATION — score 4.804/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GLMR-EUR — ACTIVE_NOW — score mémoire 9.409/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- EDGE-EUR — MEMORY_DECAY_24_72H — score mémoire 9.396/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOVE-EUR — MEMORY_24H — score mémoire 8.978/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FOLD-EUR — ACTIVE_NOW — score mémoire 8.607/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.249/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOSO-EUR — MEMORY_24H — score mémoire 8.156/10 — sources ACCELERATION — MEMORY_ONLY
- FLUID-EUR — ACTIVE_NOW — score mémoire 8.005/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 7.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- IMX-EUR — ACTIVE_NOW — score mémoire 7.806/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAND-EUR +29.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QNT-EUR +14.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +13.75% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ATH-EUR +12.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENJ-EUR +9.48% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INIT-EUR +8.75% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SUPER-EUR +8.53% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- IMX-EUR +6.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FLUID-EUR +6.86% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- UP-EUR +6.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
