# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T03:17:23.703699+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 9.467 | entrée 7.450 | trend 9.000 | rang 8.567
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : GRT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.754 | entrée 6.300 | trend 8.000 | rang 6.905
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : YGG-EUR | action LATENT_ACCELERATOR | opportunité 8.064 | entrée 5.750 | trend 8.700 | rang 7.657
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LDO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.771 | entrée 6.550 | trend 8.400 | rang 8.004
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LTC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.567
2. LDO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.004
3. JUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.928

## Accélération indépendante

- GIGA-EUR — CONFIRMED_ACCELERATION — score 9.062/10 — DETECTED_BUT_TOO_LATE
- PLUME-EUR — CONFIRMED_ACCELERATION — score 8.029/10 — DETECTED_BUT_TOO_LATE
- NIL-EUR — CONFIRMED_ACCELERATION — score 7.498/10 — DETECTED_BUT_TOO_LATE
- SAND-EUR — CONFIRMED_ACCELERATION — score 7.476/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AUCTION-EUR — CONFIRMED_ACCELERATION — score 6.617/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- YGG-EUR — CONFIRMED_ACCELERATION — score 6.540/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SENT-EUR — BUILDING_ACCELERATION — score 6.471/10 — DETECTED_BUT_TOO_LATE
- GWEI-EUR — BUILDING_ACCELERATION — score 6.352/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- UNI-EUR — BUILDING_ACCELERATION — score 6.018/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MANTA-EUR — BUILDING_ACCELERATION — score 5.991/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ICX-EUR — MEMORY_24H — score mémoire 9.089/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- GIGA-EUR — ACTIVE_NOW — score mémoire 9.062/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- SLX-EUR — MEMORY_24H — score mémoire 8.896/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 8.567/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 8.193/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.118/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PLUME-EUR — ACTIVE_NOW — score mémoire 8.029/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- NIL-EUR +54.20% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- USELESS-EUR +35.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BCH-EUR +29.01% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MET-EUR +23.09% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ZRO-EUR +22.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUPER-EUR +19.81% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- UNI-EUR +19.22% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ALLO-EUR +18.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FLOCK-EUR +17.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CHR-EUR +17.57% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
