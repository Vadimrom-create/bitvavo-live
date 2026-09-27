# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T05:25:12.697632+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : RENDER-EUR | action ACHETE_MAINTENANT | opportunité 9.444 | entrée 7.350 | trend 8.900 | rang 8.568
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : HOT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.221 | entrée 6.100 | trend 8.450 | rang 8.180
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : AEVO-EUR | action LATENT_ACCELERATOR | opportunité 7.819 | entrée 4.500 | trend 9.000 | rang 7.582
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LINK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.450 | entrée 6.550 | trend 8.750 | rang 8.063
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. RENDER-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.568
2. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.510
3. EIGEN-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.486

## Accélération indépendante

- RARE-EUR — CONFIRMED_ACCELERATION — score 8.765/10 — DETECTED_BUT_TOO_LATE
- ZKJ-EUR — CONFIRMED_ACCELERATION — score 7.993/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RUNE-EUR — CONFIRMED_ACCELERATION — score 7.587/10 — DETECTED_BUT_TOO_LATE
- BIGTIME-EUR — CONFIRMED_ACCELERATION — score 7.483/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CROSS-EUR — CONFIRMED_ACCELERATION — score 7.053/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- 2Z-EUR — BUILDING_ACCELERATION — score 6.439/10 — DETECTED_BUT_TOO_LATE
- TRIA-EUR — BUILDING_ACCELERATION — score 5.963/10 — DETECTED_BUT_TOO_LATE
- TLM-EUR — BUILDING_ACCELERATION — score 5.821/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MERL-EUR — BUILDING_ACCELERATION — score 5.701/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TOWNS-EUR — BUILDING_ACCELERATION — score 5.334/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- INX-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- GLMR-EUR — MEMORY_24H — score mémoire 9.975/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SAGA-EUR — MEMORY_24H — score mémoire 9.476/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- QNT-EUR — MEMORY_24H — score mémoire 9.139/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION — MEMORY_ONLY
- RARE-EUR — ACTIVE_NOW — score mémoire 8.765/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- VELO-EUR — MEMORY_24H — score mémoire 8.605/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 8.587/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.568/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOON-EUR — MEMORY_24H — score mémoire 8.551/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- QNT-EUR +89.39% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +48.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +46.82% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +36.53% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RUNE-EUR +26.02% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +25.21% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- AGI-EUR +22.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TAIKO-EUR +21.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRC-EUR +21.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +17.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
