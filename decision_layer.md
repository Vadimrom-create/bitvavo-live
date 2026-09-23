# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T08:57:15.700595+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : MAGIC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.181 | entrée 5.800 | trend 8.350 | rang 8.121
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BIGTIME-EUR | action LATENT_ACCELERATOR | opportunité 7.591 | entrée 4.500 | trend 8.950 | rang 7.448
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ZBT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.366 | entrée 6.750 | trend 8.700 | rang 8.427
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ZBT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.427
2. MAGIC-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 8.121
3. LTC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.064

## Accélération indépendante

- CPOOL-EUR — CONFIRMED_ACCELERATION — score 8.975/10 — DETECTED_BUT_TOO_LATE
- ZIG-EUR — CONFIRMED_ACCELERATION — score 6.502/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MEME-EUR — BUILDING_ACCELERATION — score 4.821/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ZIG-EUR — ACTIVE_NOW — score mémoire 7.390/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- IKA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 9.359/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SLX-EUR — MEMORY_24H — score mémoire 9.336/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CPOOL-EUR — ACTIVE_NOW — score mémoire 8.975/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CETUS-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZBT-EUR — ACTIVE_NOW — score mémoire 8.427/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MAGIC-EUR — ACTIVE_NOW — score mémoire 8.121/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.118/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CPOOL-EUR +47.30% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BCH-EUR +32.39% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MET-EUR +30.27% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +26.86% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHR-EUR +23.59% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- NIL-EUR +23.16% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +20.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALLO-EUR +19.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PENGU-EUR +17.48% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UP-EUR +17.35% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
