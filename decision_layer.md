# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T10:56:56.456752+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ETC-EUR | action ACHETE_MAINTENANT | opportunité 8.564 | entrée 6.850 | trend 8.700 | rang 8.099
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : INIT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.231 | entrée 5.950 | trend 8.800 | rang 7.734
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BEAM-EUR | action LATENT_ACCELERATOR | opportunité 8.892 | entrée 4.900 | trend 8.100 | rang 7.361
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : DRIFT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.391 | entrée 6.250 | trend 8.650 | rang 7.954
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ETC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.099
2. DRIFT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.954
3. LTC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.952

## Accélération indépendante

- BEAM-EUR — CONFIRMED_ACCELERATION — score 8.248/10 — DETECTED_BUT_TOO_LATE
- ZRO-EUR — CONFIRMED_ACCELERATION — score 7.198/10 — DETECTED_BUT_TOO_LATE
- EDEN-EUR — CONFIRMED_ACCELERATION — score 7.056/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GOAT-EUR — BUILDING_ACCELERATION — score 6.141/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — BUILDING_ACCELERATION — score 5.818/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CYBER-EUR — BUILDING_ACCELERATION — score 5.244/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BILL-EUR — BUILDING_ACCELERATION — score 5.043/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOSO-EUR — BUILDING_ACCELERATION — score 4.798/10 — DETECTED_BUT_TOO_LATE
- ENA-EUR — BUILDING_ACCELERATION — score 4.767/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ETC-EUR — ACTIVE_NOW — score mémoire 8.099/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ZRC-EUR — MEMORY_24H — score mémoire 9.712/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEAQ-EUR — MEMORY_24H — score mémoire 9.627/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PROM-EUR — MEMORY_24H — score mémoire 9.255/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CAT-EUR — MEMORY_24H — score mémoire 9.114/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 8.917/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CNPY-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FLOCK-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 8.485/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- NOM-EUR +37.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +34.80% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- IMU-EUR +22.81% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- LSK-EUR +19.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARX-EUR +14.28% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CNPY-EUR +10.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOSO-EUR +10.92% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- CVC-EUR +9.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +7.51% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LTC-EUR +6.81% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
