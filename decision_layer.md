# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T01:50:15.505867+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : RENDER-EUR | action ACHETE_MAINTENANT | opportunité 8.139 | entrée 7.400 | trend 8.650 | rang 7.986
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : BEAM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.733 | entrée 6.550 | trend 8.400 | rang 7.547
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ARX-EUR | action LATENT_ACCELERATOR | opportunité 8.097 | entrée 5.450 | trend 8.850 | rang 7.487
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : VET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.318 | entrée 8.200 | trend 8.350 | rang 8.186
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.186
2. LTC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.116
3. RENDER-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.986

## Accélération indépendante

- NOS-EUR — CONFIRMED_ACCELERATION — score 9.317/10 — DETECTED_BUT_TOO_LATE
- VTHO-EUR — CONFIRMED_ACCELERATION — score 8.600/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IQ-EUR — BUILDING_ACCELERATION — score 6.127/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- UP-EUR — BUILDING_ACCELERATION — score 5.101/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AERO-EUR — BUILDING_ACCELERATION — score 4.795/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- NOS-EUR — ACTIVE_NOW — score mémoire 9.317/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PEAQ-EUR — MEMORY_24H — score mémoire 9.314/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 9.012/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SLX-EUR — MEMORY_24H — score mémoire 8.896/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.600/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- DBR-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MET-EUR — MEMORY_24H — score mémoire 8.271/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- BCH-EUR +29.39% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +25.83% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +23.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FLOCK-EUR +22.48% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +22.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DRIFT-EUR +20.72% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +20.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MET-EUR +19.26% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- MLN-EUR +19.04% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ALLO-EUR +17.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
