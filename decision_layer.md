# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T11:54:10.561413+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : PEPE-EUR | action ACHETE_MAINTENANT | opportunité 8.747 | entrée 7.400 | trend 7.550 | rang 7.622
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ZK-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.959 | entrée 6.150 | trend 8.350 | rang 7.645
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : PENDLE-EUR | action LATENT_ACCELERATOR | opportunité 7.720 | entrée 4.500 | trend 8.950 | rang 7.521
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MERL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.370 | entrée 7.000 | trend 9.200 | rang 8.569
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.569
2. ALGO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.215
3. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.129

## Accélération indépendante

- LAPTOP-EUR — CONFIRMED_ACCELERATION — score 7.903/10 — DETECTED_BUT_TOO_LATE
- KAITO-EUR — CONFIRMED_ACCELERATION — score 7.355/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARX-EUR — BUILDING_ACCELERATION — score 6.275/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BAND-EUR — BUILDING_ACCELERATION — score 6.091/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- U-EUR — BUILDING_ACCELERATION — score 5.712/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TNSR-EUR — BUILDING_ACCELERATION — score 5.117/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LIGHTER-EUR — BUILDING_ACCELERATION — score 4.990/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NPC-EUR — BUILDING_ACCELERATION — score 4.924/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PEPE-EUR — ACTIVE_NOW — score mémoire 7.622/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ONDO-EUR — ACTIVE_NOW — score mémoire 7.453/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- TAO-EUR — ACTIVE_NOW — score mémoire 7.415/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- EDGE-EUR — MEMORY_24H — score mémoire 9.925/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 9.488/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RLC-EUR — MEMORY_24H — score mémoire 9.465/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMX-EUR — MEMORY_24H — score mémoire 9.317/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PHA-EUR — MEMORY_24H — score mémoire 9.074/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NOS-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MOCA-EUR — MEMORY_24H — score mémoire 8.589/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZETA-EUR +71.71% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PHA-EUR +62.42% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PTB-EUR +33.29% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NIL-EUR +31.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +29.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SEI-EUR +28.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +27.85% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PEAQ-EUR +24.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUI-EUR +24.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHIP-EUR +22.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
