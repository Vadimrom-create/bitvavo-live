# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T21:37:31.754740+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : DATAIP-EUR | action ACHETE_MAINTENANT | opportunité 9.225 | entrée 7.400 | trend 8.700 | rang 8.399
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : APE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.165 | entrée 6.400 | trend 8.700 | rang 7.835
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : GALA-EUR | action LATENT_ACCELERATOR | opportunité 8.238 | entrée 5.600 | trend 8.700 | rang 7.770
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ATH-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.332 | entrée 6.550 | trend 8.900 | rang 8.510
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ATH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.510
2. DATAIP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.399
3. LTC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.294

## Accélération indépendante

- GRASS-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- RARE-EUR — CONFIRMED_ACCELERATION — score 9.328/10 — DETECTED_BUT_TOO_LATE
- JUP-EUR — CONFIRMED_ACCELERATION — score 8.558/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AIOZ-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- QNT-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- LAYER-EUR — CONFIRMED_ACCELERATION — score 6.723/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GRT-EUR — CONFIRMED_ACCELERATION — score 6.722/10 — DETECTED_BUT_TOO_LATE
- SOON-EUR — BUILDING_ACCELERATION — score 6.067/10 — DETECTED_BUT_TOO_LATE
- U-EUR — BUILDING_ACCELERATION — score 5.700/10 — DETECTED_BUT_TOO_LATE
- WIN-EUR — BUILDING_ACCELERATION — score 5.262/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GRASS-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- RARE-EUR — ACTIVE_NOW — score mémoire 9.328/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- JUP-EUR — ACTIVE_NOW — score mémoire 8.558/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ATH-EUR — ACTIVE_NOW — score mémoire 8.510/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- POND-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- QNT-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- YB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DATAIP-EUR — ACTIVE_NOW — score mémoire 8.399/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- QNT-EUR +83.81% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +40.36% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INX-EUR +32.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRT-EUR +22.23% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- W-EUR +21.90% — DETECTED_EARLY — couche NONE — action NONE
- TREAD-EUR +20.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +18.12% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GRASS-EUR +16.75% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PUMP-EUR +14.98% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NEAR-EUR +12.74% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
