# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T14:43:56.153557+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SUI-EUR | action ACHETE_MAINTENANT | opportunité 8.186 | entrée 7.000 | trend 6.500 | rang 7.056
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SAGA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.563 | entrée 6.250 | trend 7.800 | rang 7.037
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : WAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.038 | entrée 5.650 | trend 8.700 | rang 7.747
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.747
2. ALGO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.402
3. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.318

## Accélération indépendante

- C-EUR — CONFIRMED_ACCELERATION — score 8.471/10 — DETECTED_BUT_TOO_LATE
- SYN-EUR — CONFIRMED_ACCELERATION — score 7.711/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- C-EUR — ACTIVE_NOW — score mémoire 8.471/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- AIOZ-EUR — ACTIVE_NOW — score mémoire 8.338/10 — sources V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 8.064/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SIGN-EUR — ACTIVE_NOW — score mémoire 7.991/10 — sources V4 — WATCH_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 7.918/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.877/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- CELR-EUR — MEMORY_24H — score mémoire 7.831/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.797/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 7.754/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.747/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +80.47% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +28.79% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PTB-EUR +18.09% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- C-EUR +17.98% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AVAX-EUR +16.39% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CTSI-EUR +11.88% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- S-EUR +9.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +7.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +7.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALGO-EUR +6.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
