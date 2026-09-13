# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T19:21:25.050681+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : USELESS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.882 | entrée 7.050 | trend 8.100 | rang 7.165
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.165

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- CAKE-EUR — ACTIVE_NOW — score mémoire 8.029/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.935/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PORTAL-EUR — MEMORY_24H — score mémoire 7.868/10 — sources V4 — MEMORY_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.848/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.766/10 — sources V4 — WATCH_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 7.715/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.691/10 — sources V4 — WATCH_ONLY
- YGG-EUR — ACTIVE_NOW — score mémoire 7.675/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.607/10 — sources V4 — WATCH_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 7.598/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +254.46% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CVC-EUR +56.18% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- REZ-EUR +29.64% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +24.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +18.61% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARK-EUR +18.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIL-EUR +17.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- POWR-EUR +12.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOLV-EUR +11.88% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +11.79% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
