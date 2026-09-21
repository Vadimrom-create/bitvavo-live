# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T10:31:15.238297+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 8.093 | entrée 7.500 | trend 6.850 | rang 7.168
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ARX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.455 | entrée 5.850 | trend 8.900 | rang 7.879
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BIGTIME-EUR | action LATENT_ACCELERATOR | opportunité 7.613 | entrée 4.500 | trend 8.750 | rang 7.432
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MERL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.418 | entrée 6.900 | trend 9.200 | rang 8.157
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.157
2. ALGO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.059
3. RUNE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.926

## Accélération indépendante

- RLC-EUR — CONFIRMED_ACCELERATION — score 9.465/10 — DETECTED_BUT_TOO_LATE
- CPOOL-EUR — CONFIRMED_ACCELERATION — score 8.276/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRO-EUR — CONFIRMED_ACCELERATION — score 7.290/10 — DETECTED_BUT_TOO_LATE
- CSPR-EUR — CONFIRMED_ACCELERATION — score 6.933/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SEI-EUR — CONFIRMED_ACCELERATION — score 6.914/10 — DETECTED_BUT_TOO_LATE
- USELESS-EUR — CONFIRMED_ACCELERATION — score 6.856/10 — DETECTED_BUT_TOO_LATE
- AXS-EUR — CONFIRMED_ACCELERATION — score 6.644/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- JUP-EUR — BUILDING_ACCELERATION — score 6.358/10 — DETECTED_BUT_TOO_LATE
- PARTI-EUR — BUILDING_ACCELERATION — score 5.993/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WIN-EUR — BUILDING_ACCELERATION — score 5.951/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- PORTAL-EUR — ACTIVE_NOW — score mémoire 7.611/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- EDGE-EUR — MEMORY_24H — score mémoire 9.925/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 9.488/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RLC-EUR — ACTIVE_NOW — score mémoire 9.465/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CHIP-EUR — MEMORY_24H — score mémoire 9.309/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZETA-EUR — MEMORY_24H — score mémoire 9.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NOS-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- KERNEL-EUR — MEMORY_24H — score mémoire 8.792/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOCA-EUR — MEMORY_24H — score mémoire 8.589/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 8.457/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZETA-EUR +72.47% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PHA-EUR +67.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PTB-EUR +51.74% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NIL-EUR +33.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +30.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +29.90% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- DRIFT-EUR +25.54% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SEI-EUR +25.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEAQ-EUR +24.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +23.68% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
