# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T20:36:10.072151+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : VET-EUR | action ACHETE_MAINTENANT | opportunité 9.327 | entrée 7.850 | trend 8.400 | rang 8.383
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ORCA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.776 | entrée 6.700 | trend 9.000 | rang 8.180
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : 0G-EUR | action LATENT_ACCELERATOR | opportunité 8.187 | entrée 5.700 | trend 8.650 | rang 7.752
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PYTH-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.830 | entrée 6.300 | trend 9.200 | rang 8.269
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.383
2. ALGO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.322
3. PYTH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.269

## Accélération indépendante

- ICX-EUR — CONFIRMED_ACCELERATION — score 7.440/10 — DETECTED_BUT_TOO_LATE
- ZRO-EUR — CONFIRMED_ACCELERATION — score 6.917/10 — DETECTED_BUT_TOO_LATE
- WLD-EUR — CONFIRMED_ACCELERATION — score 6.736/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NOS-EUR — CONFIRMED_ACCELERATION — score 6.527/10 — DETECTED_BUT_TOO_LATE
- TAO-EUR — BUILDING_ACCELERATION — score 5.849/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SQD-EUR — BUILDING_ACCELERATION — score 5.584/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- W-EUR — BUILDING_ACCELERATION — score 5.563/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AKT-EUR — BUILDING_ACCELERATION — score 5.406/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FARTCOIN-EUR — BUILDING_ACCELERATION — score 5.312/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FTT-EUR — BUILDING_ACCELERATION — score 4.903/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- WLD-EUR — ACTIVE_NOW — score mémoire 7.098/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 8.667/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RLC-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.383/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ALGO-EUR — ACTIVE_NOW — score mémoire 8.322/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.269/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HBAR-EUR — ACTIVE_NOW — score mémoire 8.222/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 8.194/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ONDO-EUR — ACTIVE_NOW — score mémoire 8.191/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- PHA-EUR +65.59% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ARK-EUR +28.45% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +24.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SEI-EUR +20.67% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ENA-EUR +18.84% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AERO-EUR +18.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +18.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +17.79% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +15.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- JTO-EUR +15.63% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
