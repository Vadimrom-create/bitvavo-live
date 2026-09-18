# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T23:12:07.833319+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : WLD-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.391 | entrée 6.350 | trend 8.150 | rang 6.902
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Top cross-sectionnel

1. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.902

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- VTHO-EUR — ACTIVE_NOW — score mémoire 8.119/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.048/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.923/10 — sources V4 — WATCH_ONLY
- CHILLGUY-EUR — ACTIVE_NOW — score mémoire 7.799/10 — sources V4 — DETECTED_BUT_TOO_LATE
- VET-EUR — ACTIVE_NOW — score mémoire 7.759/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 7.726/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.685/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- SIGN-EUR — ACTIVE_NOW — score mémoire 7.649/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.632/10 — sources V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 7.571/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- F-EUR +64.94% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +54.75% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +51.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +32.45% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARB-EUR +25.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +22.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZK-EUR +21.09% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- APT-EUR +20.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +20.63% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- S-EUR +19.25% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
