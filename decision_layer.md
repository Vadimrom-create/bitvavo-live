# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T03:11:05.013577+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : BCH-EUR | action ACHETE_MAINTENANT | opportunité 9.143 | entrée 8.150 | trend 7.850 | rang 8.250
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : NEAR-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.555 | entrée 6.700 | trend 8.250 | rang 7.489
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BONK-EUR | action LATENT_ACCELERATOR | opportunité 7.768 | entrée 5.550 | trend 8.200 | rang 7.431
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LTC-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.293 | entrée 6.750 | trend 8.900 | rang 7.878
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. BCH-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.250
2. LTC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.878
3. CAKE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.806

## Accélération indépendante

- SNX-EUR — CONFIRMED_ACCELERATION — score 6.590/10 — DETECTED_BUT_TOO_LATE
- PUMP-EUR — BUILDING_ACCELERATION — score 5.639/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BTT-EUR — BUILDING_ACCELERATION — score 5.502/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRO-EUR — BUILDING_ACCELERATION — score 5.206/10 — DETECTED_BUT_TOO_LATE
- XAI-EUR — BUILDING_ACCELERATION — score 5.201/10 — DETECTED_BUT_TOO_LATE
- JASMY-EUR — BUILDING_ACCELERATION — score 5.024/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VIRTUAL-EUR — BUILDING_ACCELERATION — score 4.923/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BOME-EUR — BUILDING_ACCELERATION — score 4.838/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- QKC-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- UP-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- EDGE-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- BCH-EUR — ACTIVE_NOW — score mémoire 8.250/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SEI-EUR — MEMORY_24H — score mémoire 8.074/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HBAR-EUR — MEMORY_24H — score mémoire 7.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 7.878/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +27.40% — DETECTED_EARLY — couche NONE — action NONE
- ONDO-EUR +26.38% — DETECTED_EARLY — couche NONE — action NONE
- XPL-EUR +24.13% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- TREAD-EUR +19.52% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PEAQ-EUR +18.86% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +16.90% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- FET-EUR +14.14% — DETECTED_EARLY — couche NONE — action NONE
- ARK-EUR +13.85% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XAI-EUR +13.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SNX-EUR +12.32% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
