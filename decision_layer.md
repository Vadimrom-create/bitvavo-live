# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T03:58:38.971509+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : OP-EUR | action ACHETE_MAINTENANT | opportunité 8.251 | entrée 7.100 | trend 7.550 | rang 7.558
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : COMP-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.613 | entrée 6.700 | trend 7.850 | rang 7.178
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ZK-EUR | action LATENT_ACCELERATOR | opportunité 8.924 | entrée 5.750 | trend 8.200 | rang 7.741
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MERL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.409 | entrée 6.800 | trend 8.900 | rang 8.472
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.472
2. KAS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.041
3. STX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.971

## Accélération indépendante

- ZETA-EUR — CONFIRMED_ACCELERATION — score 9.757/10 — DETECTED_BUT_TOO_LATE
- GMT-EUR — CONFIRMED_ACCELERATION — score 8.028/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARB-EUR — CONFIRMED_ACCELERATION — score 7.413/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRIA-EUR — CONFIRMED_ACCELERATION — score 6.884/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IO-EUR — CONFIRMED_ACCELERATION — score 6.738/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ENJ-EUR — BUILDING_ACCELERATION — score 6.434/10 — DETECTED_BUT_TOO_LATE
- YGG-EUR — BUILDING_ACCELERATION — score 5.863/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LPT-EUR — BUILDING_ACCELERATION — score 5.154/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CRO-EUR — BUILDING_ACCELERATION — score 4.989/10 — DETECTED_BUT_TOO_LATE
- WOO-EUR — BUILDING_ACCELERATION — score 4.984/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- OP-EUR — ACTIVE_NOW — score mémoire 7.558/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- FTT-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZETA-EUR — ACTIVE_NOW — score mémoire 9.757/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- ICX-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.883/10 — sources ACCELERATION — MEMORY_ONLY
- BOME-EUR — MEMORY_24H — score mémoire 8.655/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- USELESS-EUR — MEMORY_24H — score mémoire 8.481/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MERL-EUR — ACTIVE_NOW — score mémoire 8.472/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.376/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- PTB-EUR +97.67% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZETA-EUR +48.08% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- FTT-EUR +41.65% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +30.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +25.01% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +21.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VVV-EUR +21.20% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +20.81% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +20.23% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +20.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
