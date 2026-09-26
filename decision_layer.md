# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T08:27:14.389490+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 9.385 | entrée 7.800 | trend 8.850 | rang 8.598
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : LDO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.973 | entrée 5.800 | trend 8.950 | rang 8.119
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ROSE-EUR | action LATENT_ACCELERATOR | opportunité 8.196 | entrée 5.750 | trend 8.750 | rang 7.727
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ALICE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.088 | entrée 6.650 | trend 8.350 | rang 8.066
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LTC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.598
2. PYTH-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.138
3. LDO-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 8.119

## Accélération indépendante

- ICX-EUR — CONFIRMED_ACCELERATION — score 9.063/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- REZ-EUR — CONFIRMED_ACCELERATION — score 8.469/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TNSR-EUR — CONFIRMED_ACCELERATION — score 7.248/10 — DETECTED_BUT_TOO_LATE
- POND-EUR — CONFIRMED_ACCELERATION — score 7.172/10 — DETECTED_BUT_TOO_LATE
- SWEAT-EUR — BUILDING_ACCELERATION — score 6.227/10 — DETECTED_BUT_TOO_LATE
- VSN-EUR — BUILDING_ACCELERATION — score 6.086/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- THQ-EUR — BUILDING_ACCELERATION — score 6.012/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- FUEL-EUR — MEMORY_24H — score mémoire 9.607/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — ACTIVE_NOW — score mémoire 9.063/10 — sources ACCELERATION, V4 — WATCH_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.896/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.694/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 8.598/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ACT-EUR — MEMORY_24H — score mémoire 8.555/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- 2Z-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- POND-EUR +122.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +62.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +37.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 2Z-EUR +33.68% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARK-EUR +33.05% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ENA-EUR +23.01% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AERO-EUR +18.93% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +16.37% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- REZ-EUR +16.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CC-EUR +15.47% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
