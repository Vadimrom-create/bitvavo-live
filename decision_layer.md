# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T14:23:38.237992+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : NEAR-EUR | action ACHETE_MAINTENANT | opportunité 7.900 | entrée 7.500 | trend 8.200 | rang 7.614
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : CFG-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.070 | entrée 5.850 | trend 8.950 | rang 7.876
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BRETT-EUR | action LATENT_ACCELERATOR | opportunité 8.125 | entrée 5.450 | trend 9.000 | rang 7.797
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : DATAIP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.792 | entrée 6.300 | trend 8.450 | rang 8.082
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. DATAIP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.082
2. KAS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.082
3. A-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.030

## Accélération indépendante

- MAGIC-EUR — CONFIRMED_ACCELERATION — score 9.845/10 — DETECTED_BUT_TOO_LATE
- WIN-EUR — CONFIRMED_ACCELERATION — score 7.763/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BTT-EUR — CONFIRMED_ACCELERATION — score 7.130/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- QUID-EUR — BUILDING_ACCELERATION — score 6.496/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PUMP-EUR — BUILDING_ACCELERATION — score 6.330/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XMN-EUR — BUILDING_ACCELERATION — score 5.323/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EDGE-EUR — BUILDING_ACCELERATION — score 5.158/10 — DETECTED_BUT_TOO_LATE
- ALICE-EUR — BUILDING_ACCELERATION — score 4.973/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FLUX-EUR — BUILDING_ACCELERATION — score 4.854/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARX-EUR — BUILDING_ACCELERATION — score 4.808/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AUDIO-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MAGIC-EUR — ACTIVE_NOW — score mémoire 9.845/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- MMT-EUR — MEMORY_24H — score mémoire 9.122/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GROVE-EUR — MEMORY_24H — score mémoire 8.518/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SOON-EUR — MEMORY_24H — score mémoire 8.344/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DATAIP-EUR — ACTIVE_NOW — score mémoire 8.082/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.082/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- A-EUR — ACTIVE_NOW — score mémoire 8.030/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- RENDER-EUR — ACTIVE_NOW — score mémoire 7.992/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +54.02% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +52.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GLMR-EUR +41.02% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +33.53% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARX-EUR +27.63% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AUDIO-EUR +23.75% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GRASS-EUR +21.44% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MAGIC-EUR +20.71% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INX-EUR +17.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +15.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
