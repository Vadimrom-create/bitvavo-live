# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T22:20:45.295687+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : KAS-EUR | action ACHETE_MAINTENANT | opportunité 8.303 | entrée 7.000 | trend 8.650 | rang 7.906
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SUPER-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.672 | entrée 6.100 | trend 8.650 | rang 8.029
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ZIL-EUR | action LATENT_ACCELERATOR | opportunité 7.581 | entrée 5.400 | trend 8.600 | rang 7.431
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : COW-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.484 | entrée 6.650 | trend 9.000 | rang 8.058
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. COW-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.058
2. SUPER-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 8.029
3. KAS-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.906

## Accélération indépendante

- METIS-EUR — CONFIRMED_ACCELERATION — score 6.933/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KMNO-EUR — BUILDING_ACCELERATION — score 6.406/10 — DETECTED_BUT_TOO_LATE
- ENS-EUR — BUILDING_ACCELERATION — score 6.094/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LIGHTER-EUR — BUILDING_ACCELERATION — score 6.007/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CHIP-EUR — BUILDING_ACCELERATION — score 5.624/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PONKE-EUR — BUILDING_ACCELERATION — score 5.549/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DEEP-EUR — BUILDING_ACCELERATION — score 5.445/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARKM-EUR — BUILDING_ACCELERATION — score 5.291/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EIGEN-EUR — BUILDING_ACCELERATION — score 5.244/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GIGA-EUR — BUILDING_ACCELERATION — score 5.007/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ICX-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.883/10 — sources ACCELERATION — MEMORY_ONLY
- NOS-EUR — MEMORY_24H — score mémoire 8.445/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- UP-EUR — MEMORY_24H — score mémoire 8.113/10 — sources ACCELERATION — MEMORY_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 8.058/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- SUPER-EUR — ACTIVE_NOW — score mémoire 8.029/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- S-EUR — MEMORY_24H — score mémoire 8.013/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.906/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.900/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.847/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +42.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PTB-EUR +33.07% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FTT-EUR +28.70% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NIL-EUR +24.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +21.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +21.17% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NEAR-EUR +19.32% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +18.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +17.71% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LUNA2-EUR +16.28% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
