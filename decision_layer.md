# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T15:56:41.752852+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : JUP-EUR | action ACHETE_MAINTENANT | opportunité 8.059 | entrée 6.950 | trend 8.150 | rang 7.428
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ENA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.141 | entrée 6.700 | trend 8.300 | rang 7.424
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SIGN-EUR | action LATENT_ACCELERATOR | opportunité 7.664 | entrée 4.500 | trend 8.950 | rang 7.418
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : DBR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.141 | entrée 7.200 | trend 8.050 | rang 8.182
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. DBR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.182
2. KMNO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.823
3. BAT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.753

## Accélération indépendante

- ACH-EUR — CONFIRMED_ACCELERATION — score 9.000/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PYTH-EUR — CONFIRMED_ACCELERATION — score 8.053/10 — DETECTED_BUT_TOO_LATE
- BIO-EUR — CONFIRMED_ACCELERATION — score 8.037/10 — DETECTED_BUT_TOO_LATE
- PEOPLE-EUR — CONFIRMED_ACCELERATION — score 6.972/10 — DETECTED_BUT_TOO_LATE
- RED-EUR — CONFIRMED_ACCELERATION — score 6.956/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAI-EUR — CONFIRMED_ACCELERATION — score 6.763/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MANTRA-EUR — CONFIRMED_ACCELERATION — score 6.500/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PARTI-EUR — BUILDING_ACCELERATION — score 6.314/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NOM-EUR — BUILDING_ACCELERATION — score 6.244/10 — DETECTED_BUT_TOO_LATE
- ROBO-EUR — BUILDING_ACCELERATION — score 6.046/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- JUP-EUR — ACTIVE_NOW — score mémoire 7.428/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ALGO-EUR — ACTIVE_NOW — score mémoire 7.421/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- AMP-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FLOCK-EUR — MEMORY_24H — score mémoire 9.446/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XAI-EUR — MEMORY_24H — score mémoire 9.433/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACH-EUR — ACTIVE_NOW — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- 2Z-EUR — MEMORY_24H — score mémoire 8.723/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CNPY-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- NOM-EUR +41.18% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- LSK-EUR +30.18% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ONDO-EUR +25.64% — DETECTED_EARLY — couche NONE — action NONE
- LTC-EUR +25.40% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARX-EUR +19.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +19.11% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEAQ-EUR +18.39% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- POND-EUR +18.25% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- FET-EUR +16.70% — DETECTED_EARLY — couche NONE — action NONE
- ETC-EUR +15.99% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
