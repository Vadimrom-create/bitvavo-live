# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T13:51:11.675902+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ICP-EUR | action ACHETE_MAINTENANT | opportunité 8.295 | entrée 7.250 | trend 9.000 | rang 8.107
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ZIG-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.228 | entrée 6.000 | trend 7.950 | rang 7.607
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : KITE-EUR | action LATENT_ACCELERATOR | opportunité 9.148 | entrée 5.600 | trend 8.100 | rang 8.028
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LTC-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.404 | entrée 6.350 | trend 9.000 | rang 8.064
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ICP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.107
2. LTC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.064
3. KITE-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 8.028

## Accélération indépendante

- LAPTOP-EUR — CONFIRMED_ACCELERATION — score 8.290/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARPA-EUR — CONFIRMED_ACCELERATION — score 7.493/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SQD-EUR — BUILDING_ACCELERATION — score 5.020/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- TRIA-EUR — MEMORY_24H — score mémoire 9.219/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 9.216/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SAGA-EUR — MEMORY_24H — score mémoire 9.208/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CPOOL-EUR — MEMORY_24H — score mémoire 8.705/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LAPTOP-EUR — ACTIVE_NOW — score mémoire 8.290/10 — sources ACCELERATION, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.107/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 8.064/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LINK-EUR — MEMORY_24H — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- KITE-EUR — ACTIVE_NOW — score mémoire 8.028/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CPOOL-EUR +42.01% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ALLO-EUR +35.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MET-EUR +31.68% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SAGA-EUR +26.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SENT-EUR +23.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUPER-EUR +19.18% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DBR-EUR +18.59% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- ZRO-EUR +18.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ACE-EUR +15.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CHR-EUR +14.72% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
