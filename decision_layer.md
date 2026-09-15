# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T22:18:43.328864+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.427 | entrée 7.000 | trend 9.200 | rang 7.324
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.324
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.961

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.069/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.923/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.847/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LIGHTER-EUR — ACTIVE_NOW — score mémoire 7.755/10 — sources V4 — WATCH_ONLY
- NEO-EUR — MEMORY_24H — score mémoire 7.694/10 — sources V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.634/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.627/10 — sources V4 — WATCH_ONLY
- XPL-EUR — MEMORY_24H — score mémoire 7.565/10 — sources V4 — MEMORY_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 7.547/10 — sources V4 — WATCH_ONLY
- ORCA-EUR — MEMORY_24H — score mémoire 7.513/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ALIGN-EUR +41.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUFFER-EUR +27.17% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +23.17% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +20.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +19.08% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ASTR-EUR +13.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LAPTOP-EUR +12.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +9.64% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +9.34% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARB-EUR +8.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
