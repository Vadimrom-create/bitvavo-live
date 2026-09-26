# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T21:22:22.657949+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 8.229 | entrée 7.100 | trend 8.250 | rang 7.840
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : COMP-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.864 | entrée 5.850 | trend 9.000 | rang 7.799
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : FIL-EUR | action LATENT_ACCELERATOR | opportunité 8.337 | entrée 5.400 | trend 8.950 | rang 7.855
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : EIGEN-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.415 | entrée 6.300 | trend 9.200 | rang 8.179
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. EIGEN-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.179
2. REZ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.083
3. LTC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.064

## Accélération indépendante

- EPIC-EUR — CONFIRMED_ACCELERATION — score 7.410/10 — DETECTED_BUT_TOO_LATE
- POND-EUR — CONFIRMED_ACCELERATION — score 7.317/10 — DETECTED_BUT_TOO_LATE
- WMTX-EUR — CONFIRMED_ACCELERATION — score 7.315/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TREAD-EUR — CONFIRMED_ACCELERATION — score 7.118/10 — DETECTED_BUT_TOO_LATE
- EDGE-EUR — CONFIRMED_ACCELERATION — score 6.634/10 — DETECTED_BUT_TOO_LATE
- SHELL-EUR — BUILDING_ACCELERATION — score 6.113/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- JASMY-EUR — BUILDING_ACCELERATION — score 5.789/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GLMR-EUR — BUILDING_ACCELERATION — score 5.254/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- UNI-EUR — BUILDING_ACCELERATION — score 5.201/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- METIS-EUR — BUILDING_ACCELERATION — score 5.024/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- AMP-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RAD-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 9.483/10 — sources ACCELERATION — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- VELO-EUR — MEMORY_24H — score mémoire 8.605/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACT-EUR — MEMORY_24H — score mémoire 8.555/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- EIGEN-EUR — ACTIVE_NOW — score mémoire 8.179/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- REZ-EUR — ACTIVE_NOW — score mémoire 8.083/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- POND-EUR +119.49% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +59.15% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +51.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +29.17% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +26.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +21.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +21.28% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- 2Z-EUR +19.68% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- RUNE-EUR +17.00% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- TREAD-EUR +15.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
