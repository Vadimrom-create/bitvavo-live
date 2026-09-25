# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T23:54:41.767873+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : XLM-EUR | action ACHETE_MAINTENANT | opportunité 8.327 | entrée 7.350 | trend 7.600 | rang 7.613
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : BEAM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.739 | entrée 6.300 | trend 8.950 | rang 7.778
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : YGG-EUR | action LATENT_ACCELERATOR | opportunité 7.677 | entrée 5.550 | trend 8.700 | rang 7.551
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : BONK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.030 | entrée 7.050 | trend 8.100 | rang 7.988
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. BONK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.988
2. GMT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.875
3. SEI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.831

## Accélération indépendante

- CROSS-EUR — BUILDING_ACCELERATION — score 5.453/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PEAQ-EUR — MEMORY_24H — score mémoire 9.037/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.169/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BONK-EUR — ACTIVE_NOW — score mémoire 7.988/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- GMT-EUR — ACTIVE_NOW — score mémoire 7.875/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- OGN-EUR — MEMORY_24H — score mémoire 7.854/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SEI-EUR — ACTIVE_NOW — score mémoire 7.831/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ICP-EUR — ACTIVE_NOW — score mémoire 7.813/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +50.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QNT-EUR +27.24% — DETECTED_EARLY — couche NONE — action NONE
- ONDO-EUR +27.24% — DETECTED_EARLY — couche NONE — action NONE
- TREAD-EUR +25.97% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PEAQ-EUR +25.58% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XAI-EUR +24.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XPL-EUR +24.33% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- DBR-EUR +24.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +23.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DYM-EUR +19.41% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
