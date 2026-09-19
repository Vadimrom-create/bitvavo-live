# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T04:56:20.932294+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.795 | entrée 7.000 | trend 8.250 | rang 7.610
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.610
2. UNI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.534
3. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.347

## Accélération indépendante

- SYN-EUR — BUILDING_ACCELERATION — score 5.750/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AERO-EUR — ACTIVE_NOW — score mémoire 8.514/10 — sources V4 — WATCH_ONLY
- RAY-EUR — ACTIVE_NOW — score mémoire 8.121/10 — sources ACCELERATION, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.061/10 — sources ACCELERATION, V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 7.968/10 — sources V4 — WATCH_ONLY
- BEAM-EUR — ACTIVE_NOW — score mémoire 7.782/10 — sources V4 — WATCH_ONLY
- ZRO-EUR — MEMORY_24H — score mémoire 7.741/10 — sources V4 — MEMORY_ONLY
- T-EUR — ACTIVE_NOW — score mémoire 7.728/10 — sources ACCELERATION, V4 — WATCH_ONLY
- S-EUR — ACTIVE_NOW — score mémoire 7.690/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.676/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- USELESS-EUR — MEMORY_24H — score mémoire 7.675/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- G-EUR +64.94% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- F-EUR +33.83% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +32.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +23.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +23.38% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CPOOL-EUR +21.79% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- MORPHO-EUR +19.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +19.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +19.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +16.74% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
