# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-03T05:03:08.734933+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : WLD-EUR | action ACHETE_MAINTENANT | opportunité 8.143 | entrée 6.900 | trend 8.700 | rang 7.864
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : INIT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.702 | entrée 6.200 | trend 8.500 | rang 7.586
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MAGIC-EUR | action LATENT_ACCELERATOR | opportunité 7.720 | entrée 4.950 | trend 8.650 | rang 7.415
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : FLUID-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.917 | entrée 6.850 | trend 9.000 | rang 8.288
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. WLD-EUR — ACHETE_MAINTENANT — rank 7.864 — opportunité 8.143 — entrée 6.900 — trend 8.700

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. FLUID-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.288
2. GRASS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.929
3. ORCA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.908

## Accélération indépendante

- SYN-EUR — CONFIRMED_ACCELERATION — score 9.039/10 — DETECTED_BUT_TOO_LATE
- MOVR-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- UP-EUR — CONFIRMED_ACCELERATION — score 6.991/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOLV-EUR — BUILDING_ACCELERATION — score 5.567/10 — DETECTED_BUT_TOO_LATE
- CT-EUR — BUILDING_ACCELERATION — score 4.818/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_DECAY_24_72H — score mémoire 9.996/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SYN-EUR — ACTIVE_NOW — score mémoire 9.039/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOVE-EUR — MEMORY_24H — score mémoire 8.978/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOVR-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- FLUID-EUR — ACTIVE_NOW — score mémoire 8.288/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOSO-EUR — MEMORY_24H — score mémoire 8.156/10 — sources ACCELERATION — MEMORY_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 7.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- GRASS-EUR — ACTIVE_NOW — score mémoire 7.929/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ORCA-EUR — ACTIVE_NOW — score mémoire 7.908/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAND-EUR +74.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MANA-EUR +23.09% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ENJ-EUR +16.51% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GALA-EUR +12.99% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AXS-EUR +10.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APE-EUR +10.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ATH-EUR +9.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BAT-EUR +9.20% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- YGG-EUR +8.28% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- AGI-EUR +8.24% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

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
