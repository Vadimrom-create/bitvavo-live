# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T19:52:08.405746+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ARB-EUR | action ACHETE_MAINTENANT | opportunité 9.123 | entrée 7.500 | trend 7.500 | rang 7.897
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : EIGEN-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.724 | entrée 6.700 | trend 8.450 | rang 7.584
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : IOST-EUR | action LATENT_ACCELERATOR | opportunité 8.838 | entrée 5.750 | trend 7.650 | rang 7.659
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : GMT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.681 | entrée 6.350 | trend 9.000 | rang 8.142
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. GMT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.142
2. THE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.094
3. BEAM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.068

## Accélération indépendante

- ALIGN-EUR — CONFIRMED_ACCELERATION — score 8.827/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WMTX-EUR — CONFIRMED_ACCELERATION — score 6.965/10 — DETECTED_BUT_TOO_LATE
- CHIP-EUR — CONFIRMED_ACCELERATION — score 6.787/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — CONFIRMED_ACCELERATION — score 6.691/10 — DETECTED_BUT_TOO_LATE
- SKL-EUR — BUILDING_ACCELERATION — score 6.154/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FRAX-EUR — BUILDING_ACCELERATION — score 6.110/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAO-EUR — BUILDING_ACCELERATION — score 5.502/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- YFI-EUR — BUILDING_ACCELERATION — score 5.281/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- TAO-EUR — ACTIVE_NOW — score mémoire 7.889/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- FET-EUR — ACTIVE_NOW — score mémoire 7.419/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- VVV-EUR — ACTIVE_NOW — score mémoire 6.216/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- ALIGN-EUR — ACTIVE_NOW — score mémoire 8.827/10 — sources ACCELERATION, V4 — WATCH_ONLY
- CNPY-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 8.491/10 — sources ACCELERATION — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 8.472/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 8.429/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- XAI-EUR +41.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +34.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +31.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOM-EUR +25.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ONDO-EUR +24.40% — DETECTED_EARLY — couche NONE — action NONE
- QNT-EUR +20.84% — DETECTED_EARLY — couche NONE — action NONE
- XPL-EUR +20.81% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PLUME-EUR +19.81% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEAQ-EUR +19.65% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARK-EUR +17.23% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
