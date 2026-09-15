# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T23:00:31.835207+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : LSK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.544 | entrée 5.850 | trend 8.400 | rang 7.373
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.373
2. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.229

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.027/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.016/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.781/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.702/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NEO-EUR — MEMORY_24H — score mémoire 7.694/10 — sources V4 — MEMORY_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.667/10 — sources V4 — WATCH_ONLY
- USELESS-EUR — ACTIVE_NOW — score mémoire 7.580/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.566/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.563/10 — sources V4 — WATCH_ONLY
- ORCA-EUR — MEMORY_24H — score mémoire 7.513/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ALIGN-EUR +32.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +31.06% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PUFFER-EUR +28.88% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SYN-EUR +25.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +19.42% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- VTHO-EUR +17.92% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LAPTOP-EUR +15.43% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ASTR-EUR +14.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +12.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- G-EUR +12.00% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
