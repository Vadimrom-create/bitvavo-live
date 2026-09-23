# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T23:00:59.796713+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SOL-EUR | action ACHETE_MAINTENANT | opportunité 7.998 | entrée 7.350 | trend 8.100 | rang 7.673
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ENS-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.630 | entrée 5.900 | trend 7.850 | rang 7.183
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : KMNO-EUR | action LATENT_ACCELERATOR | opportunité 8.242 | entrée 5.700 | trend 8.550 | rang 7.553
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : DATAIP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.942 | entrée 7.200 | trend 7.850 | rang 7.955
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. DATAIP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.955
2. FLUX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.876
3. ATH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.763

## Accélération indépendante

- TOWNS-EUR — BUILDING_ACCELERATION — score 5.983/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LUMIA-EUR — BUILDING_ACCELERATION — score 5.757/10 — DETECTED_BUT_TOO_LATE
- REQ-EUR — BUILDING_ACCELERATION — score 5.314/10 — DETECTED_BUT_TOO_LATE
- FLOCK-EUR — BUILDING_ACCELERATION — score 4.976/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — BUILDING_ACCELERATION — score 4.900/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AMP-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 9.545/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZBCN-EUR — MEMORY_24H — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DATAIP-EUR — ACTIVE_NOW — score mémoire 7.955/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FLUX-EUR — ACTIVE_NOW — score mémoire 7.876/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ATH-EUR — ACTIVE_NOW — score mémoire 7.763/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AAVE-EUR — MEMORY_24H — score mémoire 7.755/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- NIL-EUR +46.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CPOOL-EUR +26.88% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SAGA-EUR +20.50% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DBR-EUR +20.01% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- NOM-EUR +15.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RAY-EUR +12.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +11.21% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CAP-EUR +10.79% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +9.85% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOSO-EUR +9.41% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
