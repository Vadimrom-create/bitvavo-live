# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T21:51:25.783816+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : DATAIP-EUR | action ACHETE_MAINTENANT | opportunité 9.214 | entrée 7.400 | trend 8.700 | rang 8.403
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AAVE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.413 | entrée 6.050 | trend 9.000 | rang 8.076
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : METIS-EUR | action LATENT_ACCELERATOR | opportunité 8.340 | entrée 5.550 | trend 8.650 | rang 7.796
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : OP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.971 | entrée 6.500 | trend 8.950 | rang 8.324
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. DATAIP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.403
2. VIRTUAL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.364
3. RENDER-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.358

## Accélération indépendante

- WOO-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- JUP-EUR — CONFIRMED_ACCELERATION — score 7.239/10 — DETECTED_BUT_TOO_LATE
- U-EUR — CONFIRMED_ACCELERATION — score 6.742/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WIN-EUR — BUILDING_ACCELERATION — score 6.232/10 — DETECTED_BUT_TOO_LATE
- LAYER-EUR — BUILDING_ACCELERATION — score 6.180/10 — DETECTED_BUT_TOO_LATE
- VELO-EUR — BUILDING_ACCELERATION — score 5.568/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- YGG-EUR — BUILDING_ACCELERATION — score 5.030/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XVG-EUR — BUILDING_ACCELERATION — score 4.775/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- GRASS-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- POND-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- QNT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WOO-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- YB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DATAIP-EUR — ACTIVE_NOW — score mémoire 8.403/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VIRTUAL-EUR — ACTIVE_NOW — score mémoire 8.364/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.358/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- OP-EUR — ACTIVE_NOW — score mémoire 8.324/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +88.69% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +44.80% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INX-EUR +35.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRT-EUR +25.77% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- W-EUR +22.56% — DETECTED_EARLY — couche NONE — action NONE
- AGI-EUR +18.55% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PUMP-EUR +16.79% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +16.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +14.31% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARX-EUR +14.22% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
