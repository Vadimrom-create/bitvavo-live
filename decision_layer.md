# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T08:26:12.636796+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ONDO-EUR | action ACHETE_MAINTENANT | opportunité 8.377 | entrée 7.450 | trend 8.750 | rang 8.093
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : MEGA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.935 | entrée 6.550 | trend 7.450 | rang 7.767
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : W-EUR | action LATENT_ACCELERATOR | opportunité 7.550 | entrée 4.500 | trend 8.750 | rang 7.357
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MERL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.271 | entrée 5.850 | trend 8.900 | rang 8.283
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.283
2. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.185
3. ONDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.093

## Accélération indépendante

- CPOOL-EUR — CONFIRMED_ACCELERATION — score 8.502/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — CONFIRMED_ACCELERATION — score 8.457/10 — DETECTED_BUT_TOO_LATE
- DEEP-EUR — CONFIRMED_ACCELERATION — score 8.051/10 — DETECTED_BUT_TOO_LATE
- BONK-EUR — CONFIRMED_ACCELERATION — score 7.534/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FLOCK-EUR — CONFIRMED_ACCELERATION — score 7.500/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LUMIA-EUR — BUILDING_ACCELERATION — score 6.274/10 — DETECTED_BUT_TOO_LATE
- XVG-EUR — BUILDING_ACCELERATION — score 6.132/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AXL-EUR — BUILDING_ACCELERATION — score 6.116/10 — DETECTED_BUT_TOO_LATE
- ZETA-EUR — BUILDING_ACCELERATION — score 5.846/10 — DETECTED_BUT_TOO_LATE
- GTC-EUR — BUILDING_ACCELERATION — score 5.793/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CTC-EUR — MEMORY_24H — score mémoire 9.245/10 — sources ACCELERATION — MEMORY_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 9.049/10 — sources ACCELERATION — MEMORY_ONLY
- BOME-EUR — MEMORY_24H — score mémoire 8.655/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CPOOL-EUR — ACTIVE_NOW — score mémoire 8.502/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — ACTIVE_NOW — score mémoire 8.457/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- BLUR-EUR — MEMORY_24H — score mémoire 8.302/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MERL-EUR — ACTIVE_NOW — score mémoire 8.283/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TAO-EUR — ACTIVE_NOW — score mémoire 8.185/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ONDO-EUR — ACTIVE_NOW — score mémoire 8.093/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZETA-EUR +71.76% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PTB-EUR +59.02% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FTT-EUR +37.20% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NIL-EUR +36.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +34.92% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +27.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +24.63% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- VVV-EUR +24.63% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NEAR-EUR +23.55% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PHA-EUR +20.36% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
