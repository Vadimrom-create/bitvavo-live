# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T22:03:19.313044+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : PEPE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.687 | entrée 6.500 | trend 8.300 | rang 7.540
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SYN-EUR | action LATENT_ACCELERATOR | opportunité 7.592 | entrée 5.100 | trend 7.300 | rang 6.129
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.811 | entrée 6.250 | trend 8.750 | rang 7.733
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.733
2. PEPE-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.540
3. DRIFT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.386

## Accélération indépendante

- CELR-EUR — CONFIRMED_ACCELERATION — score 8.342/10 — DETECTED_BUT_TOO_LATE
- EPIC-EUR — BUILDING_ACCELERATION — score 5.329/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CELR-EUR — ACTIVE_NOW — score mémoire 8.342/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- S-EUR — ACTIVE_NOW — score mémoire 8.112/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 8.105/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- APT-EUR — MEMORY_24H — score mémoire 7.947/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.876/10 — sources V4 — WATCH_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 7.862/10 — sources V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.860/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.856/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.754/10 — sources V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 7.733/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +45.64% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SKL-EUR +36.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +32.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- G-EUR +29.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +24.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +22.01% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ENA-EUR +18.53% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INJ-EUR +17.55% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SYN-EUR +17.45% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CROSS-EUR +17.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
