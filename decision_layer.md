# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T22:18:41.558465+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SOL-EUR | action ACHETE_MAINTENANT | opportunité 9.273 | entrée 7.800 | trend 8.100 | rang 8.290
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : FLUX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.423 | entrée 6.000 | trend 8.850 | rang 7.861
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BOB-EUR | action LATENT_ACCELERATOR | opportunité 7.515 | entrée 4.500 | trend 8.600 | rang 7.332
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : KMNO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.349 | entrée 6.350 | trend 8.550 | rang 8.126
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. SOL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.290
2. KMNO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.126
3. PYTH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.076

## Accélération indépendante

- NIL-EUR — CONFIRMED_ACCELERATION — score 8.930/10 — DETECTED_BUT_TOO_LATE
- MET-EUR — CONFIRMED_ACCELERATION — score 6.678/10 — DETECTED_BUT_TOO_LATE
- TOSHI-EUR — BUILDING_ACCELERATION — score 5.734/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- USELESS-EUR — BUILDING_ACCELERATION — score 5.713/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BIO-EUR — BUILDING_ACCELERATION — score 5.633/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BOME-EUR — BUILDING_ACCELERATION — score 5.351/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DATAIP-EUR — BUILDING_ACCELERATION — score 5.147/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRO-EUR — BUILDING_ACCELERATION — score 5.127/10 — DETECTED_BUT_TOO_LATE
- BONK-EUR — BUILDING_ACCELERATION — score 4.999/10 — DETECTED_BUT_TOO_LATE
- JUP-EUR — BUILDING_ACCELERATION — score 4.965/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AMP-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 9.545/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 8.968/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NIL-EUR — ACTIVE_NOW — score mémoire 8.930/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SOL-EUR — ACTIVE_NOW — score mémoire 8.290/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KMNO-EUR — ACTIVE_NOW — score mémoire 8.126/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- WIN-EUR — MEMORY_24H — score mémoire 8.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.076/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZBCN-EUR — MEMORY_24H — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- NIL-EUR +39.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CPOOL-EUR +26.58% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SAGA-EUR +24.65% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DBR-EUR +23.91% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- RAY-EUR +16.26% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CAP-EUR +13.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUPER-EUR +13.02% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MET-EUR +12.71% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOM-EUR +12.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +11.61% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
