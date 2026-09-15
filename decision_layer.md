# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T18:44:33.251701+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.654 | entrée 4.350 | trend 9.200 | rang 7.463
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.463
2. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.055

## Accélération indépendante

- SAGA-EUR — BUILDING_ACCELERATION — score 5.268/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ARB-EUR — MEMORY_24H — score mémoire 9.147/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ALIGN-EUR — MEMORY_24H — score mémoire 8.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- UNI-EUR — MEMORY_24H — score mémoire 7.836/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.816/10 — sources V4 — WATCH_ONLY
- NEO-EUR — MEMORY_24H — score mémoire 7.694/10 — sources V4 — MEMORY_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.670/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.652/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.633/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- POWR-EUR — MEMORY_24H — score mémoire 7.586/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.569/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ALIGN-EUR +31.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +30.38% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +19.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUFFER-EUR +18.83% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ASTR-EUR +13.51% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NES-EUR +11.23% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- GLMR-EUR +10.00% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- VTHO-EUR +9.80% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- G-EUR +9.65% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- LAPTOP-EUR +9.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
