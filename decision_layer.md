# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T22:42:49.965577+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : TAO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.704 | entrée 6.300 | trend 7.650 | rang 7.114
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DOT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.807 | entrée 6.600 | trend 8.300 | rang 7.593
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. DOT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.593
2. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.311
3. TAO-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.114

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- CNPY-EUR — MEMORY_24H — score mémoire 9.527/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.321/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.085/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.062/10 — sources V4 — WATCH_ONLY
- CHILLGUY-EUR — ACTIVE_NOW — score mémoire 8.044/10 — sources V4 — DETECTED_BUT_TOO_LATE
- METIS-EUR — ACTIVE_NOW — score mémoire 7.933/10 — sources V4 — WATCH_ONLY
- KMNO-EUR — ACTIVE_NOW — score mémoire 7.931/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.927/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.869/10 — sources V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.858/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AVA-EUR +77.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- COTI-EUR +50.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +40.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +40.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +39.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +27.99% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- DRIFT-EUR +21.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +18.84% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- G-EUR +18.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +18.02% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
