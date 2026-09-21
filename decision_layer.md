# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T10:47:44.118081+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : KSM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.679 | entrée 6.100 | trend 7.950 | rang 7.739
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ARX-EUR | action LATENT_ACCELERATOR | opportunité 8.143 | entrée 5.400 | trend 8.900 | rang 7.698
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MERL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.450 | entrée 6.650 | trend 9.200 | rang 8.130
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.130
2. ALGO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.974
3. XTZ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.870

## Accélération indépendante

- SEI-EUR — CONFIRMED_ACCELERATION — score 9.048/10 — DETECTED_BUT_TOO_LATE
- ARB-EUR — CONFIRMED_ACCELERATION — score 8.666/10 — DETECTED_BUT_TOO_LATE
- PONKE-EUR — CONFIRMED_ACCELERATION — score 8.206/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IMX-EUR — CONFIRMED_ACCELERATION — score 7.441/10 — DETECTED_BUT_TOO_LATE
- JTO-EUR — BUILDING_ACCELERATION — score 6.378/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PUFFER-EUR — BUILDING_ACCELERATION — score 5.898/10 — DETECTED_BUT_TOO_LATE
- AKT-EUR — BUILDING_ACCELERATION — score 5.835/10 — DETECTED_BUT_TOO_LATE
- FOLD-EUR — BUILDING_ACCELERATION — score 5.665/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XTZ-EUR — BUILDING_ACCELERATION — score 5.653/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZIG-EUR — BUILDING_ACCELERATION — score 5.234/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 9.925/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 9.488/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RLC-EUR — MEMORY_24H — score mémoire 9.465/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CHIP-EUR — MEMORY_24H — score mémoire 9.309/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZETA-EUR — MEMORY_24H — score mémoire 9.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SEI-EUR — ACTIVE_NOW — score mémoire 9.048/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- NOS-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ARB-EUR — ACTIVE_NOW — score mémoire 8.666/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- MOCA-EUR — MEMORY_24H — score mémoire 8.589/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 8.457/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- PHA-EUR +72.80% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZETA-EUR +70.84% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PTB-EUR +50.98% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NIL-EUR +33.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +30.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +29.62% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SEI-EUR +28.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEAQ-EUR +23.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KERNEL-EUR +22.99% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUI-EUR +22.67% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
