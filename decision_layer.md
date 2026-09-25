# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T06:34:28.662233+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 8.217 | entrée 7.350 | trend 8.900 | rang 8.072
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : NEAR-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.715 | entrée 6.200 | trend 8.250 | rang 7.486
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : CAKE-EUR | action LATENT_ACCELERATOR | opportunité 7.803 | entrée 5.700 | trend 8.950 | rang 7.733
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : GMT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.702 | entrée 6.750 | trend 8.250 | rang 7.954
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LTC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.072
2. GMT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.954
3. FET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.917

## Accélération indépendante

- EDGE-EUR — CONFIRMED_ACCELERATION — score 8.685/10 — DETECTED_BUT_TOO_LATE
- AXS-EUR — CONFIRMED_ACCELERATION — score 8.635/10 — DETECTED_BUT_TOO_LATE
- PHA-EUR — CONFIRMED_ACCELERATION — score 7.239/10 — DETECTED_BUT_TOO_LATE
- SLP-EUR — CONFIRMED_ACCELERATION — score 6.690/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ALICE-EUR — BUILDING_ACCELERATION — score 6.230/10 — DETECTED_BUT_TOO_LATE
- CETUS-EUR — BUILDING_ACCELERATION — score 6.127/10 — DETECTED_BUT_TOO_LATE
- SHELL-EUR — BUILDING_ACCELERATION — score 6.071/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NEO-EUR — BUILDING_ACCELERATION — score 5.529/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — BUILDING_ACCELERATION — score 5.056/10 — DETECTED_BUT_TOO_LATE
- AIXBT-EUR — BUILDING_ACCELERATION — score 4.950/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- UP-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- EDGE-EUR — ACTIVE_NOW — score mémoire 8.685/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SAGA-EUR — MEMORY_24H — score mémoire 8.681/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AXS-EUR — ACTIVE_NOW — score mémoire 8.635/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- WMTX-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 8.072/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GMT-EUR — ACTIVE_NOW — score mémoire 7.954/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +36.42% — DETECTED_EARLY — couche NONE — action NONE
- XPL-EUR +31.89% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- TREAD-EUR +31.13% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ONDO-EUR +24.64% — DETECTED_EARLY — couche NONE — action NONE
- PEAQ-EUR +21.93% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +19.71% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PHA-EUR +19.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DBR-EUR +18.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XAI-EUR +15.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRC-EUR +14.79% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
