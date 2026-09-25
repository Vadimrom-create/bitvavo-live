# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T08:26:13.869320+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AERO-EUR | action ACHETE_MAINTENANT | opportunité 9.423 | entrée 7.250 | trend 8.950 | rang 8.351
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : S-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.976 | entrée 6.050 | trend 7.350 | rang 7.595
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : CAKE-EUR | action LATENT_ACCELERATOR | opportunité 8.010 | entrée 4.500 | trend 8.950 | rang 7.676
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : JUP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.441 | entrée 7.450 | trend 8.950 | rang 8.489
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. JUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.489
2. AERO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.351
3. RENDER-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.332

## Accélération indépendante

- FUEL-EUR — CONFIRMED_ACCELERATION — score 9.306/10 — DETECTED_BUT_TOO_LATE
- CSPR-EUR — CONFIRMED_ACCELERATION — score 8.374/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DEEP-EUR — CONFIRMED_ACCELERATION — score 8.289/10 — DETECTED_BUT_TOO_LATE
- SEI-EUR — CONFIRMED_ACCELERATION — score 8.132/10 — DETECTED_BUT_TOO_LATE
- ALICE-EUR — BUILDING_ACCELERATION — score 6.325/10 — DETECTED_BUT_TOO_LATE
- APT-EUR — BUILDING_ACCELERATION — score 6.123/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BLUR-EUR — BUILDING_ACCELERATION — score 6.075/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LDO-EUR — BUILDING_ACCELERATION — score 6.071/10 — DETECTED_BUT_TOO_LATE
- AIXBT-EUR — BUILDING_ACCELERATION — score 5.920/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FIL-EUR — BUILDING_ACCELERATION — score 5.805/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- AERO-EUR — ACTIVE_NOW — score mémoire 8.351/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- NEAR-EUR — ACTIVE_NOW — score mémoire 7.914/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ICP-EUR — ACTIVE_NOW — score mémoire 7.484/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- FUEL-EUR — ACTIVE_NOW — score mémoire 9.306/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- UP-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- WMTX-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 8.489/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CSPR-EUR — ACTIVE_NOW — score mémoire 8.374/10 — sources ACCELERATION, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- TREAD-EUR +45.96% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- QNT-EUR +42.26% — DETECTED_EARLY — couche NONE — action NONE
- ONDO-EUR +33.29% — DETECTED_EARLY — couche NONE — action NONE
- XPL-EUR +30.45% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARK-EUR +23.80% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PHA-EUR +21.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +19.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LDO-EUR +19.38% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DBR-EUR +18.62% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XAI-EUR +17.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
