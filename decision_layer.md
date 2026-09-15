# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T20:39:23.575918+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : USELESS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.733 | entrée 7.600 | trend 8.100 | rang 7.364
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.364
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.045
3. NPC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.899

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- ARB-EUR — MEMORY_24H — score mémoire 9.147/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.737/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- NEO-EUR — MEMORY_24H — score mémoire 7.694/10 — sources V4 — MEMORY_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.630/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AKT-EUR — MEMORY_24H — score mémoire 7.599/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.580/10 — sources V4 — WATCH_ONLY
- XPL-EUR — MEMORY_24H — score mémoire 7.565/10 — sources V4 — MEMORY_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.562/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.557/10 — sources V4 — WATCH_ONLY
- RED-EUR — ACTIVE_NOW — score mémoire 7.543/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ALIGN-EUR +32.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +23.34% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PUFFER-EUR +15.37% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ASTR-EUR +12.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +11.68% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- G-EUR +11.34% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- GLMR-EUR +8.05% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CNPY-EUR +7.88% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ACX-EUR +7.38% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LAPTOP-EUR +7.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
