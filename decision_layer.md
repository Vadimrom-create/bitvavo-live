# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T15:01:23.261659+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : JUP-EUR | action ACHETE_MAINTENANT | opportunité 9.107 | entrée 7.450 | trend 8.150 | rang 8.088
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : CAKE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.907 | entrée 6.700 | trend 7.550 | rang 7.789
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : RED-EUR | action LATENT_ACCELERATOR | opportunité 7.813 | entrée 4.500 | trend 8.650 | rang 7.379
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : WAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.059 | entrée 6.750 | trend 8.150 | rang 7.969
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. JUP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.088
2. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.969
3. ADA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.854

## Accélération indépendante

- POND-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- XYO-EUR — CONFIRMED_ACCELERATION — score 8.937/10 — DETECTED_BUT_TOO_LATE
- PONKE-EUR — CONFIRMED_ACCELERATION — score 6.795/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DGB-EUR — CONFIRMED_ACCELERATION — score 6.621/10 — DETECTED_BUT_TOO_LATE
- ZBCN-EUR — BUILDING_ACCELERATION — score 5.961/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CTC-EUR — BUILDING_ACCELERATION — score 5.423/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — BUILDING_ACCELERATION — score 4.945/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- U-EUR — BUILDING_ACCELERATION — score 4.883/10 — DETECTED_BUT_TOO_LATE
- ADX-EUR — BUILDING_ACCELERATION — score 4.866/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XAI-EUR — BUILDING_ACCELERATION — score 4.846/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- EIGEN-EUR — ACTIVE_NOW — score mémoire 7.786/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- AMP-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- POND-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- FLOCK-EUR — MEMORY_24H — score mémoire 9.446/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — ACTIVE_NOW — score mémoire 8.937/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- 2Z-EUR — MEMORY_24H — score mémoire 8.723/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CNPY-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- REQ-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SYRUP-EUR — MEMORY_24H — score mémoire 8.308/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- NOM-EUR +35.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +25.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +24.85% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- LTC-EUR +19.95% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ONDO-EUR +18.86% — DETECTED_EARLY — couche NONE — action NONE
- ARX-EUR +15.46% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- PEAQ-EUR +14.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PLUME-EUR +12.55% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +12.29% — DETECTED_EARLY — couche NONE — action NONE
- ETC-EUR +9.92% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
