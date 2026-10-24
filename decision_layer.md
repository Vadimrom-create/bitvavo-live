# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-24T13:42:40.104114+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : INIT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.560 | entrée 6.350 | trend 8.900 | rang 7.139
  - Strong structure but imperfect current entry; prefer passive execution. High extension/chase reduces rank but does not erase the setup.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : BEAM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.149 | entrée 5.050 | trend 8.050 | rang 6.766
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. INIT-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.139
2. BEAM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.766

## Accélération indépendante

- PTB-EUR — CONFIRMED_ACCELERATION — score 9.557/10 — DETECTED_BUT_TOO_LATE
- EPIC-EUR — CONFIRMED_ACCELERATION — score 9.066/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ANIME-EUR — CONFIRMED_ACCELERATION — score 6.900/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KAT-EUR — BUILDING_ACCELERATION — score 6.044/10 — DETECTED_BUT_TOO_LATE
- GTC-EUR — BUILDING_ACCELERATION — score 5.656/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AZTEC-EUR — BUILDING_ACCELERATION — score 4.785/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- PTB-EUR — ACTIVE_NOW — score mémoire 9.557/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- EPIC-EUR — ACTIVE_NOW — score mémoire 9.066/10 — sources ACCELERATION — WATCH_ONLY
- SYN-EUR — MEMORY_24H — score mémoire 8.740/10 — sources ACCELERATION — MEMORY_ONLY
- ARK-EUR — MEMORY_24H — score mémoire 8.689/10 — sources ACCELERATION — MEMORY_ONLY
- TREE-EUR — MEMORY_24H — score mémoire 8.663/10 — sources ACCELERATION — MEMORY_ONLY
- BIRB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 7.754/10 — sources ACCELERATION — MEMORY_ONLY
- AXIS-EUR — MEMORY_24H — score mémoire 7.606/10 — sources ACCELERATION — MEMORY_ONLY
- BREV-EUR — MEMORY_24H — score mémoire 7.538/10 — sources ACCELERATION — MEMORY_ONLY
- 2Z-EUR — MEMORY_24H — score mémoire 7.503/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- BIRB-EUR +60.49% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- IRYS-EUR +42.01% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- U-EUR +18.62% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TREE-EUR +18.55% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- INIT-EUR +12.67% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- KAT-EUR +11.41% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ACU-EUR +10.69% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RECALL-EUR +10.25% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ANIME-EUR +9.71% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LUMIA-EUR +9.17% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
