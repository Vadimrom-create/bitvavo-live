# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T06:27:44.391445+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : TAO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.272 | entrée 6.800 | trend 7.650 | rang 7.140
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Top cross-sectionnel

1. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.140
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.941

## Accélération indépendante

- TREAD-EUR — CONFIRMED_ACCELERATION — score 8.348/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- TREAD-EUR — ACTIVE_NOW — score mémoire 8.348/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.271/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.127/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.961/10 — sources V4 — WATCH_ONLY
- ZRO-EUR — ACTIVE_NOW — score mémoire 7.921/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.893/10 — sources V4 — WATCH_ONLY
- KMNO-EUR — MEMORY_24H — score mémoire 7.862/10 — sources V4 — MEMORY_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 7.718/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.651/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.646/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +53.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVA-EUR +46.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HNT-EUR +24.35% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- QUID-EUR +19.20% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- HEI-EUR +18.03% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FOLD-EUR +17.82% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- USELESS-EUR +16.65% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NEAR-EUR +14.95% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- VVV-EUR +14.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +14.29% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
