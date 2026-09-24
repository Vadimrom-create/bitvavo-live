# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T19:18:58.728484+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : GMT-EUR | action ACHETE_MAINTENANT | opportunité 9.430 | entrée 7.150 | trend 9.000 | rang 8.576
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : EIGEN-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.803 | entrée 6.150 | trend 8.450 | rang 7.595
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : NEO-EUR | action LATENT_ACCELERATOR | opportunité 7.686 | entrée 5.750 | trend 8.750 | rang 7.556
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : BEAM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.793 | entrée 6.350 | trend 9.200 | rang 8.297
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. GMT-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.576
2. BEAM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.297
3. A-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.108

## Accélération indépendante

- LSK-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- PONKE-EUR — CONFIRMED_ACCELERATION — score 8.445/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WMTX-EUR — CONFIRMED_ACCELERATION — score 7.128/10 — DETECTED_BUT_TOO_LATE
- CHIP-EUR — BUILDING_ACCELERATION — score 5.893/10 — DETECTED_BUT_TOO_LATE
- VVV-EUR — BUILDING_ACCELERATION — score 5.863/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ACH-EUR — BUILDING_ACCELERATION — score 5.762/10 — DETECTED_BUT_TOO_LATE
- QKC-EUR — BUILDING_ACCELERATION — score 5.727/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WELL-EUR — BUILDING_ACCELERATION — score 5.596/10 — DETECTED_BUT_TOO_LATE
- MEW-EUR — BUILDING_ACCELERATION — score 5.552/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ACE-EUR — BUILDING_ACCELERATION — score 5.289/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- LINK-EUR — ACTIVE_NOW — score mémoire 7.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- LSK-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- UP-EUR — MEMORY_24H — score mémoire 8.796/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GMT-EUR — ACTIVE_NOW — score mémoire 8.576/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- 2Z-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CNPY-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PONKE-EUR — ACTIVE_NOW — score mémoire 8.445/10 — sources ACCELERATION, V4 — WATCH_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 8.429/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- XAI-EUR +44.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +36.81% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- NOM-EUR +28.67% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ONDO-EUR +26.06% — DETECTED_EARLY — couche NONE — action NONE
- PLUME-EUR +22.34% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +22.02% — DETECTED_EARLY — couche NONE — action NONE
- PEAQ-EUR +21.06% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XPL-EUR +19.19% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- LTC-EUR +16.97% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FET-EUR +16.92% — DETECTED_EARLY — couche NONE — action NONE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
