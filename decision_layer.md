# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T12:55:02.556149+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ETC-EUR | action ACHETE_MAINTENANT | opportunité 8.085 | entrée 7.550 | trend 8.650 | rang 7.881
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : MEME-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.224 | entrée 6.150 | trend 8.700 | rang 7.853
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ROSE-EUR | action LATENT_ACCELERATOR | opportunité 7.891 | entrée 4.950 | trend 8.600 | rang 7.496
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MERL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.263 | entrée 6.900 | trend 8.850 | rang 7.992
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.992
2. ICP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.942
3. LTC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.895

## Accélération indépendante

- ACE-EUR — CONFIRMED_ACCELERATION — score 6.742/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IMU-EUR — BUILDING_ACCELERATION — score 5.903/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SYN-EUR — BUILDING_ACCELERATION — score 5.868/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AERO-EUR — BUILDING_ACCELERATION — score 5.413/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DOS-EUR — BUILDING_ACCELERATION — score 5.331/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SYRUP-EUR — BUILDING_ACCELERATION — score 5.123/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FTT-EUR — BUILDING_ACCELERATION — score 5.122/10 — DETECTED_BUT_TOO_LATE
- U-EUR — BUILDING_ACCELERATION — score 5.015/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- TRIA-EUR — MEMORY_24H — score mémoire 9.219/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 9.216/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SAGA-EUR — MEMORY_24H — score mémoire 9.208/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LINK-EUR — MEMORY_24H — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MERL-EUR — ACTIVE_NOW — score mémoire 7.992/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PORTAL-EUR — MEMORY_24H — score mémoire 7.969/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.942/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.901/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 7.895/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CPOOL-EUR +43.76% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ALLO-EUR +32.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MET-EUR +30.28% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SAGA-EUR +29.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CHR-EUR +23.60% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SENT-EUR +23.11% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +20.79% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +19.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +19.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BCH-EUR +18.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
