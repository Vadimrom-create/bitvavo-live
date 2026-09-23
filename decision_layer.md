# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T03:51:21.201442+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 9.410 | entrée 7.950 | trend 8.750 | rang 8.573
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : MOVR-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.996 | entrée 6.100 | trend 8.400 | rang 7.572
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : LISTA-EUR | action LATENT_ACCELERATOR | opportunité 7.999 | entrée 4.500 | trend 8.750 | rang 7.537
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : W-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.190 | entrée 7.150 | trend 8.400 | rang 8.138
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LTC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.573
2. SUI-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.394
3. SOL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.279

## Accélération indépendante

- EPIC-EUR — CONFIRMED_ACCELERATION — score 7.444/10 — DETECTED_BUT_TOO_LATE
- CRV-EUR — CONFIRMED_ACCELERATION — score 7.142/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PENDLE-EUR — CONFIRMED_ACCELERATION — score 7.117/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PEOPLE-EUR — CONFIRMED_ACCELERATION — score 7.036/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BOME-EUR — CONFIRMED_ACCELERATION — score 6.812/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HNT-EUR — BUILDING_ACCELERATION — score 6.459/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LINEA-EUR — BUILDING_ACCELERATION — score 6.323/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AAVE-EUR — BUILDING_ACCELERATION — score 6.059/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TREE-EUR — BUILDING_ACCELERATION — score 5.581/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TREAD-EUR — BUILDING_ACCELERATION — score 5.500/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AAVE-EUR — ACTIVE_NOW — score mémoire 7.884/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- GIGA-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- SLX-EUR — MEMORY_24H — score mémoire 8.896/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 8.573/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SUI-EUR — ACTIVE_NOW — score mémoire 8.394/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOL-EUR — ACTIVE_NOW — score mémoire 8.279/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ONDO-EUR — ACTIVE_NOW — score mémoire 8.175/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- NIL-EUR +48.70% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- USELESS-EUR +34.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BCH-EUR +29.17% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MET-EUR +26.09% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ZRO-EUR +22.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +21.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CHR-EUR +20.54% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- UNI-EUR +19.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PENGU-EUR +17.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DRIFT-EUR +17.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
