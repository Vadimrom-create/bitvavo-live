# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T23:18:40.533513+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 8.495 | entrée 6.950 | trend 9.000 | rang 8.148
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : FIL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.698 | entrée 6.650 | trend 7.400 | rang 7.537
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : KMNO-EUR | action LATENT_ACCELERATOR | opportunité 8.170 | entrée 5.700 | trend 8.550 | rang 7.520
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : FLUX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.331 | entrée 6.250 | trend 8.850 | rang 7.900
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LTC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.148
2. FLUX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.900
3. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.846

## Accélération indépendante

- ZRC-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NIL-EUR — CONFIRMED_ACCELERATION — score 9.100/10 — DETECTED_BUT_TOO_LATE
- XMN-EUR — CONFIRMED_ACCELERATION — score 7.340/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- QKC-EUR — CONFIRMED_ACCELERATION — score 6.856/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- COTI-EUR — BUILDING_ACCELERATION — score 5.464/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VVV-EUR — BUILDING_ACCELERATION — score 5.233/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- AMP-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, V4 — WATCH_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 9.545/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NIL-EUR — ACTIVE_NOW — score mémoire 9.100/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LTC-EUR — ACTIVE_NOW — score mémoire 8.148/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZBCN-EUR — MEMORY_24H — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FLUX-EUR — ACTIVE_NOW — score mémoire 7.900/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- VET-EUR — ACTIVE_NOW — score mémoire 7.846/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- NIL-EUR +58.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CPOOL-EUR +24.26% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DBR-EUR +20.83% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- SAGA-EUR +19.20% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOM-EUR +15.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CAP-EUR +12.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RAY-EUR +10.55% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +9.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOSO-EUR +9.47% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- ZRO-EUR +7.80% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
