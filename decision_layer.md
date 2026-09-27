# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T16:20:26.524163+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : RENDER-EUR | action ACHETE_MAINTENANT | opportunité 8.513 | entrée 7.150 | trend 9.200 | rang 8.276
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AXL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.400 | entrée 6.000 | trend 8.950 | rang 7.970
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BRETT-EUR | action LATENT_ACCELERATOR | opportunité 8.024 | entrée 5.250 | trend 9.000 | rang 7.750
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : TAIKO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.174 | entrée 7.450 | trend 8.650 | rang 8.256
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. RENDER-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.276
2. TAIKO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.256
3. IMX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.114

## Accélération indépendante

- DOGS-EUR — CONFIRMED_ACCELERATION — score 8.702/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- YB-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- IMX-EUR — BUILDING_ACCELERATION — score 5.952/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PENDLE-EUR — BUILDING_ACCELERATION — score 5.732/10 — DETECTED_BUT_TOO_LATE
- INX-EUR — BUILDING_ACCELERATION — score 5.703/10 — DETECTED_BUT_TOO_LATE
- CROSS-EUR — BUILDING_ACCELERATION — score 5.656/10 — DETECTED_BUT_TOO_LATE
- TAI-EUR — BUILDING_ACCELERATION — score 5.428/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOON-EUR — BUILDING_ACCELERATION — score 5.255/10 — DETECTED_BUT_TOO_LATE
- HFT-EUR — BUILDING_ACCELERATION — score 5.180/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- INIT-EUR — BUILDING_ACCELERATION — score 5.139/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- MMT-EUR — MEMORY_24H — score mémoire 9.122/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DOGS-EUR — ACTIVE_NOW — score mémoire 8.702/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GROVE-EUR — MEMORY_24H — score mémoire 8.518/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.276/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TAIKO-EUR — ACTIVE_NOW — score mémoire 8.256/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- IMX-EUR — ACTIVE_NOW — score mémoire 8.114/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AEVO-EUR — ACTIVE_NOW — score mémoire 8.094/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- BAT-EUR — ACTIVE_NOW — score mémoire 8.082/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +57.74% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +57.66% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +39.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GLMR-EUR +33.74% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- AUDIO-EUR +32.97% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARX-EUR +30.77% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INX-EUR +22.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- W-EUR +19.85% — DETECTED_EARLY — couche NONE — action NONE
- AGI-EUR +16.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +14.82% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
