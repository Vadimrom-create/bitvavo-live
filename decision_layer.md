# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T18:19:18.907603+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : OP-EUR | action ACHETE_MAINTENANT | opportunité 9.221 | entrée 7.400 | trend 8.700 | rang 8.407
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : WAXP-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.230 | entrée 6.000 | trend 8.950 | rang 7.852
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ATH-EUR | action LATENT_ACCELERATOR | opportunité 8.347 | entrée 5.650 | trend 8.700 | rang 7.525
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LINK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.267 | entrée 7.250 | trend 9.000 | rang 8.153
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. OP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.407
2. JUP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.359
3. AXS-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.167

## Accélération indépendante

- ATH-EUR — CONFIRMED_ACCELERATION — score 7.451/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CHR-EUR — BUILDING_ACCELERATION — score 5.997/10 — DETECTED_BUT_TOO_LATE
- TRIA-EUR — BUILDING_ACCELERATION — score 5.594/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FARTCOIN-EUR — BUILDING_ACCELERATION — score 5.192/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAI-EUR — BUILDING_ACCELERATION — score 5.083/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SPX-EUR — BUILDING_ACCELERATION — score 5.000/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZBCN-EUR — BUILDING_ACCELERATION — score 4.849/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CAT-EUR — BUILDING_ACCELERATION — score 4.767/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- JUP-EUR — ACTIVE_NOW — score mémoire 8.359/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- XAI-EUR — ACTIVE_NOW — score mémoire 7.664/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- WMTX-EUR — MEMORY_24H — score mémoire 9.168/10 — sources ACCELERATION — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 8.917/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 8.882/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FUEL-EUR — MEMORY_24H — score mémoire 8.650/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- OP-EUR — ACTIVE_NOW — score mémoire 8.407/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AXS-EUR — ACTIVE_NOW — score mémoire 8.167/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.155/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- WMTX-EUR +78.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +66.28% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ARK-EUR +29.75% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +26.03% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AERO-EUR +22.49% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +22.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +21.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +20.85% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +19.59% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SEI-EUR +16.06% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
