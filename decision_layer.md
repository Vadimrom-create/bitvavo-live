# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T09:26:47.506003+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.688 | entrée 6.500 | trend 9.200 | rang 8.155
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.155
2. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.500
3. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.198

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- LAPTOP-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.155/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.794/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.662/10 — sources V4 — WATCH_ONLY
- RED-EUR — ACTIVE_NOW — score mémoire 7.646/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.640/10 — sources V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.631/10 — sources V4 — DETECTED_BUT_TOO_LATE
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.608/10 — sources V4 — WATCH_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 7.599/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.579/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PUFFER-EUR +29.95% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CAP-EUR +26.43% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +25.50% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ASTR-EUR +18.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LAPTOP-EUR +17.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ACX-EUR +11.82% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +11.56% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ACE-EUR +10.59% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- CROSS-EUR +9.29% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- COTI-EUR +9.26% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
