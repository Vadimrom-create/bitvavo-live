# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T20:34:21.948106+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : DATAIP-EUR | action ACHETE_MAINTENANT | opportunité 8.190 | entrée 7.200 | trend 8.450 | rang 7.845
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AXS-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.169 | entrée 6.050 | trend 8.700 | rang 8.316
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BEAM-EUR | action LATENT_ACCELERATOR | opportunité 8.019 | entrée 5.550 | trend 8.650 | rang 7.643
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : CC-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.335 | entrée 6.850 | trend 8.650 | rang 8.392
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. CC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.392
2. AXS-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 8.316
3. GMT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.188

## Accélération indépendante

- AMP-EUR — CONFIRMED_ACCELERATION — score 7.533/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SKY-EUR — CONFIRMED_ACCELERATION — score 6.888/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- POND-EUR — MEMORY_24H — score mémoire 8.755/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- YB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CC-EUR — ACTIVE_NOW — score mémoire 8.392/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AXS-EUR — ACTIVE_NOW — score mémoire 8.316/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GMT-EUR — ACTIVE_NOW — score mémoire 8.188/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.161/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY
- A-EUR — ACTIVE_NOW — score mémoire 8.103/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 8.083/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- QNT-EUR +56.16% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +43.77% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +30.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INX-EUR +29.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- W-EUR +23.90% — DETECTED_EARLY — couche NONE — action NONE
- GLMR-EUR +18.52% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GRT-EUR +17.95% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRC-EUR +15.25% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARX-EUR +14.46% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AUDIO-EUR +14.28% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
