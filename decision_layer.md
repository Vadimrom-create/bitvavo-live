# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T22:24:58.117799+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SEI-EUR | action ACHETE_MAINTENANT | opportunité 8.527 | entrée 7.450 | trend 8.850 | rang 7.955
  - V4 buy-ready with acceptable current entry; no structural veto. High extension/chase is retained as risk context, not an automatic veto.
- **MEILLEURE_LIMITE_PASSIVE** : CAKE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.337 | entrée 6.100 | trend 8.200 | rang 7.740
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MAGIC-EUR | action LATENT_ACCELERATOR | opportunité 9.239 | entrée 4.950 | trend 8.450 | rang 8.096
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AAVE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.184 | entrée 6.450 | trend 9.000 | rang 8.479
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.479
2. MAGIC-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 8.096
3. ORCA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.063

## Accélération indépendante

- ZEUS-EUR — CONFIRMED_ACCELERATION — score 8.458/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — CONFIRMED_ACCELERATION — score 6.915/10 — DETECTED_BUT_TOO_LATE
- CVX-EUR — CONFIRMED_ACCELERATION — score 6.805/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NOM-EUR — CONFIRMED_ACCELERATION — score 6.760/10 — DETECTED_BUT_TOO_LATE
- XMN-EUR — BUILDING_ACCELERATION — score 5.584/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GLMR-EUR — BUILDING_ACCELERATION — score 4.804/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- QNT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- YB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.479/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZEUS-EUR — ACTIVE_NOW — score mémoire 8.458/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY
- MAGIC-EUR — ACTIVE_NOW — score mémoire 8.096/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ORCA-EUR — ACTIVE_NOW — score mémoire 8.063/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +75.55% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +41.18% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INX-EUR +36.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +28.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRT-EUR +23.89% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- W-EUR +19.94% — DETECTED_EARLY — couche NONE — action NONE
- NOM-EUR +17.32% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AUDIO-EUR +16.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +15.29% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PUMP-EUR +15.14% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
