# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T06:21:02.750505+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : RENDER-EUR | action ACHETE_MAINTENANT | opportunité 9.060 | entrée 7.600 | trend 9.200 | rang 8.533
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ORCA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.941 | entrée 6.000 | trend 8.750 | rang 7.659
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ROSE-EUR | action LATENT_ACCELERATOR | opportunité 8.068 | entrée 5.650 | trend 8.950 | rang 7.784
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ATH-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.082 | entrée 6.250 | trend 9.200 | rang 8.392
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. RENDER-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.533
2. ATH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.392
3. OP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.308

## Accélération indépendante

- AMP-EUR — CONFIRMED_ACCELERATION — score 8.589/10 — DETECTED_BUT_TOO_LATE
- ARK-EUR — CONFIRMED_ACCELERATION — score 8.193/10 — DETECTED_BUT_TOO_LATE
- BCH-EUR — CONFIRMED_ACCELERATION — score 7.762/10 — DETECTED_BUT_TOO_LATE
- TAI-EUR — CONFIRMED_ACCELERATION — score 6.503/10 — DETECTED_BUT_TOO_LATE
- TRIA-EUR — BUILDING_ACCELERATION — score 5.847/10 — DETECTED_BUT_TOO_LATE
- METIS-EUR — BUILDING_ACCELERATION — score 5.319/10 — DETECTED_BUT_TOO_LATE
- ARKM-EUR — BUILDING_ACCELERATION — score 5.301/10 — DETECTED_BUT_TOO_LATE
- VIRTUAL-EUR — BUILDING_ACCELERATION — score 5.283/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRO-EUR — BUILDING_ACCELERATION — score 5.145/10 — DETECTED_BUT_TOO_LATE
- QNT-EUR — BUILDING_ACCELERATION — score 5.050/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- NEAR-EUR — ACTIVE_NOW — score mémoire 6.200/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- INX-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SAGA-EUR — MEMORY_24H — score mémoire 9.476/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION — MEMORY_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.644/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- VELO-EUR — MEMORY_24H — score mémoire 8.605/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AMP-EUR — ACTIVE_NOW — score mémoire 8.589/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — MEMORY_24H — score mémoire 8.587/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SOON-EUR — MEMORY_24H — score mémoire 8.551/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.533/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +72.92% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +42.51% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +36.53% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +32.55% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +25.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GLMR-EUR +22.36% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- RUNE-EUR +22.02% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- W-EUR +20.00% — DETECTED_EARLY — couche NONE — action NONE
- EDGE-EUR +18.98% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRC-EUR +17.79% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
