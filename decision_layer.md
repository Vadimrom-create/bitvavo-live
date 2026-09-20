# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T02:04:32.007660+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : INJ-EUR | action LATENT_ACCELERATOR | opportunité 7.713 | entrée 4.900 | trend 8.600 | rang 6.593
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SOL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.423 | entrée 4.500 | trend 7.900 | rang 7.039
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.039
2. ALGO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.745
3. INJ-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.593

## Accélération indépendante

- ZAMA-EUR — CONFIRMED_ACCELERATION — score 7.949/10 — DETECTED_BUT_TOO_LATE
- G-EUR — CONFIRMED_ACCELERATION — score 7.898/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PROVE-EUR — ACTIVE_NOW — score mémoire 8.426/10 — sources V4 — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 8.296/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 8.069/10 — sources V4 — WATCH_ONLY
- ZAMA-EUR — ACTIVE_NOW — score mémoire 7.949/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- PYTH-EUR — ACTIVE_NOW — score mémoire 7.942/10 — sources V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.925/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CELR-EUR — MEMORY_24H — score mémoire 7.906/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- G-EUR — ACTIVE_NOW — score mémoire 7.898/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- DOT-EUR — MEMORY_24H — score mémoire 7.831/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- ACH-EUR — ACTIVE_NOW — score mémoire 7.818/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +96.48% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +64.15% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZAMA-EUR +29.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +25.94% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INJ-EUR +18.03% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SKL-EUR +17.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOLV-EUR +17.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STX-EUR +16.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIL-EUR +15.85% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +15.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
