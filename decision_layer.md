# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T04:34:04.585681+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : VET-EUR | action ACHETE_MAINTENANT | opportunité 9.167 | entrée 7.600 | trend 7.900 | rang 8.091
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : VVV-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.920 | entrée 6.700 | trend 7.500 | rang 7.294
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : 0G-EUR | action LATENT_ACCELERATOR | opportunité 7.995 | entrée 5.400 | trend 8.650 | rang 7.518
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : BAT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.837 | entrée 6.450 | trend 8.650 | rang 8.066
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.091
2. BAT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.066
3. OP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.989

## Accélération indépendante

- ZRC-EUR — CONFIRMED_ACCELERATION — score 8.979/10 — DETECTED_BUT_TOO_LATE
- DYM-EUR — CONFIRMED_ACCELERATION — score 7.332/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PUNDIX-EUR — BUILDING_ACCELERATION — score 6.072/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARK-EUR — BUILDING_ACCELERATION — score 5.292/10 — DETECTED_BUT_TOO_LATE
- CVC-EUR — BUILDING_ACCELERATION — score 5.141/10 — DETECTED_BUT_TOO_LATE
- GROVE-EUR — BUILDING_ACCELERATION — score 5.104/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BONK-EUR — BUILDING_ACCELERATION — score 5.066/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IMU-EUR — BUILDING_ACCELERATION — score 4.898/10 — DETECTED_BUT_TOO_LATE
- STO-EUR — BUILDING_ACCELERATION — score 4.809/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- TRIA-EUR — MEMORY_24H — score mémoire 9.929/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — ACTIVE_NOW — score mémoire 8.979/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- TRAC-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.091/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- BAT-EUR — ACTIVE_NOW — score mémoire 8.066/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZBCN-EUR — MEMORY_24H — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_DECAY_24_72H — score mémoire 8.007/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- OP-EUR — ACTIVE_NOW — score mémoire 7.989/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 7.956/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- NIL-EUR +36.70% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOM-EUR +34.81% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CVC-EUR +16.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +15.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DBR-EUR +13.99% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SAGA-EUR +13.61% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IMU-EUR +12.81% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOSO-EUR +9.25% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- CPOOL-EUR +8.88% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +7.92% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
