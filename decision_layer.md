# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T23:09:19.941539+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LINK-EUR | action ACHETE_MAINTENANT | opportunité 7.517 | entrée 7.200 | trend 5.350 | rang 6.312
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : TREE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.096 | entrée 5.950 | trend 7.950 | rang 8.000
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : KMNO-EUR | action LATENT_ACCELERATOR | opportunité 8.166 | entrée 5.700 | trend 8.550 | rang 7.518
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : FLUX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.338 | entrée 6.250 | trend 8.850 | rang 7.900
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. TREE-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 8.000
2. FLUX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.900
3. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.762

## Accélération indépendante

- NIL-EUR — CONFIRMED_ACCELERATION — score 7.618/10 — DETECTED_BUT_TOO_LATE
- SOSO-EUR — CONFIRMED_ACCELERATION — score 7.165/10 — DETECTED_BUT_TOO_LATE
- TAI-EUR — BUILDING_ACCELERATION — score 6.373/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LUMIA-EUR — BUILDING_ACCELERATION — score 5.419/10 — DETECTED_BUT_TOO_LATE
- TOWNS-EUR — BUILDING_ACCELERATION — score 5.405/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- REQ-EUR — BUILDING_ACCELERATION — score 5.314/10 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — BUILDING_ACCELERATION — score 5.262/10 — DETECTED_BUT_TOO_LATE
- FLOCK-EUR — BUILDING_ACCELERATION — score 4.876/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- AMP-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 9.545/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZBCN-EUR — MEMORY_24H — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREE-EUR — ACTIVE_NOW — score mémoire 8.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FLUX-EUR — ACTIVE_NOW — score mémoire 7.900/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- VET-EUR — ACTIVE_NOW — score mémoire 7.762/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 7.675/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FIL-EUR — ACTIVE_NOW — score mémoire 7.628/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- NIL-EUR +52.99% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CPOOL-EUR +25.73% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SAGA-EUR +21.30% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DBR-EUR +20.83% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- NOM-EUR +14.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RAY-EUR +11.09% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CAP-EUR +10.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOSO-EUR +10.02% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- SUPER-EUR +9.46% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LSK-EUR +8.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
