# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T17:29:12.688511+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : WAL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.797 | entrée 5.850 | trend 9.200 | rang 7.761
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : COW-EUR | action LATENT_ACCELERATOR | opportunité 7.426 | entrée 5.750 | trend 8.900 | rang 7.550
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LPT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.460 | entrée 7.050 | trend 8.750 | rang 7.927
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LPT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.927
2. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.904
3. WAL-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.761

## Accélération indépendante

- SYN-EUR — CONFIRMED_ACCELERATION — score 9.518/10 — DETECTED_BUT_TOO_LATE
- TRAC-EUR — CONFIRMED_ACCELERATION — score 8.588/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZBCN-EUR — CONFIRMED_ACCELERATION — score 7.851/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LPT-EUR — CONFIRMED_ACCELERATION — score 6.879/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MOG-EUR — BUILDING_ACCELERATION — score 6.314/10 — DETECTED_BUT_TOO_LATE
- AGI-EUR — BUILDING_ACCELERATION — score 6.126/10 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — BUILDING_ACCELERATION — score 6.017/10 — DETECTED_BUT_TOO_LATE
- C-EUR — BUILDING_ACCELERATION — score 5.580/10 — DETECTED_BUT_TOO_LATE
- ZETA-EUR — BUILDING_ACCELERATION — score 5.176/10 — DETECTED_BUT_TOO_LATE
- ZEUS-EUR — BUILDING_ACCELERATION — score 5.047/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- RON-EUR — MEMORY_24H — score mémoire 9.938/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CPOOL-EUR — MEMORY_24H — score mémoire 9.834/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEPE-EUR — MEMORY_24H — score mémoire 9.525/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SYN-EUR — ACTIVE_NOW — score mémoire 9.518/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- THQ-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACU-EUR — MEMORY_24H — score mémoire 9.053/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LUMIA-EUR — MEMORY_24H — score mémoire 8.655/10 — sources ACCELERATION — MEMORY_ONLY
- TRAC-EUR — ACTIVE_NOW — score mémoire 8.588/10 — sources ACCELERATION, V4 — WATCH_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- ZRC-EUR +229.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICX-EUR +181.57% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZETA-EUR +51.86% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- FORM-EUR +47.48% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SWELL-EUR +42.51% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +33.82% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEPE-EUR +23.56% — DETECTED_EARLY — couche NONE — action NONE
- AIOZ-EUR +23.17% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PTB-EUR +22.45% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NOS-EUR +20.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
