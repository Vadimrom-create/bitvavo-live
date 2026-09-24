# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T15:42:00.530527+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : JUP-EUR | action ACHETE_MAINTENANT | opportunité 9.210 | entrée 7.400 | trend 8.150 | rang 8.069
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : COMP-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.738 | entrée 6.600 | trend 8.500 | rang 7.489
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SIGN-EUR | action LATENT_ACCELERATOR | opportunité 7.616 | entrée 4.500 | trend 8.950 | rang 7.381
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : DBR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.719 | entrée 7.300 | trend 8.050 | rang 8.021
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. JUP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.069
2. DBR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.021
3. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.881

## Accélération indépendante

- POND-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- INJ-EUR — CONFIRMED_ACCELERATION — score 7.774/10 — DETECTED_BUT_TOO_LATE
- SOON-EUR — BUILDING_ACCELERATION — score 6.249/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CFG-EUR — BUILDING_ACCELERATION — score 6.163/10 — DETECTED_BUT_TOO_LATE
- AGI-EUR — BUILDING_ACCELERATION — score 6.062/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARX-EUR — BUILDING_ACCELERATION — score 5.833/10 — DETECTED_BUT_TOO_LATE
- QNT-EUR — BUILDING_ACCELERATION — score 5.592/10 — DETECTED_BUT_TOO_LATE
- OSMO-EUR — BUILDING_ACCELERATION — score 5.546/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CHIP-EUR — BUILDING_ACCELERATION — score 5.423/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NIL-EUR — BUILDING_ACCELERATION — score 5.333/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- JUP-EUR — ACTIVE_NOW — score mémoire 8.069/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- TAIKO-EUR — ACTIVE_NOW — score mémoire 7.311/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- AMP-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FLOCK-EUR — MEMORY_24H — score mémoire 9.446/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XAI-EUR — MEMORY_24H — score mémoire 9.433/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- 2Z-EUR — MEMORY_24H — score mémoire 8.723/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CNPY-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- POND-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- NOM-EUR +39.13% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- LSK-EUR +27.53% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ONDO-EUR +25.62% — DETECTED_EARLY — couche NONE — action NONE
- LTC-EUR +23.28% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- POND-EUR +22.27% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- NIL-EUR +21.87% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PEAQ-EUR +19.70% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARX-EUR +17.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PLUME-EUR +15.62% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ETC-EUR +15.46% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
