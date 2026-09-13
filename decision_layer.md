# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T15:19:34.046457+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.636 | entrée 4.600 | trend 9.200 | rang 6.575
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.575

## Accélération indépendante

- LSK-EUR — CONFIRMED_ACCELERATION — score 6.913/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- VET-EUR — ACTIVE_NOW — score mémoire 8.134/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.092/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.037/10 — sources V4 — WATCH_ONLY
- BIGTIME-EUR — ACTIVE_NOW — score mémoire 7.931/10 — sources V4 — WATCH_ONLY
- SPX-EUR — ACTIVE_NOW — score mémoire 7.850/10 — sources V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 7.845/10 — sources ACCELERATION, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.812/10 — sources V4 — WATCH_ONLY
- AVAX-EUR — MEMORY_24H — score mémoire 7.656/10 — sources V4 — MEMORY_ONLY
- STRK-EUR — ACTIVE_NOW — score mémoire 7.655/10 — sources V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.620/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +254.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CVC-EUR +73.63% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +26.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +20.62% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- POWR-EUR +17.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRAX-EUR +14.23% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +13.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BAT-EUR +13.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FLOCK-EUR +13.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KNC-EUR +12.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
