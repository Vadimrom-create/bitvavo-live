# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T17:35:54.198342+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.837 | entrée 4.800 | trend 9.200 | rang 7.632
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.632
2. UNI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.359
3. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.319

## Accélération indépendante

- SAGA-EUR — CONFIRMED_ACCELERATION — score 9.154/10 — DETECTED_BUT_TOO_LATE
- ALIGN-EUR — CONFIRMED_ACCELERATION — score 8.355/10 — DETECTED_BUT_TOO_LATE
- LAPTOP-EUR — CONFIRMED_ACCELERATION — score 6.866/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- USELESS-EUR — BUILDING_ACCELERATION — score 5.907/10 — DETECTED_BUT_TOO_LATE
- PLUME-EUR — BUILDING_ACCELERATION — score 4.768/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- SAGA-EUR — ACTIVE_NOW — score mémoire 9.154/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- ARB-EUR — MEMORY_24H — score mémoire 9.147/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ALIGN-EUR — ACTIVE_NOW — score mémoire 8.355/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- LDO-EUR — ACTIVE_NOW — score mémoire 7.828/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.768/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.732/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.724/10 — sources V4 — WATCH_ONLY
- TIA-EUR — MEMORY_24H — score mémoire 7.702/10 — sources V4 — MEMORY_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.655/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.632/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ALIGN-EUR +41.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +36.37% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PUFFER-EUR +18.07% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +15.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NES-EUR +15.49% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ASTR-EUR +14.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +10.67% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZKJ-EUR +9.94% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LAPTOP-EUR +9.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- POWR-EUR +8.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
