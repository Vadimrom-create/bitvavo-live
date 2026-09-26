# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T06:01:50.006350+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : QNT-EUR | action ACHETE_MAINTENANT | opportunité 9.166 | entrée 7.450 | trend 7.950 | rang 8.027
  - V4 buy-ready with acceptable current entry; no structural veto. High extension/chase is retained as risk context, not an automatic veto.
- **MEILLEURE_LIMITE_PASSIVE** : ZK-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.116 | entrée 6.150 | trend 8.950 | rang 7.836
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : DUSK-EUR | action LATENT_ACCELERATOR | opportunité 8.846 | entrée 5.550 | trend 8.450 | rang 7.997
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LTC-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.317 | entrée 7.150 | trend 8.900 | rang 8.128
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LTC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.128
2. RENDER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.090
3. QNT-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.027

## Accélération indépendante

- ARK-EUR — CONFIRMED_ACCELERATION — score 9.992/10 — DETECTED_BUT_TOO_LATE
- RARE-EUR — CONFIRMED_ACCELERATION — score 8.201/10 — DETECTED_BUT_TOO_LATE
- U-EUR — CONFIRMED_ACCELERATION — score 7.226/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POND-EUR — BUILDING_ACCELERATION — score 6.109/10 — DETECTED_BUT_TOO_LATE
- NOS-EUR — BUILDING_ACCELERATION — score 5.975/10 — DETECTED_BUT_TOO_LATE
- EDGE-EUR — BUILDING_ACCELERATION — score 5.258/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ARK-EUR — ACTIVE_NOW — score mémoire 9.992/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.896/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.694/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 8.207/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RARE-EUR — ACTIVE_NOW — score mémoire 8.201/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LTC-EUR — ACTIVE_NOW — score mémoire 8.128/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.111/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- POND-EUR +116.27% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PHA-EUR +62.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +38.86% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AERO-EUR +24.93% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +22.51% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +21.27% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +19.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +16.58% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CPOOL-EUR +16.37% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SEI-EUR +16.05% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
