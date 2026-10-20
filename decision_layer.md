# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-20T13:06:04.507313+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : BEAM-EUR | action LATENT_ACCELERATOR | opportunité 7.443 | entrée 5.300 | trend 8.750 | rang 6.919
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : OSMO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.196 | entrée 5.600 | trend 8.150 | rang 6.298
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. BEAM-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.919
2. OSMO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.298

## Accélération indépendante

- DOS-EUR — BUILDING_ACCELERATION — score 5.924/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RSR-EUR — BUILDING_ACCELERATION — score 4.942/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CTR-EUR — BUILDING_ACCELERATION — score 4.868/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GNS-EUR — MEMORY_24H — score mémoire 9.505/10 — sources ACCELERATION — MEMORY_ONLY
- POND-EUR — MEMORY_24H — score mémoire 8.833/10 — sources ACCELERATION — MEMORY_ONLY
- WHUF-EUR — MEMORY_24H — score mémoire 7.643/10 — sources ACCELERATION — MEMORY_ONLY
- AVA-EUR — MEMORY_24H — score mémoire 7.332/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DODO-EUR — MEMORY_24H — score mémoire 6.968/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- METIS-EUR — MEMORY_24H — score mémoire 6.932/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- BEAM-EUR — ACTIVE_NOW — score mémoire 6.919/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- KMNO-EUR — MEMORY_24H — score mémoire 6.888/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 6.780/10 — sources ACCELERATION — MEMORY_ONLY
- TIA-EUR — MEMORY_24H — score mémoire 6.675/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- GNS-EUR +41.01% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ALT-EUR +22.45% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PHA-EUR +15.77% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- IMU-EUR +14.50% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BEAM-EUR +12.45% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PUFFER-EUR +11.82% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- IOST-EUR +10.17% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- REZ-EUR +9.99% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- WHUF-EUR +9.23% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- METIS-EUR +9.08% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
