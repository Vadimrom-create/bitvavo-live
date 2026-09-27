# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T12:46:59.028959+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAO-EUR | action ACHETE_MAINTENANT | opportunité 9.388 | entrée 7.800 | trend 8.600 | rang 8.512
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : BRETT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.875 | entrée 5.900 | trend 9.000 | rang 7.811
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ROSE-EUR | action LATENT_ACCELERATOR | opportunité 8.112 | entrée 5.150 | trend 8.950 | rang 7.800
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : EIGEN-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.361 | entrée 7.250 | trend 8.950 | rang 8.549
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. EIGEN-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.549
2. TAO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.512
3. CHZ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.428

## Accélération indépendante

- JASMY-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- RAD-EUR — CONFIRMED_ACCELERATION — score 8.910/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AUDIO-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — CONFIRMED_ACCELERATION — score 7.669/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LRC-EUR — CONFIRMED_ACCELERATION — score 7.661/10 — DETECTED_BUT_TOO_LATE
- XVG-EUR — CONFIRMED_ACCELERATION — score 7.342/10 — DETECTED_BUT_TOO_LATE
- PENGU-EUR — CONFIRMED_ACCELERATION — score 6.671/10 — DETECTED_BUT_TOO_LATE
- WIN-EUR — BUILDING_ACCELERATION — score 5.217/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAI-EUR — BUILDING_ACCELERATION — score 5.136/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PUMP-EUR — BUILDING_ACCELERATION — score 5.005/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- JASMY-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- XMN-EUR — MEMORY_24H — score mémoire 9.365/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MMT-EUR — MEMORY_24H — score mémoire 9.122/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RAD-EUR — ACTIVE_NOW — score mémoire 8.910/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- EIGEN-EUR — ACTIVE_NOW — score mémoire 8.549/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GROVE-EUR — MEMORY_24H — score mémoire 8.518/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TAO-EUR — ACTIVE_NOW — score mémoire 8.512/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AUDIO-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CHZ-EUR — ACTIVE_NOW — score mémoire 8.428/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +56.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +46.61% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- TREAD-EUR +40.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOON-EUR +31.07% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AUDIO-EUR +27.26% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- WLD-EUR +20.21% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +19.75% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +17.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HFT-EUR +16.92% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- EDGE-EUR +16.51% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
