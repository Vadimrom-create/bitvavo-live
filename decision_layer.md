# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T22:36:17.922175+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : KAS-EUR | action ACHETE_MAINTENANT | opportunité 8.344 | entrée 6.800 | trend 8.650 | rang 7.856
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : T-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.029 | entrée 6.000 | trend 8.200 | rang 7.516
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : PROVE-EUR | action LATENT_ACCELERATOR | opportunité 7.467 | entrée 4.500 | trend 8.400 | rang 7.223
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : CAKE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.513 | entrée 7.050 | trend 8.950 | rang 8.167
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. CAKE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.167
2. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.113
3. COW-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.004

## Accélération indépendante

- FTT-EUR — CONFIRMED_ACCELERATION — score 8.294/10 — DETECTED_BUT_TOO_LATE
- ENS-EUR — CONFIRMED_ACCELERATION — score 7.872/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- JUP-EUR — BUILDING_ACCELERATION — score 6.362/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DEEP-EUR — BUILDING_ACCELERATION — score 6.315/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LIGHTER-EUR — BUILDING_ACCELERATION — score 5.700/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- REQ-EUR — BUILDING_ACCELERATION — score 5.627/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CHIP-EUR — BUILDING_ACCELERATION — score 5.463/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARB-EUR — BUILDING_ACCELERATION — score 5.018/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- JUP-EUR — ACTIVE_NOW — score mémoire 7.893/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ONDO-EUR — ACTIVE_NOW — score mémoire 7.353/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- SUI-EUR — ACTIVE_NOW — score mémoire 7.179/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ICX-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.883/10 — sources ACCELERATION — MEMORY_ONLY
- NOS-EUR — MEMORY_24H — score mémoire 8.445/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FTT-EUR — ACTIVE_NOW — score mémoire 8.294/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- CAKE-EUR — ACTIVE_NOW — score mémoire 8.167/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- UP-EUR — MEMORY_24H — score mémoire 8.113/10 — sources ACCELERATION — MEMORY_ONLY
- MERL-EUR — ACTIVE_NOW — score mémoire 8.113/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +39.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +33.82% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PTB-EUR +32.49% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NIL-EUR +25.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +21.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +21.26% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +20.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +18.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CFG-EUR +16.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +16.26% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
