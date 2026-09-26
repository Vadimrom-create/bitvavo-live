# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T00:05:53.379614+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LINK-EUR | action ACHETE_MAINTENANT | opportunité 9.467 | entrée 7.200 | trend 9.000 | rang 8.656
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : WAXP-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.456 | entrée 6.750 | trend 8.900 | rang 8.008
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BEAM-EUR | action LATENT_ACCELERATOR | opportunité 7.904 | entrée 5.750 | trend 8.700 | rang 7.648
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ORCA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.357 | entrée 7.000 | trend 8.750 | rang 8.414
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LINK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.656
2. ORCA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.414
3. GALA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.349

## Accélération indépendante

- GAS-EUR — CONFIRMED_ACCELERATION — score 9.223/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ONT-EUR — CONFIRMED_ACCELERATION — score 8.859/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CVC-EUR — CONFIRMED_ACCELERATION — score 8.006/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POWR-EUR — CONFIRMED_ACCELERATION — score 7.020/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WAXP-EUR — CONFIRMED_ACCELERATION — score 6.886/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NEO-EUR — BUILDING_ACCELERATION — score 6.226/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POND-EUR — BUILDING_ACCELERATION — score 6.102/10 — DETECTED_BUT_TOO_LATE
- XMN-EUR — BUILDING_ACCELERATION — score 5.740/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WMTX-EUR — BUILDING_ACCELERATION — score 5.428/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SLX-EUR — BUILDING_ACCELERATION — score 5.149/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- WIF-EUR — ACTIVE_NOW — score mémoire 7.738/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GAS-EUR — ACTIVE_NOW — score mémoire 9.223/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 8.975/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SSV-EUR — MEMORY_24H — score mémoire 8.917/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ONT-EUR — ACTIVE_NOW — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 8.667/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 8.656/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ARK-EUR — MEMORY_24H — score mémoire 8.526/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- PHA-EUR +67.25% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- POND-EUR +50.39% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARK-EUR +29.75% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AERO-EUR +21.56% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SEI-EUR +19.78% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ENA-EUR +19.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +18.83% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WMTX-EUR +18.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RARE-EUR +17.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +17.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
