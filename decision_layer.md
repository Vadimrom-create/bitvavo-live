# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T17:03:40.584811+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 8.214 | entrée 7.600 | trend 8.250 | rang 7.758
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ALGO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.570 | entrée 6.200 | trend 8.200 | rang 6.828
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : HBAR-EUR | action LATENT_ACCELERATOR | opportunité 7.424 | entrée 4.500 | trend 7.800 | rang 6.776
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PHA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.775 | entrée 4.500 | trend 8.600 | rang 7.332
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.758
2. SOL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.623
3. PHA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.332

## Accélération indépendante

- SAGA-EUR — CONFIRMED_ACCELERATION — score 8.151/10 — DETECTED_BUT_TOO_LATE
- C-EUR — BUILDING_ACCELERATION — score 6.035/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ONDO-EUR — ACTIVE_NOW — score mémoire 7.075/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ADA-EUR — ACTIVE_NOW — score mémoire 6.539/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- PENDLE-EUR — ACTIVE_NOW — score mémoire 8.309/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 8.257/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- SAGA-EUR — ACTIVE_NOW — score mémoire 8.151/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- WAL-EUR — ACTIVE_NOW — score mémoire 8.016/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- MERL-EUR — ACTIVE_NOW — score mémoire 7.982/10 — sources V4 — WATCH_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.925/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.914/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 7.888/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +46.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +33.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +27.83% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PTB-EUR +25.80% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FTT-EUR +20.78% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NEAR-EUR +18.50% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LUNA2-EUR +17.34% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AVAX-EUR +16.15% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- S-EUR +13.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +12.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
