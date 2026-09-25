# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T21:07:49.558782+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ALGO-EUR | action ACHETE_MAINTENANT | opportunité 8.414 | entrée 7.200 | trend 9.000 | rang 8.163
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : RPL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.420 | entrée 6.200 | trend 9.000 | rang 7.920
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : 0G-EUR | action LATENT_ACCELERATOR | opportunité 7.952 | entrée 5.700 | trend 8.650 | rang 7.596
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : INJ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.805 | entrée 6.400 | trend 8.900 | rang 8.219
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.219
2. PYTH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.163
3. ALGO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.163

## Accélération indépendante

- PHA-EUR — CONFIRMED_ACCELERATION — score 7.501/10 — DETECTED_BUT_TOO_LATE
- LAPTOP-EUR — BUILDING_ACCELERATION — score 6.037/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRC-EUR — BUILDING_ACCELERATION — score 5.679/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 8.667/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 8.219/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ALGO-EUR — ACTIVE_NOW — score mémoire 8.163/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.163/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RENDER-EUR — MEMORY_24H — score mémoire 8.156/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ORCA-EUR — ACTIVE_NOW — score mémoire 8.119/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 8.112/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.111/10 — sources ACCELERATION — MEMORY_ONLY
- ALT-EUR — ACTIVE_NOW — score mémoire 8.104/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PHA-EUR +69.13% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ARK-EUR +26.85% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +21.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AERO-EUR +19.23% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ENA-EUR +18.53% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DEEP-EUR +17.54% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- EDGE-EUR +17.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +17.01% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SEI-EUR +15.92% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- JTO-EUR +14.64% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
