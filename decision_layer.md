# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T08:06:03.101978+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.492 | entrée 5.650 | trend 9.200 | rang 7.944
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.944
2. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.517
3. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.132

## Accélération indépendante

- CNPY-EUR — CONFIRMED_ACCELERATION — score 9.819/10 — DETECTED_BUT_TOO_LATE
- VTHO-EUR — BUILDING_ACCELERATION — score 5.705/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- DRIFT-EUR — BUILDING_ACCELERATION — score 5.679/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CNPY-EUR — ACTIVE_NOW — score mémoire 9.819/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.132/10 — sources V4 — DETECTED_BUT_TOO_LATE
- LDO-EUR — ACTIVE_NOW — score mémoire 8.123/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.106/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.026/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.964/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.944/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.791/10 — sources V4 — WATCH_ONLY
- PORTAL-EUR — ACTIVE_NOW — score mémoire 7.784/10 — sources V4 — WATCH_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.751/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- G-EUR +71.01% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- DRIFT-EUR +45.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +37.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +29.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +28.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +27.86% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- UNI-EUR +27.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- COTI-EUR +19.85% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRK-EUR +19.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MET-EUR +19.35% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
