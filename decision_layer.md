# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T04:17:37.057767+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : JUP-EUR | action ACHETE_MAINTENANT | opportunité 9.181 | entrée 7.150 | trend 8.950 | rang 8.451
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : FORM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.047 | entrée 5.800 | trend 8.400 | rang 7.662
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MOVR-EUR | action LATENT_ACCELERATOR | opportunité 9.248 | entrée 5.450 | trend 8.450 | rang 8.190
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HUMA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.198 | entrée 6.500 | trend 8.300 | rang 8.114
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. JUP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.451
2. MOVR-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 8.190
3. HUMA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.114

## Accélération indépendante

- QNT-EUR — CONFIRMED_ACCELERATION — score 9.139/10 — DETECTED_BUT_TOO_LATE
- TAI-EUR — CONFIRMED_ACCELERATION — score 7.885/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRC-EUR — CONFIRMED_ACCELERATION — score 7.431/10 — DETECTED_BUT_TOO_LATE
- PYTH-EUR — BUILDING_ACCELERATION — score 5.839/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TREAD-EUR — BUILDING_ACCELERATION — score 5.730/10 — DETECTED_BUT_TOO_LATE
- GLMR-EUR — BUILDING_ACCELERATION — score 5.597/10 — DETECTED_BUT_TOO_LATE
- WMTX-EUR — BUILDING_ACCELERATION — score 5.551/10 — DETECTED_BUT_TOO_LATE
- AMP-EUR — BUILDING_ACCELERATION — score 5.425/10 — DETECTED_BUT_TOO_LATE
- BAND-EUR — BUILDING_ACCELERATION — score 5.384/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RED-EUR — BUILDING_ACCELERATION — score 5.232/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- INX-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SAGA-EUR — MEMORY_24H — score mémoire 9.476/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- QNT-EUR — ACTIVE_NOW — score mémoire 9.139/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- RARE-EUR — MEMORY_24H — score mémoire 8.845/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- VELO-EUR — MEMORY_24H — score mémoire 8.605/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_DECAY_24_72H — score mémoire 8.538/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 8.451/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MOVR-EUR — ACTIVE_NOW — score mémoire 8.190/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HUMA-EUR — ACTIVE_NOW — score mémoire 8.114/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ONT-EUR — MEMORY_DECAY_24_72H — score mémoire 8.085/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- QNT-EUR +80.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +45.29% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +40.42% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +26.40% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RUNE-EUR +22.09% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +20.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRC-EUR +19.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 2Z-EUR +19.15% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GLMR-EUR +17.32% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GRASS-EUR +15.68% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
