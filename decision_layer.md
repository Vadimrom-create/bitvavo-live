# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T14:56:37.641739+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : STX-EUR | action ACHETE_MAINTENANT | opportunité 9.361 | entrée 7.550 | trend 8.600 | rang 8.413
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ROSE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.824 | entrée 5.950 | trend 8.200 | rang 7.427
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : COW-EUR | action LATENT_ACCELERATOR | opportunité 7.998 | entrée 5.100 | trend 9.200 | rang 7.836
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : GRASS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.901 | entrée 6.850 | trend 8.450 | rang 8.137
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. STX-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.413
2. GRASS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.137
3. KAS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.038

## Accélération indépendante

- SUPER-EUR — CONFIRMED_ACCELERATION — score 9.700/10 — DETECTED_BUT_TOO_LATE
- PEPE-EUR — CONFIRMED_ACCELERATION — score 8.977/10 — DETECTED_BUT_TOO_LATE
- FLOKI-EUR — CONFIRMED_ACCELERATION — score 7.508/10 — DETECTED_BUT_TOO_LATE
- CTR-EUR — CONFIRMED_ACCELERATION — score 6.998/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POND-EUR — CONFIRMED_ACCELERATION — score 6.777/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EDGE-EUR — BUILDING_ACCELERATION — score 6.271/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- REQ-EUR — BUILDING_ACCELERATION — score 5.792/10 — DETECTED_BUT_TOO_LATE
- ZBCN-EUR — BUILDING_ACCELERATION — score 5.578/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ROBO-EUR — BUILDING_ACCELERATION — score 5.017/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- VET-EUR — ACTIVE_NOW — score mémoire 7.751/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- SUPER-EUR — ACTIVE_NOW — score mémoire 9.700/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- TAI-EUR — MEMORY_24H — score mémoire 9.488/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACU-EUR — MEMORY_24H — score mémoire 9.053/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEPE-EUR — ACTIVE_NOW — score mémoire 8.977/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ARB-EUR — MEMORY_24H — score mémoire 8.746/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LQTY-EUR — MEMORY_24H — score mémoire 8.646/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 8.457/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZETA-EUR +66.23% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PHA-EUR +50.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PTB-EUR +34.59% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AIOZ-EUR +32.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FTT-EUR +30.28% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NIL-EUR +30.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +29.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SEI-EUR +26.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUI-EUR +26.16% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PROVE-EUR +24.45% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
