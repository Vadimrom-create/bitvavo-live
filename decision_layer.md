# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T14:46:38.472775+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : VET-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.238 | entrée 6.050 | trend 8.300 | rang 7.744
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ZORA-EUR | action LATENT_ACCELERATOR | opportunité 9.231 | entrée 5.250 | trend 8.200 | rang 7.960
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ICP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.769 | entrée 5.300 | trend 8.400 | rang 7.934
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ZORA-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.960
2. ICP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.934
3. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.781

## Accélération indépendante

- ZRO-EUR — CONFIRMED_ACCELERATION — score 8.735/10 — DETECTED_BUT_TOO_LATE
- ACU-EUR — CONFIRMED_ACCELERATION — score 8.042/10 — DETECTED_BUT_TOO_LATE
- PARTI-EUR — CONFIRMED_ACCELERATION — score 7.187/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CNPY-EUR — CONFIRMED_ACCELERATION — score 7.054/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TWT-EUR — CONFIRMED_ACCELERATION — score 7.048/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NIL-EUR — CONFIRMED_ACCELERATION — score 6.500/10 — DETECTED_BUT_TOO_LATE
- BEAM-EUR — BUILDING_ACCELERATION — score 6.390/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VVV-EUR — BUILDING_ACCELERATION — score 6.185/10 — DETECTED_BUT_TOO_LATE
- TOSHI-EUR — BUILDING_ACCELERATION — score 6.095/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AEVO-EUR — BUILDING_ACCELERATION — score 6.088/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- TRIA-EUR — MEMORY_24H — score mémoire 9.219/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SAGA-EUR — MEMORY_24H — score mémoire 9.208/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRO-EUR — ACTIVE_NOW — score mémoire 8.735/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CPOOL-EUR — MEMORY_24H — score mémoire 8.705/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.290/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LINK-EUR — MEMORY_24H — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACU-EUR — ACTIVE_NOW — score mémoire 8.042/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- PORTAL-EUR — MEMORY_24H — score mémoire 7.969/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZORA-EUR — ACTIVE_NOW — score mémoire 7.960/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CPOOL-EUR +40.83% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ALLO-EUR +31.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MET-EUR +26.50% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +24.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +23.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ACE-EUR +19.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DBR-EUR +17.79% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- SENT-EUR +17.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUPER-EUR +16.48% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LIGHTER-EUR +16.34% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
