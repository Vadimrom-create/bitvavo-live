# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-23T01:24:21.181939+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : CROSS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.527 | entrée 5.200 | trend 7.850 | rang 6.452
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. CROSS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.452
2. LISTA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 5.529

## Accélération indépendante

- ELSA-EUR — CONFIRMED_ACCELERATION — score 7.755/10 — DETECTED_BUT_TOO_LATE
- EPIC-EUR — CONFIRMED_ACCELERATION — score 6.856/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AUDIO-EUR — BUILDING_ACCELERATION — score 4.911/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ZBCN-EUR — MEMORY_24H — score mémoire 7.991/10 — sources ACCELERATION — MEMORY_ONLY
- ELSA-EUR — ACTIVE_NOW — score mémoire 7.755/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- ZEUS-EUR — MEMORY_24H — score mémoire 7.598/10 — sources ACCELERATION — MEMORY_ONLY
- ORCA-EUR — MEMORY_DECAY_24_72H — score mémoire 7.392/10 — sources ACCELERATION — MEMORY_ONLY
- NPC-EUR — MEMORY_DECAY_24_72H — score mémoire 7.239/10 — sources ACCELERATION — MEMORY_ONLY
- KITE-EUR — ACTIVE_NOW — score mémoire 7.073/10 — sources V4 — WATCH_ONLY
- NES-EUR — MEMORY_24H — score mémoire 7.064/10 — sources ACCELERATION — MEMORY_ONLY
- EPIC-EUR — ACTIVE_NOW — score mémoire 6.856/10 — sources ACCELERATION — WATCH_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 6.780/10 — sources ACCELERATION — MEMORY_ONLY
- RARE-EUR — MEMORY_24H — score mémoire 6.604/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY

## Audit des plus fortes hausses

- ELSA-EUR +21.94% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LISTA-EUR +17.90% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ALIGN-EUR +12.52% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DRV-EUR +9.99% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- VELO-EUR +9.69% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PUMP-EUR +9.47% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- GROVE-EUR +9.24% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ZKJ-EUR +7.02% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- KITE-EUR +6.49% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- JTO-EUR +6.32% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
