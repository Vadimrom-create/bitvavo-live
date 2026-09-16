# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T01:53:48.753956+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : VTHO-EUR | action LATENT_ACCELERATOR | opportunité 7.580 | entrée 5.300 | trend 9.200 | rang 6.641
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LSK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.361 | entrée 5.600 | trend 8.400 | rang 6.998
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Top cross-sectionnel

1. LSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.998
2. VTHO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.641

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 7.685/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.668/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.619/10 — sources V4 — WATCH_ONLY
- SIGN-EUR — ACTIVE_NOW — score mémoire 7.604/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — MEMORY_24H — score mémoire 7.598/10 — sources V4 — MEMORY_ONLY
- RED-EUR — ACTIVE_NOW — score mémoire 7.580/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.564/10 — sources V4 — WATCH_ONLY
- ORCA-EUR — MEMORY_24H — score mémoire 7.513/10 — sources V4 — MEMORY_ONLY
- ZRO-EUR — MEMORY_24H — score mémoire 7.489/10 — sources V4 — MEMORY_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.484/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PUFFER-EUR +35.05% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ALIGN-EUR +33.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LAPTOP-EUR +24.97% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- VTHO-EUR +20.49% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CROSS-EUR +19.54% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +18.06% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SYN-EUR +17.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +15.65% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARB-EUR +11.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +9.28% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
