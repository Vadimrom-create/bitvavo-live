# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T19:25:09.729498+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 9.296 | entrée 8.400 | trend 8.200 | rang 8.353
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : EDEN-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.682 | entrée 5.850 | trend 8.150 | rang 7.824
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BEAM-EUR | action LATENT_ACCELERATOR | opportunité 7.833 | entrée 5.750 | trend 8.500 | rang 7.533
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : BAT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.191 | entrée 6.200 | trend 8.100 | rang 8.011
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LTC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.353
2. BAT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.011
3. TAIKO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.006

## Accélération indépendante

- TIA-EUR — CONFIRMED_ACCELERATION — score 9.123/10 — DETECTED_BUT_TOO_LATE
- WELL-EUR — CONFIRMED_ACCELERATION — score 9.021/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SENT-EUR — CONFIRMED_ACCELERATION — score 8.708/10 — DETECTED_BUT_TOO_LATE
- MOVR-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- KAITO-EUR — CONFIRMED_ACCELERATION — score 8.161/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NOS-EUR — BUILDING_ACCELERATION — score 6.147/10 — DETECTED_BUT_TOO_LATE
- PENGU-EUR — BUILDING_ACCELERATION — score 5.421/10 — DETECTED_BUT_TOO_LATE
- IOST-EUR — BUILDING_ACCELERATION — score 5.366/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PEOPLE-EUR — BUILDING_ACCELERATION — score 5.192/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MOODENG-EUR — BUILDING_ACCELERATION — score 5.115/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- TIA-EUR — ACTIVE_NOW — score mémoire 9.123/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- WELL-EUR — ACTIVE_NOW — score mémoire 9.021/10 — sources ACCELERATION, V4 — WATCH_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 8.708/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- APE-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- MOVR-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LTC-EUR — ACTIVE_NOW — score mémoire 8.353/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HMSTR-EUR — MEMORY_24H — score mémoire 8.203/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- DRIFT-EUR +55.30% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHR-EUR +34.78% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- BCH-EUR +30.74% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +25.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +20.93% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KITE-EUR +18.33% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +17.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +16.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +16.16% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MLN-EUR +14.06% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
