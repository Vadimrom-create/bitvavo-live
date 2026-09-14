# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T21:55:47.074635+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : NPC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.621 | entrée 6.700 | trend 7.750 | rang 7.248
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : NEAR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.810 | entrée 6.450 | trend 8.100 | rang 7.276
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.276
2. NPC-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.248
3. UNI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.220

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- CNPY-EUR — MEMORY_24H — score mémoire 8.734/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.101/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.008/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.939/10 — sources V4 — WATCH_ONLY
- SOLV-EUR — ACTIVE_NOW — score mémoire 7.884/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.877/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.777/10 — sources V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 7.684/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- VVV-EUR — MEMORY_24H — score mémoire 7.623/10 — sources V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.596/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CPOOL-EUR +35.31% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CAP-EUR +34.93% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +31.31% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ARK-EUR +26.65% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- BOB-EUR +23.11% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- MTL-EUR +18.01% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- PENDLE-EUR +12.83% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SENT-EUR +12.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +11.62% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- RED-EUR +11.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
