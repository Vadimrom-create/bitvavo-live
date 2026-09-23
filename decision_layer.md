# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T08:00:16.715079+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : MANTA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.673 | entrée 6.100 | trend 8.350 | rang 7.506
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : RED-EUR | action LATENT_ACCELERATOR | opportunité 7.913 | entrée 5.700 | trend 8.650 | rang 7.623
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : KMNO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.418 | entrée 6.700 | trend 8.850 | rang 8.315
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. KMNO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.315
2. QNT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.143
3. SEI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.026

## Accélération indépendante

- MAVIA-EUR — CONFIRMED_ACCELERATION — score 8.871/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BTT-EUR — CONFIRMED_ACCELERATION — score 8.284/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LPT-EUR — CONFIRMED_ACCELERATION — score 7.701/10 — DETECTED_BUT_TOO_LATE
- KERNEL-EUR — CONFIRMED_ACCELERATION — score 7.188/10 — DETECTED_BUT_TOO_LATE
- NMR-EUR — BUILDING_ACCELERATION — score 5.022/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- IKA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CPOOL-EUR — MEMORY_24H — score mémoire 9.530/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SLX-EUR — MEMORY_24H — score mémoire 9.336/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- MAVIA-EUR — ACTIVE_NOW — score mémoire 8.871/10 — sources ACCELERATION, V4 — WATCH_ONLY
- CETUS-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- KMNO-EUR — ACTIVE_NOW — score mémoire 8.315/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- BTT-EUR — ACTIVE_NOW — score mémoire 8.284/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- QNT-EUR — ACTIVE_NOW — score mémoire 8.143/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- NIL-EUR +48.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CPOOL-EUR +37.80% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MET-EUR +34.57% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BCH-EUR +30.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +28.06% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHR-EUR +23.66% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- UP-EUR +20.66% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- ZRO-EUR +20.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SENT-EUR +19.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PENGU-EUR +19.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
