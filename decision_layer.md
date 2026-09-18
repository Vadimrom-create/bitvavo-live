# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T13:52:16.662548+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : INJ-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.975 | entrée 6.400 | trend 8.300 | rang 6.919
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : SYRUP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.870 | entrée 5.850 | trend 7.950 | rang 6.852
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. INJ-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 6.919
2. SYRUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.852

## Accélération indépendante

- BTC-EUR — BUILDING_ACCELERATION — score 6.184/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- AAVE-EUR — BUILDING_ACCELERATION — score 6.095/10 — DETECTED_BUT_TOO_LATE
- SOL-EUR — BUILDING_ACCELERATION — score 6.014/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- XRP-EUR — BUILDING_ACCELERATION — score 5.695/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- ETH-EUR — BUILDING_ACCELERATION — score 5.499/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- PEPE-EUR — BUILDING_ACCELERATION — score 5.330/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- AERO-EUR — ACTIVE_NOW — score mémoire 8.231/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.169/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.164/10 — sources V4 — WATCH_ONLY
- BNB-EUR — ACTIVE_NOW — score mémoire 7.907/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.889/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.869/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.862/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.827/10 — sources V4 — WATCH_ONLY
- PEAQ-EUR — ACTIVE_NOW — score mémoire 7.787/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.765/10 — sources V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- G-EUR +90.75% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +39.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +29.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +26.65% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DRIFT-EUR +23.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRK-EUR +23.85% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +23.81% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- APT-EUR +19.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +19.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DYDX-EUR +17.35% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
