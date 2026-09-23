# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T15:56:21.664672+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : MAVIA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.452 | entrée 5.800 | trend 8.350 | rang 7.310
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : RED-EUR | action LATENT_ACCELERATOR | opportunité 7.766 | entrée 5.250 | trend 8.650 | rang 7.556
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : WAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.533 | entrée 5.150 | trend 8.900 | rang 7.527
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. RED-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.556
2. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.527
3. ARPA-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.525

## Accélération indépendante

- U-EUR — CONFIRMED_ACCELERATION — score 9.175/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EDEN-EUR — CONFIRMED_ACCELERATION — score 9.000/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SWELL-EUR — CONFIRMED_ACCELERATION — score 7.150/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ACU-EUR — BUILDING_ACCELERATION — score 5.709/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POND-EUR — BUILDING_ACCELERATION — score 5.542/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ALLO-EUR — BUILDING_ACCELERATION — score 4.787/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- TRIA-EUR — MEMORY_24H — score mémoire 9.219/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- U-EUR — ACTIVE_NOW — score mémoire 9.175/10 — sources ACCELERATION, V4 — WATCH_ONLY
- EDEN-EUR — ACTIVE_NOW — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CPOOL-EUR — MEMORY_24H — score mémoire 8.705/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LINK-EUR — MEMORY_24H — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PORTAL-EUR — MEMORY_24H — score mémoire 7.969/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XRP-EUR — MEMORY_24H — score mémoire 7.855/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AAVE-EUR — MEMORY_24H — score mémoire 7.755/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACE-EUR — MEMORY_24H — score mémoire 7.690/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CPOOL-EUR +35.98% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SAGA-EUR +26.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MET-EUR +23.09% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ALLO-EUR +22.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PROM-EUR +18.14% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- DBR-EUR +17.02% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- NIL-EUR +16.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XMN-EUR +13.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUPER-EUR +13.53% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +12.23% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
