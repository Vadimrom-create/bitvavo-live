# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-26T14:10:15.386589+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : WIN-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.657 | entrée 6.100 | trend 8.650 | rang 6.908
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. WIN-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.908
2. INIT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.751
3. GRASS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.529

## Accélération indépendante

- PTB-EUR — CONFIRMED_ACCELERATION — score 8.912/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KAT-EUR — CONFIRMED_ACCELERATION — score 6.995/10 — DETECTED_BUT_TOO_LATE
- U-EUR — BUILDING_ACCELERATION — score 6.186/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- PTB-EUR — ACTIVE_NOW — score mémoire 8.912/10 — sources ACCELERATION — WATCH_ONLY
- WHUF-EUR — MEMORY_24H — score mémoire 8.890/10 — sources ACCELERATION — MEMORY_ONLY
- TREAD-EUR — MEMORY_DECAY_24_72H — score mémoire 8.668/10 — sources ACCELERATION — MEMORY_ONLY
- PROMPT-EUR — MEMORY_24H — score mémoire 8.512/10 — sources ACCELERATION — MEMORY_ONLY
- AMP-EUR — MEMORY_24H — score mémoire 7.596/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IQ-EUR — MEMORY_DECAY_24_72H — score mémoire 7.440/10 — sources ACCELERATION — MEMORY_ONLY
- PHA-EUR — MEMORY_24H — score mémoire 7.246/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- ELSA-EUR — MEMORY_24H — score mémoire 7.215/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HAEDAL-EUR — MEMORY_24H — score mémoire 7.035/10 — sources ACCELERATION — MEMORY_ONLY
- AVA-EUR — MEMORY_24H — score mémoire 7.018/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- NEX-EUR +24.64% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- KAT-EUR +17.79% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- QNT-EUR +15.41% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BEAM-EUR +14.34% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CHIP-EUR +10.82% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BABY-EUR +10.78% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- U-EUR +10.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- OSMO-EUR +10.26% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NOM-EUR +8.96% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HAEDAL-EUR +7.34% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
