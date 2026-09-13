# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T15:34:53.946145+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : USELESS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.145 | entrée 5.800 | trend 8.100 | rang 6.899
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Top cross-sectionnel

1. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.899

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- ETHFI-EUR — MEMORY_24H — score mémoire 8.092/10 — sources V4 — MEMORY_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.998/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 7.981/10 — sources ACCELERATION, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.956/10 — sources V4 — WATCH_ONLY
- BIGTIME-EUR — MEMORY_24H — score mémoire 7.931/10 — sources V4 — MEMORY_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.870/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.783/10 — sources V4 — WATCH_ONLY
- AVAX-EUR — MEMORY_24H — score mémoire 7.656/10 — sources V4 — MEMORY_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.635/10 — sources V4 — WATCH_ONLY
- SPX-EUR — ACTIVE_NOW — score mémoire 7.602/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +277.00% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CVC-EUR +64.47% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +22.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +21.53% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FIL-EUR +14.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRAX-EUR +12.78% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- KNC-EUR +11.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BAT-EUR +11.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- REZ-EUR +10.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ANKR-EUR +9.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
