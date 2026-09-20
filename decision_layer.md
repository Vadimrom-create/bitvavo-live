# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T20:40:52.506587+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : STX-EUR | action ACHETE_MAINTENANT | opportunité 8.776 | entrée 6.800 | trend 8.950 | rang 8.228
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ZIL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.234 | entrée 6.000 | trend 8.750 | rang 7.827
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : PROVE-EUR | action LATENT_ACCELERATOR | opportunité 7.602 | entrée 5.550 | trend 8.750 | rang 7.546
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : COW-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.687 | entrée 6.150 | trend 9.000 | rang 8.155
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. STX-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.228
2. COW-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.155
3. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.080

## Accélération indépendante

- NIL-EUR — CONFIRMED_ACCELERATION — score 8.150/10 — DETECTED_BUT_TOO_LATE
- GOAT-EUR — CONFIRMED_ACCELERATION — score 7.678/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HMSTR-EUR — CONFIRMED_ACCELERATION — score 7.041/10 — DETECTED_BUT_TOO_LATE
- HFT-EUR — BUILDING_ACCELERATION — score 5.945/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POND-EUR — BUILDING_ACCELERATION — score 5.571/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- O-EUR — BUILDING_ACCELERATION — score 5.553/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SUPER-EUR — BUILDING_ACCELERATION — score 5.540/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BICO-EUR — BUILDING_ACCELERATION — score 5.477/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DOGS-EUR — BUILDING_ACCELERATION — score 5.236/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NEAR-EUR — BUILDING_ACCELERATION — score 5.086/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- NES-EUR — MEMORY_24H — score mémoire 8.883/10 — sources ACCELERATION — MEMORY_ONLY
- PTB-EUR — MEMORY_24H — score mémoire 8.518/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NOS-EUR — MEMORY_24H — score mémoire 8.445/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.388/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 8.228/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 8.155/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- NIL-EUR — ACTIVE_NOW — score mémoire 8.150/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- MERL-EUR — ACTIVE_NOW — score mémoire 8.080/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.983/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.868/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +49.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +41.38% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PTB-EUR +29.02% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- S-EUR +25.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +24.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +18.48% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +17.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRK-EUR +17.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +16.53% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CELR-EUR +16.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
