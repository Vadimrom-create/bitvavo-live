# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T19:13:04.788085+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : EIGEN-EUR | action ACHETE_MAINTENANT | opportunité 9.429 | entrée 7.400 | trend 8.900 | rang 8.552
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ENJ-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.921 | entrée 6.550 | trend 8.700 | rang 8.101
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : AXL-EUR | action LATENT_ACCELERATOR | opportunité 8.171 | entrée 4.500 | trend 8.950 | rang 7.713
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ATH-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.392 | entrée 6.550 | trend 8.900 | rang 8.485
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. EIGEN-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.552
2. ATH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.485
3. KAS-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.475

## Accélération indépendante

- GRT-EUR — CONFIRMED_ACCELERATION — score 9.182/10 — DETECTED_BUT_TOO_LATE
- GLMR-EUR — CONFIRMED_ACCELERATION — score 8.508/10 — DETECTED_BUT_TOO_LATE
- NES-EUR — BUILDING_ACCELERATION — score 6.054/10 — DETECTED_BUT_TOO_LATE
- SOMI-EUR — BUILDING_ACCELERATION — score 5.605/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RPL-EUR — BUILDING_ACCELERATION — score 5.220/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FIDA-EUR — BUILDING_ACCELERATION — score 4.847/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NMR-EUR — BUILDING_ACCELERATION — score 4.792/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- JUP-EUR — ACTIVE_NOW — score mémoire 8.106/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- GRT-EUR — ACTIVE_NOW — score mémoire 9.182/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- MMT-EUR — MEMORY_24H — score mémoire 9.122/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- EIGEN-EUR — ACTIVE_NOW — score mémoire 8.552/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GLMR-EUR — ACTIVE_NOW — score mémoire 8.508/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- YB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ATH-EUR — ACTIVE_NOW — score mémoire 8.485/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.475/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.212/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +53.38% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +44.06% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +29.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AUDIO-EUR +28.36% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GLMR-EUR +25.05% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- INX-EUR +24.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- W-EUR +20.44% — DETECTED_EARLY — couche NONE — action NONE
- ARX-EUR +18.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +16.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +12.74% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
