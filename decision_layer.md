# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T19:49:42.350565+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : VTHO-EUR | action LATENT_ACCELERATOR | opportunité 7.986 | entrée 4.700 | trend 9.200 | rang 7.560
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : VET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.998 | entrée 5.400 | trend 8.650 | rang 7.681
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.681
2. VTHO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.560
3. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.070

## Accélération indépendante

- SAGA-EUR — BUILDING_ACCELERATION — score 4.782/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ARB-EUR — MEMORY_24H — score mémoire 9.147/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.822/10 — sources V4 — WATCH_ONLY
- LDO-EUR — MEMORY_24H — score mémoire 7.811/10 — sources V4 — MEMORY_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.727/10 — sources V4 — WATCH_ONLY
- NEO-EUR — MEMORY_24H — score mémoire 7.694/10 — sources V4 — MEMORY_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.681/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AKT-EUR — MEMORY_24H — score mémoire 7.599/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- POWR-EUR — MEMORY_24H — score mémoire 7.586/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.578/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.566/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +32.01% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ALIGN-EUR +31.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +28.25% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUFFER-EUR +14.75% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ASTR-EUR +11.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NES-EUR +11.01% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- VTHO-EUR +10.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- G-EUR +9.05% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- GLMR-EUR +8.81% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LAPTOP-EUR +8.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
