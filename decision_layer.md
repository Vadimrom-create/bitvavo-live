# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T13:40:11.208153+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HBAR-EUR | action ACHETE_MAINTENANT | opportunité 8.844 | entrée 7.400 | trend 6.550 | rang 7.401
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ENSO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.743 | entrée 6.250 | trend 8.750 | rang 7.642
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : WAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.416 | entrée 5.400 | trend 8.700 | rang 7.431
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ENSO-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.642
2. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.431
3. HBAR-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.401

## Accélération indépendante

- EPIC-EUR — CONFIRMED_ACCELERATION — score 9.138/10 — DETECTED_BUT_TOO_LATE
- G-EUR — CONFIRMED_ACCELERATION — score 7.833/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- STRK-EUR — BUILDING_ACCELERATION — score 6.435/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- HBAR-EUR — ACTIVE_NOW — score mémoire 7.401/10 — sources DECISION_LAYER, V4 — BUYABLE_NOW
- ALGO-EUR — ACTIVE_NOW — score mémoire 6.984/10 — sources DECISION_LAYER, V4 — BUYABLE_NOW
- EPIC-EUR — ACTIVE_NOW — score mémoire 9.138/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AIOZ-EUR — MEMORY_24H — score mémoire 8.123/10 — sources V4 — MEMORY_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 8.068/10 — sources V4 — WATCH_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 7.906/10 — sources V4 — WATCH_ONLY
- COTI-EUR — MEMORY_24H — score mémoire 7.904/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.880/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- G-EUR — ACTIVE_NOW — score mémoire 7.833/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.736/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +75.71% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZAMA-EUR +18.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +13.46% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- C-EUR +12.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +12.02% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- STRK-EUR +11.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +10.71% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PTB-EUR +10.65% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +7.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIL-EUR +7.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
