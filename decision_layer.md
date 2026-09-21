# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T12:07:17.176138+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAIKO-EUR | action ACHETE_MAINTENANT | opportunité 9.180 | entrée 7.400 | trend 8.150 | rang 8.114
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : LDO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.746 | entrée 6.750 | trend 8.200 | rang 7.436
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ACH-EUR | action LATENT_ACCELERATOR | opportunité 7.765 | entrée 5.450 | trend 9.000 | rang 7.654
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MERL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.739 | entrée 6.750 | trend 9.200 | rang 8.290
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.290
2. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.229
3. TAIKO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.114

## Accélération indépendante

- AIOZ-EUR — CONFIRMED_ACCELERATION — score 9.447/10 — DETECTED_BUT_TOO_LATE
- TRAC-EUR — BUILDING_ACCELERATION — score 6.469/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PROVE-EUR — BUILDING_ACCELERATION — score 5.733/10 — DETECTED_BUT_TOO_LATE
- PHA-EUR — BUILDING_ACCELERATION — score 5.500/10 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — BUILDING_ACCELERATION — score 4.917/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EIGEN-EUR — ACTIVE_NOW — score mémoire 7.802/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ONDO-EUR — ACTIVE_NOW — score mémoire 7.528/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- TAO-EUR — ACTIVE_NOW — score mémoire 7.477/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- EDGE-EUR — MEMORY_24H — score mémoire 9.925/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 9.488/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RLC-EUR — MEMORY_24H — score mémoire 9.465/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 9.447/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- IMX-EUR — MEMORY_24H — score mémoire 9.317/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOCA-EUR — MEMORY_24H — score mémoire 8.589/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZETA-EUR +74.78% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PHA-EUR +67.68% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PTB-EUR +38.81% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- KMNO-EUR +31.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +29.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SEI-EUR +26.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +26.32% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PEAQ-EUR +24.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUI-EUR +23.66% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AIOZ-EUR +21.94% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
