# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T18:59:37.263249+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : NEAR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.609 | entrée 6.300 | trend 8.100 | rang 7.632
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.632
2. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.606
3. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.437

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- ARB-EUR — MEMORY_24H — score mémoire 9.147/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ALIGN-EUR — MEMORY_24H — score mémoire 8.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.401/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 8.248/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.063/10 — sources V4 — WATCH_ONLY
- S-EUR — ACTIVE_NOW — score mémoire 8.062/10 — sources V4 — WATCH_ONLY
- LIGHTER-EUR — ACTIVE_NOW — score mémoire 8.042/10 — sources V4 — WATCH_ONLY
- YGG-EUR — ACTIVE_NOW — score mémoire 7.957/10 — sources V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.867/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.816/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ALIGN-EUR +36.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +29.06% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +24.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUFFER-EUR +15.08% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NES-EUR +12.88% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ASTR-EUR +12.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +11.55% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZKJ-EUR +11.44% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GLMR-EUR +9.49% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +9.45% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
