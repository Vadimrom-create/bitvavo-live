# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T18:12:58.340179+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : TAO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.603 | entrée 6.550 | trend 7.650 | rang 7.173
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.173

## Accélération indépendante

- USELESS-EUR — CONFIRMED_ACCELERATION — score 9.044/10 — DETECTED_BUT_TOO_LATE
- CNPY-EUR — BUILDING_ACCELERATION — score 5.607/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- USELESS-EUR — ACTIVE_NOW — score mémoire 9.044/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LDO-EUR — ACTIVE_NOW — score mémoire 8.301/10 — sources V4 — DETECTED_BUT_TOO_LATE
- AIOZ-EUR — MEMORY_24H — score mémoire 8.298/10 — sources V4 — MEMORY_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 8.286/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.012/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 7.917/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.854/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.852/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.821/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- G-EUR +84.07% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +46.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +44.66% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +33.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +27.48% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NEAR-EUR +25.18% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SAGA-EUR +22.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +21.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APT-EUR +20.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- A-EUR +20.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
