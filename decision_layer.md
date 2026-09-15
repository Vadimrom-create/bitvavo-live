# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T19:19:11.423501+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : PUMP-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.756 | entrée 6.600 | trend 7.500 | rang 7.239
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.707 | entrée 5.550 | trend 9.200 | rang 7.952
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.952
2. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.419
3. UNI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.293

## Accélération indépendante

- PUMP-EUR — BUILDING_ACCELERATION — score 6.158/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- RAY-EUR — BUILDING_ACCELERATION — score 5.000/10 — DETECTED_BUT_TOO_LATE
- XRP-EUR — BUILDING_ACCELERATION — score 4.836/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- ALIGN-EUR — BUILDING_ACCELERATION — score 4.808/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ARB-EUR — MEMORY_24H — score mémoire 9.147/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.952/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.871/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.840/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.821/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.817/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.811/10 — sources V4 — WATCH_ONLY
- NEO-EUR — MEMORY_24H — score mémoire 7.694/10 — sources V4 — MEMORY_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 7.641/10 — sources V4 — WATCH_ONLY
- AKT-EUR — MEMORY_24H — score mémoire 7.599/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ALIGN-EUR +36.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +29.61% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +26.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUFFER-EUR +16.84% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +14.29% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- VTHO-EUR +12.14% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NES-EUR +11.89% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- GLMR-EUR +11.57% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ASTR-EUR +10.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LAPTOP-EUR +9.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
