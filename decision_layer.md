# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T05:56:14.909917+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ENA-EUR | action ACHETE_MAINTENANT | opportunité 9.344 | entrée 7.150 | trend 8.650 | rang 8.472
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : BLUR-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.434 | entrée 6.000 | trend 8.750 | rang 7.930
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : IMX-EUR | action LATENT_ACCELERATOR | opportunité 8.261 | entrée 5.650 | trend 8.750 | rang 7.868
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SPK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.292 | entrée 5.850 | trend 8.650 | rang 8.307
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ENA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.472
2. SPK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.307
3. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.305

## Accélération indépendante

- AGI-EUR — CONFIRMED_ACCELERATION — score 8.644/10 — DETECTED_BUT_TOO_LATE
- NEAR-EUR — CONFIRMED_ACCELERATION — score 8.619/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POND-EUR — CONFIRMED_ACCELERATION — score 7.971/10 — DETECTED_BUT_TOO_LATE
- USELESS-EUR — CONFIRMED_ACCELERATION — score 7.765/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PROM-EUR — CONFIRMED_ACCELERATION — score 7.482/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NIL-EUR — CONFIRMED_ACCELERATION — score 7.284/10 — DETECTED_BUT_TOO_LATE
- ARB-EUR — BUILDING_ACCELERATION — score 5.930/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RENDER-EUR — BUILDING_ACCELERATION — score 5.725/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DGB-EUR — BUILDING_ACCELERATION — score 5.542/10 — DETECTED_BUT_TOO_LATE
- LQTY-EUR — BUILDING_ACCELERATION — score 5.120/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- NEAR-EUR — ACTIVE_NOW — score mémoire 8.619/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- INX-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SAGA-EUR — MEMORY_24H — score mémoire 9.476/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- QNT-EUR — MEMORY_24H — score mémoire 9.139/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION — MEMORY_ONLY
- RARE-EUR — MEMORY_24H — score mémoire 8.765/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AGI-EUR — ACTIVE_NOW — score mémoire 8.644/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- VELO-EUR — MEMORY_24H — score mémoire 8.605/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 8.587/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SOON-EUR — MEMORY_24H — score mémoire 8.551/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- QNT-EUR +73.75% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +43.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +40.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +39.28% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +26.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GLMR-EUR +25.07% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRC-EUR +23.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RUNE-EUR +21.48% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- W-EUR +17.02% — DETECTED_EARLY — couche NONE — action NONE
- PYTH-EUR +16.04% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
