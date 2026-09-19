# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T23:02:22.874844+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.964 | entrée 6.550 | trend 8.750 | rang 7.828
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.828
2. PEPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.825
3. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.790

## Accélération indépendante

- INJ-EUR — BUILDING_ACCELERATION — score 5.066/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SUPER-EUR — ACTIVE_NOW — score mémoire 8.344/10 — sources V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.143/10 — sources V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 8.044/10 — sources V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.944/10 — sources V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.936/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GRT-EUR — ACTIVE_NOW — score mémoire 7.926/10 — sources V4 — WATCH_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 7.907/10 — sources V4 — DETECTED_BUT_TOO_LATE
- APT-EUR — ACTIVE_NOW — score mémoire 7.904/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.887/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 7.866/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +58.04% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZAMA-EUR +40.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- G-EUR +25.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +25.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INJ-EUR +24.49% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +23.71% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ENA-EUR +20.32% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AVAX-EUR +19.16% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SKL-EUR +18.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RON-EUR +12.70% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
