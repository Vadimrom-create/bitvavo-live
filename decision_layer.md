# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-19T20:11:15.690524+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : ALT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.201 | entrée 5.700 | trend 8.200 | rang 6.869
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ALT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.869
2. TIA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.759
3. OSMO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 4.979

## Accélération indépendante

- SQD-EUR — BUILDING_ACCELERATION — score 4.872/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EDGE-EUR — BUILDING_ACCELERATION — score 4.851/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IMU-EUR — BUILDING_ACCELERATION — score 4.813/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CTR-EUR — MEMORY_24H — score mémoire 9.247/10 — sources ACCELERATION — MEMORY_ONLY
- WHUF-EUR — MEMORY_24H — score mémoire 8.811/10 — sources ACCELERATION — MEMORY_ONLY
- MANTRA-EUR — MEMORY_24H — score mémoire 8.592/10 — sources ACCELERATION — MEMORY_ONLY
- VVV-EUR — MEMORY_24H — score mémoire 8.341/10 — sources ACCELERATION — MEMORY_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 7.457/10 — sources ACCELERATION — MEMORY_ONLY
- HUMA-EUR — MEMORY_24H — score mémoire 6.991/10 — sources ACCELERATION — MEMORY_ONLY
- DODO-EUR — MEMORY_24H — score mémoire 6.968/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- KMNO-EUR — ACTIVE_NOW — score mémoire 6.878/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ALT-EUR — ACTIVE_NOW — score mémoire 6.869/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TIA-EUR — ACTIVE_NOW — score mémoire 6.759/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PHA-EUR +35.51% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AVA-EUR +31.82% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GTC-EUR +30.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTR-EUR +27.40% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- OSMO-EUR +23.71% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NIL-EUR +18.89% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- S-EUR +16.02% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- VVV-EUR +14.36% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BAT-EUR +12.77% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- WELL-EUR +12.46% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
