# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T06:54:04.049438+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ONDO-EUR | action ACHETE_MAINTENANT | opportunité 9.410 | entrée 7.600 | trend 8.750 | rang 8.594
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : STX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.745 | entrée 6.550 | trend 8.650 | rang 7.689
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : PENDLE-EUR | action LATENT_ACCELERATOR | opportunité 7.473 | entrée 4.500 | trend 8.650 | rang 7.332
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : INJ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.220 | entrée 6.550 | trend 8.650 | rang 7.889
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ONDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.594
2. W-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.031
3. KAS-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.903

## Accélération indépendante

- EPIC-EUR — CONFIRMED_ACCELERATION — score 9.319/10 — DETECTED_BUT_TOO_LATE
- ZBCN-EUR — CONFIRMED_ACCELERATION — score 7.677/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CTR-EUR — CONFIRMED_ACCELERATION — score 6.943/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KERNEL-EUR — BUILDING_ACCELERATION — score 6.411/10 — DETECTED_BUT_TOO_LATE
- RON-EUR — BUILDING_ACCELERATION — score 5.533/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EDEN-EUR — BUILDING_ACCELERATION — score 4.919/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CELR-EUR — BUILDING_ACCELERATION — score 4.846/10 — DETECTED_BUT_TOO_LATE
- PONKE-EUR — BUILDING_ACCELERATION — score 4.846/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LUMIA-EUR — BUILDING_ACCELERATION — score 4.821/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- INIT-EUR — MEMORY_24H — score mémoire 9.655/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- EPIC-EUR — ACTIVE_NOW — score mémoire 9.319/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CTC-EUR — MEMORY_24H — score mémoire 9.245/10 — sources ACCELERATION — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 9.049/10 — sources ACCELERATION — MEMORY_ONLY
- FORM-EUR — MEMORY_24H — score mémoire 8.879/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BOME-EUR — MEMORY_24H — score mémoire 8.655/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ONDO-EUR — ACTIVE_NOW — score mémoire 8.594/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HOME-EUR — MEMORY_24H — score mémoire 8.582/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZETA-EUR +67.56% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PTB-EUR +57.90% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FTT-EUR +40.38% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NIL-EUR +39.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +27.03% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EPIC-EUR +26.97% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NEAR-EUR +24.70% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +24.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VVV-EUR +21.68% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +21.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
