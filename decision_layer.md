# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T19:34:56.246145+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.828 | entrée 4.350 | trend 9.200 | rang 7.541
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.541
2. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.496
3. UNI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.259

## Accélération indépendante

- CNPY-EUR — BUILDING_ACCELERATION — score 6.000/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ARB-EUR — MEMORY_24H — score mémoire 9.147/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.890/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.860/10 — sources V4 — WATCH_ONLY
- LDO-EUR — MEMORY_24H — score mémoire 7.811/10 — sources V4 — MEMORY_ONLY
- NEO-EUR — MEMORY_24H — score mémoire 7.694/10 — sources V4 — MEMORY_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.690/10 — sources V4 — WATCH_ONLY
- PHA-EUR — MEMORY_24H — score mémoire 7.641/10 — sources V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.619/10 — sources V4 — WATCH_ONLY
- AKT-EUR — MEMORY_24H — score mémoire 7.599/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- POWR-EUR — MEMORY_24H — score mémoire 7.586/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CNPY-EUR +31.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +30.86% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ALIGN-EUR +30.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUFFER-EUR +15.23% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ASTR-EUR +11.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NES-EUR +11.22% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +10.09% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- VTHO-EUR +9.88% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LAPTOP-EUR +8.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GLMR-EUR +8.06% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
