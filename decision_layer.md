# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T01:20:16.315340+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 8.611 | entrée 7.800 | trend 7.850 | rang 7.925
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AIXBT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.212 | entrée 6.000 | trend 7.400 | rang 7.278
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : LISTA-EUR | action LATENT_ACCELERATOR | opportunité 7.815 | entrée 4.650 | trend 8.750 | rang 7.543
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : VET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.201 | entrée 8.450 | trend 8.100 | rang 8.012
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.012
2. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.925
3. ALGO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.907

## Accélération indépendante

- PEAQ-EUR — CONFIRMED_ACCELERATION — score 9.314/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — CONFIRMED_ACCELERATION — score 9.012/10 — DETECTED_BUT_TOO_LATE
- GRASS-EUR — CONFIRMED_ACCELERATION — score 8.913/10 — DETECTED_BUT_TOO_LATE
- SLX-EUR — CONFIRMED_ACCELERATION — score 8.896/10 — DETECTED_BUT_TOO_LATE
- AIOZ-EUR — CONFIRMED_ACCELERATION — score 8.442/10 — DETECTED_BUT_TOO_LATE
- FARTCOIN-EUR — CONFIRMED_ACCELERATION — score 7.519/10 — DETECTED_BUT_TOO_LATE
- UNI-EUR — CONFIRMED_ACCELERATION — score 7.452/10 — DETECTED_BUT_TOO_LATE
- NIL-EUR — CONFIRMED_ACCELERATION — score 7.198/10 — DETECTED_BUT_TOO_LATE
- CNPY-EUR — BUILDING_ACCELERATION — score 5.861/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRO-EUR — BUILDING_ACCELERATION — score 5.534/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- MLN-EUR — MEMORY_24H — score mémoire 9.841/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEAQ-EUR — ACTIVE_NOW — score mémoire 9.314/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — ACTIVE_NOW — score mémoire 9.012/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- GRASS-EUR — ACTIVE_NOW — score mémoire 8.913/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SLX-EUR — ACTIVE_NOW — score mémoire 8.896/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 8.442/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- MET-EUR — MEMORY_24H — score mémoire 8.271/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- BCH-EUR +31.46% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +28.27% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DRIFT-EUR +23.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- USELESS-EUR +23.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MET-EUR +20.60% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- UNI-EUR +20.15% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FLOCK-EUR +18.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +18.51% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CHR-EUR +18.50% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- TREAD-EUR +18.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
