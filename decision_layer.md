# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T11:46:49.146234+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : INJ-EUR | action ACHETE_MAINTENANT | opportunité 9.387 | entrée 7.400 | trend 8.650 | rang 8.338
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : RPL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.395 | entrée 6.300 | trend 8.500 | rang 7.643
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : RUNE-EUR | action LATENT_ACCELERATOR | opportunité 8.096 | entrée 4.500 | trend 8.700 | rang 7.508
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SENT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.567 | entrée 6.750 | trend 8.900 | rang 7.924
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. INJ-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.338
2. TIA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.232
3. ADA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.070

## Accélération indépendante

- SCR-EUR — CONFIRMED_ACCELERATION — score 9.182/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PHA-EUR — CONFIRMED_ACCELERATION — score 9.016/10 — DETECTED_BUT_TOO_LATE
- CETUS-EUR — CONFIRMED_ACCELERATION — score 6.737/10 — DETECTED_BUT_TOO_LATE
- U-EUR — CONFIRMED_ACCELERATION — score 6.668/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WAXP-EUR — BUILDING_ACCELERATION — score 5.752/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PIXEL-EUR — BUILDING_ACCELERATION — score 5.131/10 — DETECTED_BUT_TOO_LATE
- NIL-EUR — BUILDING_ACCELERATION — score 4.994/10 — DETECTED_BUT_TOO_LATE
- UNI-EUR — BUILDING_ACCELERATION — score 4.983/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- SCR-EUR — ACTIVE_NOW — score mémoire 9.182/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GLMR-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 9.016/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- TAI-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 8.374/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 8.338/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- TIA-EUR — ACTIVE_NOW — score mémoire 8.232/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ARK-EUR — MEMORY_24H — score mémoire 8.166/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ADA-EUR — ACTIVE_NOW — score mémoire 8.070/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- TREAD-EUR +47.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +35.71% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +35.45% — DETECTED_EARLY — couche NONE — action NONE
- PHA-EUR +30.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ONDO-EUR +28.20% — DETECTED_EARLY — couche NONE — action NONE
- XPL-EUR +27.61% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- FET-EUR +23.48% — DETECTED_EARLY — couche NONE — action NONE
- PEAQ-EUR +21.78% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +20.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RON-EUR +19.50% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
