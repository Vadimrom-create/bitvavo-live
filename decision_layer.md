# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T19:00:51.085698+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : INJ-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.410 | entrée 6.250 | trend 8.300 | rang 6.559
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DOT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.031 | entrée 7.400 | trend 8.300 | rang 7.781
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. DOT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.781
2. LSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.331
3. INJ-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 6.559

## Accélération indépendante

- STRK-EUR — CONFIRMED_ACCELERATION — score 9.982/10 — DETECTED_BUT_TOO_LATE
- CNPY-EUR — BUILDING_ACCELERATION — score 5.236/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- STRK-EUR — ACTIVE_NOW — score mémoire 9.982/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- XVG-EUR — ACTIVE_NOW — score mémoire 8.468/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.186/10 — sources V4 — DETECTED_BUT_TOO_LATE
- YB-EUR — ACTIVE_NOW — score mémoire 8.037/10 — sources V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 8.017/10 — sources V4 — DETECTED_BUT_TOO_LATE
- VET-EUR — ACTIVE_NOW — score mémoire 7.962/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.944/10 — sources V4 — DETECTED_BUT_TOO_LATE
- DOT-EUR — ACTIVE_NOW — score mémoire 7.781/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 7.676/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.675/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- G-EUR +67.86% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +46.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +38.43% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NEAR-EUR +25.46% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- C-EUR +24.52% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +23.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +22.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +21.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +20.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ETHFI-EUR +19.87% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
