# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T20:32:00.102379+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAIKO-EUR | action ACHETE_MAINTENANT | opportunité 9.251 | entrée 7.000 | trend 8.200 | rang 8.188
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : BEAM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.911 | entrée 5.950 | trend 8.950 | rang 7.815
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : NEO-EUR | action LATENT_ACCELERATOR | opportunité 7.692 | entrée 5.750 | trend 8.750 | rang 7.556
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SEI-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.334 | entrée 7.500 | trend 8.850 | rang 8.398
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. SEI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.398
2. TAIKO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.188
3. SUI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.988

## Accélération indépendante

- LSK-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- MIRA-EUR — CONFIRMED_ACCELERATION — score 9.601/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — CONFIRMED_ACCELERATION — score 7.647/10 — DETECTED_BUT_TOO_LATE
- BTT-EUR — BUILDING_ACCELERATION — score 5.882/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VELO-EUR — BUILDING_ACCELERATION — score 5.505/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SNX-EUR — BUILDING_ACCELERATION — score 5.120/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- LSK-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- MIRA-EUR — ACTIVE_NOW — score mémoire 9.601/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SEI-EUR — ACTIVE_NOW — score mémoire 8.398/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- TAIKO-EUR — ACTIVE_NOW — score mémoire 8.188/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SUI-EUR — ACTIVE_NOW — score mémoire 7.988/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PYTH-EUR — ACTIVE_NOW — score mémoire 7.864/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +47.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XAI-EUR +37.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +24.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ONDO-EUR +23.75% — DETECTED_EARLY — couche NONE — action NONE
- QNT-EUR +22.98% — DETECTED_EARLY — couche NONE — action NONE
- XPL-EUR +21.93% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARK-EUR +20.70% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PLUME-EUR +19.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEAQ-EUR +18.71% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +17.80% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
