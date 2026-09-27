# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T19:28:42.813011+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : KAS-EUR | action ACHETE_MAINTENANT | opportunité 8.997 | entrée 7.450 | trend 9.200 | rang 8.414
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SAND-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.948 | entrée 6.150 | trend 8.400 | rang 7.972
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BRETT-EUR | action LATENT_ACCELERATOR | opportunité 8.298 | entrée 5.650 | trend 9.000 | rang 7.931
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : DUSK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.327 | entrée 6.450 | trend 8.650 | rang 8.289
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. KAS-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.414
2. RENDER-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.382
3. EIGEN-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.325

## Accélération indépendante

- DYM-EUR — CONFIRMED_ACCELERATION — score 9.679/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KMNO-EUR — BUILDING_ACCELERATION — score 5.916/10 — DETECTED_BUT_TOO_LATE
- RED-EUR — BUILDING_ACCELERATION — score 5.738/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARX-EUR — BUILDING_ACCELERATION — score 4.800/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- JUP-EUR — ACTIVE_NOW — score mémoire 7.984/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ARB-EUR — ACTIVE_NOW — score mémoire 7.210/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- DYM-EUR — ACTIVE_NOW — score mémoire 9.679/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GRT-EUR — MEMORY_24H — score mémoire 9.182/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MMT-EUR — MEMORY_24H — score mémoire 9.122/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GLMR-EUR — MEMORY_24H — score mémoire 8.508/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- YB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.414/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.382/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- QNT-EUR +53.14% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +45.33% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +30.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AUDIO-EUR +29.27% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- INX-EUR +25.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GLMR-EUR +22.15% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- W-EUR +20.67% — DETECTED_EARLY — couche NONE — action NONE
- ARX-EUR +20.09% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +16.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRT-EUR +13.81% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
