# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T11:35:13.823238+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : RENDER-EUR | action ACHETE_MAINTENANT | opportunité 7.734 | entrée 6.850 | trend 7.900 | rang 7.346
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ARK-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.862 | entrée 6.100 | trend 8.200 | rang 7.887
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : STRK-EUR | action LATENT_ACCELERATOR | opportunité 8.129 | entrée 5.750 | trend 7.550 | rang 7.147
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MERL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.620 | entrée 6.400 | trend 8.300 | rang 7.896
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.896
2. ARK-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.887
3. LTC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.826

## Accélération indépendante

- FLOCK-EUR — CONFIRMED_ACCELERATION — score 9.446/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BEAM-EUR — CONFIRMED_ACCELERATION — score 8.656/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — CONFIRMED_ACCELERATION — score 7.061/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BILL-EUR — CONFIRMED_ACCELERATION — score 6.848/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GOAT-EUR — CONFIRMED_ACCELERATION — score 6.506/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EDEN-EUR — BUILDING_ACCELERATION — score 6.140/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BTT-EUR — BUILDING_ACCELERATION — score 5.871/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- THE-EUR — BUILDING_ACCELERATION — score 5.703/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PHA-EUR — BUILDING_ACCELERATION — score 5.251/10 — DETECTED_BUT_TOO_LATE
- CELR-EUR — BUILDING_ACCELERATION — score 5.165/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ZRC-EUR — MEMORY_24H — score mémoire 9.712/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEAQ-EUR — MEMORY_24H — score mémoire 9.627/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FLOCK-EUR — ACTIVE_NOW — score mémoire 9.446/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PROM-EUR — MEMORY_24H — score mémoire 9.255/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 8.917/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BEAM-EUR — ACTIVE_NOW — score mémoire 8.656/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CNPY-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- C98-EUR — MEMORY_24H — score mémoire 8.347/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- EDGE-EUR — MEMORY_24H — score mémoire 7.950/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- NOM-EUR +37.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +32.99% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- LSK-EUR +20.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IMU-EUR +18.94% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARX-EUR +16.31% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CNPY-EUR +12.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BEAM-EUR +12.10% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOSO-EUR +10.71% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- CVC-EUR +9.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +9.11% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
