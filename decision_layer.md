# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T21:02:53.568121+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : PYTH-EUR | action ACHETE_MAINTENANT | opportunité 7.656 | entrée 6.900 | trend 8.300 | rang 7.521
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : DOT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.663 | entrée 6.300 | trend 8.750 | rang 7.671
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : FIL-EUR | action LATENT_ACCELERATOR | opportunité 8.333 | entrée 5.650 | trend 8.950 | rang 7.925
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ALGO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.238 | entrée 6.300 | trend 9.000 | rang 8.025
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ALGO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.025
2. EIGEN-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.005
3. LTC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.990

## Accélération indépendante

- RAD-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- LRC-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- ZEUS-EUR — CONFIRMED_ACCELERATION — score 7.964/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOON-EUR — BUILDING_ACCELERATION — score 5.321/10 — DETECTED_BUT_TOO_LATE
- BILL-EUR — BUILDING_ACCELERATION — score 5.046/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- AMP-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RAD-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 9.483/10 — sources ACCELERATION — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- VELO-EUR — MEMORY_24H — score mémoire 8.605/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACT-EUR — MEMORY_24H — score mémoire 8.555/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- LRC-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ALGO-EUR — ACTIVE_NOW — score mémoire 8.025/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- POND-EUR +106.58% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +60.21% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +42.55% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +37.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QNT-EUR +23.46% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +20.46% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- 2Z-EUR +18.96% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- AGI-EUR +18.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RUNE-EUR +17.19% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- KAS-EUR +16.29% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
