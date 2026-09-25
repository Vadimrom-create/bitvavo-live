# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T13:45:16.519035+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : OP-EUR | action ACHETE_MAINTENANT | opportunité 8.722 | entrée 7.450 | trend 8.950 | rang 8.100
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : JUP-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.143 | entrée 6.650 | trend 8.950 | rang 7.768
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ALT-EUR | action LATENT_ACCELERATOR | opportunité 7.683 | entrée 5.650 | trend 8.550 | rang 7.507
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : COMP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.370 | entrée 7.250 | trend 8.750 | rang 8.029
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. OP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.100
2. COMP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.029
3. ICP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.950

## Accélération indépendante

- XMN-EUR — CONFIRMED_ACCELERATION — score 9.141/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GLMR-EUR — BUILDING_ACCELERATION — score 6.400/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CNPY-EUR — BUILDING_ACCELERATION — score 4.879/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- OP-EUR — ACTIVE_NOW — score mémoire 8.100/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- HUMA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XMN-EUR — ACTIVE_NOW — score mémoire 9.141/10 — sources ACCELERATION, V4 — WATCH_ONLY
- SCR-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- PHA-EUR — MEMORY_24H — score mémoire 8.218/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- COMP-EUR — ACTIVE_NOW — score mémoire 8.029/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.950/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZK-EUR — ACTIVE_NOW — score mémoire 7.899/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FIL-EUR — MEMORY_24H — score mémoire 7.854/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- PHA-EUR +41.32% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- TREAD-EUR +35.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +29.63% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XPL-EUR +24.97% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- NIL-EUR +23.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +23.26% — DETECTED_EARLY — couche NONE — action NONE
- DBR-EUR +18.99% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +18.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PIXEL-EUR +17.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FET-EUR +17.17% — DETECTED_EARLY — couche NONE — action NONE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
