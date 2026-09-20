# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T20:07:40.960928+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : VET-EUR | action ACHETE_MAINTENANT | opportunité 8.531 | entrée 7.000 | trend 7.900 | rang 7.803
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : MERL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.708 | entrée 5.850 | trend 8.700 | rang 7.598
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ARX-EUR | action LATENT_ACCELERATOR | opportunité 7.742 | entrée 5.200 | trend 8.300 | rang 7.388
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : COW-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.718 | entrée 6.500 | trend 9.000 | rang 8.187
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. COW-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.187
2. CAKE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.182
3. STX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.955

## Accélération indépendante

- NOS-EUR — CONFIRMED_ACCELERATION — score 8.780/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FTT-EUR — CONFIRMED_ACCELERATION — score 8.388/10 — DETECTED_BUT_TOO_LATE
- SAGA-EUR — CONFIRMED_ACCELERATION — score 7.640/10 — DETECTED_BUT_TOO_LATE
- POND-EUR — CONFIRMED_ACCELERATION — score 7.452/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PUMP-EUR — CONFIRMED_ACCELERATION — score 7.311/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- S-EUR — CONFIRMED_ACCELERATION — score 6.732/10 — DETECTED_BUT_TOO_LATE
- ZRO-EUR — CONFIRMED_ACCELERATION — score 6.575/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CELR-EUR — BUILDING_ACCELERATION — score 5.755/10 — DETECTED_BUT_TOO_LATE
- ZIL-EUR — BUILDING_ACCELERATION — score 5.748/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ALLO-EUR — BUILDING_ACCELERATION — score 5.735/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- PUMP-EUR — ACTIVE_NOW — score mémoire 7.311/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ONDO-EUR — ACTIVE_NOW — score mémoire 7.299/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- NES-EUR — MEMORY_24H — score mémoire 8.883/10 — sources ACCELERATION — MEMORY_ONLY
- EDEN-EUR — MEMORY_24H — score mémoire 8.850/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NOS-EUR — ACTIVE_NOW — score mémoire 8.780/10 — sources ACCELERATION, V4 — WATCH_ONLY
- PTB-EUR — MEMORY_24H — score mémoire 8.518/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- C-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FTT-EUR — ACTIVE_NOW — score mémoire 8.388/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- COW-EUR — ACTIVE_NOW — score mémoire 8.187/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 8.182/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +58.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +53.84% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PTB-EUR +27.26% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- S-EUR +24.38% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CELR-EUR +20.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +18.06% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- STRK-EUR +17.25% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LUNA2-EUR +17.12% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AVAX-EUR +16.99% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +16.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
