# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T02:41:28.890772+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : DOGE-EUR | action ACHETE_MAINTENANT | opportunité 8.356 | entrée 7.250 | trend 7.250 | rang 7.479
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ZBT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.791 | entrée 6.400 | trend 8.150 | rang 7.358
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : AVNT-EUR | action LATENT_ACCELERATOR | opportunité 7.859 | entrée 5.550 | trend 8.400 | rang 7.545
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : BEAM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.210 | entrée 6.800 | trend 8.400 | rang 8.317
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. BEAM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.317
2. LTC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.086
3. RENDER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.970

## Accélération indépendante

- ZRO-EUR — CONFIRMED_ACCELERATION — score 7.607/10 — DETECTED_BUT_TOO_LATE
- MORPHO-EUR — CONFIRMED_ACCELERATION — score 7.497/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RARE-EUR — CONFIRMED_ACCELERATION — score 6.611/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARK-EUR — CONFIRMED_ACCELERATION — score 6.526/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MAVIA-EUR — CONFIRMED_ACCELERATION — score 6.500/10 — DETECTED_BUT_TOO_LATE
- FLUX-EUR — BUILDING_ACCELERATION — score 6.458/10 — DETECTED_BUT_TOO_LATE
- POWR-EUR — BUILDING_ACCELERATION — score 6.360/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PHA-EUR — BUILDING_ACCELERATION — score 6.287/10 — DETECTED_BUT_TOO_LATE
- ZKC-EUR — BUILDING_ACCELERATION — score 5.947/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SKY-EUR — BUILDING_ACCELERATION — score 5.868/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ICX-EUR — MEMORY_24H — score mémoire 9.089/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SLX-EUR — MEMORY_24H — score mémoire 8.896/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- DBR-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BEAM-EUR — ACTIVE_NOW — score mémoire 8.317/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 8.193/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.118/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 8.086/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- NIL-EUR +31.22% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BCH-EUR +27.81% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +24.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +23.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MET-EUR +21.78% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- UP-EUR +21.54% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- ZRO-EUR +21.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DRIFT-EUR +19.00% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FLOCK-EUR +18.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KITE-EUR +18.09% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
