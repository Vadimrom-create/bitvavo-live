# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T01:21:59.828422+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : CC-EUR | action ACHETE_MAINTENANT | opportunité 8.957 | entrée 7.600 | trend 8.650 | rang 8.301
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : EIGEN-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.189 | entrée 5.800 | trend 9.200 | rang 8.015
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : IMX-EUR | action LATENT_ACCELERATOR | opportunité 8.450 | entrée 5.650 | trend 9.000 | rang 8.011
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : FIL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.422 | entrée 7.350 | trend 8.950 | rang 8.155
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. CC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.301
2. RAY-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.295
3. FIL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.155

## Accélération indépendante

- AGI-EUR — CONFIRMED_ACCELERATION — score 8.923/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DOGS-EUR — CONFIRMED_ACCELERATION — score 8.220/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DATAIP-EUR — CONFIRMED_ACCELERATION — score 7.627/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRIA-EUR — BUILDING_ACCELERATION — score 6.024/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NOT-EUR — BUILDING_ACCELERATION — score 6.020/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRC-EUR — BUILDING_ACCELERATION — score 5.856/10 — DETECTED_BUT_TOO_LATE
- SOON-EUR — BUILDING_ACCELERATION — score 5.526/10 — DETECTED_BUT_TOO_LATE
- QNT-EUR — BUILDING_ACCELERATION — score 5.445/10 — DETECTED_BUT_TOO_LATE
- GRAM-EUR — BUILDING_ACCELERATION — score 5.398/10 — DETECTED_BUT_TOO_LATE
- DYDX-EUR — BUILDING_ACCELERATION — score 5.397/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PONKE-EUR — MEMORY_DECAY_24_72H — score mémoire 9.122/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AGI-EUR — ACTIVE_NOW — score mémoire 8.923/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RARE-EUR — MEMORY_24H — score mémoire 8.845/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ONT-EUR — MEMORY_DECAY_24_72H — score mémoire 8.625/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- VELO-EUR — MEMORY_24H — score mémoire 8.605/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AMP-EUR — MEMORY_24H — score mémoire 8.528/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CC-EUR — ACTIVE_NOW — score mémoire 8.301/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RAY-EUR — ACTIVE_NOW — score mémoire 8.295/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- DOGS-EUR — ACTIVE_NOW — score mémoire 8.220/10 — sources ACCELERATION, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +70.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +53.71% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HFT-EUR +38.25% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- RARE-EUR +34.11% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- 2Z-EUR +21.09% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +19.22% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +18.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RUNE-EUR +17.05% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- TREAD-EUR +15.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +15.60% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
