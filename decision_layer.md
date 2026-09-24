# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T03:22:41.771706+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ETC-EUR | action ACHETE_MAINTENANT | opportunité 9.190 | entrée 6.950 | trend 8.400 | rang 7.990
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ZK-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.073 | entrée 6.050 | trend 7.350 | rang 7.564
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : 0G-EUR | action LATENT_ACCELERATOR | opportunité 7.914 | entrée 5.150 | trend 8.650 | rang 7.476
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PLUME-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.457 | entrée 6.750 | trend 8.700 | rang 7.984
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ETC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.990
2. PLUME-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.984
3. VET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.974

## Accélération indépendante

- MOVR-EUR — CONFIRMED_ACCELERATION — score 7.624/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRO-EUR — CONFIRMED_ACCELERATION — score 7.201/10 — DETECTED_BUT_TOO_LATE
- NIL-EUR — CONFIRMED_ACCELERATION — score 7.190/10 — DETECTED_BUT_TOO_LATE
- TRB-EUR — CONFIRMED_ACCELERATION — score 6.786/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RE-EUR — CONFIRMED_ACCELERATION — score 6.715/10 — DETECTED_BUT_TOO_LATE
- DBR-EUR — BUILDING_ACCELERATION — score 6.384/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KSM-EUR — BUILDING_ACCELERATION — score 5.752/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- COMP-EUR — BUILDING_ACCELERATION — score 5.751/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BAT-EUR — BUILDING_ACCELERATION — score 5.670/10 — DETECTED_BUT_TOO_LATE
- UMA-EUR — BUILDING_ACCELERATION — score 5.488/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ETC-EUR — ACTIVE_NOW — score mémoire 7.990/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- IMU-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- TRIA-EUR — MEMORY_24H — score mémoire 9.929/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- IKA-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TRAC-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NOM-EUR — MEMORY_24H — score mémoire 8.393/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZBCN-EUR — MEMORY_24H — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PLUME-EUR — ACTIVE_NOW — score mémoire 7.984/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- NIL-EUR +36.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOM-EUR +30.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +14.19% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +13.95% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DBR-EUR +12.95% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CPOOL-EUR +11.07% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LSK-EUR +9.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +9.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOSO-EUR +8.99% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- RAY-EUR +7.70% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
