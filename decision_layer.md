# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T19:25:20.958059+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 8.215 | entrée 7.600 | trend 8.500 | rang 7.921
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : ZAMA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.146 | entrée 6.400 | trend 7.950 | rang 7.691
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.921
2. ZAMA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.691
3. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.522

## Accélération indépendante

- SKL-EUR — CONFIRMED_ACCELERATION — score 9.028/10 — DETECTED_BUT_TOO_LATE
- ZAMA-EUR — CONFIRMED_ACCELERATION — score 7.174/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SKL-EUR — ACTIVE_NOW — score mémoire 9.028/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PTB-EUR — MEMORY_24H — score mémoire 8.518/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- C-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- T-EUR — ACTIVE_NOW — score mémoire 8.244/10 — sources ACCELERATION, V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 8.170/10 — sources V4 — WATCH_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 8.067/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 8.051/10 — sources V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 7.921/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.852/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 7.766/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +49.02% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CELR-EUR +30.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PTB-EUR +25.07% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SKL-EUR +23.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRK-EUR +18.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +17.46% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- S-EUR +16.81% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +16.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +15.67% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +14.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
