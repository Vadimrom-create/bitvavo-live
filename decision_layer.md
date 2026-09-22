# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T16:55:44.292292+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 8.405 | entrée 7.450 | trend 7.850 | rang 7.768
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : LISTA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.768 | entrée 5.900 | trend 8.500 | rang 7.418
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : THE-EUR | action LATENT_ACCELERATOR | opportunité 7.415 | entrée 4.500 | trend 8.700 | rang 7.309
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : DRIFT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.241 | entrée 5.950 | trend 8.200 | rang 7.948
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. DRIFT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.948
2. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.900
3. RUNE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.886

## Accélération indépendante

- EPIC-EUR — CONFIRMED_ACCELERATION — score 9.280/10 — DETECTED_BUT_TOO_LATE
- FLUX-EUR — CONFIRMED_ACCELERATION — score 9.085/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DUSK-EUR — CONFIRMED_ACCELERATION — score 8.672/10 — DETECTED_BUT_TOO_LATE
- MLN-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- THQ-EUR — CONFIRMED_ACCELERATION — score 8.073/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BEL-EUR — CONFIRMED_ACCELERATION — score 7.737/10 — DETECTED_BUT_TOO_LATE
- AGLD-EUR — CONFIRMED_ACCELERATION — score 7.711/10 — DETECTED_BUT_TOO_LATE
- CAT-EUR — CONFIRMED_ACCELERATION — score 7.705/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NEIRO-EUR — CONFIRMED_ACCELERATION — score 6.505/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BTT-EUR — BUILDING_ACCELERATION — score 6.310/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CHR-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- YGG-EUR — MEMORY_24H — score mémoire 9.515/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- EPIC-EUR — ACTIVE_NOW — score mémoire 9.280/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- FLUX-EUR — ACTIVE_NOW — score mémoire 9.085/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DUSK-EUR — ACTIVE_NOW — score mémoire 8.672/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- MLN-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- U-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- THQ-EUR — ACTIVE_NOW — score mémoire 8.073/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CHR-EUR +36.32% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- MLN-EUR +32.12% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- NIL-EUR +27.40% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FLOCK-EUR +25.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BCH-EUR +24.36% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +22.11% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +18.08% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +17.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KITE-EUR +16.46% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +14.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
