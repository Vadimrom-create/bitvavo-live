# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T20:20:26.082950+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ETC-EUR | action ACHETE_MAINTENANT | opportunité 9.028 | entrée 7.450 | trend 8.100 | rang 8.177
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : LISTA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.688 | entrée 6.000 | trend 8.500 | rang 7.551
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : 0G-EUR | action LATENT_ACCELERATOR | opportunité 7.554 | entrée 4.500 | trend 8.600 | rang 7.317
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SOL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.869 | entrée 7.800 | trend 8.500 | rang 7.853
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ETC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.177
2. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.853
3. FET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.785

## Accélération indépendante

- XMN-EUR — CONFIRMED_ACCELERATION — score 7.265/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- USELESS-EUR — BUILDING_ACCELERATION — score 6.201/10 — DETECTED_BUT_TOO_LATE
- SWELL-EUR — BUILDING_ACCELERATION — score 5.633/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MLN-EUR — BUILDING_ACCELERATION — score 5.460/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SXT-EUR — BUILDING_ACCELERATION — score 5.361/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- TREAD-EUR — MEMORY_24H — score mémoire 9.440/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- APE-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- ETC-EUR — ACTIVE_NOW — score mémoire 8.177/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOL-EUR — ACTIVE_NOW — score mémoire 7.853/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CHR-EUR — MEMORY_24H — score mémoire 7.801/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TRAC-EUR — MEMORY_24H — score mémoire 7.788/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 7.785/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZEN-EUR — ACTIVE_NOW — score mémoire 7.761/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- DRIFT-EUR +41.72% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHR-EUR +31.64% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- BCH-EUR +27.16% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +24.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +20.26% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- USELESS-EUR +17.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KITE-EUR +17.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GOAT-EUR +15.17% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PENGU-EUR +14.99% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +14.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
