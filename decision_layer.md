# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T18:32:51.326319+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : LSK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.379 | entrée 5.000 | trend 8.400 | rang 7.228
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Top cross-sectionnel

1. LSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.228
2. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.915

## Accélération indépendante

- NPC-EUR — BUILDING_ACCELERATION — score 4.765/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- USELESS-EUR — MEMORY_24H — score mémoire 9.044/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AIOZ-EUR — MEMORY_24H — score mémoire 8.298/10 — sources V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.264/10 — sources V4 — DETECTED_BUT_TOO_LATE
- PHA-EUR — ACTIVE_NOW — score mémoire 8.162/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.035/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.011/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.958/10 — sources V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 7.902/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.804/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.801/10 — sources V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- G-EUR +72.35% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- F-EUR +42.77% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +41.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRK-EUR +35.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +26.56% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NEAR-EUR +22.94% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARB-EUR +22.81% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +20.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +20.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APT-EUR +19.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
