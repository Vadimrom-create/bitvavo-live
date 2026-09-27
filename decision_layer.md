# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T21:21:45.185488+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : KAS-EUR | action ACHETE_MAINTENANT | opportunité 8.558 | entrée 7.200 | trend 9.200 | rang 8.335
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : APE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.219 | entrée 6.400 | trend 8.700 | rang 7.828
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : GALA-EUR | action LATENT_ACCELERATOR | opportunité 8.126 | entrée 5.300 | trend 8.700 | rang 7.746
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : OP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.774 | entrée 6.700 | trend 8.950 | rang 8.302
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. KAS-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.335
2. OP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.302
3. RENDER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.149

## Accélération indépendante

- IMX-EUR — CONFIRMED_ACCELERATION — score 6.529/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SAGA-EUR — BUILDING_ACCELERATION — score 6.335/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NOM-EUR — BUILDING_ACCELERATION — score 6.031/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — BUILDING_ACCELERATION — score 5.982/10 — DETECTED_BUT_TOO_LATE
- QNT-EUR — BUILDING_ACCELERATION — score 5.393/10 — DETECTED_BUT_TOO_LATE
- JASMY-EUR — BUILDING_ACCELERATION — score 5.266/10 — DETECTED_BUT_TOO_LATE
- GIGA-EUR — BUILDING_ACCELERATION — score 5.263/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CETUS-EUR — BUILDING_ACCELERATION — score 5.040/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KMNO-EUR — BUILDING_ACCELERATION — score 4.754/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- POND-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- YB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.335/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- OP-EUR — ACTIVE_NOW — score mémoire 8.302/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.149/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 8.141/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RUNE-EUR — ACTIVE_NOW — score mémoire 8.139/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY
- VIRTUAL-EUR — ACTIVE_NOW — score mémoire 8.109/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +63.03% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +41.89% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INX-EUR +30.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +23.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRT-EUR +19.58% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- W-EUR +19.27% — DETECTED_EARLY — couche NONE — action NONE
- AUDIO-EUR +17.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUMP-EUR +15.25% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRC-EUR +14.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +14.64% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
