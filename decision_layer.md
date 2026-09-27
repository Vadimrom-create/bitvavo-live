# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T17:12:17.529541+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ORCA-EUR | action ACHETE_MAINTENANT | opportunité 9.364 | entrée 7.550 | trend 8.950 | rang 8.654
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : THE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.281 | entrée 6.600 | trend 8.500 | rang 7.618
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ROSE-EUR | action LATENT_ACCELERATOR | opportunité 8.540 | entrée 5.700 | trend 8.950 | rang 7.982
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : EIGEN-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.370 | entrée 7.050 | trend 8.900 | rang 8.573
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ORCA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.654
2. EIGEN-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.573
3. AXL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.420

## Accélération indépendante

- DYDX-EUR — CONFIRMED_ACCELERATION — score 7.560/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ESP-EUR — CONFIRMED_ACCELERATION — score 6.548/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- APE-EUR — BUILDING_ACCELERATION — score 4.855/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DRIFT-EUR — BUILDING_ACCELERATION — score 4.778/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ZRC-EUR — MEMORY_24H — score mémoire 9.612/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MMT-EUR — MEMORY_24H — score mémoire 9.122/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ORCA-EUR — ACTIVE_NOW — score mémoire 8.654/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- EIGEN-EUR — ACTIVE_NOW — score mémoire 8.573/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GROVE-EUR — MEMORY_24H — score mémoire 8.518/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- YB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AXL-EUR — ACTIVE_NOW — score mémoire 8.420/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.115/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 8.035/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +51.63% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +49.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +33.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AUDIO-EUR +30.35% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARX-EUR +25.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INX-EUR +22.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +20.63% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- W-EUR +18.63% — DETECTED_EARLY — couche NONE — action NONE
- GLMR-EUR +17.62% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PYTH-EUR +11.22% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
