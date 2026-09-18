# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T09:19:32.247718+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.502 | entrée 5.000 | trend 9.200 | rang 7.727
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.727
2. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.918

## Accélération indépendante

- RAY-EUR — CONFIRMED_ACCELERATION — score 9.566/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- RAY-EUR — ACTIVE_NOW — score mémoire 9.566/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- LDO-EUR — ACTIVE_NOW — score mémoire 8.321/10 — sources V4 — WATCH_ONLY
- SYRUP-EUR — ACTIVE_NOW — score mémoire 7.965/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.958/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.887/10 — sources V4 — DETECTED_BUT_TOO_LATE
- VET-EUR — ACTIVE_NOW — score mémoire 7.844/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.843/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.811/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.808/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.808/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- G-EUR +87.42% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- DRIFT-EUR +38.02% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +37.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +31.51% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +29.15% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- STRK-EUR +26.11% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RAY-EUR +25.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +25.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +23.06% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- COTI-EUR +17.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
