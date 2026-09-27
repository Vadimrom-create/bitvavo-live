# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T01:38:33.192894+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : CC-EUR | action ACHETE_MAINTENANT | opportunité 8.983 | entrée 7.450 | trend 8.650 | rang 8.332
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ROSE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.254 | entrée 5.900 | trend 8.950 | rang 7.953
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ATH-EUR | action LATENT_ACCELERATOR | opportunité 8.202 | entrée 5.200 | trend 9.000 | rang 7.877
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : EIGEN-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.613 | entrée 6.400 | trend 9.200 | rang 8.274
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. CC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.332
2. EIGEN-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.274
3. FIL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.244

## Accélération indépendante

- ZRC-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- TRIA-EUR — CONFIRMED_ACCELERATION — score 7.998/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- QKC-EUR — CONFIRMED_ACCELERATION — score 7.962/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DOGS-EUR — CONFIRMED_ACCELERATION — score 7.902/10 — DETECTED_BUT_TOO_LATE
- NOT-EUR — BUILDING_ACCELERATION — score 6.432/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- C-EUR — BUILDING_ACCELERATION — score 6.342/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PYTH-EUR — BUILDING_ACCELERATION — score 6.325/10 — DETECTED_BUT_TOO_LATE
- HFT-EUR — BUILDING_ACCELERATION — score 5.626/10 — DETECTED_BUT_TOO_LATE
- KITE-EUR — BUILDING_ACCELERATION — score 5.501/10 — DETECTED_BUT_TOO_LATE
- CAP-EUR — BUILDING_ACCELERATION — score 5.491/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- W-EUR — ACTIVE_NOW — score mémoire 7.930/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ZRC-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- PONKE-EUR — MEMORY_DECAY_24_72H — score mémoire 9.067/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.923/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RARE-EUR — MEMORY_24H — score mémoire 8.845/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- VELO-EUR — MEMORY_24H — score mémoire 8.605/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ONT-EUR — MEMORY_DECAY_24_72H — score mémoire 8.574/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AMP-EUR — MEMORY_24H — score mémoire 8.528/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CC-EUR — ACTIVE_NOW — score mémoire 8.332/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +67.79% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +51.16% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +35.11% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- 2Z-EUR +20.60% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- AGI-EUR +18.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOON-EUR +17.80% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RUNE-EUR +17.70% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ZRC-EUR +16.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HFT-EUR +15.93% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- KMNO-EUR +15.34% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
