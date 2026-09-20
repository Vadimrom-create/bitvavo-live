# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T21:43:19.090247+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : CAKE-EUR | action ACHETE_MAINTENANT | opportunité 9.121 | entrée 7.250 | trend 8.950 | rang 8.340
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ZRO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.410 | entrée 6.000 | trend 8.500 | rang 7.540
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : PROVE-EUR | action LATENT_ACCELERATOR | opportunité 7.913 | entrée 5.650 | trend 8.750 | rang 7.658
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : STX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.524 | entrée 6.700 | trend 8.950 | rang 8.045
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. CAKE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.340
2. STX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.045
3. AIOZ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.956

## Accélération indépendante

- ICX-EUR — CONFIRMED_ACCELERATION — score 9.062/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FLOCK-EUR — CONFIRMED_ACCELERATION — score 7.500/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DYM-EUR — CONFIRMED_ACCELERATION — score 6.625/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PTB-EUR — BUILDING_ACCELERATION — score 5.971/10 — DETECTED_BUT_TOO_LATE
- LRC-EUR — BUILDING_ACCELERATION — score 5.846/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRO-EUR — BUILDING_ACCELERATION — score 5.605/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SUSHI-EUR — BUILDING_ACCELERATION — score 5.558/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FTT-EUR — BUILDING_ACCELERATION — score 5.457/10 — DETECTED_BUT_TOO_LATE
- NIL-EUR — BUILDING_ACCELERATION — score 5.253/10 — DETECTED_BUT_TOO_LATE
- THQ-EUR — BUILDING_ACCELERATION — score 5.080/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ICX-EUR — ACTIVE_NOW — score mémoire 9.062/10 — sources ACCELERATION, V4 — WATCH_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.883/10 — sources ACCELERATION — MEMORY_ONLY
- NOS-EUR — MEMORY_24H — score mémoire 8.445/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 8.340/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- UP-EUR — MEMORY_24H — score mémoire 8.113/10 — sources ACCELERATION — MEMORY_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 8.045/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.956/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 7.931/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.887/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.862/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +53.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PTB-EUR +34.02% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FTT-EUR +30.33% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NIL-EUR +27.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +21.23% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- S-EUR +19.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +17.26% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AVAX-EUR +17.18% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +17.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CELR-EUR +16.88% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
