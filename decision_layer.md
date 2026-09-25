# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T12:00:00.103721+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : INJ-EUR | action ACHETE_MAINTENANT | opportunité 8.801 | entrée 7.200 | trend 8.650 | rang 8.079
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : RPL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.208 | entrée 6.300 | trend 8.500 | rang 7.625
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : COMP-EUR | action LATENT_ACCELERATOR | opportunité 8.182 | entrée 4.500 | trend 8.750 | rang 7.632
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : APT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.279 | entrée 6.650 | trend 8.700 | rang 8.220
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. APT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.220
2. INJ-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.079
3. HBAR-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.069

## Accélération indépendante

- SCR-EUR — CONFIRMED_ACCELERATION — score 9.062/10 — DETECTED_BUT_TOO_LATE
- GLMR-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- CAKE-EUR — CONFIRMED_ACCELERATION — score 7.505/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WMTX-EUR — BUILDING_ACCELERATION — score 6.136/10 — DETECTED_BUT_TOO_LATE
- IQ-EUR — BUILDING_ACCELERATION — score 5.496/10 — DETECTED_BUT_TOO_LATE
- BEAM-EUR — BUILDING_ACCELERATION — score 5.278/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EDGE-EUR — BUILDING_ACCELERATION — score 5.135/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- SCR-EUR — ACTIVE_NOW — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PHA-EUR — MEMORY_24H — score mémoire 9.016/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GLMR-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- TAI-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 8.374/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- APT-EUR — ACTIVE_NOW — score mémoire 8.220/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ARK-EUR — MEMORY_24H — score mémoire 8.166/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 8.079/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HBAR-EUR — ACTIVE_NOW — score mémoire 8.069/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- TREAD-EUR +46.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QNT-EUR +34.58% — DETECTED_EARLY — couche NONE — action NONE
- ARK-EUR +33.98% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XPL-EUR +25.98% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ONDO-EUR +25.79% — DETECTED_EARLY — couche NONE — action NONE
- FET-EUR +22.61% — DETECTED_EARLY — couche NONE — action NONE
- PHA-EUR +21.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DEEP-EUR +21.18% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- PEAQ-EUR +21.00% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +19.99% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
