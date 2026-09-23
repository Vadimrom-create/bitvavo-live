# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T00:25:04.529285+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : BNB-EUR | action ACHETE_MAINTENANT | opportunité 8.508 | entrée 7.000 | trend 6.750 | rang 7.314
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : CHZ-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.609 | entrée 6.050 | trend 7.350 | rang 6.987
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : RPL-EUR | action LATENT_ACCELERATOR | opportunité 7.631 | entrée 4.500 | trend 8.200 | rang 7.226
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MOVR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.163 | entrée 6.700 | trend 8.000 | rang 7.970
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. MOVR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.970
2. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.963
3. BEAM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.821

## Accélération indépendante

- T-EUR — CONFIRMED_ACCELERATION — score 8.931/10 — DETECTED_BUT_TOO_LATE
- DATAIP-EUR — CONFIRMED_ACCELERATION — score 6.705/10 — DETECTED_BUT_TOO_LATE
- G-EUR — CONFIRMED_ACCELERATION — score 6.563/10 — DETECTED_BUT_TOO_LATE
- ENS-EUR — BUILDING_ACCELERATION — score 6.125/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FARTCOIN-EUR — BUILDING_ACCELERATION — score 5.260/10 — DETECTED_BUT_TOO_LATE
- DUSK-EUR — BUILDING_ACCELERATION — score 5.149/10 — DETECTED_BUT_TOO_LATE
- BLEND-EUR — BUILDING_ACCELERATION — score 5.045/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VVV-EUR — BUILDING_ACCELERATION — score 4.909/10 — DETECTED_BUT_TOO_LATE
- GRASS-EUR — BUILDING_ACCELERATION — score 4.839/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- TREAD-EUR — MEMORY_24H — score mémoire 9.440/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- T-EUR — ACTIVE_NOW — score mémoire 8.931/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MET-EUR — MEMORY_24H — score mémoire 8.271/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 8.193/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.118/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MOVR-EUR — ACTIVE_NOW — score mémoire 7.970/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOL-EUR — ACTIVE_NOW — score mémoire 7.963/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- DRIFT-EUR +28.69% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BCH-EUR +27.40% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHR-EUR +22.48% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- NIL-EUR +21.26% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +20.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +20.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +18.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MET-EUR +17.98% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- TIA-EUR +17.66% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KITE-EUR +16.83% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
