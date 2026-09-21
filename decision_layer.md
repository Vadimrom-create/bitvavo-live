# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T20:49:45.437554+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : W-EUR | action ACHETE_MAINTENANT | opportunité 9.308 | entrée 7.400 | trend 8.450 | rang 8.395
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : BIGTIME-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.358 | entrée 5.800 | trend 8.700 | rang 7.851
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MERL-EUR | action LATENT_ACCELERATOR | opportunité 8.007 | entrée 5.650 | trend 8.900 | rang 7.773
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : RENDER-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.240 | entrée 7.650 | trend 8.100 | rang 8.091
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. W-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.395
2. RENDER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.091
3. ALGO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.033

## Accélération indépendante

- CSPR-EUR — CONFIRMED_ACCELERATION — score 9.135/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SNX-EUR — CONFIRMED_ACCELERATION — score 8.226/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AVA-EUR — CONFIRMED_ACCELERATION — score 7.830/10 — DETECTED_BUT_TOO_LATE
- EDGE-EUR — BUILDING_ACCELERATION — score 6.485/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PTB-EUR — BUILDING_ACCELERATION — score 6.308/10 — DETECTED_BUT_TOO_LATE
- AGI-EUR — BUILDING_ACCELERATION — score 5.902/10 — DETECTED_BUT_TOO_LATE
- HFT-EUR — BUILDING_ACCELERATION — score 5.802/10 — DETECTED_BUT_TOO_LATE
- BOB-EUR — BUILDING_ACCELERATION — score 5.356/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GRASS-EUR — BUILDING_ACCELERATION — score 5.297/10 — DETECTED_BUT_TOO_LATE
- DUSK-EUR — BUILDING_ACCELERATION — score 5.266/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- STX-EUR — ACTIVE_NOW — score mémoire 7.937/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- WLD-EUR — ACTIVE_NOW — score mémoire 6.550/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- RON-EUR — MEMORY_24H — score mémoire 9.938/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 9.738/10 — sources ACCELERATION — MEMORY_ONLY
- ZKJ-EUR — MEMORY_24H — score mémoire 9.182/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CSPR-EUR — ACTIVE_NOW — score mémoire 9.135/10 — sources ACCELERATION, V4 — WATCH_ONLY
- THQ-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 8.767/10 — sources ACCELERATION — MEMORY_ONLY
- LUMIA-EUR — MEMORY_24H — score mémoire 8.655/10 — sources ACCELERATION — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ICX-EUR +119.56% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRC-EUR +117.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZETA-EUR +52.80% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- AIOZ-EUR +41.18% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FORM-EUR +39.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PTB-EUR +36.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +33.49% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SWELL-EUR +23.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +22.97% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEPE-EUR +22.17% — DETECTED_EARLY — couche NONE — action NONE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
