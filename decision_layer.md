# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T08:45:43.640406+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : EIGEN-EUR | action ACHETE_MAINTENANT | opportunité 9.498 | entrée 7.650 | trend 9.200 | rang 8.634
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AKT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.493 | entrée 6.100 | trend 8.650 | rang 7.879
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SPK-EUR | action LATENT_ACCELERATOR | opportunité 8.261 | entrée 5.600 | trend 8.900 | rang 7.840
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : CHZ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.340 | entrée 6.550 | trend 8.750 | rang 8.432
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. EIGEN-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.634
2. RENDER-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.608
3. CHZ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.432

## Accélération indépendante

- ARX-EUR — CONFIRMED_ACCELERATION — score 9.302/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IKA-EUR — BUILDING_ACCELERATION — score 5.770/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LQTY-EUR — BUILDING_ACCELERATION — score 5.548/10 — DETECTED_BUT_TOO_LATE
- NIL-EUR — BUILDING_ACCELERATION — score 5.281/10 — DETECTED_BUT_TOO_LATE
- XVG-EUR — BUILDING_ACCELERATION — score 5.189/10 — DETECTED_BUT_TOO_LATE
- BREV-EUR — BUILDING_ACCELERATION — score 5.077/10 — DETECTED_BUT_TOO_LATE
- EIGEN-EUR — BUILDING_ACCELERATION — score 5.073/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MET-EUR — BUILDING_ACCELERATION — score 4.954/10 — DETECTED_BUT_TOO_LATE
- QUID-EUR — BUILDING_ACCELERATION — score 4.915/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ID-EUR — BUILDING_ACCELERATION — score 4.889/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- WMTX-EUR — MEMORY_24H — score mémoire 9.850/10 — sources ACCELERATION — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 9.365/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ARX-EUR — ACTIVE_NOW — score mémoire 9.302/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- EIGEN-EUR — ACTIVE_NOW — score mémoire 8.634/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.608/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AMP-EUR — MEMORY_24H — score mémoire 8.589/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CHZ-EUR — ACTIVE_NOW — score mémoire 8.432/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.432/10 — sources ACCELERATION — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.427/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 8.425/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +70.58% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +55.93% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +43.44% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +32.67% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HFT-EUR +24.59% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- AGI-EUR +23.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- W-EUR +19.81% — DETECTED_EARLY — couche NONE — action NONE
- EDGE-EUR +18.50% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XVG-EUR +17.14% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- TRIA-EUR +15.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
