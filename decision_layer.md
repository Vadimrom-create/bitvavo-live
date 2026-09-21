# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T00:27:35.662571+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : WAL-EUR | action ACHETE_MAINTENANT | opportunité 9.225 | entrée 6.950 | trend 9.200 | rang 8.401
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ARX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.709 | entrée 6.150 | trend 8.900 | rang 8.106
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : AIOZ-EUR | action LATENT_ACCELERATOR | opportunité 7.878 | entrée 4.500 | trend 8.550 | rang 7.482
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ZK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.267 | entrée 6.900 | trend 8.400 | rang 8.336
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. WAL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.401
2. PYTH-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.358
3. ZK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.336

## Accélération indépendante

- DEEP-EUR — CONFIRMED_ACCELERATION — score 8.733/10 — DETECTED_BUT_TOO_LATE
- SUI-EUR — CONFIRMED_ACCELERATION — score 8.174/10 — DETECTED_BUT_TOO_LATE
- HEI-EUR — CONFIRMED_ACCELERATION — score 7.213/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AZTEC-EUR — CONFIRMED_ACCELERATION — score 7.150/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AVAX-EUR — BUILDING_ACCELERATION — score 6.491/10 — DETECTED_BUT_TOO_LATE
- CETUS-EUR — BUILDING_ACCELERATION — score 6.422/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- METIS-EUR — BUILDING_ACCELERATION — score 6.379/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CHIP-EUR — BUILDING_ACCELERATION — score 6.298/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZIL-EUR — BUILDING_ACCELERATION — score 6.279/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ASTR-EUR — BUILDING_ACCELERATION — score 6.050/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- STX-EUR — ACTIVE_NOW — score mémoire 7.969/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- NPC-EUR — ACTIVE_NOW — score mémoire 7.575/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ICX-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.883/10 — sources ACCELERATION — MEMORY_ONLY
- DEEP-EUR — ACTIVE_NOW — score mémoire 8.733/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- NOS-EUR — MEMORY_24H — score mémoire 8.445/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 8.401/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.376/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.358/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ZK-EUR — ACTIVE_NOW — score mémoire 8.336/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +51.11% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +36.57% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PTB-EUR +31.50% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NIL-EUR +24.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +24.64% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- S-EUR +21.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +18.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +18.93% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CFG-EUR +18.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VVV-EUR +14.46% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
