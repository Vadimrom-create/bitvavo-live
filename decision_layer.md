# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T20:17:04.880900+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LINK-EUR | action ACHETE_MAINTENANT | opportunité 8.296 | entrée 7.350 | trend 9.000 | rang 8.168
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : PIXEL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.208 | entrée 6.150 | trend 8.700 | rang 7.811
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BAT-EUR | action LATENT_ACCELERATOR | opportunité 7.834 | entrée 4.500 | trend 8.950 | rang 7.604
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : BRETT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.355 | entrée 6.350 | trend 9.000 | rang 8.545
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. BRETT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.545
2. CFG-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.396
3. LINK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.168

## Accélération indépendante

- POND-EUR — CONFIRMED_ACCELERATION — score 8.755/10 — DETECTED_BUT_TOO_LATE
- CETUS-EUR — CONFIRMED_ACCELERATION — score 6.799/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SAGA-EUR — BUILDING_ACCELERATION — score 6.170/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PONKE-EUR — BUILDING_ACCELERATION — score 5.728/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SKY-EUR — BUILDING_ACCELERATION — score 5.635/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARB-EUR — BUILDING_ACCELERATION — score 5.552/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AIXBT-EUR — BUILDING_ACCELERATION — score 4.965/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ARB-EUR — ACTIVE_NOW — score mémoire 6.823/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- POND-EUR — ACTIVE_NOW — score mémoire 8.755/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- BRETT-EUR — ACTIVE_NOW — score mémoire 8.545/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GLMR-EUR — MEMORY_24H — score mémoire 8.508/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- YB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CFG-EUR — ACTIVE_NOW — score mémoire 8.396/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 8.168/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.133/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- QNT-EUR +56.59% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +42.33% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +28.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INX-EUR +28.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AUDIO-EUR +24.20% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- W-EUR +22.88% — DETECTED_EARLY — couche NONE — action NONE
- GRT-EUR +21.21% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +20.46% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARX-EUR +14.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +13.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
