# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T13:53:45.228187+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 9.292 | entrée 8.050 | trend 8.250 | rang 8.409
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AEVO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.655 | entrée 5.850 | trend 8.500 | rang 7.912
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ALT-EUR | action LATENT_ACCELERATOR | opportunité 7.978 | entrée 5.650 | trend 8.750 | rang 7.738
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ROSE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.720 | entrée 6.300 | trend 8.950 | rang 8.117
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.409
2. WLD-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.360
3. WAL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.210

## Accélération indépendante

- EDGE-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- 2Z-EUR — CONFIRMED_ACCELERATION — score 7.464/10 — DETECTED_BUT_TOO_LATE
- U-EUR — CONFIRMED_ACCELERATION — score 7.091/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EIGEN-EUR — CONFIRMED_ACCELERATION — score 6.944/10 — DETECTED_BUT_TOO_LATE
- WCT-EUR — BUILDING_ACCELERATION — score 5.920/10 — DETECTED_BUT_TOO_LATE
- NIL-EUR — BUILDING_ACCELERATION — score 5.674/10 — DETECTED_BUT_TOO_LATE
- DYDX-EUR — BUILDING_ACCELERATION — score 5.564/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ENJ-EUR — BUILDING_ACCELERATION — score 5.436/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EGLD-EUR — BUILDING_ACCELERATION — score 5.217/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- OP-EUR — BUILDING_ACCELERATION — score 5.183/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDGE-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- XMN-EUR — MEMORY_24H — score mémoire 9.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 9.830/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RAD-EUR — MEMORY_24H — score mémoire 9.291/10 — sources ACCELERATION — MEMORY_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACT-EUR — MEMORY_24H — score mémoire 8.555/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WMTX-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.409/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- POND-EUR +153.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +75.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 2Z-EUR +32.96% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- AMP-EUR +29.18% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +28.39% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARK-EUR +21.88% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PROM-EUR +18.05% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- RUNE-EUR +14.47% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ENA-EUR +14.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AERO-EUR +13.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
