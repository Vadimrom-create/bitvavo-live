# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T04:22:36.307123+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : PLUME-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.667 | entrée 6.250 | trend 8.550 | rang 7.460
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : RED-EUR | action LATENT_ACCELERATOR | opportunité 7.581 | entrée 5.400 | trend 8.650 | rang 7.358
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : CAKE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.462 | entrée 5.900 | trend 8.950 | rang 8.051
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. CAKE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.051
2. LTC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.843
3. PYTH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.710

## Accélération indépendante

- NOM-EUR — CONFIRMED_ACCELERATION — score 9.128/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRC-EUR — CONFIRMED_ACCELERATION — score 8.742/10 — DETECTED_BUT_TOO_LATE
- EDGE-EUR — CONFIRMED_ACCELERATION — score 7.885/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — CONFIRMED_ACCELERATION — score 7.522/10 — DETECTED_BUT_TOO_LATE
- ARX-EUR — BUILDING_ACCELERATION — score 5.206/10 — DETECTED_BUT_TOO_LATE
- GIGA-EUR — BUILDING_ACCELERATION — score 5.190/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XAI-EUR — BUILDING_ACCELERATION — score 5.061/10 — DETECTED_BUT_TOO_LATE
- DBR-EUR — BUILDING_ACCELERATION — score 5.028/10 — DETECTED_BUT_TOO_LATE
- PROMPT-EUR — BUILDING_ACCELERATION — score 4.917/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XLM-EUR — BUILDING_ACCELERATION — score 4.896/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- QKC-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NOM-EUR — ACTIVE_NOW — score mémoire 9.128/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- UP-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- ZRC-EUR — ACTIVE_NOW — score mémoire 8.742/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.051/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 8.051/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HBAR-EUR — MEMORY_24H — score mémoire 7.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- QNT-EUR +34.24% — DETECTED_EARLY — couche NONE — action NONE
- XPL-EUR +30.36% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- TREAD-EUR +29.62% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- EDGE-EUR +28.50% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ONDO-EUR +26.78% — DETECTED_EARLY — couche NONE — action NONE
- PEAQ-EUR +25.20% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARK-EUR +16.64% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FET-EUR +15.73% — DETECTED_EARLY — couche NONE — action NONE
- XAI-EUR +15.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DBR-EUR +14.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
