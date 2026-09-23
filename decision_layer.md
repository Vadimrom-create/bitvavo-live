# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T21:11:52.571364+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : WIF-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.601 | entrée 6.600 | trend 7.450 | rang 7.666
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ZRO-EUR | action LATENT_ACCELERATOR | opportunité 7.435 | entrée 5.400 | trend 8.200 | rang 6.781
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PYTH-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.658 | entrée 6.250 | trend 8.450 | rang 7.969
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. PYTH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.969
2. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.803
3. WIF-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.666

## Accélération indépendante

- NOM-EUR — CONFIRMED_ACCELERATION — score 8.867/10 — DETECTED_BUT_TOO_LATE
- TRAC-EUR — CONFIRMED_ACCELERATION — score 8.303/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — BUILDING_ACCELERATION — score 6.209/10 — DETECTED_BUT_TOO_LATE
- DATAIP-EUR — BUILDING_ACCELERATION — score 4.925/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CPOOL-EUR — BUILDING_ACCELERATION — score 4.800/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AMP-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TRIA-EUR — MEMORY_24H — score mémoire 9.219/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NOM-EUR — ACTIVE_NOW — score mémoire 8.867/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- TRAC-EUR — ACTIVE_NOW — score mémoire 8.303/10 — sources ACCELERATION, V4 — WATCH_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZBCN-EUR — MEMORY_24H — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 7.969/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- BEAM-EUR — ACTIVE_NOW — score mémoire 7.895/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XRP-EUR — MEMORY_24H — score mémoire 7.855/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +31.27% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CPOOL-EUR +27.03% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DBR-EUR +24.41% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- NIL-EUR +23.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOM-EUR +18.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RAY-EUR +17.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +12.18% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +11.62% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MET-EUR +11.06% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LIGHTER-EUR +9.99% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
