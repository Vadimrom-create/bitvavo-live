# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T19:52:47.918786+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : JUP-EUR | action ACHETE_MAINTENANT | opportunité 8.581 | entrée 6.950 | trend 8.450 | rang 7.942
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : GRASS-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.601 | entrée 6.700 | trend 7.600 | rang 7.249
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SIGN-EUR | action LATENT_ACCELERATOR | opportunité 7.554 | entrée 4.500 | trend 8.950 | rang 7.473
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : COW-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.331 | entrée 7.350 | trend 9.000 | rang 8.584
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. COW-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.584
2. CAKE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.005
3. JUP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.942

## Accélération indépendante

- FTT-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- NES-EUR — CONFIRMED_ACCELERATION — score 8.883/10 — DETECTED_BUT_TOO_LATE
- ZEN-EUR — CONFIRMED_ACCELERATION — score 8.798/10 — DETECTED_BUT_TOO_LATE
- SYN-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- S-EUR — CONFIRMED_ACCELERATION — score 8.240/10 — DETECTED_BUT_TOO_LATE
- NEAR-EUR — BUILDING_ACCELERATION — score 6.044/10 — DETECTED_BUT_TOO_LATE
- SOLV-EUR — BUILDING_ACCELERATION — score 5.767/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RENDER-EUR — BUILDING_ACCELERATION — score 5.694/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PHA-EUR — BUILDING_ACCELERATION — score 5.466/10 — DETECTED_BUT_TOO_LATE
- FOLD-EUR — BUILDING_ACCELERATION — score 5.217/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.777/10 — sources DECISION_LAYER, V4 — BUYABLE_NOW
- FTT-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- NES-EUR — ACTIVE_NOW — score mémoire 8.883/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- EDEN-EUR — MEMORY_24H — score mémoire 8.850/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZEN-EUR — ACTIVE_NOW — score mémoire 8.798/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- COW-EUR — ACTIVE_NOW — score mémoire 8.584/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PTB-EUR — MEMORY_24H — score mémoire 8.518/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- C-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SKL-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SYN-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- SAGA-EUR +51.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +43.65% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PTB-EUR +27.84% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- S-EUR +23.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CELR-EUR +23.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +17.58% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AVAX-EUR +15.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +15.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRK-EUR +15.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +14.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
