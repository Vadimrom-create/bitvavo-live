# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T08:04:52.060581+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 9.198 | entrée 7.650 | trend 8.900 | rang 8.551
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AVAX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.674 | entrée 6.750 | trend 7.400 | rang 7.159
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SIGN-EUR | action LATENT_ACCELERATOR | opportunité 7.437 | entrée 4.500 | trend 8.700 | rang 7.262
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ORCA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.106 | entrée 6.450 | trend 7.950 | rang 8.005
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LTC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.551
2. RENDER-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.292
3. ALGO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.218

## Accélération indépendante

- PEAQ-EUR — CONFIRMED_ACCELERATION — score 8.691/10 — DETECTED_BUT_TOO_LATE
- FUEL-EUR — CONFIRMED_ACCELERATION — score 6.643/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LDO-EUR — CONFIRMED_ACCELERATION — score 6.558/10 — DETECTED_BUT_TOO_LATE
- ARX-EUR — BUILDING_ACCELERATION — score 6.287/10 — DETECTED_BUT_TOO_LATE
- IKA-EUR — BUILDING_ACCELERATION — score 6.276/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SPK-EUR — BUILDING_ACCELERATION — score 6.236/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MORPHO-EUR — BUILDING_ACCELERATION — score 6.189/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MON-EUR — BUILDING_ACCELERATION — score 6.086/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TREAD-EUR — BUILDING_ACCELERATION — score 5.467/10 — DETECTED_BUT_TOO_LATE
- ONDO-EUR — BUILDING_ACCELERATION — score 5.437/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- UP-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- PEAQ-EUR — ACTIVE_NOW — score mémoire 8.691/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LTC-EUR — ACTIVE_NOW — score mémoire 8.551/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WMTX-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.292/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- ALGO-EUR — ACTIVE_NOW — score mémoire 8.218/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NOS-EUR — MEMORY_24H — score mémoire 8.008/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- TREAD-EUR +50.92% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- QNT-EUR +42.10% — DETECTED_EARLY — couche NONE — action NONE
- ONDO-EUR +29.65% — DETECTED_EARLY — couche NONE — action NONE
- XPL-EUR +26.85% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARK-EUR +23.07% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +20.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DBR-EUR +18.67% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PHA-EUR +18.38% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEAQ-EUR +17.17% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TAI-EUR +15.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
