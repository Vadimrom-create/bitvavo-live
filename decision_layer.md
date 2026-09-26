# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T19:17:39.760008+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : PYTH-EUR | action ACHETE_MAINTENANT | opportunité 8.472 | entrée 7.250 | trend 8.850 | rang 8.121
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : WAL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.338 | entrée 6.050 | trend 8.950 | rang 8.024
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SNX-EUR | action LATENT_ACCELERATOR | opportunité 8.446 | entrée 5.300 | trend 9.000 | rang 8.001
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AEVO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.291 | entrée 6.350 | trend 8.750 | rang 8.284
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. AEVO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.284
2. AVNT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.268
3. PYTH-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.121

## Accélération indépendante

- LAPTOP-EUR — CONFIRMED_ACCELERATION — score 8.144/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KAIA-EUR — CONFIRMED_ACCELERATION — score 6.854/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PYTH-EUR — BUILDING_ACCELERATION — score 5.753/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRIA-EUR — BUILDING_ACCELERATION — score 5.476/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MAVIA-EUR — BUILDING_ACCELERATION — score 5.401/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WELL-EUR — BUILDING_ACCELERATION — score 5.394/10 — DETECTED_BUT_TOO_LATE
- MLN-EUR — BUILDING_ACCELERATION — score 5.275/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 9.483/10 — sources ACCELERATION — MEMORY_ONLY
- RAD-EUR — MEMORY_24H — score mémoire 9.291/10 — sources ACCELERATION — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACT-EUR — MEMORY_24H — score mémoire 8.555/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.418/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_DECAY_24_72H — score mémoire 8.302/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AEVO-EUR — ACTIVE_NOW — score mémoire 8.284/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AVNT-EUR — ACTIVE_NOW — score mémoire 8.268/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LAPTOP-EUR — ACTIVE_NOW — score mémoire 8.144/10 — sources ACCELERATION, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- POND-EUR +127.16% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +43.10% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +38.97% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +35.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QNT-EUR +24.16% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +21.17% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- 2Z-EUR +20.05% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- AGI-EUR +18.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KAS-EUR +17.71% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WLD-EUR +15.85% — DETECTED_EARLY — couche NONE — action NONE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
