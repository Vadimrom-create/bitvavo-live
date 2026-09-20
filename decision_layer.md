# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T01:03:24.302620+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.008 | entrée 7.600 | trend 8.450 | rang 7.531
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.531
2. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.251
3. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.914

## Accélération indépendante

- CELR-EUR — CONFIRMED_ACCELERATION — score 7.906/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- WAL-EUR — ACTIVE_NOW — score mémoire 8.052/10 — sources V4 — WATCH_ONLY
- AAVE-EUR — MEMORY_24H — score mémoire 7.941/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CELR-EUR — ACTIVE_NOW — score mémoire 7.906/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- SAGA-EUR — ACTIVE_NOW — score mémoire 7.846/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- STX-EUR — ACTIVE_NOW — score mémoire 7.844/10 — sources V4 — DETECTED_BUT_TOO_LATE
- DOT-EUR — ACTIVE_NOW — score mémoire 7.831/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- MIOTA-EUR — ACTIVE_NOW — score mémoire 7.808/10 — sources V4 — WATCH_ONLY
- BIGTIME-EUR — ACTIVE_NOW — score mémoire 7.804/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.798/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ETC-EUR — MEMORY_24H — score mémoire 7.770/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CELR-EUR +74.72% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +45.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +31.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +24.48% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XTZ-EUR +22.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +22.29% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- INJ-EUR +20.75% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZIL-EUR +20.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +18.75% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SKL-EUR +17.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
