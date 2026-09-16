# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T13:23:51.470109+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : TAO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.133 | entrée 6.450 | trend 7.650 | rang 7.031
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Top cross-sectionnel

1. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.031
2. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.719

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- IOST-EUR — MEMORY_24H — score mémoire 8.811/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.986/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- DOT-EUR — ACTIVE_NOW — score mémoire 7.952/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- KAS-EUR — ACTIVE_NOW — score mémoire 7.876/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.807/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.738/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.683/10 — sources V4 — WATCH_ONLY
- UNI-EUR — MEMORY_24H — score mémoire 7.629/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ALGO-EUR — MEMORY_24H — score mémoire 7.613/10 — sources V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.599/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +116.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +47.28% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +27.37% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ARB-EUR +19.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +18.65% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HEI-EUR +14.50% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- USELESS-EUR +14.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CNPY-EUR +14.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IOST-EUR +14.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZKJ-EUR +10.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
