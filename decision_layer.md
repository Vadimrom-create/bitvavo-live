# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T23:34:20.567026+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.780 | entrée 5.300 | trend 9.200 | rang 6.959
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.959

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.006/10 — sources V4 — WATCH_ONLY
- XTZ-EUR — ACTIVE_NOW — score mémoire 7.908/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.897/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.885/10 — sources V4 — WATCH_ONLY
- XPL-EUR — ACTIVE_NOW — score mémoire 7.745/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.742/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.717/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.711/10 — sources V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.651/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.598/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ALIGN-EUR +38.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +33.37% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PUFFER-EUR +31.59% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LAPTOP-EUR +23.61% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CNPY-EUR +23.13% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SYN-EUR +18.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +16.89% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ASTR-EUR +13.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +13.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +11.49% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
