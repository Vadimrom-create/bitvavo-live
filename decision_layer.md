# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T16:54:19.517287+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : LSK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.622 | entrée 5.800 | trend 8.400 | rang 7.346
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.346
2. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.119
3. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.030

## Accélération indépendante

- UNI-EUR — BUILDING_ACCELERATION — score 5.887/10 — DETECTED_BUT_TOO_LATE
- EDEN-EUR — BUILDING_ACCELERATION — score 5.739/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- VET-EUR — ACTIVE_NOW — score mémoire 8.289/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 8.001/10 — sources V4 — WATCH_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 7.985/10 — sources V4 — DETECTED_BUT_TOO_LATE
- LDO-EUR — ACTIVE_NOW — score mémoire 7.934/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.869/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.868/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.864/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.793/10 — sources V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.791/10 — sources V4 — DETECTED_BUT_TOO_LATE
- YB-EUR — ACTIVE_NOW — score mémoire 7.786/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AVA-EUR +96.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +30.39% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- KSM-EUR +28.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +25.72% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- UNI-EUR +23.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +22.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +21.62% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PEAQ-EUR +21.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +19.97% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GALA-EUR +18.86% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
