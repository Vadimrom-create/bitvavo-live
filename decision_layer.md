# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T22:34:05.717798+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SOL-EUR | action ACHETE_MAINTENANT | opportunité 7.651 | entrée 7.150 | trend 8.100 | rang 7.497
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : FLUX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.242 | entrée 6.000 | trend 8.850 | rang 7.844
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : BEAM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.606 | entrée 6.350 | trend 8.950 | rang 8.045
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. BEAM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.045
2. FLUX-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.844
3. KMNO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.815

## Accélération indépendante

- NIL-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- CHR-EUR — CONFIRMED_ACCELERATION — score 7.554/10 — DETECTED_BUT_TOO_LATE
- PONKE-EUR — BUILDING_ACCELERATION — score 6.330/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- 0G-EUR — BUILDING_ACCELERATION — score 6.156/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NOS-EUR — BUILDING_ACCELERATION — score 5.797/10 — DETECTED_BUT_TOO_LATE
- UNI-EUR — BUILDING_ACCELERATION — score 5.653/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PEAQ-EUR — BUILDING_ACCELERATION — score 5.393/10 — DETECTED_BUT_TOO_LATE
- ACE-EUR — BUILDING_ACCELERATION — score 4.885/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- AMP-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 9.545/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 8.968/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NIL-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- WIN-EUR — MEMORY_24H — score mémoire 8.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZBCN-EUR — MEMORY_24H — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BEAM-EUR — ACTIVE_NOW — score mémoire 8.045/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FLUX-EUR — ACTIVE_NOW — score mémoire 7.844/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KMNO-EUR — ACTIVE_NOW — score mémoire 7.815/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- NIL-EUR +45.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CPOOL-EUR +26.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DBR-EUR +23.51% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- SAGA-EUR +22.53% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RAY-EUR +13.80% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CAP-EUR +10.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOM-EUR +10.79% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUPER-EUR +10.55% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LIGHTER-EUR +10.15% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- UP-EUR +8.95% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
