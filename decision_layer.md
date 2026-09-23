# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T23:58:24.495131+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ICP-EUR | action ACHETE_MAINTENANT | opportunité 8.398 | entrée 7.200 | trend 8.500 | rang 7.894
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : LIGHTER-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.091 | entrée 6.150 | trend 7.850 | rang 7.697
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : TURBO-EUR | action LATENT_ACCELERATOR | opportunité 8.981 | entrée 5.700 | trend 7.550 | rang 7.702
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HOT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.112 | entrée 6.200 | trend 7.900 | rang 7.869
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ICP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.894
2. HOT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.869
3. THE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.846

## Accélération indépendante

- MET-EUR — CONFIRMED_ACCELERATION — score 8.271/10 — DETECTED_BUT_TOO_LATE
- ZAMA-EUR — CONFIRMED_ACCELERATION — score 7.655/10 — DETECTED_BUT_TOO_LATE
- TIA-EUR — CONFIRMED_ACCELERATION — score 7.463/10 — DETECTED_BUT_TOO_LATE
- LMWR-EUR — CONFIRMED_ACCELERATION — score 7.092/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FOLD-EUR — BUILDING_ACCELERATION — score 5.016/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SUPER-EUR — BUILDING_ACCELERATION — score 4.913/10 — DETECTED_BUT_TOO_LATE
- HNT-EUR — BUILDING_ACCELERATION — score 4.812/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- OPEN-EUR — BUILDING_ACCELERATION — score 4.753/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- XPL-EUR — ACTIVE_NOW — score mémoire 7.026/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- TREAD-EUR — MEMORY_24H — score mémoire 9.440/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MET-EUR — ACTIVE_NOW — score mémoire 8.271/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PUFFER-EUR — MEMORY_24H — score mémoire 8.193/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.118/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.894/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- DRIFT-EUR +34.93% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BCH-EUR +29.33% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +28.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CHR-EUR +25.57% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- USELESS-EUR +24.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +19.85% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FLOCK-EUR +18.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +18.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TIA-EUR +17.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MET-EUR +16.64% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
