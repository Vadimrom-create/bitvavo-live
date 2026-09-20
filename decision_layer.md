# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T22:14:37.699462+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : WAL-EUR | action ACHETE_MAINTENANT | opportunité 8.923 | entrée 7.050 | trend 8.700 | rang 8.318
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : IOST-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.168 | entrée 5.900 | trend 7.850 | rang 7.975
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : GRT-EUR | action LATENT_ACCELERATOR | opportunité 7.869 | entrée 5.650 | trend 8.450 | rang 7.481
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PENDLE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.285 | entrée 6.050 | trend 8.850 | rang 8.233
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. WAL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.318
2. PENDLE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.233
3. COW-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.080

## Accélération indépendante

- S-EUR — CONFIRMED_ACCELERATION — score 8.013/10 — DETECTED_BUT_TOO_LATE
- ARB-EUR — CONFIRMED_ACCELERATION — score 6.594/10 — DETECTED_BUT_TOO_LATE
- KMNO-EUR — CONFIRMED_ACCELERATION — score 6.534/10 — DETECTED_BUT_TOO_LATE
- ONG-EUR — BUILDING_ACCELERATION — score 6.135/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- OP-EUR — BUILDING_ACCELERATION — score 5.261/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ICX-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.883/10 — sources ACCELERATION — MEMORY_ONLY
- NOS-EUR — MEMORY_24H — score mémoire 8.445/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 8.318/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 8.233/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- UP-EUR — MEMORY_24H — score mémoire 8.113/10 — sources ACCELERATION — MEMORY_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 8.080/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- S-EUR — ACTIVE_NOW — score mémoire 8.013/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- IOST-EUR — ACTIVE_NOW — score mémoire 7.975/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.862/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +40.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PTB-EUR +31.81% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FTT-EUR +28.25% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- S-EUR +26.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +23.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +20.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EPIC-EUR +19.36% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +18.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +18.02% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LUNA2-EUR +17.29% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
