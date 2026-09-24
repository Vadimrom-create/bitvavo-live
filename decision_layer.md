# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T08:15:24.883378+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ETC-EUR | action ACHETE_MAINTENANT | opportunité 9.314 | entrée 7.400 | trend 8.400 | rang 8.140
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SKY-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.501 | entrée 6.100 | trend 7.350 | rang 7.439
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : LIGHTER-EUR | action LATENT_ACCELERATOR | opportunité 8.499 | entrée 5.500 | trend 8.000 | rang 7.418
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : COMP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.386 | entrée 7.050 | trend 8.500 | rang 7.961
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ETC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.140
2. TAO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.063
3. COMP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.961

## Accélération indépendante

- NIL-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- PEAQ-EUR — CONFIRMED_ACCELERATION — score 9.627/10 — DETECTED_BUT_TOO_LATE
- PROM-EUR — CONFIRMED_ACCELERATION — score 9.255/10 — DETECTED_BUT_TOO_LATE
- AGI-EUR — CONFIRMED_ACCELERATION — score 7.749/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ENS-EUR — BUILDING_ACCELERATION — score 5.890/10 — DETECTED_BUT_TOO_LATE
- CNPY-EUR — BUILDING_ACCELERATION — score 5.687/10 — DETECTED_BUT_TOO_LATE
- BILL-EUR — BUILDING_ACCELERATION — score 5.316/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ETC-EUR — BUILDING_ACCELERATION — score 5.226/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CROSS-EUR — BUILDING_ACCELERATION — score 4.914/10 — DETECTED_BUT_TOO_LATE
- PLUME-EUR — BUILDING_ACCELERATION — score 4.763/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ETC-EUR — ACTIVE_NOW — score mémoire 8.140/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- NIL-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PEAQ-EUR — ACTIVE_NOW — score mémoire 9.627/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PROM-EUR — ACTIVE_NOW — score mémoire 9.255/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CELR-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 8.917/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VTHO-EUR — MEMORY_24H — score mémoire 8.660/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FLOCK-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- C98-EUR — MEMORY_24H — score mémoire 8.347/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- NOM-EUR +51.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +41.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +39.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RAY-EUR +17.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IMU-EUR +13.00% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CELR-EUR +10.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOSO-EUR +9.91% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- LTC-EUR +8.99% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CNPY-EUR +8.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DBR-EUR +7.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
