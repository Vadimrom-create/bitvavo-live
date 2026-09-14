# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T00:28:24.481446+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : WLD-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.197 | entrée 5.850 | trend 8.150 | rang 7.113
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Top cross-sectionnel

1. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.113

## Accélération indépendante

- FIL-EUR — CONFIRMED_ACCELERATION — score 7.453/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.913/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.776/10 — sources V4 — WATCH_ONLY
- APT-EUR — MEMORY_24H — score mémoire 7.715/10 — sources V4 — MEMORY_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.634/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.626/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.580/10 — sources V4 — WATCH_ONLY
- ZIG-EUR — MEMORY_24H — score mémoire 7.576/10 — sources V4 — MEMORY_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.558/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.543/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.524/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +108.65% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- VTHO-EUR +25.39% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CVC-EUR +25.16% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +20.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOLV-EUR +17.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZKJ-EUR +16.51% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- IQ-EUR +14.73% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- MTL-EUR +12.94% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- REZ-EUR +9.91% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIL-EUR +9.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
