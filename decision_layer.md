# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T17:14:52.870542+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAIKO-EUR | action ACHETE_MAINTENANT | opportunité 9.378 | entrée 7.500 | trend 8.700 | rang 8.471
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ZEN-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.194 | entrée 5.850 | trend 8.300 | rang 8.009
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : RLC-EUR | action LATENT_ACCELERATOR | opportunité 8.947 | entrée 5.550 | trend 7.300 | rang 7.460
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : WAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.440 | entrée 7.150 | trend 8.850 | rang 8.110
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. TAIKO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.471
2. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.110
3. ZEN-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 8.009

## Accélération indépendante

- PROM-EUR — CONFIRMED_ACCELERATION — score 8.708/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EPIC-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- CHR-EUR — CONFIRMED_ACCELERATION — score 7.801/10 — DETECTED_BUT_TOO_LATE
- USELESS-EUR — CONFIRMED_ACCELERATION — score 7.387/10 — DETECTED_BUT_TOO_LATE
- DGB-EUR — CONFIRMED_ACCELERATION — score 7.233/10 — DETECTED_BUT_TOO_LATE
- MET-EUR — CONFIRMED_ACCELERATION — score 6.809/10 — DETECTED_BUT_TOO_LATE
- PEOPLE-EUR — CONFIRMED_ACCELERATION — score 6.809/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CAT-EUR — CONFIRMED_ACCELERATION — score 6.669/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RLC-EUR — BUILDING_ACCELERATION — score 6.184/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- STO-EUR — BUILDING_ACCELERATION — score 6.017/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PROM-EUR — ACTIVE_NOW — score mémoire 8.708/10 — sources ACCELERATION, V4 — WATCH_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- EPIC-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- U-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TAIKO-EUR — ACTIVE_NOW — score mémoire 8.471/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 8.110/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- 0G-EUR — ACTIVE_NOW — score mémoire 8.009/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZEN-EUR — ACTIVE_NOW — score mémoire 8.009/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOL-EUR — ACTIVE_NOW — score mémoire 7.939/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CHR-EUR +45.48% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- NIL-EUR +31.41% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +23.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BCH-EUR +22.97% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FLOCK-EUR +22.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +19.65% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +19.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KITE-EUR +17.18% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MLN-EUR +15.17% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- S-EUR +15.14% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
