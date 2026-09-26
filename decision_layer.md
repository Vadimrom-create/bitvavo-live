# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T09:49:02.680201+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AXS-EUR | action ACHETE_MAINTENANT | opportunité 9.452 | entrée 7.800 | trend 9.000 | rang 8.666
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ROSE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.493 | entrée 6.150 | trend 8.950 | rang 8.079
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : IOST-EUR | action LATENT_ACCELERATOR | opportunité 9.200 | entrée 4.800 | trend 8.400 | rang 8.043
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : C-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.186 | entrée 6.900 | trend 8.650 | rang 8.263
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. AXS-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.666
2. C-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.263
3. LTC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.115

## Accélération indépendante

- ZRC-EUR — CONFIRMED_ACCELERATION — score 9.830/10 — DETECTED_BUT_TOO_LATE
- POND-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- IMU-EUR — CONFIRMED_ACCELERATION — score 8.394/10 — DETECTED_BUT_TOO_LATE
- SAGA-EUR — BUILDING_ACCELERATION — score 5.120/10 — DETECTED_BUT_TOO_LATE
- PROM-EUR — BUILDING_ACCELERATION — score 5.028/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SAPIEN-EUR — BUILDING_ACCELERATION — score 4.894/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- XPL-EUR — ACTIVE_NOW — score mémoire 7.594/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ZRC-EUR — ACTIVE_NOW — score mémoire 9.830/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 9.063/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AXS-EUR — ACTIVE_NOW — score mémoire 8.666/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ACT-EUR — MEMORY_24H — score mémoire 8.555/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- POND-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- IMU-EUR — ACTIVE_NOW — score mémoire 8.394/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- POND-EUR +163.73% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +66.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 2Z-EUR +40.85% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARK-EUR +32.32% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PHA-EUR +29.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +22.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AERO-EUR +17.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +16.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PROM-EUR +15.93% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- TNSR-EUR +15.05% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
