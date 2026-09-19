# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T20:03:54.346179+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : ONDO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.283 | entrée 6.000 | trend 7.800 | rang 7.529
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : TAO-EUR | action LATENT_ACCELERATOR | opportunité 7.483 | entrée 4.500 | trend 7.950 | rang 7.084
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SUI-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.327 | entrée 7.800 | trend 8.450 | rang 7.876
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. SUI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.876
2. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.707
3. ONDO-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.529

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- WAL-EUR — ACTIVE_NOW — score mémoire 8.082/10 — sources V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.082/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 7.970/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- LPT-EUR — ACTIVE_NOW — score mémoire 7.909/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.898/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- SUI-EUR — ACTIVE_NOW — score mémoire 7.876/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 7.801/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- APT-EUR — ACTIVE_NOW — score mémoire 7.789/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- DYDX-EUR — ACTIVE_NOW — score mémoire 7.762/10 — sources V4 — WATCH_ONLY
- MIOTA-EUR — ACTIVE_NOW — score mémoire 7.717/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZAMA-EUR +41.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +37.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +37.25% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +34.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CELR-EUR +29.21% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- XTZ-EUR +28.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +22.88% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INJ-EUR +20.17% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +20.04% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CROSS-EUR +18.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
