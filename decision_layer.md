# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T14:34:28.608996+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : FET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.883 | entrée 7.500 | trend 7.650 | rang 7.316
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.316
2. SYRUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.236

## Accélération indépendante

- ONDO-EUR — BUILDING_ACCELERATION — score 5.996/10 — DETECTED_BUT_TOO_LATE
- SYRUP-EUR — BUILDING_ACCELERATION — score 5.557/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- PEPE-EUR — BUILDING_ACCELERATION — score 4.867/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- RAY-EUR — BUILDING_ACCELERATION — score 4.815/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- VET-EUR — ACTIVE_NOW — score mémoire 8.544/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.300/10 — sources V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 8.234/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 8.091/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.039/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.939/10 — sources V4 — WATCH_ONLY
- AKT-EUR — ACTIVE_NOW — score mémoire 7.856/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.762/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.734/10 — sources V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 7.710/10 — sources V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- AVA-EUR +93.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +26.45% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AGI-EUR +24.56% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PEAQ-EUR +23.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +21.88% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDEN-EUR +20.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LIGHTER-EUR +18.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- COTI-EUR +17.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +17.83% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FLOCK-EUR +17.08% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
