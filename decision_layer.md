# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T23:08:36.942773+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : KMNO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.779 | entrée 6.600 | trend 8.850 | rang 7.584
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : YGG-EUR | action LATENT_ACCELERATOR | opportunité 7.980 | entrée 5.550 | trend 8.700 | rang 7.681
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : GMT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.305 | entrée 6.100 | trend 9.000 | rang 8.015
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. GMT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.015
2. DATAIP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.902
3. ICP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.851

## Accélération indépendante

- DBR-EUR — CONFIRMED_ACCELERATION — score 6.969/10 — DETECTED_BUT_TOO_LATE
- CPOOL-EUR — BUILDING_ACCELERATION — score 5.667/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — BUILDING_ACCELERATION — score 5.259/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- PEAQ-EUR — MEMORY_24H — score mémoire 9.037/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.087/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- GMT-EUR — ACTIVE_NOW — score mémoire 8.015/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- DATAIP-EUR — ACTIVE_NOW — score mémoire 7.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- OGN-EUR — MEMORY_24H — score mémoire 7.854/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.851/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 7.807/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +42.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DBR-EUR +30.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +28.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XAI-EUR +27.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QNT-EUR +26.49% — DETECTED_EARLY — couche NONE — action NONE
- ONDO-EUR +25.33% — DETECTED_EARLY — couche NONE — action NONE
- PEAQ-EUR +24.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XPL-EUR +24.16% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARK-EUR +22.26% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LSK-EUR +21.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
