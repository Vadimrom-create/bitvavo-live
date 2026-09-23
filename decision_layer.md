# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T05:50:40.229749+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : WLD-EUR | action ACHETE_MAINTENANT | opportunité 9.132 | entrée 7.900 | trend 7.800 | rang 8.197
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : BEAM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.338 | entrée 5.950 | trend 8.700 | rang 7.817
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ACH-EUR | action LATENT_ACCELERATOR | opportunité 8.252 | entrée 5.650 | trend 8.200 | rang 7.540
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : FET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.050 | entrée 8.200 | trend 8.400 | rang 8.041
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. WLD-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.197
2. LTC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.098
3. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.041

## Accélération indépendante

- NIL-EUR — CONFIRMED_ACCELERATION — score 8.663/10 — DETECTED_BUT_TOO_LATE
- ZAMA-EUR — CONFIRMED_ACCELERATION — score 7.777/10 — DETECTED_BUT_TOO_LATE
- PHA-EUR — CONFIRMED_ACCELERATION — score 6.889/10 — DETECTED_BUT_TOO_LATE
- CPOOL-EUR — BUILDING_ACCELERATION — score 6.469/10 — DETECTED_BUT_TOO_LATE
- USELESS-EUR — BUILDING_ACCELERATION — score 6.064/10 — DETECTED_BUT_TOO_LATE
- SENT-EUR — BUILDING_ACCELERATION — score 5.953/10 — DETECTED_BUT_TOO_LATE
- QKC-EUR — BUILDING_ACCELERATION — score 5.870/10 — DETECTED_BUT_TOO_LATE
- MEW-EUR — BUILDING_ACCELERATION — score 5.653/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PEAQ-EUR — BUILDING_ACCELERATION — score 5.248/10 — DETECTED_BUT_TOO_LATE
- QUID-EUR — BUILDING_ACCELERATION — score 5.116/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SLX-EUR — MEMORY_24H — score mémoire 9.336/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 8.755/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NIL-EUR — ACTIVE_NOW — score mémoire 8.663/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- NES-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SAGA-EUR — MEMORY_24H — score mémoire 8.405/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 8.197/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.118/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 8.098/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- NIL-EUR +49.53% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CPOOL-EUR +32.08% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MET-EUR +31.55% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BCH-EUR +28.14% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- USELESS-EUR +27.99% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +25.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CHR-EUR +25.17% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRO-EUR +20.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUPER-EUR +20.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SENT-EUR +20.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
