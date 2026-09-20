# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T21:56:05.723851+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : CAKE-EUR | action ACHETE_MAINTENANT | opportunité 8.158 | entrée 6.800 | trend 8.950 | rang 7.930
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ZRO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.318 | entrée 6.000 | trend 8.500 | rang 7.976
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ZIL-EUR | action LATENT_ACCELERATOR | opportunité 7.579 | entrée 4.750 | trend 8.750 | rang 7.446
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : RENDER-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.191 | entrée 7.600 | trend 8.100 | rang 8.030
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. RENDER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.030
2. ZRO-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.976
3. IOST-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.963

## Accélération indépendante

- JUP-EUR — BUILDING_ACCELERATION — score 4.796/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ICX-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.883/10 — sources ACCELERATION — MEMORY_ONLY
- NOS-EUR — MEMORY_24H — score mémoire 8.445/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- UP-EUR — MEMORY_24H — score mémoire 8.113/10 — sources ACCELERATION — MEMORY_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.030/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ZRO-EUR — ACTIVE_NOW — score mémoire 7.976/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- IOST-EUR — ACTIVE_NOW — score mémoire 7.963/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 7.956/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.930/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 7.906/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +50.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +33.44% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PTB-EUR +33.38% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NIL-EUR +29.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +20.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +18.03% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EPIC-EUR +17.97% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LUNA2-EUR +17.36% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- KMNO-EUR +16.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +16.64% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
