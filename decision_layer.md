# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T00:00:26.028393+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : STX-EUR | action ACHETE_MAINTENANT | opportunité 9.010 | entrée 6.900 | trend 8.350 | rang 7.967
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : PROVE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.696 | entrée 6.100 | trend 8.400 | rang 7.902
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ENSO-EUR | action LATENT_ACCELERATOR | opportunité 7.605 | entrée 5.550 | trend 8.500 | rang 7.464
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : COW-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.597 | entrée 6.850 | trend 9.000 | rang 8.137
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. COW-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.137
2. STX-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.967
3. PENDLE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.905

## Accélération indépendante

- FTT-EUR — CONFIRMED_ACCELERATION — score 7.476/10 — DETECTED_BUT_TOO_LATE
- STX-EUR — BUILDING_ACCELERATION — score 5.518/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SAGA-EUR — BUILDING_ACCELERATION — score 4.826/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- STX-EUR — ACTIVE_NOW — score mémoire 7.967/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ICX-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.883/10 — sources ACCELERATION — MEMORY_ONLY
- NOS-EUR — MEMORY_24H — score mémoire 8.445/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.376/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 8.137/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- UP-EUR — MEMORY_24H — score mémoire 8.113/10 — sources ACCELERATION — MEMORY_ONLY
- S-EUR — MEMORY_24H — score mémoire 8.013/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.905/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.902/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +50.59% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +38.37% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PTB-EUR +32.95% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +23.77% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +21.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +19.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +17.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CFG-EUR +16.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +16.16% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LUNA2-EUR +14.73% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
