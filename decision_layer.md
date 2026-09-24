# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T07:21:59.818535+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 8.273 | entrée 7.750 | trend 8.550 | rang 7.906
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : BAT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.587 | entrée 6.450 | trend 8.650 | rang 8.007
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. BAT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.007
2. LTC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.906
3. ETC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.759

## Accélération indépendante

- FLOCK-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- AVA-EUR — BUILDING_ACCELERATION — score 5.848/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRIA-EUR — BUILDING_ACCELERATION — score 5.435/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZEUS-EUR — BUILDING_ACCELERATION — score 5.337/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- T-EUR — BUILDING_ACCELERATION — score 5.252/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LSK-EUR — BUILDING_ACCELERATION — score 4.907/10 — DETECTED_BUT_TOO_LATE
- HOME-EUR — BUILDING_ACCELERATION — score 4.861/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CELR-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 8.917/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VTHO-EUR — MEMORY_24H — score mémoire 8.660/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FLOCK-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- TRAC-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- C98-EUR — MEMORY_24H — score mémoire 8.347/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 8.307/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZBCN-EUR — MEMORY_24H — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BAT-EUR — ACTIVE_NOW — score mémoire 8.007/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- NOM-EUR +52.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +28.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +26.51% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RAY-EUR +18.49% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IMU-EUR +13.08% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- DBR-EUR +10.79% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOSO-EUR +10.65% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- CELR-EUR +10.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +7.42% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CVC-EUR +6.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
