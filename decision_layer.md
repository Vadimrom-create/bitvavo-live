# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T06:18:26.214160+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : VET-EUR | action ACHETE_MAINTENANT | opportunité 8.847 | entrée 7.250 | trend 7.900 | rang 7.814
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : 0G-EUR | action LATENT_ACCELERATOR | opportunité 7.633 | entrée 4.500 | trend 8.300 | rang 7.070
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : COMP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.095 | entrée 6.900 | trend 8.500 | rang 7.846
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. COMP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.846
2. PLUME-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.844
3. VET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.814

## Accélération indépendante

- LSK-EUR — CONFIRMED_ACCELERATION — score 8.176/10 — DETECTED_BUT_TOO_LATE
- SAGA-EUR — CONFIRMED_ACCELERATION — score 7.066/10 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — CONFIRMED_ACCELERATION — score 6.877/10 — DETECTED_BUT_TOO_LATE
- BOME-EUR — CONFIRMED_ACCELERATION — score 6.815/10 — DETECTED_BUT_TOO_LATE
- INIT-EUR — BUILDING_ACCELERATION — score 6.268/10 — DETECTED_BUT_TOO_LATE
- NOM-EUR — BUILDING_ACCELERATION — score 6.000/10 — DETECTED_BUT_TOO_LATE
- XAI-EUR — BUILDING_ACCELERATION — score 5.822/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TOWNS-EUR — BUILDING_ACCELERATION — score 5.346/10 — DETECTED_BUT_TOO_LATE
- ACE-EUR — BUILDING_ACCELERATION — score 4.789/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- TRIA-EUR — MEMORY_24H — score mémoire 9.929/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 8.917/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VTHO-EUR — MEMORY_24H — score mémoire 8.660/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TRAC-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- C98-EUR — MEMORY_24H — score mémoire 8.347/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 8.307/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- EGLD-EUR — MEMORY_24H — score mémoire 8.216/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LSK-EUR — ACTIVE_NOW — score mémoire 8.176/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ZBCN-EUR — MEMORY_24H — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- NOM-EUR +57.85% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +21.79% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RAY-EUR +16.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IMU-EUR +15.77% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOSO-EUR +11.50% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- DBR-EUR +11.30% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- VTHO-EUR +11.02% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +9.84% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BOME-EUR +8.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ACU-EUR +7.97% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
