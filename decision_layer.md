# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-25T19:22:40.185916+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : DODO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.921 | entrée 6.100 | trend 8.800 | rang 7.054
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : ELSA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.831 | entrée 6.900 | trend 8.650 | rang 7.449
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ELSA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.449
2. INIT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.439
3. DODO-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.054

## Accélération indépendante

- U-EUR — CONFIRMED_ACCELERATION — score 6.844/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZEUS-EUR — BUILDING_ACCELERATION — score 5.489/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DODO-EUR — BUILDING_ACCELERATION — score 4.903/10 — DETECTED_BUT_TOO_LATE
- GIGA-EUR — BUILDING_ACCELERATION — score 4.848/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- TREAD-EUR — MEMORY_24H — score mémoire 8.974/10 — sources ACCELERATION — MEMORY_ONLY
- BIRB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- IQ-EUR — MEMORY_24H — score mémoire 7.702/10 — sources ACCELERATION — MEMORY_ONLY
- AMP-EUR — MEMORY_24H — score mémoire 7.596/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BABY-EUR — MEMORY_24H — score mémoire 7.580/10 — sources ACCELERATION — MEMORY_ONLY
- CHIP-EUR — MEMORY_DECAY_24_72H — score mémoire 7.473/10 — sources ACCELERATION — MEMORY_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 7.452/10 — sources ACCELERATION — MEMORY_ONLY
- ELSA-EUR — ACTIVE_NOW — score mémoire 7.449/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- INIT-EUR — ACTIVE_NOW — score mémoire 7.439/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- USELESS-EUR — MEMORY_24H — score mémoire 7.391/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- CAP-EUR +38.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +24.31% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CNPY-EUR +21.65% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- T-EUR +18.45% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GRASS-EUR +13.00% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CT-EUR +11.30% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- INIT-EUR +10.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ENA-EUR +10.25% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- QNT-EUR +9.02% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- KMNO-EUR +8.25% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
