# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T10:24:16.926354+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SEI-EUR | action ACHETE_MAINTENANT | opportunité 8.864 | entrée 8.100 | trend 8.850 | rang 8.475
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SPK-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.513 | entrée 6.150 | trend 8.900 | rang 7.960
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ARKM-EUR | action LATENT_ACCELERATOR | opportunité 8.247 | entrée 5.550 | trend 8.750 | rang 7.757
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : EIGEN-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.401 | entrée 6.950 | trend 9.200 | rang 8.220
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. SEI-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.475
2. RENDER-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.416
3. EIGEN-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.220

## Accélération indépendante

- AGI-EUR — BUILDING_ACCELERATION — score 6.443/10 — DETECTED_BUT_TOO_LATE
- PONKE-EUR — BUILDING_ACCELERATION — score 5.829/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SPK-EUR — BUILDING_ACCELERATION — score 5.299/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GLMR-EUR — BUILDING_ACCELERATION — score 5.239/10 — DETECTED_BUT_TOO_LATE
- HFT-EUR — BUILDING_ACCELERATION — score 5.089/10 — DETECTED_BUT_TOO_LATE
- TRUST-EUR — BUILDING_ACCELERATION — score 5.020/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- XMN-EUR — MEMORY_24H — score mémoire 9.365/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VELO-EUR — MEMORY_24H — score mémoire 8.767/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AMP-EUR — MEMORY_24H — score mémoire 8.589/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SEI-EUR — ACTIVE_NOW — score mémoire 8.475/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.427/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.416/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- EIGEN-EUR — ACTIVE_NOW — score mémoire 8.220/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NEO-EUR — ACTIVE_NOW — score mémoire 8.209/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 8.195/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAIA-EUR — ACTIVE_NOW — score mémoire 8.146/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +59.85% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +56.58% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- TREAD-EUR +54.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOON-EUR +37.82% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +26.77% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +25.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HFT-EUR +23.98% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- W-EUR +20.31% — DETECTED_EARLY — couche NONE — action NONE
- XVG-EUR +16.96% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- EDGE-EUR +16.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
