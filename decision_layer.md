# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T04:39:49.132362+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HBAR-EUR | action ACHETE_MAINTENANT | opportunité 8.964 | entrée 7.650 | trend 8.100 | rang 7.984
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : 0G-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.192 | entrée 5.900 | trend 8.400 | rang 7.954
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : PENDLE-EUR | action LATENT_ACCELERATOR | opportunité 7.846 | entrée 5.550 | trend 8.950 | rang 7.734
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : WAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.944 | entrée 6.000 | trend 9.200 | rang 8.322
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.322
2. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.050
3. HBAR-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.984

## Accélération indépendante

- DYDX-EUR — CONFIRMED_ACCELERATION — score 8.517/10 — DETECTED_BUT_TOO_LATE
- PROVE-EUR — CONFIRMED_ACCELERATION — score 7.390/10 — DETECTED_BUT_TOO_LATE
- CAP-EUR — CONFIRMED_ACCELERATION — score 6.524/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GLM-EUR — BUILDING_ACCELERATION — score 6.365/10 — DETECTED_BUT_TOO_LATE
- ZRX-EUR — BUILDING_ACCELERATION — score 5.534/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LAYER-EUR — BUILDING_ACCELERATION — score 5.518/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOLV-EUR — BUILDING_ACCELERATION — score 5.479/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CNPY-EUR — BUILDING_ACCELERATION — score 4.991/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MLN-EUR — BUILDING_ACCELERATION — score 4.907/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZKJ-EUR — BUILDING_ACCELERATION — score 4.792/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- FTT-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.883/10 — sources ACCELERATION — MEMORY_ONLY
- FORM-EUR — MEMORY_24H — score mémoire 8.879/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BOME-EUR — MEMORY_24H — score mémoire 8.655/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SAFE-EUR — MEMORY_24H — score mémoire 8.565/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DYDX-EUR — ACTIVE_NOW — score mémoire 8.517/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LSK-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- USELESS-EUR — MEMORY_24H — score mémoire 8.481/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.376/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- PTB-EUR +87.00% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZETA-EUR +64.48% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- FTT-EUR +38.95% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +29.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +27.28% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +24.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VVV-EUR +22.26% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +19.34% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AVAX-EUR +18.78% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- S-EUR +18.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
