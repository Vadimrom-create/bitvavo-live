# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T13:36:27.730298+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ONDO-EUR | action ACHETE_MAINTENANT | opportunité 9.259 | entrée 7.800 | trend 8.300 | rang 8.374
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : BIGTIME-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.044 | entrée 6.000 | trend 8.900 | rang 7.734
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BRETT-EUR | action LATENT_ACCELERATOR | opportunité 7.957 | entrée 5.450 | trend 9.000 | rang 7.794
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : CFG-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.872 | entrée 6.600 | trend 8.950 | rang 8.335
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ONDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.374
2. CFG-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.335
3. ENJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.308

## Accélération indépendante

- SOON-EUR — CONFIRMED_ACCELERATION — score 8.344/10 — DETECTED_BUT_TOO_LATE
- WMTX-EUR — CONFIRMED_ACCELERATION — score 7.680/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- W-EUR — CONFIRMED_ACCELERATION — score 7.602/10 — DETECTED_BUT_TOO_LATE
- GRASS-EUR — CONFIRMED_ACCELERATION — score 6.651/10 — DETECTED_BUT_TOO_LATE
- ARX-EUR — CONFIRMED_ACCELERATION — score 6.512/10 — DETECTED_BUT_TOO_LATE
- BRETT-EUR — BUILDING_ACCELERATION — score 6.476/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PENGU-EUR — BUILDING_ACCELERATION — score 5.854/10 — DETECTED_BUT_TOO_LATE
- USELESS-EUR — BUILDING_ACCELERATION — score 5.745/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- COW-EUR — BUILDING_ACCELERATION — score 5.633/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PEPE-EUR — BUILDING_ACCELERATION — score 5.547/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- AUDIO-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 9.365/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MMT-EUR — MEMORY_24H — score mémoire 9.122/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- EDGE-EUR — MEMORY_24H — score mémoire 8.936/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GROVE-EUR — MEMORY_24H — score mémoire 8.518/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ONDO-EUR — ACTIVE_NOW — score mémoire 8.374/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOON-EUR — ACTIVE_NOW — score mémoire 8.344/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CFG-EUR — ACTIVE_NOW — score mémoire 8.335/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ENJ-EUR — ACTIVE_NOW — score mémoire 8.308/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +54.50% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +54.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GLMR-EUR +46.42% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- AUDIO-EUR +38.77% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +33.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +21.68% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- W-EUR +18.29% — DETECTED_EARLY — couche NONE — action NONE
- WLD-EUR +17.92% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INX-EUR +17.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARX-EUR +17.67% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
