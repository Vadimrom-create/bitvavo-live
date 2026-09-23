# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T08:41:24.016978+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAIKO-EUR | action ACHETE_MAINTENANT | opportunité 8.107 | entrée 6.900 | trend 8.700 | rang 7.925
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : MEME-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.879 | entrée 5.900 | trend 8.700 | rang 7.704
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : RED-EUR | action LATENT_ACCELERATOR | opportunité 8.127 | entrée 5.700 | trend 8.650 | rang 7.710
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MOVR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.287 | entrée 6.200 | trend 8.400 | rang 8.224
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. MOVR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.224
2. KMNO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.167
3. TAIKO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.925

## Accélération indépendante

- ICX-EUR — CONFIRMED_ACCELERATION — score 9.359/10 — DETECTED_BUT_TOO_LATE
- BOB-EUR — CONFIRMED_ACCELERATION — score 8.371/10 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — CONFIRMED_ACCELERATION — score 7.500/10 — DETECTED_BUT_TOO_LATE
- BEAM-EUR — CONFIRMED_ACCELERATION — score 7.214/10 — DETECTED_BUT_TOO_LATE
- BTT-EUR — CONFIRMED_ACCELERATION — score 6.852/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- COTI-EUR — BUILDING_ACCELERATION — score 6.480/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HFT-EUR — BUILDING_ACCELERATION — score 6.062/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MEME-EUR — BUILDING_ACCELERATION — score 5.778/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SUPER-EUR — BUILDING_ACCELERATION — score 5.723/10 — DETECTED_BUT_TOO_LATE
- MOVR-EUR — BUILDING_ACCELERATION — score 5.602/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ZIG-EUR — ACTIVE_NOW — score mémoire 7.455/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- NPC-EUR — ACTIVE_NOW — score mémoire 7.431/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- IKA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ICX-EUR — ACTIVE_NOW — score mémoire 9.359/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- SLX-EUR — MEMORY_24H — score mémoire 9.336/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CETUS-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BOB-EUR — ACTIVE_NOW — score mémoire 8.371/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- MOVR-EUR — ACTIVE_NOW — score mémoire 8.224/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KMNO-EUR — ACTIVE_NOW — score mémoire 8.167/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- CPOOL-EUR +42.93% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BCH-EUR +34.40% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +31.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MET-EUR +31.27% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +29.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHR-EUR +26.48% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ALLO-EUR +22.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +20.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PENGU-EUR +20.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SENT-EUR +19.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
