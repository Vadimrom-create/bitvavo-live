# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T13:31:01.048568+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : KMNO-EUR | action ACHETE_MAINTENANT | opportunité 9.302 | entrée 7.500 | trend 8.550 | rang 8.440
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : APT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.375 | entrée 6.550 | trend 7.550 | rang 7.355
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : PLUME-EUR | action LATENT_ACCELERATOR | opportunité 7.841 | entrée 4.500 | trend 8.650 | rang 7.381
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LTC-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.600 | entrée 6.750 | trend 9.200 | rang 7.883
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. KMNO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.440
2. ETC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.027
3. VET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.026

## Accélération indépendante

- ICX-EUR — CONFIRMED_ACCELERATION — score 9.456/10 — DETECTED_BUT_TOO_LATE
- LUNA2-EUR — CONFIRMED_ACCELERATION — score 8.989/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- REZ-EUR — CONFIRMED_ACCELERATION — score 8.510/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SYRUP-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MORPHO-EUR — CONFIRMED_ACCELERATION — score 8.175/10 — DETECTED_BUT_TOO_LATE
- CPOOL-EUR — CONFIRMED_ACCELERATION — score 7.347/10 — DETECTED_BUT_TOO_LATE
- PENGU-EUR — CONFIRMED_ACCELERATION — score 7.230/10 — DETECTED_BUT_TOO_LATE
- THE-EUR — CONFIRMED_ACCELERATION — score 7.073/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DGB-EUR — CONFIRMED_ACCELERATION — score 7.018/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FORM-EUR — CONFIRMED_ACCELERATION — score 6.900/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ICP-EUR — ACTIVE_NOW — score mémoire 7.328/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ENA-EUR — ACTIVE_NOW — score mémoire 6.535/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- AMP-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — ACTIVE_NOW — score mémoire 9.456/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- FLOCK-EUR — MEMORY_24H — score mémoire 9.446/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LUNA2-EUR — ACTIVE_NOW — score mémoire 8.989/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 8.917/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- REZ-EUR — ACTIVE_NOW — score mémoire 8.510/10 — sources ACCELERATION, V4 — WATCH_ONLY
- CNPY-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- NOM-EUR +37.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +27.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +26.77% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARX-EUR +15.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IMU-EUR +13.39% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- LTC-EUR +12.88% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ONDO-EUR +10.95% — DETECTED_EARLY — couche NONE — action NONE
- PEAQ-EUR +10.58% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MORPHO-EUR +10.47% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- INIT-EUR +8.43% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
