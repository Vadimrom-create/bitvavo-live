# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T15:46:42.815566+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.812 | entrée 7.200 | trend 7.950 | rang 7.507
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.507
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.417
3. ZAMA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.105

## Accélération indépendante

- SAGA-EUR — BUILDING_ACCELERATION — score 6.195/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- COW-EUR — ACTIVE_NOW — score mémoire 8.014/10 — sources V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.933/10 — sources V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.920/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.885/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.845/10 — sources V4 — WATCH_ONLY
- CELR-EUR — MEMORY_24H — score mémoire 7.831/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ATH-EUR — ACTIVE_NOW — score mémoire 7.792/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.787/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- XTZ-EUR — ACTIVE_NOW — score mémoire 7.742/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- BIGTIME-EUR — MEMORY_24H — score mémoire 7.662/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CELR-EUR +62.82% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +30.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +19.14% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- C-EUR +18.71% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PTB-EUR +18.54% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +17.18% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ALGO-EUR +11.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +10.09% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SKL-EUR +9.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +8.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
