# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T21:04:36.842945+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ONDO-EUR | action ACHETE_MAINTENANT | opportunité 9.273 | entrée 8.400 | trend 8.100 | rang 8.265
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : GOAT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.948 | entrée 6.700 | trend 7.500 | rang 7.797
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : IMX-EUR | action LATENT_ACCELERATOR | opportunité 7.424 | entrée 4.500 | trend 8.450 | rang 7.165
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : RENDER-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.261 | entrée 8.200 | trend 8.100 | rang 8.052
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ONDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.265
2. RENDER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.052
3. SOL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.906

## Accélération indépendante

- ICX-EUR — BUILDING_ACCELERATION — score 5.729/10 — DETECTED_BUT_TOO_LATE
- CATI-EUR — BUILDING_ACCELERATION — score 5.243/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EDGE-EUR — BUILDING_ACCELERATION — score 5.059/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PONKE-EUR — BUILDING_ACCELERATION — score 4.952/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ONDO-EUR — ACTIVE_NOW — score mémoire 8.265/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- STX-EUR — ACTIVE_NOW — score mémoire 7.753/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- RON-EUR — MEMORY_24H — score mémoire 9.938/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 9.738/10 — sources ACCELERATION — MEMORY_ONLY
- ZKJ-EUR — MEMORY_24H — score mémoire 9.182/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 9.135/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- THQ-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 8.767/10 — sources ACCELERATION — MEMORY_ONLY
- LUMIA-EUR — MEMORY_24H — score mémoire 8.655/10 — sources ACCELERATION — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZRC-EUR +126.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICX-EUR +108.89% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZETA-EUR +54.48% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- FORM-EUR +41.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +39.74% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PHA-EUR +36.45% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PTB-EUR +34.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +25.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +25.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEPE-EUR +23.93% — DETECTED_EARLY — couche NONE — action NONE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
