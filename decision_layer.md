# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T17:05:20.207974+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : FET-EUR | action ACHETE_MAINTENANT | opportunité 8.232 | entrée 7.500 | trend 8.850 | rang 8.020
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : OP-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.789 | entrée 6.750 | trend 8.400 | rang 7.657
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MOVR-EUR | action LATENT_ACCELERATOR | opportunité 8.296 | entrée 5.750 | trend 8.950 | rang 7.864
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : JUP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.010 | entrée 7.650 | trend 8.950 | rang 8.037
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. JUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.037
2. FET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.020
3. RENDER-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.000

## Accélération indépendante

- STO-EUR — CONFIRMED_ACCELERATION — score 8.737/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RARE-EUR — CONFIRMED_ACCELERATION — score 7.018/10 — DETECTED_BUT_TOO_LATE
- OGN-EUR — BUILDING_ACCELERATION — score 6.333/10 — DETECTED_BUT_TOO_LATE
- C-EUR — BUILDING_ACCELERATION — score 5.330/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MAVIA-EUR — BUILDING_ACCELERATION — score 5.216/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- THE-EUR — BUILDING_ACCELERATION — score 5.196/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AERO-EUR — BUILDING_ACCELERATION — score 5.101/10 — DETECTED_BUT_TOO_LATE
- DODO-EUR — BUILDING_ACCELERATION — score 4.866/10 — DETECTED_BUT_TOO_LATE
- TOSHI-EUR — BUILDING_ACCELERATION — score 4.795/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XYO-EUR — BUILDING_ACCELERATION — score 4.772/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ZRC-EUR — MEMORY_24H — score mémoire 9.898/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- STO-EUR — ACTIVE_NOW — score mémoire 8.737/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 8.037/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- REQ-EUR — MEMORY_24H — score mémoire 8.033/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 8.020/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HUMA-EUR — MEMORY_24H — score mémoire 7.999/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AXS-EUR — ACTIVE_NOW — score mémoire 7.980/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 7.970/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PHA-EUR +56.10% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- RARE-EUR +28.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +26.26% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +22.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +21.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AERO-EUR +20.31% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +19.84% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ENA-EUR +19.00% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +15.66% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- DBR-EUR +14.86% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
