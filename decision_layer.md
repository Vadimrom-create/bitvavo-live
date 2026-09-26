# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T05:34:37.623667+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : VET-EUR | action ACHETE_MAINTENANT | opportunité 9.104 | entrée 7.450 | trend 8.150 | rang 8.062
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : RPL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.642 | entrée 6.100 | trend 9.000 | rang 8.049
  - Strong structure but imperfect current entry; prefer passive execution. High extension/chase reduces rank but does not erase the setup.
- **MEILLEUR_LATENT_ACCELERATOR** : ALGO-EUR | action LATENT_ACCELERATOR | opportunité 8.496 | entrée 5.600 | trend 9.000 | rang 8.060
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HBAR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.895 | entrée 6.550 | trend 8.450 | rang 8.160
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HBAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.160
2. LTC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.131
3. VET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.062

## Accélération indépendante

- IO-EUR — CONFIRMED_ACCELERATION — score 9.043/10 — DETECTED_BUT_TOO_LATE
- 2Z-EUR — CONFIRMED_ACCELERATION — score 7.249/10 — DETECTED_BUT_TOO_LATE
- WMTX-EUR — CONFIRMED_ACCELERATION — score 6.918/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- REZ-EUR — BUILDING_ACCELERATION — score 5.989/10 — DETECTED_BUT_TOO_LATE
- ZEUS-EUR — BUILDING_ACCELERATION — score 5.971/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ATH-EUR — BUILDING_ACCELERATION — score 5.664/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZIG-EUR — BUILDING_ACCELERATION — score 5.025/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- VET-EUR — ACTIVE_NOW — score mémoire 8.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IO-EUR — ACTIVE_NOW — score mémoire 9.043/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- XMN-EUR — MEMORY_24H — score mémoire 8.896/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.694/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 8.207/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HBAR-EUR — ACTIVE_NOW — score mémoire 8.160/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 8.131/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- POND-EUR +114.97% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PHA-EUR +65.82% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ARK-EUR +32.17% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AERO-EUR +25.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ENA-EUR +23.15% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WMTX-EUR +18.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SEI-EUR +17.81% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +17.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +16.10% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +16.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
