# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T21:57:11.786911+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : NEAR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.167 | entrée 5.650 | trend 8.100 | rang 6.871
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Top cross-sectionnel

1. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.871
2. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.758

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- ARB-EUR — MEMORY_24H — score mémoire 9.147/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.258/10 — sources V4 — WATCH_ONLY
- NEO-EUR — MEMORY_24H — score mémoire 7.694/10 — sources V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.673/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.667/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.637/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.622/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — MEMORY_24H — score mémoire 7.567/10 — sources V4 — MEMORY_ONLY
- XPL-EUR — MEMORY_24H — score mémoire 7.565/10 — sources V4 — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.553/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ALIGN-EUR +44.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUFFER-EUR +25.44% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +22.86% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +21.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +19.68% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ASTR-EUR +13.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- G-EUR +10.72% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LAPTOP-EUR +8.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +8.78% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NES-EUR +7.55% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
