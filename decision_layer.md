# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T02:48:09.662740+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 8.516 | entrée 7.300 | trend 7.900 | rang 7.504
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : NEO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.460 | entrée 6.250 | trend 7.350 | rang 7.266
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SUPER-EUR | action LATENT_ACCELERATOR | opportunité 8.602 | entrée 5.400 | trend 7.950 | rang 7.449
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PLUME-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.314 | entrée 6.500 | trend 8.400 | rang 8.267
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. PLUME-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.267
2. AKT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.859
3. ZORA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.736

## Accélération indépendante

- MANTA-EUR — CONFIRMED_ACCELERATION — score 9.228/10 — DETECTED_BUT_TOO_LATE
- ICP-EUR — CONFIRMED_ACCELERATION — score 7.685/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VTHO-EUR — CONFIRMED_ACCELERATION — score 7.185/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZEN-EUR — CONFIRMED_ACCELERATION — score 7.064/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- STRK-EUR — CONFIRMED_ACCELERATION — score 6.763/10 — DETECTED_BUT_TOO_LATE
- MOODENG-EUR — CONFIRMED_ACCELERATION — score 6.750/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IMX-EUR — BUILDING_ACCELERATION — score 6.325/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ONT-EUR — BUILDING_ACCELERATION — score 5.971/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FLOKI-EUR — BUILDING_ACCELERATION — score 5.762/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MIOTA-EUR — BUILDING_ACCELERATION — score 5.740/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- LTC-EUR — ACTIVE_NOW — score mémoire 7.504/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- EIGEN-EUR — ACTIVE_NOW — score mémoire 7.047/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- IMU-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- TRIA-EUR — MEMORY_24H — score mémoire 9.929/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MANTA-EUR — ACTIVE_NOW — score mémoire 9.228/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- IKA-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TRAC-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NOM-EUR — MEMORY_24H — score mémoire 8.393/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PLUME-EUR — ACTIVE_NOW — score mémoire 8.267/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- NIL-EUR +50.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOM-EUR +34.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +18.33% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CPOOL-EUR +15.25% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +11.39% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DBR-EUR +11.30% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IMU-EUR +10.97% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- LSK-EUR +10.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +10.49% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CAP-EUR +9.88% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
