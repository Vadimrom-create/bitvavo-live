# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T14:22:28.175662+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : JUP-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.924 | entrée 6.450 | trend 8.950 | rang 7.762
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ZK-EUR | action LATENT_ACCELERATOR | opportunité 7.978 | entrée 5.450 | trend 8.700 | rang 7.676
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : OP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.420 | entrée 7.200 | trend 8.950 | rang 8.139
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. OP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.139
2. PYTH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.073
3. CAKE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.925

## Accélération indépendante

- POND-EUR — CONFIRMED_ACCELERATION — score 7.558/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DBR-EUR — CONFIRMED_ACCELERATION — score 7.014/10 — DETECTED_BUT_TOO_LATE
- QUID-EUR — CONFIRMED_ACCELERATION — score 6.692/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAI-EUR — BUILDING_ACCELERATION — score 5.933/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SCR-EUR — BUILDING_ACCELERATION — score 5.695/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NIL-EUR — BUILDING_ACCELERATION — score 5.477/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- RUNE-EUR — MEMORY_24H — score mémoire 8.153/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- OP-EUR — ACTIVE_NOW — score mémoire 8.139/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.073/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.925/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 7.865/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- OGN-EUR — MEMORY_24H — score mémoire 7.854/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.837/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 7.794/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 7.762/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PHA-EUR +53.55% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- TREAD-EUR +40.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +24.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DBR-EUR +19.86% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +17.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QNT-EUR +16.75% — DETECTED_EARLY — couche NONE — action NONE
- NIL-EUR +16.21% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHIP-EUR +14.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +14.66% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XPL-EUR +14.07% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
