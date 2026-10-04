# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-04T02:22:16.600615+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : FLUID-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.738 | entrée 6.200 | trend 9.200 | rang 7.302
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : AAVE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.258 | entrée 6.500 | trend 9.200 | rang 7.935
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.935
2. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.526
3. SYRUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.355

## Accélération indépendante

- ZIG-EUR — CONFIRMED_ACCELERATION — score 6.875/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GLMR-EUR — CONFIRMED_ACCELERATION — score 6.781/10 — DETECTED_BUT_TOO_LATE
- EDGE-EUR — BUILDING_ACCELERATION — score 5.807/10 — DETECTED_BUT_TOO_LATE
- ELSA-EUR — BUILDING_ACCELERATION — score 5.095/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- MOVE-EUR — MEMORY_DECAY_24_72H — score mémoire 8.700/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARK-EUR — MEMORY_24H — score mémoire 8.048/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.935/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ATH-EUR — MEMORY_24H — score mémoire 7.764/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FLOCK-EUR — MEMORY_24H — score mémoire 7.645/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RLC-EUR — MEMORY_24H — score mémoire 7.622/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 7.582/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BAT-EUR — MEMORY_24H — score mémoire 7.532/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 7.526/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- GLMR-EUR +44.50% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +32.80% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TREAD-EUR +25.38% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HFT-EUR +22.99% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FUN-EUR +21.81% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- STRK-EUR +21.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +17.19% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- MERL-EUR +15.10% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZRO-EUR +14.81% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PUMP-EUR +12.07% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
