# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T23:45:30.459552+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ICP-EUR | action ACHETE_MAINTENANT | opportunité 8.395 | entrée 7.200 | trend 8.500 | rang 7.953
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : CHZ-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.958 | entrée 6.650 | trend 7.350 | rang 7.614
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : TAIKO-EUR | action LATENT_ACCELERATOR | opportunité 7.926 | entrée 4.500 | trend 8.350 | rang 7.381
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : FIL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.214 | entrée 7.000 | trend 8.050 | rang 7.972
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. FIL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.972
2. ICP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.953
3. PROVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.914

## Accélération indépendante

- ZAMA-EUR — CONFIRMED_ACCELERATION — score 7.873/10 — DETECTED_BUT_TOO_LATE
- MET-EUR — CONFIRMED_ACCELERATION — score 6.674/10 — DETECTED_BUT_TOO_LATE
- BTT-EUR — BUILDING_ACCELERATION — score 5.429/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- OPEN-EUR — BUILDING_ACCELERATION — score 5.366/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AUCTION-EUR — BUILDING_ACCELERATION — score 5.050/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRAC-EUR — BUILDING_ACCELERATION — score 4.797/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GROVE-EUR — BUILDING_ACCELERATION — score 4.778/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- XPL-EUR — ACTIVE_NOW — score mémoire 7.039/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- TREAD-EUR — MEMORY_24H — score mémoire 9.440/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LMWR-EUR — MEMORY_24H — score mémoire 8.748/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 8.193/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.118/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FIL-EUR — ACTIVE_NOW — score mémoire 7.972/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- DRIFT-EUR +36.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BCH-EUR +29.66% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +29.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CHR-EUR +26.57% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- USELESS-EUR +24.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +18.78% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FLOCK-EUR +18.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +17.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BTT-EUR +16.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KITE-EUR +16.34% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
