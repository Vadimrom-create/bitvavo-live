# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T08:35:56.411320+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ONDO-EUR | action ACHETE_MAINTENANT | opportunité 7.446 | entrée 7.400 | trend 7.900 | rang 7.394
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : RENDER-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.571 | entrée 6.400 | trend 7.300 | rang 7.059
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ARK-EUR | action LATENT_ACCELERATOR | opportunité 7.525 | entrée 5.650 | trend 8.200 | rang 7.191
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : TAIKO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.122 | entrée 7.250 | trend 7.900 | rang 7.939
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. TAIKO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.939
2. BAT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.698
3. COMP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.689

## Accélération indépendante

- NOM-EUR — CONFIRMED_ACCELERATION — score 7.309/10 — DETECTED_BUT_TOO_LATE
- SYN-EUR — CONFIRMED_ACCELERATION — score 7.156/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRC-EUR — CONFIRMED_ACCELERATION — score 6.835/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAIKO-EUR — BUILDING_ACCELERATION — score 5.862/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- NIL-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEAQ-EUR — MEMORY_24H — score mémoire 9.627/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PROM-EUR — MEMORY_24H — score mémoire 9.255/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CELR-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 8.917/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VTHO-EUR — MEMORY_24H — score mémoire 8.660/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FLOCK-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- C98-EUR — MEMORY_24H — score mémoire 8.347/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 8.307/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- NOM-EUR +56.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +36.24% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- LSK-EUR +35.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RAY-EUR +14.77% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IMU-EUR +12.83% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CELR-EUR +11.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOSO-EUR +10.04% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- ARX-EUR +9.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CNPY-EUR +9.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +7.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
