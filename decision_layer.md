# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T19:34:05.181369+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : NEAR-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.492 | entrée 6.550 | trend 8.100 | rang 6.428
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VVV-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.111 | entrée 6.900 | trend 7.600 | rang 7.501
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VVV-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.501
2. NEAR-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 6.428

## Accélération indépendante

- NPC-EUR — BUILDING_ACCELERATION — score 5.151/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CNPY-EUR — MEMORY_24H — score mémoire 9.527/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 8.297/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.273/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.883/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.867/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.857/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.770/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.764/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.698/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.654/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AVA-EUR +86.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +51.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- COTI-EUR +32.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +30.61% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CROSS-EUR +30.59% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +21.31% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- UNI-EUR +21.02% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +20.95% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- KSM-EUR +19.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +19.33% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
