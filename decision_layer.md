# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T21:27:22.151049+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : CAKE-EUR | action ACHETE_MAINTENANT | opportunité 8.960 | entrée 7.450 | trend 8.950 | rang 8.334
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ARX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.046 | entrée 5.900 | trend 8.300 | rang 7.593
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : PROVE-EUR | action LATENT_ACCELERATOR | opportunité 7.867 | entrée 5.650 | trend 8.750 | rang 7.672
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : STX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.601 | entrée 6.700 | trend 8.950 | rang 8.065
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. CAKE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.334
2. STX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.065
3. VVV-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.862

## Accélération indépendante

- UP-EUR — CONFIRMED_ACCELERATION — score 8.113/10 — DETECTED_BUT_TOO_LATE
- CFG-EUR — CONFIRMED_ACCELERATION — score 7.076/10 — DETECTED_BUT_TOO_LATE
- LRC-EUR — BUILDING_ACCELERATION — score 6.290/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRO-EUR — BUILDING_ACCELERATION — score 6.010/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FLOCK-EUR — BUILDING_ACCELERATION — score 5.754/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BRETT-EUR — BUILDING_ACCELERATION — score 5.032/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GALA-EUR — BUILDING_ACCELERATION — score 4.888/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- NES-EUR — MEMORY_24H — score mémoire 8.883/10 — sources ACCELERATION — MEMORY_ONLY
- PTB-EUR — MEMORY_24H — score mémoire 8.518/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NOS-EUR — MEMORY_24H — score mémoire 8.445/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.388/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 8.334/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 8.150/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- UP-EUR — ACTIVE_NOW — score mémoire 8.113/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- STX-EUR — ACTIVE_NOW — score mémoire 8.065/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- VVV-EUR — ACTIVE_NOW — score mémoire 7.862/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- MERL-EUR — ACTIVE_NOW — score mémoire 7.850/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +50.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PTB-EUR +32.92% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FTT-EUR +32.26% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NIL-EUR +23.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CELR-EUR +22.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +19.47% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- S-EUR +19.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +16.98% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +16.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LUNA2-EUR +15.87% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
