# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T22:57:09.405582+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ALGO-EUR | action ACHETE_MAINTENANT | opportunité 8.934 | entrée 7.000 | trend 7.800 | rang 7.955
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : FLUX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.680 | entrée 6.200 | trend 8.550 | rang 7.260
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SSV-EUR | action LATENT_ACCELERATOR | opportunité 7.878 | entrée 4.500 | trend 8.400 | rang 7.428
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : FET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.600 | entrée 7.750 | trend 8.400 | rang 8.016
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.016
2. ALGO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.955
3. SOL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.953

## Accélération indépendante

- A-EUR — CONFIRMED_ACCELERATION — score 8.945/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PUFFER-EUR — CONFIRMED_ACCELERATION — score 8.193/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FTT-EUR — CONFIRMED_ACCELERATION — score 8.118/10 — DETECTED_BUT_TOO_LATE
- UNI-EUR — CONFIRMED_ACCELERATION — score 6.596/10 — DETECTED_BUT_TOO_LATE
- SHELL-EUR — BUILDING_ACCELERATION — score 6.199/10 — DETECTED_BUT_TOO_LATE
- TRIA-EUR — BUILDING_ACCELERATION — score 5.963/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ATOM-EUR — BUILDING_ACCELERATION — score 5.854/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DRIFT-EUR — BUILDING_ACCELERATION — score 5.835/10 — DETECTED_BUT_TOO_LATE
- SKL-EUR — BUILDING_ACCELERATION — score 5.699/10 — DETECTED_BUT_TOO_LATE
- CELR-EUR — BUILDING_ACCELERATION — score 5.685/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- TREAD-EUR — MEMORY_24H — score mémoire 9.440/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- A-EUR — ACTIVE_NOW — score mémoire 8.945/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LMWR-EUR — MEMORY_24H — score mémoire 8.748/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PUFFER-EUR — ACTIVE_NOW — score mémoire 8.193/10 — sources ACCELERATION, V4 — WATCH_ONLY
- FTT-EUR — ACTIVE_NOW — score mémoire 8.118/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- BTT-EUR — MEMORY_24H — score mémoire 8.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- DRIFT-EUR +36.69% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +31.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +27.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BCH-EUR +25.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHR-EUR +24.99% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- FLOCK-EUR +22.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +17.88% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KITE-EUR +17.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GOAT-EUR +15.16% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- UNI-EUR +14.86% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
