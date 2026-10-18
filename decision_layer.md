# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-18T17:28:38.784931+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : TIA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.968 | entrée 5.550 | trend 7.950 | rang 6.693
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. TIA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.693
2. ALT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.650
3. RSR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.506

## Accélération indépendante

- GTC-EUR — CONFIRMED_ACCELERATION — score 8.028/10 — DETECTED_BUT_TOO_LATE
- EPIC-EUR — BUILDING_ACCELERATION — score 6.478/10 — DETECTED_BUT_TOO_LATE
- ELSA-EUR — BUILDING_ACCELERATION — score 5.865/10 — DETECTED_BUT_TOO_LATE
- POND-EUR — BUILDING_ACCELERATION — score 5.657/10 — DETECTED_BUT_TOO_LATE
- ZBCN-EUR — BUILDING_ACCELERATION — score 5.096/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TREAD-EUR — BUILDING_ACCELERATION — score 5.007/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AVA-EUR — BUILDING_ACCELERATION — score 4.982/10 — DETECTED_BUT_TOO_LATE
- ZIG-EUR — BUILDING_ACCELERATION — score 4.855/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- JASMY-EUR — BUILDING_ACCELERATION — score 4.807/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GTC-EUR — ACTIVE_NOW — score mémoire 8.028/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- WAL-EUR — MEMORY_24H — score mémoire 7.187/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_DECAY_24_72H — score mémoire 7.049/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BEAM-EUR — MEMORY_24H — score mémoire 6.981/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- METIS-EUR — MEMORY_24H — score mémoire 6.971/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- AXL-EUR — MEMORY_DECAY_24_72H — score mémoire 6.964/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- EDU-EUR — MEMORY_24H — score mémoire 6.958/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DUSK-EUR — MEMORY_24H — score mémoire 6.864/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- KMNO-EUR — MEMORY_24H — score mémoire 6.761/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TIA-EUR — ACTIVE_NOW — score mémoire 6.693/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ELSA-EUR +19.86% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WHUF-EUR +17.58% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- QKC-EUR +17.57% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GTC-EUR +17.37% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AIOZ-EUR +7.16% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- OSMO-EUR +7.14% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GLMR-EUR +6.50% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AMP-EUR +4.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HBAR-EUR +3.52% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SENT-EUR +2.61% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
