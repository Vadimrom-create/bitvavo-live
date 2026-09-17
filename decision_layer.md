# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T06:51:29.059724+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : TAO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.334 | entrée 7.250 | trend 7.650 | rang 7.197
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Top cross-sectionnel

1. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.197
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.985

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- TREAD-EUR — MEMORY_24H — score mémoire 8.348/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.265/10 — sources V4 — WATCH_ONLY
- GRT-EUR — ACTIVE_NOW — score mémoire 8.119/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.115/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.992/10 — sources V4 — WATCH_ONLY
- KMNO-EUR — MEMORY_24H — score mémoire 7.862/10 — sources V4 — MEMORY_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.779/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 7.778/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.763/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.759/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AVA-EUR +59.99% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +29.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +26.44% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HNT-EUR +23.54% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- QUID-EUR +17.70% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- USELESS-EUR +17.06% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SAGA-EUR +16.75% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NEAR-EUR +15.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- VVV-EUR +14.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +14.03% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
