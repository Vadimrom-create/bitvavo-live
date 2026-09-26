# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T18:01:13.144310+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : DATAIP-EUR | action ACHETE_MAINTENANT | opportunité 8.008 | entrée 6.800 | trend 8.200 | rang 7.607
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : RPL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.292 | entrée 5.850 | trend 9.000 | rang 7.979
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ROSE-EUR | action LATENT_ACCELERATOR | opportunité 7.846 | entrée 5.650 | trend 8.950 | rang 7.682
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : FLUX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.221 | entrée 7.250 | trend 8.600 | rang 8.345
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. FLUX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.345
2. AXS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.202
3. ATOM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.127

## Accélération indépendante

- TRAC-EUR — CONFIRMED_ACCELERATION — score 8.482/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GRASS-EUR — CONFIRMED_ACCELERATION — score 7.153/10 — DETECTED_BUT_TOO_LATE
- HEI-EUR — CONFIRMED_ACCELERATION — score 6.658/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WMTX-EUR — BUILDING_ACCELERATION — score 6.448/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- C98-EUR — BUILDING_ACCELERATION — score 6.300/10 — DETECTED_BUT_TOO_LATE
- POND-EUR — BUILDING_ACCELERATION — score 6.219/10 — DETECTED_BUT_TOO_LATE
- EDGE-EUR — BUILDING_ACCELERATION — score 6.094/10 — DETECTED_BUT_TOO_LATE
- IMU-EUR — BUILDING_ACCELERATION — score 5.435/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AMP-EUR — BUILDING_ACCELERATION — score 5.238/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- XMN-EUR — MEMORY_24H — score mémoire 9.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 9.483/10 — sources ACCELERATION — MEMORY_ONLY
- RAD-EUR — MEMORY_24H — score mémoire 9.291/10 — sources ACCELERATION — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACT-EUR — MEMORY_24H — score mémoire 8.555/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_DECAY_24_72H — score mémoire 8.538/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TRAC-EUR — ACTIVE_NOW — score mémoire 8.482/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.418/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FLUX-EUR — ACTIVE_NOW — score mémoire 8.345/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- POND-EUR +105.34% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +51.21% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +43.01% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +41.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QNT-EUR +25.61% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- 2Z-EUR +21.70% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- KAS-EUR +20.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +19.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +19.03% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WLD-EUR +16.09% — DETECTED_EARLY — couche NONE — action NONE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
