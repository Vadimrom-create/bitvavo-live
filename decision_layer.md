# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T01:54:07.431739+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ADA-EUR | action ACHETE_MAINTENANT | opportunité 9.422 | entrée 7.900 | trend 8.750 | rang 8.547
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ZK-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.297 | entrée 5.950 | trend 9.200 | rang 7.988
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : CETUS-EUR | action LATENT_ACCELERATOR | opportunité 8.036 | entrée 5.650 | trend 9.000 | rang 7.785
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : JUP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.472 | entrée 6.700 | trend 8.950 | rang 8.021
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ADA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.547
2. KAS-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.200
3. DOT-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.167

## Accélération indépendante

- FUEL-EUR — CONFIRMED_ACCELERATION — score 7.694/10 — DETECTED_BUT_TOO_LATE
- BIGTIME-EUR — CONFIRMED_ACCELERATION — score 7.421/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ADA-EUR — CONFIRMED_ACCELERATION — score 7.132/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WAXP-EUR — BUILDING_ACCELERATION — score 6.000/10 — DETECTED_BUT_TOO_LATE
- CAP-EUR — BUILDING_ACCELERATION — score 5.868/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ACU-EUR — BUILDING_ACCELERATION — score 5.813/10 — DETECTED_BUT_TOO_LATE
- FOLD-EUR — BUILDING_ACCELERATION — score 5.650/10 — DETECTED_BUT_TOO_LATE
- ZAMA-EUR — BUILDING_ACCELERATION — score 5.509/10 — DETECTED_BUT_TOO_LATE
- AVAX-EUR — BUILDING_ACCELERATION — score 5.160/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LDO-EUR — BUILDING_ACCELERATION — score 5.067/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.694/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ADA-EUR — ACTIVE_NOW — score mémoire 8.547/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.200/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- DOT-EUR — ACTIVE_NOW — score mémoire 8.167/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.111/10 — sources ACCELERATION — MEMORY_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 8.103/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.103/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- POND-EUR +75.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PHA-EUR +68.47% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ARK-EUR +33.00% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +32.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- WMTX-EUR +30.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SEI-EUR +22.00% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AERO-EUR +20.99% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ENA-EUR +17.48% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WAXP-EUR +16.76% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CC-EUR +16.75% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
