# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T17:24:06.010438+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : RENDER-EUR | action ACHETE_MAINTENANT | opportunité 8.323 | entrée 7.150 | trend 9.000 | rang 8.143
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : GRT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.187 | entrée 5.850 | trend 8.300 | rang 8.053
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ZK-EUR | action LATENT_ACCELERATOR | opportunité 8.035 | entrée 5.250 | trend 8.950 | rang 7.712
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LINK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.197 | entrée 7.150 | trend 9.000 | rang 8.053
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. RENDER-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.143
2. GRT-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 8.053
3. LINK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.053

## Accélération indépendante

- SWELL-EUR — CONFIRMED_ACCELERATION — score 8.882/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FUEL-EUR — CONFIRMED_ACCELERATION — score 8.650/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HFT-EUR — CONFIRMED_ACCELERATION — score 7.660/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GRT-EUR — CONFIRMED_ACCELERATION — score 7.459/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BEAM-EUR — CONFIRMED_ACCELERATION — score 7.236/10 — DETECTED_BUT_TOO_LATE
- SAGA-EUR — CONFIRMED_ACCELERATION — score 6.692/10 — DETECTED_BUT_TOO_LATE
- DGB-EUR — BUILDING_ACCELERATION — score 6.193/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SPK-EUR — BUILDING_ACCELERATION — score 6.044/10 — DETECTED_BUT_TOO_LATE
- AGI-EUR — BUILDING_ACCELERATION — score 5.937/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — BUILDING_ACCELERATION — score 5.668/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SWELL-EUR — ACTIVE_NOW — score mémoire 8.882/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- STO-EUR — MEMORY_24H — score mémoire 8.737/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FUEL-EUR — ACTIVE_NOW — score mémoire 8.650/10 — sources ACCELERATION, V4 — WATCH_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.143/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GRT-EUR — ACTIVE_NOW — score mémoire 8.053/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 8.053/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- REQ-EUR — MEMORY_24H — score mémoire 8.033/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 8.021/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AXS-EUR — ACTIVE_NOW — score mémoire 8.014/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PHA-EUR +56.04% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ARK-EUR +27.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WMTX-EUR +26.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RARE-EUR +23.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +21.67% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AERO-EUR +19.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ENA-EUR +19.50% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +18.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +16.79% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SPK-EUR +15.61% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
