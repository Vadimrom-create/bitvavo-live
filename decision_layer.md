# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T19:55:50.349992+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : NPC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.445 | entrée 6.300 | trend 7.750 | rang 7.012
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : USELESS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.473 | entrée 6.700 | trend 8.100 | rang 6.955
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. NPC-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.012
2. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.955

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 8.356/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.974/10 — sources V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.969/10 — sources V4 — WATCH_ONLY
- SYRUP-EUR — ACTIVE_NOW — score mémoire 7.965/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.903/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.824/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.715/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.696/10 — sources V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 7.647/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.643/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CNPY-EUR +38.73% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CPOOL-EUR +36.17% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CAP-EUR +22.71% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +19.17% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- MTL-EUR +16.20% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- SENT-EUR +13.48% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PENDLE-EUR +10.34% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- NEAR-EUR +9.29% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ACX-EUR +9.11% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- T-EUR +9.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
