# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T09:51:19.327640+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : DATAIP-EUR | action ACHETE_MAINTENANT | opportunité 9.302 | entrée 7.250 | trend 8.450 | rang 8.360
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : TRUST-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.558 | entrée 6.350 | trend 9.000 | rang 8.104
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ALT-EUR | action LATENT_ACCELERATOR | opportunité 7.854 | entrée 4.500 | trend 9.000 | rang 7.633
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : KAIA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.541 | entrée 6.600 | trend 8.750 | rang 8.063
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. DATAIP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.360
2. EIGEN-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.197
3. TRUST-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 8.104

## Accélération indépendante

- HFT-EUR — CONFIRMED_ACCELERATION — score 7.990/10 — DETECTED_BUT_TOO_LATE
- CVX-EUR — CONFIRMED_ACCELERATION — score 6.869/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GRASS-EUR — CONFIRMED_ACCELERATION — score 6.671/10 — DETECTED_BUT_TOO_LATE
- PUFFER-EUR — BUILDING_ACCELERATION — score 6.167/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BAT-EUR — BUILDING_ACCELERATION — score 6.036/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARX-EUR — BUILDING_ACCELERATION — score 6.005/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — BUILDING_ACCELERATION — score 6.000/10 — DETECTED_BUT_TOO_LATE
- AXL-EUR — BUILDING_ACCELERATION — score 5.516/10 — DETECTED_BUT_TOO_LATE
- PROM-EUR — BUILDING_ACCELERATION — score 5.486/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KMNO-EUR — BUILDING_ACCELERATION — score 5.376/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- XMN-EUR — MEMORY_24H — score mémoire 9.365/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VELO-EUR — MEMORY_24H — score mémoire 8.767/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AMP-EUR — MEMORY_24H — score mémoire 8.589/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.427/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DATAIP-EUR — ACTIVE_NOW — score mémoire 8.360/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- EIGEN-EUR — ACTIVE_NOW — score mémoire 8.197/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TRUST-EUR — ACTIVE_NOW — score mémoire 8.104/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- OP-EUR — ACTIVE_NOW — score mémoire 8.102/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.074/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAIA-EUR — ACTIVE_NOW — score mémoire 8.063/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +66.81% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +49.32% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +45.18% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +39.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AMP-EUR +30.84% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HFT-EUR +26.12% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- W-EUR +24.08% — DETECTED_EARLY — couche NONE — action NONE
- AGI-EUR +21.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XVG-EUR +18.22% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- WLD-EUR +17.01% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
