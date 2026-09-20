# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T08:50:31.277303+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : INJ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.584 | entrée 6.400 | trend 8.300 | rang 7.627
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.627
2. ENA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.589
3. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.436

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- RAY-EUR — ACTIVE_NOW — score mémoire 7.922/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.885/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 7.838/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.785/10 — sources V4 — WATCH_ONLY
- BIGTIME-EUR — ACTIVE_NOW — score mémoire 7.775/10 — sources V4 — WATCH_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 7.734/10 — sources V4 — WATCH_ONLY
- XTZ-EUR — ACTIVE_NOW — score mémoire 7.731/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.641/10 — sources V4 — WATCH_ONLY
- VVV-EUR — ACTIVE_NOW — score mémoire 7.630/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 7.627/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- CELR-EUR +77.34% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIL-EUR +23.81% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SKL-EUR +16.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +15.46% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SOLV-EUR +11.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STX-EUR +10.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +10.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- JTO-EUR +10.38% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +10.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +10.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
