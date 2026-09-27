# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T08:07:47.267241+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : RENDER-EUR | action ACHETE_MAINTENANT | opportunité 9.526 | entrée 7.800 | trend 9.200 | rang 8.635
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AEVO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.551 | entrée 5.850 | trend 9.000 | rang 8.061
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SPK-EUR | action LATENT_ACCELERATOR | opportunité 8.301 | entrée 5.600 | trend 8.900 | rang 7.815
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : A-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.269 | entrée 6.400 | trend 8.700 | rang 8.344
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. RENDER-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.635
2. FIL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.450
3. A-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.344

## Accélération indépendante

- ARB-EUR — CONFIRMED_ACCELERATION — score 7.258/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GMX-EUR — CONFIRMED_ACCELERATION — score 6.712/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ORCA-EUR — CONFIRMED_ACCELERATION — score 6.502/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOON-EUR — BUILDING_ACCELERATION — score 6.461/10 — DETECTED_BUT_TOO_LATE
- SUPER-EUR — BUILDING_ACCELERATION — score 6.352/10 — DETECTED_BUT_TOO_LATE
- HAEDAL-EUR — BUILDING_ACCELERATION — score 6.280/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ATOM-EUR — BUILDING_ACCELERATION — score 6.181/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NOS-EUR — BUILDING_ACCELERATION — score 6.067/10 — DETECTED_BUT_TOO_LATE
- W-EUR — BUILDING_ACCELERATION — score 5.863/10 — DETECTED_BUT_TOO_LATE
- TOWNS-EUR — BUILDING_ACCELERATION — score 5.842/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ARB-EUR — ACTIVE_NOW — score mémoire 7.258/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- WMTX-EUR — MEMORY_24H — score mémoire 9.850/10 — sources ACCELERATION — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 9.365/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 8.687/10 — sources ACCELERATION — MEMORY_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.635/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AMP-EUR — MEMORY_24H — score mémoire 8.589/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FIL-EUR — ACTIVE_NOW — score mémoire 8.450/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.427/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- A-EUR — ACTIVE_NOW — score mémoire 8.344/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +66.07% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +57.13% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +40.98% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +33.41% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +24.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- W-EUR +22.29% — DETECTED_EARLY — couche NONE — action NONE
- EDGE-EUR +20.49% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HFT-EUR +19.50% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PYTH-EUR +17.06% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +16.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
