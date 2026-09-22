# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T20:36:39.834855+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ETC-EUR | action ACHETE_MAINTENANT | opportunité 8.532 | entrée 7.300 | trend 8.100 | rang 7.899
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : 0G-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.762 | entrée 6.200 | trend 8.600 | rang 7.621
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : DUSK-EUR | action LATENT_ACCELERATOR | opportunité 8.174 | entrée 5.350 | trend 8.350 | rang 7.465
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : FET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.084 | entrée 8.200 | trend 8.400 | rang 8.137
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.137
2. ETC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.899
3. PYTH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.790

## Accélération indépendante

- XYO-EUR — CONFIRMED_ACCELERATION — score 6.700/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — BUILDING_ACCELERATION — score 6.180/10 — DETECTED_BUT_TOO_LATE
- AIXBT-EUR — BUILDING_ACCELERATION — score 5.962/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PTB-EUR — BUILDING_ACCELERATION — score 5.916/10 — DETECTED_BUT_TOO_LATE
- LAPTOP-EUR — BUILDING_ACCELERATION — score 5.554/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRO-EUR — BUILDING_ACCELERATION — score 5.388/10 — DETECTED_BUT_TOO_LATE
- MERL-EUR — BUILDING_ACCELERATION — score 5.381/10 — DETECTED_BUT_TOO_LATE
- SWEAT-EUR — BUILDING_ACCELERATION — score 5.375/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BOME-EUR — BUILDING_ACCELERATION — score 5.296/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NES-EUR — BUILDING_ACCELERATION — score 5.244/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- TREAD-EUR — MEMORY_24H — score mémoire 9.440/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- APE-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 8.137/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ETC-EUR — ACTIVE_NOW — score mémoire 7.899/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CHR-EUR — MEMORY_24H — score mémoire 7.801/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 7.790/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TRAC-EUR — MEMORY_24H — score mémoire 7.788/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SOL-EUR — ACTIVE_NOW — score mémoire 7.781/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- DRIFT-EUR +44.79% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHR-EUR +28.41% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- BCH-EUR +28.33% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +25.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PENGU-EUR +18.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KITE-EUR +17.09% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- USELESS-EUR +16.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +16.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +16.29% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +16.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
