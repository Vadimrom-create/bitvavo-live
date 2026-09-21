# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T20:18:05.659637+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SOL-EUR | action ACHETE_MAINTENANT | opportunité 8.371 | entrée 7.850 | trend 8.200 | rang 7.907
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : WAL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.402 | entrée 6.100 | trend 9.200 | rang 8.122
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SUPER-EUR | action LATENT_ACCELERATOR | opportunité 8.603 | entrée 5.650 | trend 8.600 | rang 7.909
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : RENDER-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.261 | entrée 8.200 | trend 8.100 | rang 8.249
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. RENDER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.249
2. WAL-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 8.122
3. JUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.057

## Accélération indépendante

- GRASS-EUR — CONFIRMED_ACCELERATION — score 9.817/10 — DETECTED_BUT_TOO_LATE
- CRO-EUR — CONFIRMED_ACCELERATION — score 9.234/10 — DETECTED_BUT_TOO_LATE
- BTT-EUR — CONFIRMED_ACCELERATION — score 9.053/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAO-EUR — CONFIRMED_ACCELERATION — score 8.816/10 — DETECTED_BUT_TOO_LATE
- TAI-EUR — CONFIRMED_ACCELERATION — score 8.592/10 — DETECTED_BUT_TOO_LATE
- VELO-EUR — BUILDING_ACCELERATION — score 6.440/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NOS-EUR — BUILDING_ACCELERATION — score 6.387/10 — DETECTED_BUT_TOO_LATE
- FORM-EUR — BUILDING_ACCELERATION — score 6.309/10 — DETECTED_BUT_TOO_LATE
- WLD-EUR — BUILDING_ACCELERATION — score 5.913/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRC-EUR — BUILDING_ACCELERATION — score 5.443/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- RON-EUR — MEMORY_24H — score mémoire 9.938/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- GRASS-EUR — ACTIVE_NOW — score mémoire 9.817/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PTB-EUR — MEMORY_24H — score mémoire 9.534/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CRO-EUR — ACTIVE_NOW — score mémoire 9.234/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- ZKJ-EUR — MEMORY_24H — score mémoire 9.182/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- THQ-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BTT-EUR — ACTIVE_NOW — score mémoire 9.053/10 — sources ACCELERATION — WATCH_ONLY
- TAO-EUR — ACTIVE_NOW — score mémoire 8.816/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LUMIA-EUR — MEMORY_24H — score mémoire 8.655/10 — sources ACCELERATION — MEMORY_ONLY
- TAI-EUR — ACTIVE_NOW — score mémoire 8.592/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- ZRC-EUR +116.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICX-EUR +107.00% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZETA-EUR +57.69% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- FORM-EUR +39.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +38.05% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PHA-EUR +34.36% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PTB-EUR +33.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SWELL-EUR +26.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOS-EUR +25.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEPE-EUR +23.90% — DETECTED_EARLY — couche NONE — action NONE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
