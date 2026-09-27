# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T20:49:16.589026+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : KAS-EUR | action ACHETE_MAINTENANT | opportunité 8.342 | entrée 6.950 | trend 9.200 | rang 8.193
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : CFG-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.377 | entrée 6.000 | trend 8.750 | rang 8.423
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : AXS-EUR | action LATENT_ACCELERATOR | opportunité 8.539 | entrée 5.550 | trend 8.700 | rang 7.966
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : APE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.346 | entrée 6.750 | trend 8.700 | rang 8.344
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. CFG-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 8.423
2. APE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.344
3. GALA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.337

## Accélération indépendante

- SKY-EUR — CONFIRMED_ACCELERATION — score 9.054/10 — DETECTED_BUT_TOO_LATE
- POND-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- LMWR-EUR — BUILDING_ACCELERATION — score 5.100/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BOME-EUR — BUILDING_ACCELERATION — score 5.018/10 — DETECTED_BUT_TOO_LATE
- QNT-EUR — BUILDING_ACCELERATION — score 4.907/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SKY-EUR — ACTIVE_NOW — score mémoire 9.054/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- POND-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- YB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CFG-EUR — ACTIVE_NOW — score mémoire 8.423/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- APE-EUR — ACTIVE_NOW — score mémoire 8.344/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GALA-EUR — ACTIVE_NOW — score mémoire 8.337/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SAFE-EUR — ACTIVE_NOW — score mémoire 8.203/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- BAT-EUR — ACTIVE_NOW — score mémoire 8.195/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.193/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +59.77% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +46.79% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INX-EUR +30.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +26.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- W-EUR +23.97% — DETECTED_EARLY — couche NONE — action NONE
- GRT-EUR +18.98% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PUMP-EUR +16.44% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRC-EUR +15.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GLMR-EUR +15.46% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- NEAR-EUR +14.86% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
