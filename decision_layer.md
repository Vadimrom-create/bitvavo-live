# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T14:06:11.579265+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 8.485 | entrée 7.200 | trend 9.000 | rang 8.197
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AXS-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.032 | entrée 6.100 | trend 8.700 | rang 7.795
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ROSE-EUR | action LATENT_ACCELERATOR | opportunité 8.268 | entrée 5.200 | trend 8.600 | rang 7.723
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ZEN-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.087 | entrée 6.400 | trend 8.650 | rang 8.230
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ZEN-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.230
2. ZBT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.200
3. LTC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.197

## Accélération indépendante

- ACU-EUR — CONFIRMED_ACCELERATION — score 8.063/10 — DETECTED_BUT_TOO_LATE
- ACE-EUR — CONFIRMED_ACCELERATION — score 7.690/10 — DETECTED_BUT_TOO_LATE
- ARX-EUR — BUILDING_ACCELERATION — score 6.363/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PONKE-EUR — BUILDING_ACCELERATION — score 6.353/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SKY-EUR — BUILDING_ACCELERATION — score 6.094/10 — DETECTED_BUT_TOO_LATE
- LIGHTER-EUR — BUILDING_ACCELERATION — score 5.431/10 — DETECTED_BUT_TOO_LATE
- SUPER-EUR — BUILDING_ACCELERATION — score 5.395/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ICP-EUR — ACTIVE_NOW — score mémoire 8.054/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- TRIA-EUR — MEMORY_24H — score mémoire 9.219/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 9.216/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SAGA-EUR — MEMORY_24H — score mémoire 9.208/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CPOOL-EUR — MEMORY_24H — score mémoire 8.705/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MIRA-EUR — ACTIVE_NOW — score mémoire 8.471/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.290/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZEN-EUR — ACTIVE_NOW — score mémoire 8.230/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZBT-EUR — ACTIVE_NOW — score mémoire 8.200/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 8.197/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CPOOL-EUR +39.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ALLO-EUR +36.38% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MET-EUR +30.83% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SAGA-EUR +24.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SENT-EUR +22.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUPER-EUR +21.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ACE-EUR +20.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +18.88% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DBR-EUR +18.20% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- LIGHTER-EUR +16.55% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
