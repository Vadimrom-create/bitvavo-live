# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T09:41:15.833829+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : RAY-EUR | action ACHETE_MAINTENANT | opportunité 8.998 | entrée 7.200 | trend 8.000 | rang 8.035
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ALT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.361 | entrée 6.150 | trend 8.450 | rang 7.758
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : LTC-EUR | action LATENT_ACCELERATOR | opportunité 8.070 | entrée 4.500 | trend 8.900 | rang 7.686
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : COMP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.311 | entrée 6.650 | trend 8.750 | rang 8.409
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. COMP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.409
2. PYTH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.408
3. CAKE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.393

## Accélération indépendante

- PEAQ-EUR — CONFIRMED_ACCELERATION — score 8.896/10 — DETECTED_BUT_TOO_LATE
- VELO-EUR — CONFIRMED_ACCELERATION — score 7.756/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NEAR-EUR — CONFIRMED_ACCELERATION — score 7.409/10 — DETECTED_BUT_TOO_LATE
- RAY-EUR — CONFIRMED_ACCELERATION — score 6.815/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SYN-EUR — CONFIRMED_ACCELERATION — score 6.591/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KERNEL-EUR — CONFIRMED_ACCELERATION — score 6.588/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WAXP-EUR — CONFIRMED_ACCELERATION — score 6.562/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XMN-EUR — BUILDING_ACCELERATION — score 6.257/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRX-EUR — BUILDING_ACCELERATION — score 6.000/10 — DETECTED_BUT_TOO_LATE
- DIA-EUR — BUILDING_ACCELERATION — score 5.924/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- INJ-EUR — ACTIVE_NOW — score mémoire 7.690/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEAQ-EUR — ACTIVE_NOW — score mémoire 8.896/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- XPL-EUR — MEMORY_24H — score mémoire 8.847/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WMTX-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- COMP-EUR — ACTIVE_NOW — score mémoire 8.409/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.408/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CAKE-EUR — ACTIVE_NOW — score mémoire 8.393/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 8.374/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 8.264/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- TREAD-EUR +45.02% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- QNT-EUR +36.43% — DETECTED_EARLY — couche NONE — action NONE
- XPL-EUR +33.33% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PEAQ-EUR +31.70% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ONDO-EUR +31.30% — DETECTED_EARLY — couche NONE — action NONE
- PHA-EUR +22.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +21.92% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FET-EUR +20.15% — DETECTED_EARLY — couche NONE — action NONE
- DBR-EUR +19.30% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WAXP-EUR +18.15% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
