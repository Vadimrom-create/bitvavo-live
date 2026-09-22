# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T22:27:53.579299+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 8.172 | entrée 7.450 | trend 6.450 | rang 7.035
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : MAGIC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.958 | entrée 6.150 | trend 7.350 | rang 7.075
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BREV-EUR | action LATENT_ACCELERATOR | opportunité 7.810 | entrée 4.500 | trend 8.450 | rang 7.389
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SSV-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.217 | entrée 5.800 | trend 8.400 | rang 8.200
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. SSV-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.200
2. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.190
3. AVAX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.948

## Accélération indépendante

- NES-EUR — CONFIRMED_ACCELERATION — score 9.000/10 — DETECTED_BUT_TOO_LATE
- UNI-EUR — CONFIRMED_ACCELERATION — score 7.909/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PUFFER-EUR — CONFIRMED_ACCELERATION — score 7.559/10 — DETECTED_BUT_TOO_LATE
- SUSHI-EUR — CONFIRMED_ACCELERATION — score 7.461/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRAC-EUR — CONFIRMED_ACCELERATION — score 7.151/10 — DETECTED_BUT_TOO_LATE
- THQ-EUR — BUILDING_ACCELERATION — score 6.383/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRO-EUR — BUILDING_ACCELERATION — score 6.298/10 — DETECTED_BUT_TOO_LATE
- TRB-EUR — BUILDING_ACCELERATION — score 5.658/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICNT-EUR — BUILDING_ACCELERATION — score 5.471/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MAGIC-EUR — BUILDING_ACCELERATION — score 5.052/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- TREAD-EUR — MEMORY_24H — score mémoire 9.440/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — ACTIVE_NOW — score mémoire 9.000/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- LMWR-EUR — MEMORY_24H — score mémoire 8.748/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SSV-EUR — ACTIVE_NOW — score mémoire 8.200/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 8.190/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- BTT-EUR — MEMORY_24H — score mémoire 8.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AVAX-EUR — ACTIVE_NOW — score mémoire 7.948/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- KERNEL-EUR +35.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DRIFT-EUR +32.23% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHR-EUR +26.22% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- USELESS-EUR +25.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BCH-EUR +24.10% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FLOCK-EUR +19.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +16.85% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KITE-EUR +16.34% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +16.10% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NES-EUR +15.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
