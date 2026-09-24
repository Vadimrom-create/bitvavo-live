# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T05:23:17.404004+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAO-EUR | action ACHETE_MAINTENANT | opportunité 9.098 | entrée 8.050 | trend 7.600 | rang 8.000
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ARK-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.731 | entrée 5.900 | trend 8.200 | rang 6.908
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ARPA-EUR | action LATENT_ACCELERATOR | opportunité 8.879 | entrée 5.700 | trend 8.700 | rang 7.917
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : INJ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.152 | entrée 7.600 | trend 8.600 | rang 8.190
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.190
2. TAO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.000
3. PEPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.960

## Accélération indépendante

- LSK-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- BOME-EUR — CONFIRMED_ACCELERATION — score 8.692/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — CONFIRMED_ACCELERATION — score 8.307/10 — DETECTED_BUT_TOO_LATE
- EGLD-EUR — CONFIRMED_ACCELERATION — score 8.216/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SAFE-EUR — CONFIRMED_ACCELERATION — score 7.178/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VTHO-EUR — CONFIRMED_ACCELERATION — score 7.171/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRB-EUR — CONFIRMED_ACCELERATION — score 7.052/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRC-EUR — CONFIRMED_ACCELERATION — score 6.677/10 — DETECTED_BUT_TOO_LATE
- CTSI-EUR — CONFIRMED_ACCELERATION — score 6.506/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ACH-EUR — BUILDING_ACCELERATION — score 6.456/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- LSK-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- TRIA-EUR — MEMORY_24H — score mémoire 9.929/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BOME-EUR — ACTIVE_NOW — score mémoire 8.692/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- TRAC-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- C98-EUR — MEMORY_24H — score mémoire 8.347/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — ACTIVE_NOW — score mémoire 8.307/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- EGLD-EUR — ACTIVE_NOW — score mémoire 8.216/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 8.190/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ZBCN-EUR — MEMORY_24H — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- NIL-EUR +36.19% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOM-EUR +33.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +25.02% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RAY-EUR +15.80% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DBR-EUR +13.80% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +10.44% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CVC-EUR +10.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IMU-EUR +9.47% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOSO-EUR +9.06% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- ACU-EUR +8.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
