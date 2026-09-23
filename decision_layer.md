# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T15:00:54.531858+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : MEW-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.091 | entrée 5.950 | trend 7.850 | rang 7.542
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ARPA-EUR | action LATENT_ACCELERATOR | opportunité 8.367 | entrée 5.000 | trend 9.000 | rang 7.884
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : WAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.486 | entrée 5.200 | trend 8.900 | rang 7.972
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.972
2. LPT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.966
3. ARPA-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.884

## Accélération indépendante

- SAGA-EUR — CONFIRMED_ACCELERATION — score 8.191/10 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — BUILDING_ACCELERATION — score 6.430/10 — DETECTED_BUT_TOO_LATE
- ACU-EUR — BUILDING_ACCELERATION — score 6.226/10 — DETECTED_BUT_TOO_LATE
- AGLD-EUR — BUILDING_ACCELERATION — score 6.044/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SWELL-EUR — BUILDING_ACCELERATION — score 6.032/10 — DETECTED_BUT_TOO_LATE
- CTR-EUR — BUILDING_ACCELERATION — score 5.739/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- INIT-EUR — BUILDING_ACCELERATION — score 5.728/10 — DETECTED_BUT_TOO_LATE
- NEO-EUR — BUILDING_ACCELERATION — score 5.284/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LAPTOP-EUR — BUILDING_ACCELERATION — score 5.221/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NOT-EUR — BUILDING_ACCELERATION — score 5.005/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- TRIA-EUR — MEMORY_24H — score mémoire 9.219/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CPOOL-EUR — MEMORY_24H — score mémoire 8.705/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SAGA-EUR — ACTIVE_NOW — score mémoire 8.191/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- WIN-EUR — MEMORY_24H — score mémoire 8.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LINK-EUR — MEMORY_24H — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.972/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PORTAL-EUR — MEMORY_24H — score mémoire 7.969/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LPT-EUR — ACTIVE_NOW — score mémoire 7.966/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ARPA-EUR — ACTIVE_NOW — score mémoire 7.884/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XRP-EUR — MEMORY_24H — score mémoire 7.855/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CPOOL-EUR +38.34% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ALLO-EUR +31.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +28.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MET-EUR +26.79% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +25.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DBR-EUR +19.04% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- KMNO-EUR +17.53% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +17.29% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PROM-EUR +16.30% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ACE-EUR +15.11% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
