# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T11:21:15.861449+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : STX-EUR | action ACHETE_MAINTENANT | opportunité 7.941 | entrée 6.800 | trend 8.600 | rang 7.658
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ROSE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.891 | entrée 6.050 | trend 8.500 | rang 7.527
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ACH-EUR | action LATENT_ACCELERATOR | opportunité 8.134 | entrée 5.200 | trend 9.000 | rang 7.714
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MERL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.844 | entrée 6.100 | trend 9.200 | rang 8.212
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.212
2. KSM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.113
3. COW-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.003

## Accélération indépendante

- AIOZ-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TREAD-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- CETUS-EUR — CONFIRMED_ACCELERATION — score 7.960/10 — DETECTED_BUT_TOO_LATE
- FET-EUR — CONFIRMED_ACCELERATION — score 7.846/10 — DETECTED_BUT_TOO_LATE
- XMN-EUR — CONFIRMED_ACCELERATION — score 7.298/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LAPTOP-EUR — CONFIRMED_ACCELERATION — score 7.018/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MON-EUR — CONFIRMED_ACCELERATION — score 6.666/10 — DETECTED_BUT_TOO_LATE
- MAVIA-EUR — BUILDING_ACCELERATION — score 6.240/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HUMA-EUR — BUILDING_ACCELERATION — score 5.983/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XPL-EUR — BUILDING_ACCELERATION — score 5.837/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AIOZ-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- EDGE-EUR — MEMORY_24H — score mémoire 9.925/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 9.488/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RLC-EUR — MEMORY_24H — score mémoire 9.465/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMX-EUR — MEMORY_24H — score mémoire 9.317/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PHA-EUR — MEMORY_24H — score mémoire 9.074/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NOS-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SEI-EUR — MEMORY_24H — score mémoire 8.603/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOCA-EUR — MEMORY_24H — score mémoire 8.589/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TREAD-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- PHA-EUR +75.03% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZETA-EUR +70.20% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PTB-EUR +57.23% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SEI-EUR +34.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +32.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +30.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +27.14% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PEAQ-EUR +25.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUI-EUR +25.11% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EPIC-EUR +22.65% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
