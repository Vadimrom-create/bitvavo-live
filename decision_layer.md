# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T00:18:14.105731+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SOL-EUR | action ACHETE_MAINTENANT | opportunité 8.113 | entrée 7.850 | trend 8.200 | rang 7.815
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : YGG-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.740 | entrée 6.650 | trend 8.700 | rang 7.673
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : NEO-EUR | action LATENT_ACCELERATOR | opportunité 8.113 | entrée 5.750 | trend 8.750 | rang 7.780
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : KMNO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.152 | entrée 7.000 | trend 8.850 | rang 8.306
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. KMNO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.306
2. ENA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.035
3. KAS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.021

## Accélération indépendante

- WMTX-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- SYN-EUR — CONFIRMED_ACCELERATION — score 9.107/10 — DETECTED_BUT_TOO_LATE
- MANTRA-EUR — CONFIRMED_ACCELERATION — score 9.028/10 — DETECTED_BUT_TOO_LATE
- DATAIP-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- XPL-EUR — CONFIRMED_ACCELERATION — score 7.348/10 — DETECTED_BUT_TOO_LATE
- SAGA-EUR — CONFIRMED_ACCELERATION — score 7.249/10 — DETECTED_BUT_TOO_LATE
- WAXP-EUR — CONFIRMED_ACCELERATION — score 7.023/10 — DETECTED_BUT_TOO_LATE
- DGB-EUR — BUILDING_ACCELERATION — score 6.364/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SEI-EUR — BUILDING_ACCELERATION — score 6.187/10 — DETECTED_BUT_TOO_LATE
- FET-EUR — BUILDING_ACCELERATION — score 6.156/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- XLM-EUR — ACTIVE_NOW — score mémoire 7.558/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- WMTX-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- SYN-EUR — ACTIVE_NOW — score mémoire 9.107/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PEAQ-EUR — MEMORY_24H — score mémoire 9.037/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MANTRA-EUR — ACTIVE_NOW — score mémoire 9.028/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- DATAIP-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- KMNO-EUR — ACTIVE_NOW — score mémoire 8.306/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +61.59% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QNT-EUR +27.23% — DETECTED_EARLY — couche NONE — action NONE
- ONDO-EUR +27.08% — DETECTED_EARLY — couche NONE — action NONE
- XPL-EUR +26.71% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- TREAD-EUR +25.87% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARK-EUR +24.26% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEAQ-EUR +21.99% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XAI-EUR +21.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FET-EUR +19.53% — DETECTED_EARLY — couche NONE — action NONE
- DBR-EUR +18.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
