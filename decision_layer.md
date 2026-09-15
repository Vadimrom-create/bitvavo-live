# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T20:22:57.047548+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.719 | entrée 5.950 | trend 8.650 | rang 7.576
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.576
2. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.027
3. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.996

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- ARB-EUR — MEMORY_24H — score mémoire 9.147/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.729/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NEO-EUR — MEMORY_24H — score mémoire 7.694/10 — sources V4 — MEMORY_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.641/10 — sources V4 — WATCH_ONLY
- AKT-EUR — MEMORY_24H — score mémoire 7.599/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- YGG-EUR — MEMORY_24H — score mémoire 7.579/10 — sources V4 — MEMORY_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.576/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XPL-EUR — MEMORY_24H — score mémoire 7.565/10 — sources V4 — MEMORY_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.540/10 — sources V4 — WATCH_ONLY
- ORCA-EUR — MEMORY_24H — score mémoire 7.513/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +29.00% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ALIGN-EUR +28.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUFFER-EUR +14.62% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +13.97% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ASTR-EUR +12.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +11.30% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +9.94% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +8.60% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NES-EUR +7.53% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LAPTOP-EUR +7.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
