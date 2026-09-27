# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T18:18:28.228739+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 8.793 | entrée 7.800 | trend 9.000 | rang 8.409
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ROSE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.495 | entrée 6.100 | trend 8.950 | rang 7.993
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : RED-EUR | action LATENT_ACCELERATOR | opportunité 8.136 | entrée 5.700 | trend 8.650 | rang 7.740
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : APT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.275 | entrée 6.650 | trend 8.650 | rang 8.387
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.409
2. APT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.387
3. LINK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.347

## Accélération indépendante

- REQ-EUR — CONFIRMED_ACCELERATION — score 7.245/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- USELESS-EUR — BUILDING_ACCELERATION — score 6.318/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PUMP-EUR — BUILDING_ACCELERATION — score 6.275/10 — DETECTED_BUT_TOO_LATE
- FLUX-EUR — BUILDING_ACCELERATION — score 5.696/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARB-EUR — BUILDING_ACCELERATION — score 5.662/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POPCAT-EUR — BUILDING_ACCELERATION — score 5.637/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IMX-EUR — BUILDING_ACCELERATION — score 5.584/10 — DETECTED_BUT_TOO_LATE
- SOON-EUR — BUILDING_ACCELERATION — score 5.235/10 — DETECTED_BUT_TOO_LATE
- AUDIO-EUR — BUILDING_ACCELERATION — score 5.124/10 — DETECTED_BUT_TOO_LATE
- ASTR-EUR — BUILDING_ACCELERATION — score 5.095/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CC-EUR — ACTIVE_NOW — score mémoire 7.993/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- NEAR-EUR — ACTIVE_NOW — score mémoire 7.792/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ENA-EUR — ACTIVE_NOW — score mémoire 7.583/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- MMT-EUR — MEMORY_24H — score mémoire 9.122/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GROVE-EUR — MEMORY_24H — score mémoire 8.518/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- YB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.409/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- APT-EUR — ACTIVE_NOW — score mémoire 8.387/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 8.347/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SOON-EUR +50.21% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +49.17% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- TREAD-EUR +40.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AUDIO-EUR +26.17% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- INX-EUR +25.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARX-EUR +21.81% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +18.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GLMR-EUR +17.30% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- W-EUR +16.24% — DETECTED_EARLY — couche NONE — action NONE
- PUMP-EUR +13.97% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
