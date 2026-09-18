# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T19:20:01.976995+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : LSK-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.799 | entrée 6.100 | trend 8.400 | rang 7.553
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DOT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.969 | entrée 6.750 | trend 8.300 | rang 7.660
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. DOT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.660
2. LSK-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.553
3. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.271

## Accélération indépendante

- ZEN-EUR — CONFIRMED_ACCELERATION — score 6.873/10 — DETECTED_BUT_TOO_LATE
- STRK-EUR — BUILDING_ACCELERATION — score 6.108/10 — DETECTED_BUT_TOO_LATE
- PUMP-EUR — BUILDING_ACCELERATION — score 5.851/10 — DETECTED_BUT_TOO_LATE
- AVAX-EUR — BUILDING_ACCELERATION — score 5.427/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- SOL-EUR — BUILDING_ACCELERATION — score 4.799/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- XVG-EUR — ACTIVE_NOW — score mémoire 8.206/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.110/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.102/10 — sources V4 — DETECTED_BUT_TOO_LATE
- VET-EUR — ACTIVE_NOW — score mémoire 8.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ENS-EUR — ACTIVE_NOW — score mémoire 8.017/10 — sources V4 — DETECTED_BUT_TOO_LATE
- METIS-EUR — ACTIVE_NOW — score mémoire 7.938/10 — sources V4 — DETECTED_BUT_TOO_LATE
- ICP-EUR — ACTIVE_NOW — score mémoire 7.856/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 7.787/10 — sources V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 7.780/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.766/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- G-EUR +58.75% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +50.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +38.66% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NEAR-EUR +26.34% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CNPY-EUR +25.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +24.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +23.15% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIG-EUR +22.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZK-EUR +22.38% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- S-EUR +21.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
