# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T21:12:00.276217+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : LSK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.503 | entrée 6.000 | trend 8.400 | rang 7.435
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.435
2. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.276
3. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.098

## Accélération indépendante

- ALIGN-EUR — CONFIRMED_ACCELERATION — score 9.807/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ALIGN-EUR — ACTIVE_NOW — score mémoire 9.807/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- ARB-EUR — MEMORY_24H — score mémoire 9.147/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.749/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.708/10 — sources V4 — WATCH_ONLY
- NEO-EUR — MEMORY_24H — score mémoire 7.694/10 — sources V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.662/10 — sources V4 — WATCH_ONLY
- LDO-EUR — MEMORY_24H — score mémoire 7.632/10 — sources V4 — MEMORY_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.567/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- XPL-EUR — MEMORY_24H — score mémoire 7.565/10 — sources V4 — MEMORY_ONLY
- ORCA-EUR — MEMORY_24H — score mémoire 7.513/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ALIGN-EUR +53.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +19.24% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PUFFER-EUR +16.55% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- VTHO-EUR +15.33% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CNPY-EUR +12.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ASTR-EUR +12.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- G-EUR +11.50% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CROSS-EUR +7.90% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LAPTOP-EUR +7.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DYM-EUR +7.66% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
