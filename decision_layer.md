# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T04:58:16.143589+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : INJ-EUR | action ACHETE_MAINTENANT | opportunité 9.155 | entrée 7.600 | trend 8.400 | rang 8.295
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : BEAM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.332 | entrée 5.800 | trend 8.900 | rang 7.953
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SNX-EUR | action LATENT_ACCELERATOR | opportunité 7.876 | entrée 5.450 | trend 8.700 | rang 7.322
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PLUME-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.268 | entrée 7.200 | trend 8.200 | rang 8.143
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. INJ-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.295
2. PLUME-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.143
3. TAO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.063

## Accélération indépendante

- QKC-EUR — CONFIRMED_ACCELERATION — score 9.563/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — CONFIRMED_ACCELERATION — score 9.235/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MOVR-EUR — CONFIRMED_ACCELERATION — score 8.853/10 — DETECTED_BUT_TOO_LATE
- ACE-EUR — CONFIRMED_ACCELERATION — score 8.127/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RON-EUR — BUILDING_ACCELERATION — score 6.468/10 — DETECTED_BUT_TOO_LATE
- GLMR-EUR — BUILDING_ACCELERATION — score 5.597/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SIGN-EUR — BUILDING_ACCELERATION — score 5.367/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KAITO-EUR — BUILDING_ACCELERATION — score 5.278/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DIA-EUR — BUILDING_ACCELERATION — score 5.208/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- QKC-EUR — ACTIVE_NOW — score mémoire 9.563/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICX-EUR — ACTIVE_NOW — score mémoire 9.235/10 — sources ACCELERATION, V4 — WATCH_ONLY
- UP-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- MOVR-EUR — ACTIVE_NOW — score mémoire 8.853/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — MEMORY_24H — score mémoire 8.742/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WMTX-EUR — MEMORY_24H — score mémoire 8.409/10 — sources ACCELERATION — MEMORY_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 8.295/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- QNT-EUR +34.68% — DETECTED_EARLY — couche NONE — action NONE
- TREAD-EUR +32.62% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- XPL-EUR +26.82% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ONDO-EUR +25.27% — DETECTED_EARLY — couche NONE — action NONE
- PEAQ-EUR +23.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +22.61% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- XAI-EUR +18.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FET-EUR +15.73% — DETECTED_EARLY — couche NONE — action NONE
- DBR-EUR +15.60% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TAI-EUR +14.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
