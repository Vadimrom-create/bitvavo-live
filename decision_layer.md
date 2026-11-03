# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-03T01:27:16.807577+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : BEAM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.560 | entrée 5.300 | trend 7.800 | rang 6.462
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. BEAM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.462

## Accélération indépendante

- NPC-EUR — CONFIRMED_ACCELERATION — score 6.718/10 — DETECTED_BUT_TOO_LATE
- EPIC-EUR — BUILDING_ACCELERATION — score 5.745/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRUST-EUR — BUILDING_ACCELERATION — score 5.035/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ACU-EUR — MEMORY_24H — score mémoire 9.208/10 — sources ACCELERATION — MEMORY_ONLY
- RUNE-EUR — MEMORY_24H — score mémoire 8.445/10 — sources ACCELERATION — MEMORY_ONLY
- SOLV-EUR — MEMORY_24H — score mémoire 6.894/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 6.718/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- PEPE-EUR — MEMORY_DECAY_24_72H — score mémoire 6.546/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BEAM-EUR — ACTIVE_NOW — score mémoire 6.462/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PARTI-EUR — MEMORY_24H — score mémoire 6.415/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_DECAY_24_72H — score mémoire 6.406/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- INIT-EUR — MEMORY_24H — score mémoire 6.318/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HAEDAL-EUR — MEMORY_24H — score mémoire 6.255/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY

## Audit des plus fortes hausses

- XMN-EUR +19.55% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HAEDAL-EUR +19.16% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HOT-EUR +10.48% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CAT-EUR +9.20% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CSPR-EUR +8.64% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICNT-EUR +8.00% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RUNE-EUR +6.94% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NOM-EUR +5.95% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TRUST-EUR +5.19% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LAPTOP-EUR +5.13% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
