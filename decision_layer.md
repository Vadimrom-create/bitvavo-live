# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-17T05:30:29.252049+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DODO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.068 | entrée 6.250 | trend 7.950 | rang 6.852
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. DODO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.852
2. KITE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.335
3. CROSS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 5.342

## Accélération indépendante

- EPIC-EUR — CONFIRMED_ACCELERATION — score 7.286/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- INIT-EUR — BUILDING_ACCELERATION — score 6.426/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FARTCOIN-EUR — BUILDING_ACCELERATION — score 5.933/10 — DETECTED_BUT_TOO_LATE
- SQD-EUR — BUILDING_ACCELERATION — score 5.871/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IMU-EUR — BUILDING_ACCELERATION — score 5.672/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CROSS-EUR — BUILDING_ACCELERATION — score 4.881/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- HFT-EUR — MEMORY_24H — score mémoire 9.204/10 — sources ACCELERATION — MEMORY_ONLY
- EPIC-EUR — ACTIVE_NOW — score mémoire 7.286/10 — sources ACCELERATION — WATCH_ONLY
- AMP-EUR — MEMORY_24H — score mémoire 7.254/10 — sources ACCELERATION — MEMORY_ONLY
- DODO-EUR — ACTIVE_NOW — score mémoire 6.852/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 6.696/10 — sources ACCELERATION — MEMORY_ONLY
- ASTER-EUR — MEMORY_DECAY_24_72H — score mémoire 6.436/10 — sources ACCELERATION — MEMORY_ONLY
- INIT-EUR — ACTIVE_NOW — score mémoire 6.426/10 — sources ACCELERATION — WATCH_ONLY
- KITE-EUR — ACTIVE_NOW — score mémoire 6.335/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- CAP-EUR — MEMORY_24H — score mémoire 6.287/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- BEAM-EUR — MEMORY_24H — score mémoire 6.108/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- HUMA-EUR +38.81% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CROSS-EUR +29.83% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- O-EUR +15.20% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AXIS-EUR +12.33% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HFT-EUR +11.98% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICP-EUR +11.30% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LIGHTER-EUR +11.16% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MMT-EUR +10.40% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZAMA-EUR +9.47% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- GLMR-EUR +9.20% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
