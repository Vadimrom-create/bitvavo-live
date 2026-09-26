# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T23:29:09.342263+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ALGO-EUR | action ACHETE_MAINTENANT | opportunité 8.839 | entrée 7.350 | trend 9.000 | rang 8.376
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : GALA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.799 | entrée 6.350 | trend 9.000 | rang 7.830
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : IO-EUR | action LATENT_ACCELERATOR | opportunité 8.048 | entrée 4.950 | trend 8.750 | rang 7.686
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ROSE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.823 | entrée 6.700 | trend 8.950 | rang 8.223
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ALGO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.376
2. W-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.342
3. ROSE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.223

## Accélération indépendante

- ICX-EUR — BUILDING_ACCELERATION — score 5.553/10 — DETECTED_BUT_TOO_LATE
- LAPTOP-EUR — BUILDING_ACCELERATION — score 5.425/10 — DETECTED_BUT_TOO_LATE
- LRC-EUR — BUILDING_ACCELERATION — score 5.345/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- STO-EUR — BUILDING_ACCELERATION — score 5.022/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- STX-EUR — BUILDING_ACCELERATION — score 4.878/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TREAD-EUR — BUILDING_ACCELERATION — score 4.856/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- AMP-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_DECAY_24_72H — score mémoire 9.497/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 9.483/10 — sources ACCELERATION — MEMORY_ONLY
- QNT-EUR — MEMORY_24H — score mémoire 9.115/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- VELO-EUR — MEMORY_24H — score mémoire 8.605/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ALGO-EUR — ACTIVE_NOW — score mémoire 8.376/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 8.342/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ROSE-EUR — ACTIVE_NOW — score mémoire 8.223/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CC-EUR — ACTIVE_NOW — score mémoire 8.177/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- POND-EUR +85.28% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +51.85% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +47.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +45.57% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +35.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- 2Z-EUR +24.73% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- KMNO-EUR +23.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +16.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOON-EUR +16.76% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RUNE-EUR +15.43% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
