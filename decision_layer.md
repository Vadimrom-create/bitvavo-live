# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T18:24:40.161079+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : UNI-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.906 | entrée 6.950 | trend 7.750 | rang 7.836
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. UNI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.836
2. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.773
3. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.513

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- ARB-EUR — MEMORY_24H — score mémoire 9.147/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ALIGN-EUR — MEMORY_24H — score mémoire 8.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- UNI-EUR — ACTIVE_NOW — score mémoire 7.836/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.800/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.773/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.706/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.704/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.695/10 — sources V4 — WATCH_ONLY
- NEO-EUR — ACTIVE_NOW — score mémoire 7.694/10 — sources V4 — WATCH_ONLY
- SYRUP-EUR — ACTIVE_NOW — score mémoire 7.644/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ALIGN-EUR +38.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +33.05% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PUFFER-EUR +19.44% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +16.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ASTR-EUR +14.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NES-EUR +14.32% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LAPTOP-EUR +10.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +9.64% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CROSS-EUR +9.00% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- GLMR-EUR +8.73% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
