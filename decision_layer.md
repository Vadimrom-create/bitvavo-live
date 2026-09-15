# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T10:59:38.536958+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : FET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.219 | entrée 6.250 | trend 7.650 | rang 7.065
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Top cross-sectionnel

1. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.065

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- LAPTOP-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.046/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- USELESS-EUR — ACTIVE_NOW — score mémoire 7.974/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- UNI-EUR — ACTIVE_NOW — score mémoire 7.947/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.871/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- BNB-EUR — ACTIVE_NOW — score mémoire 7.814/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.751/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.703/10 — sources V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.660/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PUFFER-EUR +30.66% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +24.20% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +20.23% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ASTR-EUR +15.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LAPTOP-EUR +13.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CAP-EUR +12.94% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CROSS-EUR +10.65% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FLOCK-EUR +10.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ACE-EUR +7.72% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- COTI-EUR +7.45% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
