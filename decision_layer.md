# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T18:38:03.595330+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : OP-EUR | action ACHETE_MAINTENANT | opportunité 9.146 | entrée 7.600 | trend 8.700 | rang 8.344
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : RED-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.387 | entrée 6.050 | trend 8.700 | rang 7.857
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ORCA-EUR | action LATENT_ACCELERATOR | opportunité 8.008 | entrée 5.750 | trend 8.500 | rang 7.576
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PYTH-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.599 | entrée 6.450 | trend 9.200 | rang 8.182
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. OP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.344
2. PYTH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.182
3. JUP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.168

## Accélération indépendante

- ICX-EUR — CONFIRMED_ACCELERATION — score 9.081/10 — DETECTED_BUT_TOO_LATE
- NIL-EUR — CONFIRMED_ACCELERATION — score 8.667/10 — DETECTED_BUT_TOO_LATE
- POND-EUR — CONFIRMED_ACCELERATION — score 8.536/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- U-EUR — CONFIRMED_ACCELERATION — score 7.682/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EDGE-EUR — BUILDING_ACCELERATION — score 5.814/10 — DETECTED_BUT_TOO_LATE
- BILL-EUR — BUILDING_ACCELERATION — score 5.778/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AZTEC-EUR — BUILDING_ACCELERATION — score 5.724/10 — DETECTED_BUT_TOO_LATE
- WELL-EUR — BUILDING_ACCELERATION — score 5.587/10 — DETECTED_BUT_TOO_LATE
- GRT-EUR — BUILDING_ACCELERATION — score 5.414/10 — DETECTED_BUT_TOO_LATE
- SUSHI-EUR — BUILDING_ACCELERATION — score 5.273/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- OP-EUR — ACTIVE_NOW — score mémoire 8.344/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- WMTX-EUR — MEMORY_24H — score mémoire 9.168/10 — sources ACCELERATION — MEMORY_ONLY
- ICX-EUR — ACTIVE_NOW — score mémoire 9.081/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- SWELL-EUR — MEMORY_24H — score mémoire 8.882/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NIL-EUR — ACTIVE_NOW — score mémoire 8.667/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- FUEL-EUR — MEMORY_24H — score mémoire 8.650/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- POND-EUR — ACTIVE_NOW — score mémoire 8.536/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FLUX-EUR — ACTIVE_NOW — score mémoire 8.305/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.182/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- WMTX-EUR +70.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +67.53% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ARK-EUR +30.75% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +26.53% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +24.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +22.59% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AERO-EUR +21.61% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ENA-EUR +20.56% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SEI-EUR +17.69% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CC-EUR +15.96% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
