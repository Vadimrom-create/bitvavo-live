# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T19:20:22.110618+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : VET-EUR | action ACHETE_MAINTENANT | opportunité 8.275 | entrée 7.750 | trend 8.400 | rang 7.828
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : MERL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.052 | entrée 6.100 | trend 8.950 | rang 7.898
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : COW-EUR | action LATENT_ACCELERATOR | opportunité 7.885 | entrée 5.550 | trend 8.900 | rang 7.735
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : WAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.106 | entrée 6.250 | trend 9.200 | rang 7.993
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.993
2. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.984
3. MORPHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.976

## Accélération indépendante

- AIOZ-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- SYN-EUR — CONFIRMED_ACCELERATION — score 9.483/10 — DETECTED_BUT_TOO_LATE
- SWELL-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- SAGA-EUR — BUILDING_ACCELERATION — score 6.218/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — BUILDING_ACCELERATION — score 6.188/10 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — BUILDING_ACCELERATION — score 6.059/10 — DETECTED_BUT_TOO_LATE
- PHA-EUR — BUILDING_ACCELERATION — score 5.972/10 — DETECTED_BUT_TOO_LATE
- PROVE-EUR — BUILDING_ACCELERATION — score 5.727/10 — DETECTED_BUT_TOO_LATE
- RAY-EUR — BUILDING_ACCELERATION — score 5.464/10 — DETECTED_BUT_TOO_LATE
- LMWR-EUR — BUILDING_ACCELERATION — score 5.284/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- VET-EUR — ACTIVE_NOW — score mémoire 7.828/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- AIOZ-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- RON-EUR — MEMORY_24H — score mémoire 9.938/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SYN-EUR — ACTIVE_NOW — score mémoire 9.483/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- THQ-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACU-EUR — MEMORY_24H — score mémoire 9.053/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LUMIA-EUR — MEMORY_24H — score mémoire 8.655/10 — sources ACCELERATION — MEMORY_ONLY
- TRAC-EUR — MEMORY_24H — score mémoire 8.588/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZRC-EUR +131.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICX-EUR +72.31% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZETA-EUR +59.25% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PHA-EUR +43.11% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FORM-EUR +36.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +35.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SWELL-EUR +33.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PTB-EUR +32.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +26.73% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEPE-EUR +24.82% — DETECTED_EARLY — couche NONE — action NONE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
