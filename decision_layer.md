# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T21:40:36.664215+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : LSK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.327 | entrée 5.000 | trend 8.400 | rang 7.174
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Top cross-sectionnel

1. LSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.174

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- CNPY-EUR — MEMORY_24H — score mémoire 8.734/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.090/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.906/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — MEMORY_24H — score mémoire 7.899/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.851/10 — sources V4 — WATCH_ONLY
- KAVA-EUR — ACTIVE_NOW — score mémoire 7.824/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.776/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.679/10 — sources V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 7.676/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- VVV-EUR — MEMORY_24H — score mémoire 7.623/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CPOOL-EUR +42.67% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +32.24% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CAP-EUR +28.78% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +24.79% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- MTL-EUR +17.76% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- BOB-EUR +16.20% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PENDLE-EUR +13.21% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SENT-EUR +11.85% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RED-EUR +11.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ACX-EUR +10.95% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
