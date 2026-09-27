# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T04:52:03.775108+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : NEAR-EUR | action ACHETE_MAINTENANT | opportunité 8.092 | entrée 7.500 | trend 8.250 | rang 7.832
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ENJ-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.120 | entrée 6.000 | trend 7.900 | rang 7.999
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : WOO-EUR | action LATENT_ACCELERATOR | opportunité 9.174 | entrée 5.450 | trend 8.200 | rang 8.066
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : EIGEN-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.697 | entrée 6.650 | trend 8.900 | rang 8.199
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. EIGEN-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.199
2. RENDER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.100
3. WOO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 8.066

## Accélération indépendante

- TREAD-EUR — CONFIRMED_ACCELERATION — score 8.587/10 — DETECTED_BUT_TOO_LATE
- TAIKO-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- TAI-EUR — BUILDING_ACCELERATION — score 6.452/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HEI-EUR — BUILDING_ACCELERATION — score 6.293/10 — DETECTED_BUT_TOO_LATE
- WMTX-EUR — BUILDING_ACCELERATION — score 5.820/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GLMR-EUR — BUILDING_ACCELERATION — score 5.452/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- INX-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SAGA-EUR — MEMORY_24H — score mémoire 9.476/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- QNT-EUR — MEMORY_24H — score mémoire 9.139/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RARE-EUR — MEMORY_24H — score mémoire 8.845/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- VELO-EUR — MEMORY_24H — score mémoire 8.605/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — ACTIVE_NOW — score mémoire 8.587/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- TAIKO-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- FTT-EUR — MEMORY_24H — score mémoire 8.427/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_DECAY_24_72H — score mémoire 8.423/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- EIGEN-EUR — ACTIVE_NOW — score mémoire 8.199/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +89.94% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +39.09% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +36.69% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +25.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +24.11% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRC-EUR +23.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RUNE-EUR +20.16% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +19.38% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +18.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TAIKO-EUR +18.29% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
