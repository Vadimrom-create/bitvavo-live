# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T05:03:19.954807+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : VET-EUR | action ACHETE_MAINTENANT | opportunité 9.148 | entrée 7.250 | trend 7.900 | rang 7.960
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : G-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.894 | entrée 5.950 | trend 7.400 | rang 7.535
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : KMNO-EUR | action LATENT_ACCELERATOR | opportunité 7.646 | entrée 4.500 | trend 8.600 | rang 7.333
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : BAT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.734 | entrée 6.450 | trend 8.650 | rang 8.035
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. BAT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.035
2. VET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.960
3. RENDER-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.920

## Accélération indépendante

- C98-EUR — CONFIRMED_ACCELERATION — score 8.347/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RAY-EUR — CONFIRMED_ACCELERATION — score 7.486/10 — DETECTED_BUT_TOO_LATE
- BOME-EUR — CONFIRMED_ACCELERATION — score 7.423/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PEOPLE-EUR — CONFIRMED_ACCELERATION — score 6.631/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MOG-EUR — BUILDING_ACCELERATION — score 6.042/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MET-EUR — BUILDING_ACCELERATION — score 5.835/10 — DETECTED_BUT_TOO_LATE
- AIOZ-EUR — BUILDING_ACCELERATION — score 5.815/10 — DETECTED_BUT_TOO_LATE
- TWT-EUR — BUILDING_ACCELERATION — score 5.754/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ALGO-EUR — BUILDING_ACCELERATION — score 5.579/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BIO-EUR — BUILDING_ACCELERATION — score 5.515/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- TRIA-EUR — MEMORY_24H — score mémoire 9.929/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.979/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TRAC-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- C98-EUR — ACTIVE_NOW — score mémoire 8.347/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZBCN-EUR — MEMORY_24H — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BAT-EUR — ACTIVE_NOW — score mémoire 8.035/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.960/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WIN-EUR — MEMORY_DECAY_24_72H — score mémoire 7.925/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 7.920/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- NIL-EUR +39.22% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOM-EUR +32.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +16.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DBR-EUR +15.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IMU-EUR +14.79% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- RAY-EUR +13.84% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CVC-EUR +11.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +11.34% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOSO-EUR +9.06% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- CPOOL-EUR +8.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
