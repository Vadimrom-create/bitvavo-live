# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T10:12:55.877752+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : DOT-EUR | action ACHETE_MAINTENANT | opportunité 9.178 | entrée 8.050 | trend 8.000 | rang 8.236
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ARX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.809 | entrée 5.850 | trend 8.900 | rang 7.977
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : CELO-EUR | action LATENT_ACCELERATOR | opportunité 7.679 | entrée 4.500 | trend 8.750 | rang 7.379
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MANTA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.074 | entrée 6.550 | trend 8.200 | rang 8.080
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. DOT-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.236
2. MANTA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.080
3. ALGO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.071

## Accélération indépendante

- CHIP-EUR — CONFIRMED_ACCELERATION — score 9.309/10 — DETECTED_BUT_TOO_LATE
- KERNEL-EUR — CONFIRMED_ACCELERATION — score 8.792/10 — DETECTED_BUT_TOO_LATE
- SFP-EUR — CONFIRMED_ACCELERATION — score 8.323/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PHA-EUR — CONFIRMED_ACCELERATION — score 8.269/10 — DETECTED_BUT_TOO_LATE
- DRIFT-EUR — CONFIRMED_ACCELERATION — score 6.727/10 — DETECTED_BUT_TOO_LATE
- NES-EUR — BUILDING_ACCELERATION — score 6.166/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARB-EUR — BUILDING_ACCELERATION — score 5.782/10 — DETECTED_BUT_TOO_LATE
- SOLV-EUR — BUILDING_ACCELERATION — score 5.289/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CELR-EUR — BUILDING_ACCELERATION — score 4.988/10 — DETECTED_BUT_TOO_LATE
- HEI-EUR — BUILDING_ACCELERATION — score 4.900/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PORTAL-EUR — ACTIVE_NOW — score mémoire 7.782/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- STX-EUR — ACTIVE_NOW — score mémoire 7.626/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- EDGE-EUR — MEMORY_24H — score mémoire 9.925/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 9.488/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CHIP-EUR — ACTIVE_NOW — score mémoire 9.309/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- ZETA-EUR — MEMORY_24H — score mémoire 9.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NOS-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- KERNEL-EUR — ACTIVE_NOW — score mémoire 8.792/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- MOCA-EUR — MEMORY_24H — score mémoire 8.589/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 8.457/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZETA-EUR +70.28% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PHA-EUR +65.60% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PTB-EUR +54.21% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NIL-EUR +34.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +33.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +29.85% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- DRIFT-EUR +29.12% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +26.28% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEAQ-EUR +25.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +23.63% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
