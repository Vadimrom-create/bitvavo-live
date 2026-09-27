# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T07:37:07.088262+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : RENDER-EUR | action ACHETE_MAINTENANT | opportunité 8.813 | entrée 7.600 | trend 9.200 | rang 8.433
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ALT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.844 | entrée 6.150 | trend 9.000 | rang 8.228
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ZK-EUR | action LATENT_ACCELERATOR | opportunité 8.390 | entrée 5.700 | trend 8.650 | rang 7.691
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : RED-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.326 | entrée 5.950 | trend 8.950 | rang 8.432
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. RENDER-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.433
2. RED-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.432
3. GALA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.250

## Accélération indépendante

- GLMR-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- SUI-EUR — CONFIRMED_ACCELERATION — score 9.056/10 — DETECTED_BUT_TOO_LATE
- QUID-EUR — CONFIRMED_ACCELERATION — score 8.687/10 — DETECTED_BUT_TOO_LATE
- XVG-EUR — CONFIRMED_ACCELERATION — score 7.820/10 — DETECTED_BUT_TOO_LATE
- DEEP-EUR — CONFIRMED_ACCELERATION — score 7.633/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MOVE-EUR — CONFIRMED_ACCELERATION — score 7.362/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VELO-EUR — CONFIRMED_ACCELERATION — score 7.361/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CETUS-EUR — BUILDING_ACCELERATION — score 5.894/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WIN-EUR — BUILDING_ACCELERATION — score 5.664/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MEME-EUR — BUILDING_ACCELERATION — score 5.320/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GLMR-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- WMTX-EUR — MEMORY_24H — score mémoire 9.850/10 — sources ACCELERATION — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 9.365/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SUI-EUR — ACTIVE_NOW — score mémoire 9.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- QUID-EUR — ACTIVE_NOW — score mémoire 8.687/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- AGI-EUR — MEMORY_24H — score mémoire 8.644/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AMP-EUR — MEMORY_24H — score mémoire 8.589/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SOON-EUR — MEMORY_24H — score mémoire 8.551/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.433/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +70.62% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +57.44% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +39.86% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +33.33% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +26.25% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +21.63% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- W-EUR +18.81% — DETECTED_EARLY — couche NONE — action NONE
- HFT-EUR +16.83% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PYTH-EUR +16.53% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RUNE-EUR +16.29% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
