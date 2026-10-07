# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-07T06:23:37.156777+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : RENDER-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.592 | entrée 6.700 | trend 8.700 | rang 7.366
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. RENDER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.366
2. SENT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.204
3. ESP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.160

## Accélération indépendante

- PARTI-EUR — CONFIRMED_ACCELERATION — score 8.123/10 — DETECTED_BUT_TOO_LATE
- GTC-EUR — BUILDING_ACCELERATION — score 6.208/10 — DETECTED_BUT_TOO_LATE
- SWEAT-EUR — BUILDING_ACCELERATION — score 4.922/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- POND-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- UMA-EUR — MEMORY_24H — score mémoire 9.443/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CHIP-EUR — MEMORY_24H — score mémoire 8.278/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PARTI-EUR — ACTIVE_NOW — score mémoire 8.123/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SOSO-EUR — MEMORY_24H — score mémoire 7.615/10 — sources ACCELERATION — MEMORY_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 7.366/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 7.349/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ARPA-EUR — MEMORY_24H — score mémoire 7.305/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MIOTA-EUR — MEMORY_24H — score mémoire 7.205/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 7.204/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZEUS-EUR +74.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NMR-EUR +39.42% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ORCA-EUR +18.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- POND-EUR +18.17% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- EDGE-EUR +14.61% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SAND-EUR +14.37% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PARTI-EUR +10.07% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CAP-EUR +9.96% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SOSO-EUR +9.04% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MAGIC-EUR +8.64% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
