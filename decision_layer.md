# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T20:00:58.328965+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 9.296 | entrée 8.150 | trend 8.200 | rang 8.339
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : LISTA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.665 | entrée 6.000 | trend 8.500 | rang 7.546
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : IOST-EUR | action LATENT_ACCELERATOR | opportunité 8.069 | entrée 5.500 | trend 7.500 | rang 7.258
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LPT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.148 | entrée 7.100 | trend 8.100 | rang 8.216
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LTC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.339
2. LPT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.216
3. RENDER-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.161

## Accélération indépendante

- BTT-EUR — CONFIRMED_ACCELERATION — score 6.842/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TIA-EUR — CONFIRMED_ACCELERATION — score 6.517/10 — DETECTED_BUT_TOO_LATE
- NOS-EUR — BUILDING_ACCELERATION — score 6.144/10 — DETECTED_BUT_TOO_LATE
- FTT-EUR — BUILDING_ACCELERATION — score 5.932/10 — DETECTED_BUT_TOO_LATE
- KERNEL-EUR — BUILDING_ACCELERATION — score 5.530/10 — DETECTED_BUT_TOO_LATE
- TAI-EUR — BUILDING_ACCELERATION — score 5.392/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ALLO-EUR — BUILDING_ACCELERATION — score 5.359/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PENGU-EUR — BUILDING_ACCELERATION — score 5.098/10 — DETECTED_BUT_TOO_LATE
- RECALL-EUR — BUILDING_ACCELERATION — score 4.818/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- TREAD-EUR — MEMORY_24H — score mémoire 9.440/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- APE-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 8.339/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LPT-EUR — ACTIVE_NOW — score mémoire 8.216/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.161/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOL-EUR — ACTIVE_NOW — score mémoire 7.955/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FIL-EUR — ACTIVE_NOW — score mémoire 7.835/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.823/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- DRIFT-EUR +41.28% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHR-EUR +31.50% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- BCH-EUR +25.71% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +24.38% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +20.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KITE-EUR +18.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- USELESS-EUR +16.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +16.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GOAT-EUR +15.79% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TIA-EUR +15.63% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
