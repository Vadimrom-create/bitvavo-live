# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T01:50:35.378097+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : VET-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.751 | entrée 6.000 | trend 8.450 | rang 7.446
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : INJ-EUR | action LATENT_ACCELERATOR | opportunité 7.830 | entrée 4.900 | trend 8.600 | rang 6.582
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SOL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.628 | entrée 6.550 | trend 7.900 | rang 7.379
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.446
2. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.379
3. ALGO-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 6.686

## Accélération indépendante

- G-EUR — CONFIRMED_ACCELERATION — score 7.806/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PENDLE-EUR — ACTIVE_NOW — score mémoire 8.076/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.914/10 — sources V4 — WATCH_ONLY
- CELR-EUR — MEMORY_24H — score mémoire 7.906/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZK-EUR — MEMORY_24H — score mémoire 7.863/10 — sources V4 — MEMORY_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 7.845/10 — sources V4 — WATCH_ONLY
- DOT-EUR — MEMORY_24H — score mémoire 7.831/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 7.817/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- G-EUR — ACTIVE_NOW — score mémoire 7.806/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- STX-EUR — ACTIVE_NOW — score mémoire 7.788/10 — sources V4 — DETECTED_BUT_TOO_LATE
- ACH-EUR — ACTIVE_NOW — score mémoire 7.779/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +80.06% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +57.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +28.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +21.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +20.48% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- INJ-EUR +19.06% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SKL-EUR +18.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIL-EUR +17.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOLV-EUR +17.11% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +14.51% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
