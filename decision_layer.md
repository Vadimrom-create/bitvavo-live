# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T19:56:47.780406+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : XDC-EUR | action ACHETE_MAINTENANT | opportunité 9.286 | entrée 7.450 | trend 8.700 | rang 8.405
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ATH-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.493 | entrée 5.850 | trend 8.900 | rang 7.952
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BAT-EUR | action LATENT_ACCELERATOR | opportunité 7.871 | entrée 4.500 | trend 8.950 | rang 7.611
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : A-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.721 | entrée 6.850 | trend 8.950 | rang 8.222
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. XDC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.405
2. RENDER-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.350
3. EIGEN-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.259

## Accélération indépendante

- ACX-EUR — CONFIRMED_ACCELERATION — score 8.120/10 — DETECTED_BUT_TOO_LATE
- XYO-EUR — CONFIRMED_ACCELERATION — score 7.039/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CAT-EUR — BUILDING_ACCELERATION — score 5.829/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GRT-EUR — BUILDING_ACCELERATION — score 5.715/10 — DETECTED_BUT_TOO_LATE
- GNO-EUR — BUILDING_ACCELERATION — score 5.509/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TREE-EUR — BUILDING_ACCELERATION — score 5.257/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CPOOL-EUR — BUILDING_ACCELERATION — score 4.876/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- JUP-EUR — ACTIVE_NOW — score mémoire 7.986/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- GLMR-EUR — MEMORY_24H — score mémoire 8.508/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- YB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XDC-EUR — ACTIVE_NOW — score mémoire 8.405/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.350/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- EIGEN-EUR — ACTIVE_NOW — score mémoire 8.259/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- A-EUR — ACTIVE_NOW — score mémoire 8.222/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.191/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.161/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +50.30% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +46.31% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +30.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AUDIO-EUR +28.20% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- INX-EUR +27.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GLMR-EUR +23.22% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- W-EUR +18.70% — DETECTED_EARLY — couche NONE — action NONE
- GRT-EUR +17.20% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +16.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARX-EUR +15.69% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
