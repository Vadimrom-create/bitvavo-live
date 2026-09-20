# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T21:10:38.707382+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AIOZ-EUR | action ACHETE_MAINTENANT | opportunité 8.180 | entrée 7.300 | trend 8.550 | rang 7.943
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : STX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.575 | entrée 6.700 | trend 8.950 | rang 7.965
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : PROVE-EUR | action LATENT_ACCELERATOR | opportunité 7.528 | entrée 5.550 | trend 8.750 | rang 7.508
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MERL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.361 | entrée 6.300 | trend 8.700 | rang 7.967
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.967
2. STX-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.965
3. AIOZ-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.943

## Accélération indépendante

- FLOCK-EUR — CONFIRMED_ACCELERATION — score 8.158/10 — DETECTED_BUT_TOO_LATE
- UP-EUR — CONFIRMED_ACCELERATION — score 7.319/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MLN-EUR — BUILDING_ACCELERATION — score 6.027/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRC-EUR — BUILDING_ACCELERATION — score 5.439/10 — DETECTED_BUT_TOO_LATE
- HEI-EUR — BUILDING_ACCELERATION — score 5.327/10 — DETECTED_BUT_TOO_LATE
- CSPR-EUR — BUILDING_ACCELERATION — score 4.819/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- NES-EUR — MEMORY_24H — score mémoire 8.883/10 — sources ACCELERATION — MEMORY_ONLY
- PTB-EUR — MEMORY_24H — score mémoire 8.518/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NOS-EUR — MEMORY_24H — score mémoire 8.445/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.388/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FLOCK-EUR — ACTIVE_NOW — score mémoire 8.158/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- NIL-EUR — MEMORY_24H — score mémoire 8.150/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MERL-EUR — ACTIVE_NOW — score mémoire 7.967/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 7.965/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.943/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.900/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +50.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +34.48% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PTB-EUR +30.07% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CELR-EUR +23.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +20.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +18.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +16.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +16.61% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EPIC-EUR +16.06% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LUNA2-EUR +15.89% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
