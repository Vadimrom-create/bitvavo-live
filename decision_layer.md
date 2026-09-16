# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T04:52:08.125488+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.646 | entrée 6.900 | trend 9.200 | rang 8.083
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.083
2. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.208

## Accélération indépendante

- LSK-EUR — CONFIRMED_ACCELERATION — score 6.808/10 — DETECTED_BUT_TOO_LATE
- ALIGN-EUR — BUILDING_ACCELERATION — score 6.185/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ICP-EUR — ACTIVE_NOW — score mémoire 8.310/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 8.142/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.083/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.841/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.793/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.779/10 — sources V4 — WATCH_ONLY
- RED-EUR — ACTIVE_NOW — score mémoire 7.708/10 — sources V4 — WATCH_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 7.667/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ALGO-EUR — MEMORY_24H — score mémoire 7.613/10 — sources V4 — MEMORY_ONLY
- AVAX-EUR — ACTIVE_NOW — score mémoire 7.608/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +34.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SYN-EUR +27.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +22.25% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ARB-EUR +17.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALIGN-EUR +12.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LAPTOP-EUR +11.79% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- USELESS-EUR +11.14% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FOLD-EUR +10.75% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- GLMR-EUR +9.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUFFER-EUR +8.10% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
