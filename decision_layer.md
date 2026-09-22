# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T16:40:41.125171+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : DRIFT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.722 | entrée 6.150 | trend 8.200 | rang 7.719
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ZIL-EUR | action LATENT_ACCELERATOR | opportunité 7.431 | entrée 5.650 | trend 8.100 | rang 6.902
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MERL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.094 | entrée 6.900 | trend 8.850 | rang 8.220
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.220
2. THE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.045
3. FLUX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.950

## Accélération indépendante

- YGG-EUR — CONFIRMED_ACCELERATION — score 9.515/10 — DETECTED_BUT_TOO_LATE
- SAGA-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- ZRO-EUR — CONFIRMED_ACCELERATION — score 6.930/10 — DETECTED_BUT_TOO_LATE
- VELO-EUR — CONFIRMED_ACCELERATION — score 6.548/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DYM-EUR — BUILDING_ACCELERATION — score 5.909/10 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — BUILDING_ACCELERATION — score 5.527/10 — DETECTED_BUT_TOO_LATE
- EPIC-EUR — BUILDING_ACCELERATION — score 5.219/10 — DETECTED_BUT_TOO_LATE
- AGLD-EUR — BUILDING_ACCELERATION — score 5.158/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PTB-EUR — BUILDING_ACCELERATION — score 5.146/10 — DETECTED_BUT_TOO_LATE
- AIOZ-EUR — BUILDING_ACCELERATION — score 5.092/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CHR-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- YGG-EUR — ACTIVE_NOW — score mémoire 9.515/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- SAGA-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- U-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MAGIC-EUR — MEMORY_24H — score mémoire 8.394/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MERL-EUR — ACTIVE_NOW — score mémoire 8.220/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- THE-EUR — ACTIVE_NOW — score mémoire 8.045/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FLUX-EUR — ACTIVE_NOW — score mémoire 7.950/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CHR-EUR +44.76% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- NIL-EUR +25.89% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FLOCK-EUR +24.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BCH-EUR +22.50% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +20.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +17.51% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +17.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +16.50% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KITE-EUR +16.20% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- S-EUR +13.42% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
