# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T05:40:26.549586+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : FET-EUR | action ACHETE_MAINTENANT | opportunité 9.214 | entrée 7.350 | trend 7.900 | rang 8.058
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : CYBER-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.388 | entrée 6.700 | trend 7.350 | rang 7.350
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ARPA-EUR | action LATENT_ACCELERATOR | opportunité 8.511 | entrée 5.200 | trend 8.700 | rang 7.666
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : DRIFT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.212 | entrée 7.000 | trend 8.300 | rang 8.245
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. DRIFT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.245
2. FET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.058
3. BAT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.052

## Accélération indépendante

- NOM-EUR — CONFIRMED_ACCELERATION — score 8.377/10 — DETECTED_BUT_TOO_LATE
- RAY-EUR — BUILDING_ACCELERATION — score 5.753/10 — DETECTED_BUT_TOO_LATE
- ARKM-EUR — BUILDING_ACCELERATION — score 5.235/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- 2Z-EUR — BUILDING_ACCELERATION — score 4.798/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- LSK-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TRIA-EUR — MEMORY_24H — score mémoire 9.929/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BOME-EUR — MEMORY_24H — score mémoire 8.692/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TRAC-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NOM-EUR — ACTIVE_NOW — score mémoire 8.377/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- C98-EUR — MEMORY_24H — score mémoire 8.347/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 8.307/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DRIFT-EUR — ACTIVE_NOW — score mémoire 8.245/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- EGLD-EUR — MEMORY_24H — score mémoire 8.216/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- NOM-EUR +40.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +36.41% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LSK-EUR +19.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RAY-EUR +17.46% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DBR-EUR +12.10% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IMU-EUR +11.47% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRO-EUR +10.99% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOSO-EUR +8.79% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- CELR-EUR +8.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ACU-EUR +8.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
