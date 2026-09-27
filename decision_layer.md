# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T08:59:20.717316+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : EIGEN-EUR | action ACHETE_MAINTENANT | opportunité 8.866 | entrée 6.900 | trend 9.200 | rang 8.254
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ZK-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.111 | entrée 6.150 | trend 8.700 | rang 7.779
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SPK-EUR | action LATENT_ACCELERATOR | opportunité 8.292 | entrée 5.600 | trend 8.900 | rang 7.858
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : CRO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.279 | entrée 6.500 | trend 8.700 | rang 8.318
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. CRO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.318
2. EIGEN-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.254
3. JUP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.178

## Accélération indépendante

- ARX-EUR — CONFIRMED_ACCELERATION — score 8.815/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HUMA-EUR — CONFIRMED_ACCELERATION — score 7.685/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAI-EUR — CONFIRMED_ACCELERATION — score 7.237/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GNS-EUR — BUILDING_ACCELERATION — score 6.254/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CSPR-EUR — BUILDING_ACCELERATION — score 5.650/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WMTX-EUR — BUILDING_ACCELERATION — score 5.339/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ID-EUR — BUILDING_ACCELERATION — score 5.279/10 — DETECTED_BUT_TOO_LATE
- IKA-EUR — BUILDING_ACCELERATION — score 5.198/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MET-EUR — BUILDING_ACCELERATION — score 4.954/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ORCA-EUR — ACTIVE_NOW — score mémoire 8.092/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- XMN-EUR — MEMORY_24H — score mémoire 9.365/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ARX-EUR — ACTIVE_NOW — score mémoire 8.815/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AMP-EUR — MEMORY_24H — score mémoire 8.589/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.432/10 — sources ACCELERATION — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.427/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CRO-EUR — ACTIVE_NOW — score mémoire 8.318/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- EIGEN-EUR — ACTIVE_NOW — score mémoire 8.254/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 8.178/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.162/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +75.44% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +56.98% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +46.66% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +32.83% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HFT-EUR +24.99% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- AGI-EUR +24.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +20.10% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- W-EUR +18.35% — DETECTED_EARLY — couche NONE — action NONE
- XVG-EUR +18.04% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- TRIA-EUR +16.81% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
