# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T17:49:59.169925+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.354 | entrée 5.000 | trend 9.200 | rang 7.696
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.696
2. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.453
3. NPC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.290

## Accélération indépendante

- ALIGN-EUR — CONFIRMED_ACCELERATION — score 8.942/10 — DETECTED_BUT_TOO_LATE
- SAGA-EUR — CONFIRMED_ACCELERATION — score 7.060/10 — DETECTED_BUT_TOO_LATE
- NPC-EUR — BUILDING_ACCELERATION — score 5.981/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- USELESS-EUR — BUILDING_ACCELERATION — score 5.068/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ARB-EUR — MEMORY_24H — score mémoire 9.147/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ALIGN-EUR — ACTIVE_NOW — score mémoire 8.942/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- VET-EUR — ACTIVE_NOW — score mémoire 8.454/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 8.135/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.097/10 — sources V4 — WATCH_ONLY
- NEAR-EUR — ACTIVE_NOW — score mémoire 7.890/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ICP-EUR — ACTIVE_NOW — score mémoire 7.825/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.798/10 — sources V4 — WATCH_ONLY
- ZRO-EUR — ACTIVE_NOW — score mémoire 7.795/10 — sources V4 — WATCH_ONLY
- COMP-EUR — ACTIVE_NOW — score mémoire 7.776/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ALIGN-EUR +36.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +36.38% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PUFFER-EUR +18.07% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +17.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ASTR-EUR +15.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NES-EUR +14.53% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LAPTOP-EUR +12.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +11.62% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- POWR-EUR +9.48% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CAP-EUR +9.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
