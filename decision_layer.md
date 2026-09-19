# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T08:52:29.118671+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAO-EUR | action ACHETE_MAINTENANT | opportunité 8.530 | entrée 7.500 | trend 7.200 | rang 7.551
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : AVAX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.255 | entrée 8.200 | trend 8.450 | rang 7.845
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. AVAX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.845
2. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.797
3. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.618

## Accélération indépendante

- SYN-EUR — CONFIRMED_ACCELERATION — score 8.094/10 — DETECTED_BUT_TOO_LATE
- G-EUR — CONFIRMED_ACCELERATION — score 6.500/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AAVE-EUR — ACTIVE_NOW — score mémoire 8.683/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ARX-EUR — ACTIVE_NOW — score mémoire 8.180/10 — sources V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 8.109/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SYN-EUR — ACTIVE_NOW — score mémoire 8.094/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LSK-EUR — MEMORY_24H — score mémoire 8.067/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACH-EUR — MEMORY_24H — score mémoire 8.031/10 — sources V4 — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.012/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 8.001/10 — sources V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 7.958/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.930/10 — sources V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- SYN-EUR +53.08% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZAMA-EUR +42.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +35.17% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HEI-EUR +32.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +27.37% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- XTZ-EUR +25.59% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +23.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INJ-EUR +21.47% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SAGA-EUR +19.47% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- EPIC-EUR +19.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
