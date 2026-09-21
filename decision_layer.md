# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T16:40:45.317278+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : STX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.646 | entrée 6.500 | trend 8.600 | rang 7.625
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : W-EUR | action LATENT_ACCELERATOR | opportunité 7.431 | entrée 5.300 | trend 8.750 | rang 7.436
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MERL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.095 | entrée 6.700 | trend 8.950 | rang 7.922
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.922
2. KAS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.901
3. COW-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.631

## Accélération indépendante

- ALLO-EUR — CONFIRMED_ACCELERATION — score 9.122/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — CONFIRMED_ACCELERATION — score 8.634/10 — DETECTED_BUT_TOO_LATE
- CNPY-EUR — CONFIRMED_ACCELERATION — score 7.984/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SYN-EUR — CONFIRMED_ACCELERATION — score 6.624/10 — DETECTED_BUT_TOO_LATE
- ZKJ-EUR — BUILDING_ACCELERATION — score 5.543/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LISTA-EUR — BUILDING_ACCELERATION — score 4.800/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SAGA-EUR — BUILDING_ACCELERATION — score 4.783/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- FORM-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RON-EUR — MEMORY_24H — score mémoire 9.938/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CPOOL-EUR — MEMORY_24H — score mémoire 9.834/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.639/10 — sources ACCELERATION — MEMORY_ONLY
- PEPE-EUR — MEMORY_24H — score mémoire 9.525/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ALLO-EUR — ACTIVE_NOW — score mémoire 9.122/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- THQ-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACU-EUR — MEMORY_24H — score mémoire 9.053/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LUMIA-EUR — MEMORY_24H — score mémoire 8.655/10 — sources ACCELERATION — MEMORY_ONLY
- ICX-EUR — ACTIVE_NOW — score mémoire 8.634/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- ZRC-EUR +306.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICX-EUR +267.78% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZETA-EUR +55.78% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PHA-EUR +38.31% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FORM-EUR +37.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SWELL-EUR +28.97% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PTB-EUR +24.69% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +24.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +24.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +23.10% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
