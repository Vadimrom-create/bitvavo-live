# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T16:24:52.552596+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.012 | entrée 7.250 | trend 8.650 | rang 7.746
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.746
2. DOT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.529
3. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.987

## Accélération indépendante

- ZIG-EUR — CONFIRMED_ACCELERATION — score 8.066/10 — DETECTED_BUT_TOO_LATE
- USELESS-EUR — CONFIRMED_ACCELERATION — score 7.679/10 — DETECTED_BUT_TOO_LATE
- ARB-EUR — BUILDING_ACCELERATION — score 5.985/10 — DETECTED_BUT_TOO_LATE
- CNPY-EUR — BUILDING_ACCELERATION — score 5.733/10 — DETECTED_BUT_TOO_LATE
- STRK-EUR — BUILDING_ACCELERATION — score 4.871/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ICP-EUR — ACTIVE_NOW — score mémoire 8.331/10 — sources V4 — DETECTED_BUT_TOO_LATE
- YB-EUR — ACTIVE_NOW — score mémoire 8.204/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.171/10 — sources V4 — DETECTED_BUT_TOO_LATE
- ZIG-EUR — ACTIVE_NOW — score mémoire 8.066/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.965/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PEAQ-EUR — MEMORY_24H — score mémoire 7.955/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LPT-EUR — MEMORY_24H — score mémoire 7.863/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.806/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.746/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KMNO-EUR — ACTIVE_NOW — score mémoire 7.728/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- G-EUR +84.75% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +52.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +51.59% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- C-EUR +43.62% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +33.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +26.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +25.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARB-EUR +23.33% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- S-EUR +22.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +22.69% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
