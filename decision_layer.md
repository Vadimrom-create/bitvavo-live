# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T19:35:47.893823+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAO-EUR | action ACHETE_MAINTENANT | opportunité 8.813 | entrée 7.650 | trend 7.600 | rang 7.835
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : BEAM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.110 | entrée 5.950 | trend 9.200 | rang 7.934
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : GRT-EUR | action LATENT_ACCELERATOR | opportunité 7.920 | entrée 5.550 | trend 8.550 | rang 7.503
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : GMT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.106 | entrée 6.700 | trend 9.000 | rang 8.318
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. GMT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.318
2. ICP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.072
3. BEAM-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.934

## Accélération indépendante

- CHIP-EUR — CONFIRMED_ACCELERATION — score 8.856/10 — DETECTED_BUT_TOO_LATE
- GIGA-EUR — CONFIRMED_ACCELERATION — score 8.491/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XPL-EUR — CONFIRMED_ACCELERATION — score 8.005/10 — DETECTED_BUT_TOO_LATE
- COTI-EUR — CONFIRMED_ACCELERATION — score 7.836/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAO-EUR — CONFIRMED_ACCELERATION — score 7.592/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PTB-EUR — CONFIRMED_ACCELERATION — score 7.465/10 — DETECTED_BUT_TOO_LATE
- WMTX-EUR — CONFIRMED_ACCELERATION — score 7.123/10 — DETECTED_BUT_TOO_LATE
- AIOZ-EUR — CONFIRMED_ACCELERATION — score 7.119/10 — DETECTED_BUT_TOO_LATE
- PENDLE-EUR — CONFIRMED_ACCELERATION — score 7.043/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRC-EUR — BUILDING_ACCELERATION — score 6.336/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- TAO-EUR — ACTIVE_NOW — score mémoire 7.835/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- VVV-EUR — ACTIVE_NOW — score mémoire 7.135/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- CHIP-EUR — ACTIVE_NOW — score mémoire 8.856/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CNPY-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- GIGA-EUR — ACTIVE_NOW — score mémoire 8.491/10 — sources ACCELERATION — WATCH_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 8.429/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- GMT-EUR — ACTIVE_NOW — score mémoire 8.318/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- XAI-EUR +43.88% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +34.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOM-EUR +27.11% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ONDO-EUR +24.77% — DETECTED_EARLY — couche NONE — action NONE
- TREAD-EUR +24.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XPL-EUR +22.95% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- QNT-EUR +21.22% — DETECTED_EARLY — couche NONE — action NONE
- PLUME-EUR +20.70% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEAQ-EUR +20.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +16.57% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
