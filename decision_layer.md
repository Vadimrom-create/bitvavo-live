# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T20:12:21.548263+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SOL-EUR | action ACHETE_MAINTENANT | opportunité 9.201 | entrée 7.800 | trend 8.200 | rang 8.290
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : WAL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.466 | entrée 6.100 | trend 9.200 | rang 8.142
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MERL-EUR | action LATENT_ACCELERATOR | opportunité 8.049 | entrée 5.300 | trend 8.900 | rang 7.782
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : RENDER-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.130 | entrée 8.200 | trend 8.100 | rang 8.218
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. SOL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.290
2. VET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.257
3. RENDER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.218

## Accélération indépendante

- BTT-EUR — CONFIRMED_ACCELERATION — score 8.990/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GRASS-EUR — CONFIRMED_ACCELERATION — score 8.805/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAO-EUR — CONFIRMED_ACCELERATION — score 8.519/10 — DETECTED_BUT_TOO_LATE
- C-EUR — CONFIRMED_ACCELERATION — score 7.827/10 — DETECTED_BUT_TOO_LATE
- KAS-EUR — CONFIRMED_ACCELERATION — score 7.710/10 — DETECTED_BUT_TOO_LATE
- SOMI-EUR — BUILDING_ACCELERATION — score 6.002/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GRAM-EUR — BUILDING_ACCELERATION — score 5.691/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LISTA-EUR — BUILDING_ACCELERATION — score 5.497/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WLD-EUR — BUILDING_ACCELERATION — score 5.450/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- JTO-EUR — BUILDING_ACCELERATION — score 5.396/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- VET-EUR — ACTIVE_NOW — score mémoire 8.257/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- XLM-EUR — ACTIVE_NOW — score mémoire 7.399/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- RON-EUR — MEMORY_24H — score mémoire 9.938/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PTB-EUR — MEMORY_24H — score mémoire 9.534/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZKJ-EUR — MEMORY_24H — score mémoire 9.182/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- THQ-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BTT-EUR — ACTIVE_NOW — score mémoire 8.990/10 — sources ACCELERATION — WATCH_ONLY
- GRASS-EUR — ACTIVE_NOW — score mémoire 8.805/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LUMIA-EUR — MEMORY_24H — score mémoire 8.655/10 — sources ACCELERATION — MEMORY_ONLY
- TAO-EUR — ACTIVE_NOW — score mémoire 8.519/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- ICX-EUR +112.46% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRC-EUR +112.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZETA-EUR +56.87% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- AIOZ-EUR +39.05% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PHA-EUR +38.06% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FORM-EUR +35.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PTB-EUR +31.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SWELL-EUR +30.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOS-EUR +24.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEPE-EUR +23.99% — DETECTED_EARLY — couche NONE — action NONE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
