# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T18:55:12.724296+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 9.399 | entrée 7.650 | trend 8.650 | rang 8.459
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : RPL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.233 | entrée 5.950 | trend 8.500 | rang 8.176
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MANA-EUR | action LATENT_ACCELERATOR | opportunité 7.723 | entrée 4.500 | trend 9.000 | rang 7.573
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PYTH-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.592 | entrée 6.450 | trend 9.200 | rang 8.218
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LTC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.459
2. PYTH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.218
3. RPL-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 8.176

## Accélération indépendante

- LDO-EUR — CONFIRMED_ACCELERATION — score 9.165/10 — DETECTED_BUT_TOO_LATE
- RON-EUR — CONFIRMED_ACCELERATION — score 6.895/10 — DETECTED_BUT_TOO_LATE
- ZRO-EUR — CONFIRMED_ACCELERATION — score 6.834/10 — DETECTED_BUT_TOO_LATE
- ARK-EUR — BUILDING_ACCELERATION — score 6.220/10 — DETECTED_BUT_TOO_LATE
- RARE-EUR — BUILDING_ACCELERATION — score 5.860/10 — DETECTED_BUT_TOO_LATE
- OGN-EUR — BUILDING_ACCELERATION — score 5.360/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HFT-EUR — BUILDING_ACCELERATION — score 5.329/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- JUP-EUR — BUILDING_ACCELERATION — score 5.279/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- OP-EUR — ACTIVE_NOW — score mémoire 8.158/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- JUP-EUR — ACTIVE_NOW — score mémoire 8.134/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- WMTX-EUR — MEMORY_24H — score mémoire 9.168/10 — sources ACCELERATION — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 9.165/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ICX-EUR — MEMORY_24H — score mémoire 9.081/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 8.882/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 8.667/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FUEL-EUR — MEMORY_24H — score mémoire 8.650/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- POND-EUR — MEMORY_24H — score mémoire 8.536/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- PHA-EUR +66.86% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- WMTX-EUR +54.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +32.98% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +29.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +26.44% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AERO-EUR +22.49% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +20.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +18.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SEI-EUR +17.19% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CC-EUR +16.79% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
