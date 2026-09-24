# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T00:49:39.532420+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 8.673 | entrée 7.350 | trend 9.000 | rang 8.252
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ZK-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.966 | entrée 6.250 | trend 7.350 | rang 7.144
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BEAM-EUR | action LATENT_ACCELERATOR | opportunité 7.576 | entrée 4.850 | trend 8.750 | rang 7.407
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SENT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.361 | entrée 7.400 | trend 8.600 | rang 8.160
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LTC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.252
2. SENT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.160
3. SEI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.995

## Accélération indépendante

- NOM-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- ZIG-EUR — CONFIRMED_ACCELERATION — score 8.591/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FLUX-EUR — BUILDING_ACCELERATION — score 6.345/10 — DETECTED_BUT_TOO_LATE
- DEEP-EUR — BUILDING_ACCELERATION — score 5.845/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CAKE-EUR — BUILDING_ACCELERATION — score 5.678/10 — DETECTED_BUT_TOO_LATE
- SENT-EUR — BUILDING_ACCELERATION — score 5.658/10 — DETECTED_BUT_TOO_LATE
- ZBT-EUR — BUILDING_ACCELERATION — score 4.796/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- AMP-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NOM-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- IKA-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 8.883/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZIG-EUR — ACTIVE_NOW — score mémoire 8.591/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 8.252/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 8.160/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — MEMORY_24H — score mémoire 8.129/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- NIL-EUR +49.85% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOM-EUR +42.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DBR-EUR +23.54% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- SAGA-EUR +18.30% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- UP-EUR +14.19% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- ZRO-EUR +11.53% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CAP-EUR +10.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +9.88% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RAY-EUR +8.71% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CPOOL-EUR +7.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
