# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T21:49:54.884335+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : NPC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.637 | entrée 6.050 | trend 7.750 | rang 7.136
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DOT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.062 | entrée 7.450 | trend 8.300 | rang 7.543
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. DOT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.543
2. COTI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.209
3. NPC-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.136

## Accélération indépendante

- ZEN-EUR — BUILDING_ACCELERATION — score 5.786/10 — DETECTED_BUT_TOO_LATE
- G-EUR — BUILDING_ACCELERATION — score 5.745/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- VET-EUR — ACTIVE_NOW — score mémoire 8.401/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.932/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PEAQ-EUR — ACTIVE_NOW — score mémoire 7.903/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.829/10 — sources V4 — WATCH_ONLY
- ORCA-EUR — MEMORY_24H — score mémoire 7.810/10 — sources V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.794/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.776/10 — sources V4 — WATCH_ONLY
- COMP-EUR — ACTIVE_NOW — score mémoire 7.773/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.728/10 — sources V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 7.664/10 — sources V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- STRK-EUR +58.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- G-EUR +45.79% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- F-EUR +41.88% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARB-EUR +25.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +24.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +24.31% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- APT-EUR +24.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +23.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +22.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +21.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
