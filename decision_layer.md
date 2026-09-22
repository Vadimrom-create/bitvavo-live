# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T21:06:41.285050+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ETC-EUR | action ACHETE_MAINTENANT | opportunité 9.202 | entrée 7.750 | trend 8.100 | rang 8.250
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : BEAM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.758 | entrée 5.950 | trend 8.500 | rang 7.513
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : DEEP-EUR | action LATENT_ACCELERATOR | opportunité 8.155 | entrée 5.200 | trend 8.300 | rang 7.343
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : WAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.563 | entrée 7.100 | trend 8.850 | rang 7.992
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ETC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.250
2. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.992
3. ARX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.792

## Accélération indépendante

- CTC-EUR — CONFIRMED_ACCELERATION — score 8.914/10 — DETECTED_BUT_TOO_LATE
- GRT-EUR — BUILDING_ACCELERATION — score 6.288/10 — DETECTED_BUT_TOO_LATE
- LUNA-EUR — BUILDING_ACCELERATION — score 5.703/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SAFE-EUR — BUILDING_ACCELERATION — score 4.900/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARX-EUR — BUILDING_ACCELERATION — score 4.843/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- TREAD-EUR — MEMORY_24H — score mémoire 9.440/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CTC-EUR — ACTIVE_NOW — score mémoire 8.914/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- APE-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ETC-EUR — ACTIVE_NOW — score mémoire 8.250/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.992/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CHR-EUR — MEMORY_24H — score mémoire 7.801/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AXL-EUR — ACTIVE_NOW — score mémoire 7.798/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- DRIFT-EUR +33.47% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHR-EUR +30.05% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- BCH-EUR +28.01% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +22.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +17.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +17.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PENGU-EUR +16.99% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +16.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KITE-EUR +16.31% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +15.62% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
