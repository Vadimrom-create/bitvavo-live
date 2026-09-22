# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T23:31:41.118243+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ICP-EUR | action ACHETE_MAINTENANT | opportunité 9.278 | entrée 7.400 | trend 8.500 | rang 8.366
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : TURBO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.241 | entrée 5.950 | trend 7.550 | rang 7.207
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SSV-EUR | action LATENT_ACCELERATOR | opportunité 8.103 | entrée 4.500 | trend 8.400 | rang 7.439
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : TAO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.307 | entrée 8.050 | trend 8.250 | rang 8.044
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ICP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.366
2. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.044
3. RENDER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.036

## Accélération indépendante

- ICX-EUR — CONFIRMED_ACCELERATION — score 6.907/10 — DETECTED_BUT_TOO_LATE
- EIGEN-EUR — BUILDING_ACCELERATION — score 6.347/10 — DETECTED_BUT_TOO_LATE
- C98-EUR — BUILDING_ACCELERATION — score 5.785/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DIA-EUR — BUILDING_ACCELERATION — score 5.783/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MON-EUR — BUILDING_ACCELERATION — score 5.527/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRUST-EUR — BUILDING_ACCELERATION — score 5.401/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- STRK-EUR — BUILDING_ACCELERATION — score 5.342/10 — DETECTED_BUT_TOO_LATE
- O-EUR — BUILDING_ACCELERATION — score 5.107/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MANTA-EUR — BUILDING_ACCELERATION — score 4.906/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRO-EUR — BUILDING_ACCELERATION — score 4.802/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- XPL-EUR — ACTIVE_NOW — score mémoire 7.165/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- TREAD-EUR — MEMORY_24H — score mémoire 9.440/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LMWR-EUR — MEMORY_24H — score mémoire 8.748/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.366/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 8.193/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.118/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- DRIFT-EUR +33.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +29.59% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BCH-EUR +27.62% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHR-EUR +25.68% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- USELESS-EUR +25.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +20.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FLOCK-EUR +19.02% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +17.79% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BTT-EUR +16.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KITE-EUR +16.34% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
