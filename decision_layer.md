# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-12T02:03:54.558818+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : BEAM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.491 | entrée 5.750 | trend 7.750 | rang 6.466
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. BEAM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.466

## Accélération indépendante

- WIN-EUR — CONFIRMED_ACCELERATION — score 9.693/10 — DETECTED_BUT_TOO_LATE
- MLN-EUR — BUILDING_ACCELERATION — score 6.326/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZEUS-EUR — BUILDING_ACCELERATION — score 6.265/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- WIN-EUR — ACTIVE_NOW — score mémoire 9.693/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- CPOOL-EUR — MEMORY_DECAY_24_72H — score mémoire 8.635/10 — sources ACCELERATION — MEMORY_ONLY
- THQ-EUR — MEMORY_DECAY_24_72H — score mémoire 8.026/10 — sources ACCELERATION — MEMORY_ONLY
- MERL-EUR — MEMORY_DECAY_24_72H — score mémoire 7.883/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- FOLD-EUR — MEMORY_DECAY_24_72H — score mémoire 7.406/10 — sources ACCELERATION — MEMORY_ONLY
- PEPE-EUR — MEMORY_DECAY_24_72H — score mémoire 6.942/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 6.872/10 — sources ACCELERATION — MEMORY_ONLY
- BEAM-EUR — ACTIVE_NOW — score mémoire 6.466/10 — sources DECISION_LAYER — WATCH_ONLY
- GRASS-EUR — MEMORY_24H — score mémoire 6.449/10 — sources ACCELERATION — MEMORY_ONLY
- NPC-EUR — MEMORY_24H — score mémoire 6.431/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- EPIC-EUR +12.02% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TREAD-EUR +10.36% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- WHUF-EUR +10.02% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GNS-EUR +9.98% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZBCN-EUR +8.39% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- MLN-EUR +6.99% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GRAM-EUR +6.44% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HAEDAL-EUR +6.30% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ARX-EUR +5.96% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SXT-EUR +5.69% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
