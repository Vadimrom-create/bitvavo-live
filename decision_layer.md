# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T19:32:37.780466+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 9.284 | entrée 8.200 | trend 8.200 | rang 8.229
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : EDEN-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.964 | entrée 5.850 | trend 8.150 | rang 7.497
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : RUNE-EUR | action LATENT_ACCELERATOR | opportunité 7.800 | entrée 4.500 | trend 8.850 | rang 7.554
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : W-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.582 | entrée 6.500 | trend 8.400 | rang 7.929
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LTC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.229
2. W-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.929
3. SOL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.902

## Accélération indépendante

- TIA-EUR — CONFIRMED_ACCELERATION — score 9.615/10 — DETECTED_BUT_TOO_LATE
- SENT-EUR — CONFIRMED_ACCELERATION — score 7.596/10 — DETECTED_BUT_TOO_LATE
- MOVR-EUR — CONFIRMED_ACCELERATION — score 7.500/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MET-EUR — CONFIRMED_ACCELERATION — score 6.623/10 — DETECTED_BUT_TOO_LATE
- WELL-EUR — BUILDING_ACCELERATION — score 6.093/10 — DETECTED_BUT_TOO_LATE
- PENGU-EUR — BUILDING_ACCELERATION — score 6.033/10 — DETECTED_BUT_TOO_LATE
- DYDX-EUR — BUILDING_ACCELERATION — score 5.995/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- U-EUR — BUILDING_ACCELERATION — score 5.489/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BILL-EUR — BUILDING_ACCELERATION — score 5.413/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IOST-EUR — BUILDING_ACCELERATION — score 5.359/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- TIA-EUR — ACTIVE_NOW — score mémoire 9.615/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- TAI-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- APE-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 8.229/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAITO-EUR — MEMORY_24H — score mémoire 8.161/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 7.929/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOL-EUR — ACTIVE_NOW — score mémoire 7.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CHR-EUR — MEMORY_24H — score mémoire 7.801/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- DRIFT-EUR +53.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHR-EUR +35.37% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- BCH-EUR +29.17% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +25.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +21.75% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KITE-EUR +17.73% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +17.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- USELESS-EUR +14.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GOAT-EUR +14.76% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +14.51% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
