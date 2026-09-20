# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T18:01:52.216977+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : ZAMA-EUR | action LATENT_ACCELERATOR | opportunité 7.404 | entrée 4.500 | trend 7.950 | rang 6.619
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.863 | entrée 7.400 | trend 8.500 | rang 7.745
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.745
2. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.594
3. APT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.444

## Accélération indépendante

- C-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- STRK-EUR — CONFIRMED_ACCELERATION — score 7.992/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SAGA-EUR — MEMORY_24H — score mémoire 9.730/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PTB-EUR — MEMORY_24H — score mémoire 8.518/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- C-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- AIOZ-EUR — ACTIVE_NOW — score mémoire 8.235/10 — sources V4 — WATCH_ONLY
- ARX-EUR — ACTIVE_NOW — score mémoire 8.152/10 — sources V4 — WATCH_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 8.037/10 — sources V4 — WATCH_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 8.016/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- STRK-EUR — ACTIVE_NOW — score mémoire 7.992/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- VVV-EUR — ACTIVE_NOW — score mémoire 7.929/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SUSHI-EUR — ACTIVE_NOW — score mémoire 7.890/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +47.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +36.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PTB-EUR +35.63% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FTT-EUR +25.17% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- C-EUR +21.48% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LUNA2-EUR +17.89% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AVAX-EUR +14.15% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +13.59% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +13.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVA-EUR +12.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
