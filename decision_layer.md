# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T11:21:56.853133+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : NEAR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.224 | entrée 7.350 | trend 8.100 | rang 7.419
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.419

## Accélération indépendante

- SYN-EUR — CONFIRMED_ACCELERATION — score 8.664/10 — DETECTED_BUT_TOO_LATE
- LSK-EUR — BUILDING_ACCELERATION — score 6.000/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SYN-EUR — ACTIVE_NOW — score mémoire 8.664/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.092/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.050/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.047/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.004/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.004/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.766/10 — sources V4 — WATCH_ONLY
- CVC-EUR — MEMORY_24H — score mémoire 7.734/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 7.723/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- DOT-EUR — ACTIVE_NOW — score mémoire 7.720/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- SYN-EUR +127.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +70.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CNPY-EUR +23.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +17.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +16.27% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FOLD-EUR +15.46% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HEI-EUR +13.47% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ALIGN-EUR +12.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- G-EUR +9.08% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZKJ-EUR +8.18% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
