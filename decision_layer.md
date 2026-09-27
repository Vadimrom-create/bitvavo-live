# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T07:52:21.026047+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : RENDER-EUR | action ACHETE_MAINTENANT | opportunité 9.493 | entrée 7.300 | trend 9.200 | rang 8.669
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : EIGEN-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.331 | entrée 5.950 | trend 9.200 | rang 7.970
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SPK-EUR | action LATENT_ACCELERATOR | opportunité 8.208 | entrée 5.600 | trend 8.900 | rang 7.873
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LDO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.335 | entrée 6.650 | trend 8.650 | rang 8.366
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. RENDER-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.669
2. LDO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.366
3. BABY-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.232

## Accélération indépendante

- DEEP-EUR — CONFIRMED_ACCELERATION — score 7.546/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VELO-EUR — CONFIRMED_ACCELERATION — score 7.278/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GLMR-EUR — CONFIRMED_ACCELERATION — score 7.165/10 — DETECTED_BUT_TOO_LATE
- SUPER-EUR — CONFIRMED_ACCELERATION — score 6.957/10 — DETECTED_BUT_TOO_LATE
- CETUS-EUR — CONFIRMED_ACCELERATION — score 6.932/10 — DETECTED_BUT_TOO_LATE
- AXL-EUR — CONFIRMED_ACCELERATION — score 6.653/10 — DETECTED_BUT_TOO_LATE
- METIS-EUR — BUILDING_ACCELERATION — score 5.942/10 — DETECTED_BUT_TOO_LATE
- ASTR-EUR — BUILDING_ACCELERATION — score 5.936/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WIN-EUR — BUILDING_ACCELERATION — score 5.567/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GMT-EUR — BUILDING_ACCELERATION — score 5.449/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- WMTX-EUR — MEMORY_24H — score mémoire 9.850/10 — sources ACCELERATION — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 9.365/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 8.687/10 — sources ACCELERATION — MEMORY_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.669/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AMP-EUR — MEMORY_24H — score mémoire 8.589/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SOON-EUR — MEMORY_24H — score mémoire 8.551/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.427/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.366/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- BABY-EUR — ACTIVE_NOW — score mémoire 8.232/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +70.33% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +62.61% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +42.42% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +34.03% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +24.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- W-EUR +20.29% — DETECTED_EARLY — couche NONE — action NONE
- EDGE-EUR +20.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HFT-EUR +17.19% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PYTH-EUR +16.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RUNE-EUR +14.37% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
