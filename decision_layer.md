# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T08:00:47.425701+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : NEAR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.740 | entrée 7.000 | trend 8.100 | rang 6.719
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.719

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- VET-EUR — ACTIVE_NOW — score mémoire 8.294/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- YGG-EUR — ACTIVE_NOW — score mémoire 8.127/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.088/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.060/10 — sources V4 — WATCH_ONLY
- TAO-EUR — ACTIVE_NOW — score mémoire 7.990/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.984/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.866/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.855/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.807/10 — sources V4 — WATCH_ONLY
- MASK-EUR — ACTIVE_NOW — score mémoire 7.755/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AVA-EUR +62.02% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +29.51% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HNT-EUR +27.10% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PEAQ-EUR +20.25% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QUID-EUR +18.20% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- NEAR-EUR +17.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RAY-EUR +15.79% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +14.64% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LIGHTER-EUR +14.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALIGN-EUR +13.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
