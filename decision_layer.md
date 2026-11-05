# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-05T22:55:56.569317+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : ELSA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.879 | entrée 5.800 | trend 8.000 | rang 6.619
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ELSA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.619

## Accélération indépendante

- UP-EUR — CONFIRMED_ACCELERATION — score 8.025/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EPIC-EUR — BUILDING_ACCELERATION — score 5.319/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ESP-EUR — BUILDING_ACCELERATION — score 4.983/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 9.632/10 — sources ACCELERATION — MEMORY_ONLY
- ADX-EUR — MEMORY_DECAY_24_72H — score mémoire 8.969/10 — sources ACCELERATION — MEMORY_ONLY
- CHILLGUY-EUR — MEMORY_DECAY_24_72H — score mémoire 8.826/10 — sources ACCELERATION — MEMORY_ONLY
- PUFFER-EUR — MEMORY_DECAY_24_72H — score mémoire 8.619/10 — sources ACCELERATION — MEMORY_ONLY
- ALIGN-EUR — MEMORY_24H — score mémoire 8.589/10 — sources ACCELERATION — MEMORY_ONLY
- UP-EUR — ACTIVE_NOW — score mémoire 8.025/10 — sources ACCELERATION — WATCH_ONLY
- BREV-EUR — MEMORY_DECAY_24_72H — score mémoire 7.884/10 — sources ACCELERATION — MEMORY_ONLY
- ARX-EUR — MEMORY_24H — score mémoire 7.773/10 — sources ACCELERATION — MEMORY_ONLY
- JTO-EUR — MEMORY_DECAY_24_72H — score mémoire 7.603/10 — sources ACCELERATION — MEMORY_ONLY
- KMNO-EUR — MEMORY_DECAY_24_72H — score mémoire 7.378/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- ALIGN-EUR +20.64% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CYBER-EUR +16.86% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- EDGE-EUR +16.71% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CAP-EUR +14.50% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- UP-EUR +12.66% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PROMPT-EUR +10.10% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BIRB-EUR +7.59% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PARTI-EUR +5.28% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TREAD-EUR +4.65% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- LAPTOP-EUR +4.61% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
