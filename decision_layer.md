# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T23:04:53.264289+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : OP-EUR | action ACHETE_MAINTENANT | opportunité 9.214 | entrée 7.850 | trend 8.950 | rang 8.476
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : CAKE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.536 | entrée 6.100 | trend 8.950 | rang 8.067
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : IO-EUR | action LATENT_ACCELERATOR | opportunité 8.066 | entrée 5.550 | trend 8.750 | rang 7.667
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PLUME-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.398 | entrée 7.250 | trend 8.850 | rang 8.251
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. OP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.476
2. ONDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.270
3. LINK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.262

## Accélération indépendante

- PONKE-EUR — CONFIRMED_ACCELERATION — score 9.578/10 — DETECTED_BUT_TOO_LATE
- ARK-EUR — CONFIRMED_ACCELERATION — score 8.526/10 — DETECTED_BUT_TOO_LATE
- OGN-EUR — BUILDING_ACCELERATION — score 6.459/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AIOZ-EUR — BUILDING_ACCELERATION — score 5.307/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- OP-EUR — ACTIVE_NOW — score mémoire 8.476/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ARB-EUR — ACTIVE_NOW — score mémoire 6.857/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- PHA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PONKE-EUR — ACTIVE_NOW — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 8.667/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARK-EUR — ACTIVE_NOW — score mémoire 8.526/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ONDO-EUR — ACTIVE_NOW — score mémoire 8.270/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LINK-EUR — ACTIVE_NOW — score mémoire 8.262/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PLUME-EUR — ACTIVE_NOW — score mémoire 8.251/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- PHA-EUR +73.67% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ARK-EUR +34.70% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AERO-EUR +22.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +22.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SEI-EUR +20.34% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ENA-EUR +19.83% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +17.66% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUI-EUR +17.54% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +17.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DEEP-EUR +16.77% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
