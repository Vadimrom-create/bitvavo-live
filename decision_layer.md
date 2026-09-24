# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T23:26:11.873332+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : GMT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.040 | entrée 6.100 | trend 9.000 | rang 7.903
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ATH-EUR | action LATENT_ACCELERATOR | opportunité 8.875 | entrée 5.450 | trend 8.100 | rang 7.652
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : BONK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.258 | entrée 7.400 | trend 8.100 | rang 8.152
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. BONK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.152
2. ICP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.000
3. DRIFT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.982

## Accélération indépendante

- ZRC-EUR — CONFIRMED_ACCELERATION — score 8.343/10 — DETECTED_BUT_TOO_LATE
- DYM-EUR — CONFIRMED_ACCELERATION — score 6.953/10 — DETECTED_BUT_TOO_LATE
- SAGA-EUR — BUILDING_ACCELERATION — score 5.948/10 — DETECTED_BUT_TOO_LATE
- ARX-EUR — BUILDING_ACCELERATION — score 5.000/10 — DETECTED_BUT_TOO_LATE
- SYN-EUR — BUILDING_ACCELERATION — score 4.780/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- PEAQ-EUR — MEMORY_24H — score mémoire 9.037/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- ZRC-EUR — ACTIVE_NOW — score mémoire 8.343/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- BONK-EUR — ACTIVE_NOW — score mémoire 8.152/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ICP-EUR — ACTIVE_NOW — score mémoire 8.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- DRIFT-EUR — ACTIVE_NOW — score mémoire 7.982/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GMT-EUR — ACTIVE_NOW — score mémoire 7.903/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- OGN-EUR — MEMORY_24H — score mémoire 7.854/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +50.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DBR-EUR +29.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QNT-EUR +27.41% — DETECTED_EARLY — couche NONE — action NONE
- TREAD-EUR +26.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XAI-EUR +26.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ONDO-EUR +25.88% — DETECTED_EARLY — couche NONE — action NONE
- PEAQ-EUR +25.09% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XPL-EUR +23.84% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARK-EUR +23.29% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DYM-EUR +19.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
