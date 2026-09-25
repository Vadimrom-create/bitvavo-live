# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T16:32:45.519136+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : RENDER-EUR | action ACHETE_MAINTENANT | opportunité 8.700 | entrée 7.300 | trend 9.000 | rang 8.298
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : BEAM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.251 | entrée 5.800 | trend 8.900 | rang 7.875
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ALGO-EUR | action LATENT_ACCELERATOR | opportunité 7.745 | entrée 4.500 | trend 8.750 | rang 7.472
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AXS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.466 | entrée 7.100 | trend 9.000 | rang 8.076
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. RENDER-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.298
2. FET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.202
3. LINK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.170

## Accélération indépendante

- SPK-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- HUMA-EUR — CONFIRMED_ACCELERATION — score 7.999/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AAVE-EUR — CONFIRMED_ACCELERATION — score 7.978/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RARE-EUR — CONFIRMED_ACCELERATION — score 7.337/10 — DETECTED_BUT_TOO_LATE
- XPL-EUR — CONFIRMED_ACCELERATION — score 7.258/10 — DETECTED_BUT_TOO_LATE
- BEAM-EUR — CONFIRMED_ACCELERATION — score 7.009/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GRASS-EUR — CONFIRMED_ACCELERATION — score 6.936/10 — DETECTED_BUT_TOO_LATE
- REZ-EUR — CONFIRMED_ACCELERATION — score 6.871/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DYM-EUR — BUILDING_ACCELERATION — score 6.295/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- THE-EUR — BUILDING_ACCELERATION — score 6.086/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- SPK-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.298/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 8.202/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 8.170/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AXS-EUR — ACTIVE_NOW — score mémoire 8.076/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.076/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- HFT-EUR — MEMORY_DECAY_24_72H — score mémoire 8.060/10 — sources ACCELERATION — MEMORY_ONLY
- REQ-EUR — MEMORY_24H — score mémoire 8.033/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 8.018/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PHA-EUR +49.01% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- TREAD-EUR +29.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +27.08% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +25.99% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SPK-EUR +19.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +18.92% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ENA-EUR +17.89% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +17.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DBR-EUR +16.93% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AERO-EUR +15.67% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
