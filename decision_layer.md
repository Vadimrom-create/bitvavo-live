# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T09:58:43.997586+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : NPC-EUR | action ACHETE_MAINTENANT | opportunité 8.445 | entrée 7.050 | trend 7.200 | rang 7.228
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ARX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.197 | entrée 5.850 | trend 8.850 | rang 7.672
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : 0G-EUR | action LATENT_ACCELERATOR | opportunité 7.598 | entrée 5.550 | trend 8.600 | rang 7.471
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PROVE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.169 | entrée 6.050 | trend 8.200 | rang 8.040
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. PROVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.040
2. TAIKO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.920
3. INIT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.795

## Accélération indépendante

- FLOCK-EUR — CONFIRMED_ACCELERATION — score 7.086/10 — DETECTED_BUT_TOO_LATE
- BTT-EUR — CONFIRMED_ACCELERATION — score 6.926/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VVV-EUR — BUILDING_ACCELERATION — score 6.372/10 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — BUILDING_ACCELERATION — score 5.960/10 — DETECTED_BUT_TOO_LATE
- CNPY-EUR — BUILDING_ACCELERATION — score 5.858/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZBCN-EUR — BUILDING_ACCELERATION — score 5.408/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NPC-EUR — BUILDING_ACCELERATION — score 5.318/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- NPC-EUR — ACTIVE_NOW — score mémoire 7.228/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- NEAR-EUR — ACTIVE_NOW — score mémoire 7.170/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- SWEAT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 9.015/10 — sources ACCELERATION — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 8.130/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 8.040/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 7.941/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TAIKO-EUR — ACTIVE_NOW — score mémoire 7.920/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- INIT-EUR — ACTIVE_NOW — score mémoire 7.795/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ICX-EUR +103.83% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRC-EUR +98.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +42.11% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +37.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WIF-EUR +22.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +21.30% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CARV-EUR +20.89% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PEPE-EUR +20.19% — DETECTED_EARLY — couche NONE — action NONE
- TREAD-EUR +19.85% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +17.09% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
