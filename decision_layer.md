# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T11:39:16.637783+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ONDO-EUR | action ACHETE_MAINTENANT | opportunité 9.218 | entrée 8.150 | trend 8.150 | rang 8.095
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : WAL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.592 | entrée 6.700 | trend 8.950 | rang 8.075
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ZK-EUR | action LATENT_ACCELERATOR | opportunité 8.693 | entrée 5.700 | trend 8.350 | rang 7.929
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MERL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.479 | entrée 7.000 | trend 9.200 | rang 8.620
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.620
2. ONDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.095
3. WAL-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 8.075

## Accélération indépendante

- LAPTOP-EUR — CONFIRMED_ACCELERATION — score 9.710/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GIGA-EUR — CONFIRMED_ACCELERATION — score 8.044/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LUMIA-EUR — CONFIRMED_ACCELERATION — score 7.811/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HNT-EUR — CONFIRMED_ACCELERATION — score 7.378/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SYN-EUR — BUILDING_ACCELERATION — score 6.448/10 — DETECTED_BUT_TOO_LATE
- TNSR-EUR — BUILDING_ACCELERATION — score 6.423/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LSK-EUR — BUILDING_ACCELERATION — score 6.342/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MTL-EUR — BUILDING_ACCELERATION — score 6.148/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VERONA-EUR — BUILDING_ACCELERATION — score 5.841/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HUMA-EUR — BUILDING_ACCELERATION — score 5.811/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ONDO-EUR — ACTIVE_NOW — score mémoire 8.095/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- EDGE-EUR — MEMORY_24H — score mémoire 9.925/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LAPTOP-EUR — ACTIVE_NOW — score mémoire 9.710/10 — sources ACCELERATION, V4 — WATCH_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 9.488/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RLC-EUR — MEMORY_24H — score mémoire 9.465/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMX-EUR — MEMORY_24H — score mémoire 9.317/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PHA-EUR — MEMORY_24H — score mémoire 9.074/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NOS-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MERL-EUR — ACTIVE_NOW — score mémoire 8.620/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MOCA-EUR — MEMORY_24H — score mémoire 8.589/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZETA-EUR +70.42% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PHA-EUR +62.51% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PTB-EUR +48.49% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FTT-EUR +32.64% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- KMNO-EUR +30.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +30.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SEI-EUR +28.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUI-EUR +25.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEAQ-EUR +23.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CETUS-EUR +22.98% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
