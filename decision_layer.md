# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T10:41:53.327405+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : RENDER-EUR | action ACHETE_MAINTENANT | opportunité 8.386 | entrée 7.800 | trend 9.200 | rang 8.331
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : 0G-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.539 | entrée 6.150 | trend 8.650 | rang 7.973
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : GALA-EUR | action LATENT_ACCELERATOR | opportunité 8.038 | entrée 5.750 | trend 8.700 | rang 7.708
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : GMT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.243 | entrée 7.350 | trend 8.500 | rang 8.359
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. GMT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.359
2. RENDER-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.331
3. BRETT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.305

## Accélération indépendante

- EDGE-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- AMP-EUR — CONFIRMED_ACCELERATION — score 9.138/10 — DETECTED_BUT_TOO_LATE
- GRASS-EUR — CONFIRMED_ACCELERATION — score 7.995/10 — DETECTED_BUT_TOO_LATE
- BRETT-EUR — CONFIRMED_ACCELERATION — score 7.809/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRAC-EUR — CONFIRMED_ACCELERATION — score 6.931/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FUEL-EUR — BUILDING_ACCELERATION — score 5.730/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WLD-EUR — BUILDING_ACCELERATION — score 5.627/10 — DETECTED_BUT_TOO_LATE
- XAI-EUR — BUILDING_ACCELERATION — score 5.381/10 — DETECTED_BUT_TOO_LATE
- DODO-EUR — BUILDING_ACCELERATION — score 5.290/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CPOOL-EUR — BUILDING_ACCELERATION — score 4.960/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- EDGE-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- XMN-EUR — MEMORY_24H — score mémoire 9.365/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AMP-EUR — ACTIVE_NOW — score mémoire 9.138/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- VELO-EUR — MEMORY_24H — score mémoire 8.767/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.427/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- GMT-EUR — ACTIVE_NOW — score mémoire 8.359/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.331/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- BRETT-EUR — ACTIVE_NOW — score mémoire 8.305/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- EIGEN-EUR — ACTIVE_NOW — score mémoire 8.224/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SEI-EUR — ACTIVE_NOW — score mémoire 8.207/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +59.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +53.05% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- TREAD-EUR +42.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AMP-EUR +38.44% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +36.40% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +28.54% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HFT-EUR +24.27% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- AGI-EUR +23.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +18.47% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- W-EUR +17.66% — DETECTED_EARLY — couche NONE — action NONE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
