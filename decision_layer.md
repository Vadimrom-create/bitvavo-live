# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T14:56:41.238615+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : IOST-EUR | action LATENT_ACCELERATOR | opportunité 7.523 | entrée 5.550 | trend 7.550 | rang 6.546
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : TAO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.346 | entrée 6.150 | trend 7.650 | rang 6.991
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Top cross-sectionnel

1. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.991
2. IOST-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.546
3. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.353

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.841/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.818/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.818/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZORA-EUR — MEMORY_24H — score mémoire 7.801/10 — sources V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.657/10 — sources V4 — WATCH_ONLY
- ALGO-EUR — MEMORY_24H — score mémoire 7.613/10 — sources V4 — MEMORY_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.602/10 — sources V4 — WATCH_ONLY
- DOT-EUR — ACTIVE_NOW — score mémoire 7.596/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AVAX-EUR — MEMORY_24H — score mémoire 7.587/10 — sources V4 — MEMORY_ONLY
- ZEN-EUR — MEMORY_24H — score mémoire 7.586/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SYN-EUR +126.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +47.29% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HEI-EUR +19.78% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FOLD-EUR +17.30% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- USELESS-EUR +17.04% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARB-EUR +16.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +13.64% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- IOST-EUR +12.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TAI-EUR +11.71% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SOSO-EUR +6.38% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
