# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T09:08:13.445056+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAO-EUR | action ACHETE_MAINTENANT | opportunité 8.961 | entrée 7.300 | trend 7.200 | rang 7.739
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : SOL-EUR | action LATENT_ACCELERATOR | opportunité 7.575 | entrée 4.500 | trend 8.250 | rang 7.199
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AVAX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.338 | entrée 7.750 | trend 8.450 | rang 7.717
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. TAO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.739
2. AVAX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.717
3. RAY-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.443

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- AAVE-EUR — ACTIVE_NOW — score mémoire 8.606/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 8.149/10 — sources V4 — DETECTED_BUT_TOO_LATE
- PENDLE-EUR — ACTIVE_NOW — score mémoire 8.119/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 8.094/10 — sources V4 — WATCH_ONLY
- SYN-EUR — MEMORY_24H — score mémoire 8.094/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 8.087/10 — sources V4 — WATCH_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 8.067/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.936/10 — sources V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 7.895/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ARX-EUR — ACTIVE_NOW — score mémoire 7.891/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +42.01% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZAMA-EUR +40.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HEI-EUR +35.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +29.77% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- XTZ-EUR +28.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +25.27% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIG-EUR +23.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +19.79% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- EPIC-EUR +19.02% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INJ-EUR +18.93% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
