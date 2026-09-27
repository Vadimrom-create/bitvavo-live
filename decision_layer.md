# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T05:07:07.598878+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 8.220 | entrée 7.150 | trend 8.400 | rang 7.885
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : BLUR-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.094 | entrée 6.000 | trend 8.750 | rang 7.833
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ROSE-EUR | action LATENT_ACCELERATOR | opportunité 7.749 | entrée 4.600 | trend 8.950 | rang 7.579
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : RENDER-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.730 | entrée 6.450 | trend 8.900 | rang 8.234
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. RENDER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.234
2. EIGEN-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.211
3. SEI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.107

## Accélération indépendante

- GLMR-EUR — CONFIRMED_ACCELERATION — score 9.975/10 — DETECTED_BUT_TOO_LATE
- HFT-EUR — CONFIRMED_ACCELERATION — score 9.000/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOON-EUR — CONFIRMED_ACCELERATION — score 8.551/10 — DETECTED_BUT_TOO_LATE
- NES-EUR — CONFIRMED_ACCELERATION — score 8.377/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- W-EUR — CONFIRMED_ACCELERATION — score 7.133/10 — DETECTED_BUT_TOO_LATE
- HEI-EUR — CONFIRMED_ACCELERATION — score 6.879/10 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — CONFIRMED_ACCELERATION — score 6.803/10 — DETECTED_BUT_TOO_LATE
- PYTH-EUR — BUILDING_ACCELERATION — score 5.925/10 — DETECTED_BUT_TOO_LATE
- POND-EUR — BUILDING_ACCELERATION — score 5.831/10 — DETECTED_BUT_TOO_LATE
- TAIKO-EUR — BUILDING_ACCELERATION — score 5.732/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- INX-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- GLMR-EUR — ACTIVE_NOW — score mémoire 9.975/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- SAGA-EUR — MEMORY_24H — score mémoire 9.476/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- QNT-EUR — MEMORY_24H — score mémoire 9.139/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HFT-EUR — ACTIVE_NOW — score mémoire 9.000/10 — sources ACCELERATION — WATCH_ONLY
- VELO-EUR — MEMORY_24H — score mémoire 8.605/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 8.587/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SOON-EUR — ACTIVE_NOW — score mémoire 8.551/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- FTT-EUR — MEMORY_24H — score mémoire 8.427/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — ACTIVE_NOW — score mémoire 8.377/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +92.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +48.61% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +32.83% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +31.47% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- RARE-EUR +29.30% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +23.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRC-EUR +22.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TAIKO-EUR +20.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RUNE-EUR +19.47% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +19.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
