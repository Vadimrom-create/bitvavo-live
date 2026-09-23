# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T04:05:07.550659+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 9.258 | entrée 7.400 | trend 8.500 | rang 8.447
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : DUSK-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.181 | entrée 6.600 | trend 8.400 | rang 7.450
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : TAIKO-EUR | action LATENT_ACCELERATOR | opportunité 8.049 | entrée 4.500 | trend 8.700 | rang 7.544
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AXS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.229 | entrée 7.100 | trend 8.450 | rang 8.261
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.447
2. AXS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.261
3. LTC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.089

## Accélération indépendante

- ATH-EUR — CONFIRMED_ACCELERATION — score 8.678/10 — DETECTED_BUT_TOO_LATE
- WIN-EUR — CONFIRMED_ACCELERATION — score 8.088/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRUST-EUR — CONFIRMED_ACCELERATION — score 7.474/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PEOPLE-EUR — CONFIRMED_ACCELERATION — score 7.167/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TREAD-EUR — CONFIRMED_ACCELERATION — score 6.500/10 — DETECTED_BUT_TOO_LATE
- UP-EUR — CONFIRMED_ACCELERATION — score 6.500/10 — DETECTED_BUT_TOO_LATE
- ALICE-EUR — BUILDING_ACCELERATION — score 6.011/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZBCN-EUR — BUILDING_ACCELERATION — score 5.890/10 — DETECTED_BUT_TOO_LATE
- SNX-EUR — BUILDING_ACCELERATION — score 5.751/10 — DETECTED_BUT_TOO_LATE
- IQ-EUR — BUILDING_ACCELERATION — score 5.651/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- GIGA-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- ATH-EUR — ACTIVE_NOW — score mémoire 8.678/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 8.447/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AXS-EUR — ACTIVE_NOW — score mémoire 8.261/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.118/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 8.089/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WIN-EUR — ACTIVE_NOW — score mémoire 8.088/10 — sources ACCELERATION, V4 — WATCH_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 8.081/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- NIL-EUR +40.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- USELESS-EUR +33.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BCH-EUR +28.32% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MET-EUR +25.88% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ZRO-EUR +22.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +21.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CHR-EUR +19.81% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- UP-EUR +19.69% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- UNI-EUR +17.41% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FLOCK-EUR +17.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
