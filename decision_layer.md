# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T08:27:51.880844+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 9.101 | entrée 7.950 | trend 8.750 | rang 8.492
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : BEAM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.623 | entrée 6.050 | trend 8.950 | rang 8.038
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SPK-EUR | action LATENT_ACCELERATOR | opportunité 8.326 | entrée 5.600 | trend 8.900 | rang 7.750
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ROSE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.270 | entrée 6.800 | trend 8.950 | rang 8.475
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.492
2. ROSE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.475
3. FIL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.415

## Accélération indépendante

- HFT-EUR — CONFIRMED_ACCELERATION — score 8.432/10 — DETECTED_BUT_TOO_LATE
- MEW-EUR — CONFIRMED_ACCELERATION — score 6.769/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- JASMY-EUR — BUILDING_ACCELERATION — score 6.076/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POND-EUR — BUILDING_ACCELERATION — score 5.921/10 — DETECTED_BUT_TOO_LATE
- XYO-EUR — BUILDING_ACCELERATION — score 5.566/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KERNEL-EUR — BUILDING_ACCELERATION — score 5.394/10 — DETECTED_BUT_TOO_LATE
- QNT-EUR — BUILDING_ACCELERATION — score 5.319/10 — DETECTED_BUT_TOO_LATE
- FIDA-EUR — BUILDING_ACCELERATION — score 4.834/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- WMTX-EUR — MEMORY_24H — score mémoire 9.850/10 — sources ACCELERATION — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 9.365/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 8.687/10 — sources ACCELERATION — MEMORY_ONLY
- AMP-EUR — MEMORY_24H — score mémoire 8.589/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.492/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ROSE-EUR — ACTIVE_NOW — score mémoire 8.475/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HFT-EUR — ACTIVE_NOW — score mémoire 8.432/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- FTT-EUR — MEMORY_24H — score mémoire 8.427/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FIL-EUR — ACTIVE_NOW — score mémoire 8.415/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +66.73% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +50.47% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +43.34% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +32.52% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HFT-EUR +28.95% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- AGI-EUR +24.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- W-EUR +20.66% — DETECTED_EARLY — couche NONE — action NONE
- EDGE-EUR +19.84% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PYTH-EUR +17.09% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XVG-EUR +15.11% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
