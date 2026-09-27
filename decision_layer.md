# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T16:53:44.745005+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : KAS-EUR | action ACHETE_MAINTENANT | opportunité 8.135 | entrée 7.200 | trend 8.900 | rang 8.018
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : A-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.785 | entrée 6.000 | trend 8.950 | rang 7.709
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : CRO-EUR | action LATENT_ACCELERATOR | opportunité 8.186 | entrée 5.500 | trend 8.700 | rang 7.766
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : RENDER-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.135 | entrée 6.500 | trend 9.200 | rang 8.055
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. RENDER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.055
2. KAS-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.018
3. BAT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.009

## Accélération indépendante

- AZTEC-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- HFT-EUR — CONFIRMED_ACCELERATION — score 7.806/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOON-EUR — CONFIRMED_ACCELERATION — score 7.168/10 — DETECTED_BUT_TOO_LATE
- GLMR-EUR — CONFIRMED_ACCELERATION — score 6.546/10 — DETECTED_BUT_TOO_LATE
- NOM-EUR — BUILDING_ACCELERATION — score 6.330/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BIGTIME-EUR — BUILDING_ACCELERATION — score 6.135/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LAPTOP-EUR — BUILDING_ACCELERATION — score 5.859/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LMWR-EUR — BUILDING_ACCELERATION — score 5.415/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GRAM-EUR — BUILDING_ACCELERATION — score 5.026/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AZTEC-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — MEMORY_24H — score mémoire 9.612/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MMT-EUR — MEMORY_24H — score mémoire 9.122/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DOGS-EUR — MEMORY_24H — score mémoire 8.702/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GROVE-EUR — MEMORY_24H — score mémoire 8.518/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- YB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.055/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.018/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- BAT-EUR — ACTIVE_NOW — score mémoire 8.009/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SOON-EUR +57.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +54.60% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +33.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AUDIO-EUR +31.16% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARX-EUR +27.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +21.76% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- W-EUR +20.68% — DETECTED_EARLY — couche NONE — action NONE
- INX-EUR +20.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +16.92% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRAM-EUR +13.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
