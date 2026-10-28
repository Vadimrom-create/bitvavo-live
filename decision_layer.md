# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-28T08:26:11.234781+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : PARTI-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.083 | entrée 4.650 | trend 8.450 | rang 6.836
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. PARTI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.836
2. DODO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.537
3. ELSA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.429

## Accélération indépendante

- BLUR-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- ICNT-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- AGI-EUR — BUILDING_ACCELERATION — score 6.072/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VSN-EUR — BUILDING_ACCELERATION — score 5.191/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PROMPT-EUR — BUILDING_ACCELERATION — score 5.069/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FOLD-EUR — BUILDING_ACCELERATION — score 5.051/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CELO-EUR — BUILDING_ACCELERATION — score 4.904/10 — DETECTED_BUT_TOO_LATE
- LAPTOP-EUR — BUILDING_ACCELERATION — score 4.854/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- BLUR-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- ICNT-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- U-EUR — MEMORY_DECAY_24_72H — score mémoire 8.443/10 — sources ACCELERATION — MEMORY_ONLY
- GROVE-EUR — MEMORY_24H — score mémoire 7.991/10 — sources ACCELERATION — MEMORY_ONLY
- BEAM-EUR — MEMORY_24H — score mémoire 6.884/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PARTI-EUR — ACTIVE_NOW — score mémoire 6.836/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- BABY-EUR — MEMORY_24H — score mémoire 6.780/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AZTEC-EUR — MEMORY_24H — score mémoire 6.763/10 — sources ACCELERATION — MEMORY_ONLY
- CHIP-EUR — MEMORY_24H — score mémoire 6.726/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- MEGA-EUR — MEMORY_24H — score mémoire 6.691/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- GROVE-EUR +110.24% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- XAN-EUR +64.61% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HAEDAL-EUR +27.45% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INIT-EUR +17.34% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PUFFER-EUR +16.71% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SOLV-EUR +16.32% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ACU-EUR +15.50% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PEPE-EUR +14.89% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SHELL-EUR +14.60% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DOS-EUR +14.31% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
