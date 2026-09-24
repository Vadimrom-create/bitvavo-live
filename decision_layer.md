# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T00:27:07.444402+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 8.477 | entrée 7.150 | trend 9.000 | rang 8.146
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ZK-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.017 | entrée 6.250 | trend 7.350 | rang 7.107
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BEAM-EUR | action LATENT_ACCELERATOR | opportunité 7.751 | entrée 5.300 | trend 8.750 | rang 7.542
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SENT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.381 | entrée 6.950 | trend 8.600 | rang 7.785
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LTC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.146
2. SENT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.785
3. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.635

## Accélération indépendante

- DBR-EUR — CONFIRMED_ACCELERATION — score 9.184/10 — DETECTED_BUT_TOO_LATE
- IKA-EUR — CONFIRMED_ACCELERATION — score 9.062/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KERNEL-EUR — CONFIRMED_ACCELERATION — score 6.932/10 — DETECTED_BUT_TOO_LATE
- NOM-EUR — CONFIRMED_ACCELERATION — score 6.883/10 — DETECTED_BUT_TOO_LATE
- SPX-EUR — BUILDING_ACCELERATION — score 6.441/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CTC-EUR — BUILDING_ACCELERATION — score 5.846/10 — DETECTED_BUT_TOO_LATE
- TRAC-EUR — BUILDING_ACCELERATION — score 5.237/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BIRB-EUR — BUILDING_ACCELERATION — score 5.148/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- UP-EUR — BUILDING_ACCELERATION — score 5.001/10 — DETECTED_BUT_TOO_LATE
- ESP-EUR — BUILDING_ACCELERATION — score 4.806/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- AMP-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DBR-EUR — ACTIVE_NOW — score mémoire 9.184/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- IKA-EUR — ACTIVE_NOW — score mémoire 9.062/10 — sources ACCELERATION, V4 — WATCH_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 8.883/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 8.146/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.129/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZBCN-EUR — MEMORY_24H — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 7.785/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- NIL-EUR +55.48% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DBR-EUR +25.68% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- NOM-EUR +18.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +17.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- UP-EUR +16.35% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- CPOOL-EUR +11.61% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CAP-EUR +10.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +9.69% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LSK-EUR +9.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RAY-EUR +9.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
