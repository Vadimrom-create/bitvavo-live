# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T21:37:02.571126+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : PEPE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.727 | entrée 6.300 | trend 8.300 | rang 7.505
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.067 | entrée 6.250 | trend 8.750 | rang 7.851
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.851
2. PEPE-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.505
3. ONDO-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.447

## Accélération indépendante

- G-EUR — CONFIRMED_ACCELERATION — score 7.101/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SENT-EUR — ACTIVE_NOW — score mémoire 8.018/10 — sources V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.979/10 — sources V4 — WATCH_ONLY
- ENS-EUR — ACTIVE_NOW — score mémoire 7.907/10 — sources V4 — WATCH_ONLY
- APT-EUR — ACTIVE_NOW — score mémoire 7.907/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.852/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 7.851/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.802/10 — sources V4 — WATCH_ONLY
- S-EUR — ACTIVE_NOW — score mémoire 7.799/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.730/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PEAQ-EUR — MEMORY_24H — score mémoire 7.726/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZAMA-EUR +35.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +29.42% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CELR-EUR +26.49% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +25.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +25.11% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +20.45% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SOLV-EUR +20.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +17.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INJ-EUR +17.11% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AVAX-EUR +16.45% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
