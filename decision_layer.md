# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T15:31:57.110171+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : WLD-EUR | action ACHETE_MAINTENANT | opportunité 8.983 | entrée 7.600 | trend 7.100 | rang 7.756
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AVNT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.065 | entrée 6.100 | trend 7.350 | rang 7.328
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BREV-EUR | action LATENT_ACCELERATOR | opportunité 7.502 | entrée 4.500 | trend 8.450 | rang 7.246
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : 0G-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.921 | entrée 6.250 | trend 8.600 | rang 8.031
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. 0G-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.031
2. RENDER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.926
3. RUNE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.802

## Accélération indépendante

- PEAQ-EUR — CONFIRMED_ACCELERATION — score 7.834/10 — DETECTED_BUT_TOO_LATE
- GIGA-EUR — BUILDING_ACCELERATION — score 6.188/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ONT-EUR — BUILDING_ACCELERATION — score 6.123/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IOST-EUR — BUILDING_ACCELERATION — score 5.923/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AVA-EUR — BUILDING_ACCELERATION — score 5.912/10 — DETECTED_BUT_TOO_LATE
- MTL-EUR — BUILDING_ACCELERATION — score 5.830/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KSM-EUR — BUILDING_ACCELERATION — score 5.822/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CHZ-EUR — BUILDING_ACCELERATION — score 5.818/10 — DETECTED_BUT_TOO_LATE
- PUNDIX-EUR — BUILDING_ACCELERATION — score 5.739/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SAND-EUR — BUILDING_ACCELERATION — score 5.694/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- 0G-EUR — ACTIVE_NOW — score mémoire 8.031/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 7.926/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PEAQ-EUR — ACTIVE_NOW — score mémoire 7.834/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- RUNE-EUR — ACTIVE_NOW — score mémoire 7.802/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MERL-EUR — ACTIVE_NOW — score mémoire 7.763/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.761/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 7.756/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ICX-EUR +87.99% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- FLOCK-EUR +31.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BCH-EUR +23.68% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +23.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +21.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SAGA-EUR +15.58% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- KITE-EUR +15.11% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AVA-EUR +15.01% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOS-EUR +14.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +14.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
