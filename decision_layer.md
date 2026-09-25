# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T01:48:10.402721+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TIA-EUR | action ACHETE_MAINTENANT | opportunité 9.197 | entrée 7.700 | trend 8.150 | rang 8.289
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : CAKE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.971 | entrée 6.100 | trend 8.950 | rang 7.861
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MANTRA-EUR | action LATENT_ACCELERATOR | opportunité 7.988 | entrée 5.400 | trend 9.000 | rang 7.639
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : JUP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.343 | entrée 6.900 | trend 8.700 | rang 7.918
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. TIA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.289
2. JUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.918
3. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.889

## Accélération indépendante

- QKC-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- BTT-EUR — CONFIRMED_ACCELERATION — score 8.082/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AXS-EUR — CONFIRMED_ACCELERATION — score 7.564/10 — DETECTED_BUT_TOO_LATE
- SAGA-EUR — BUILDING_ACCELERATION — score 5.833/10 — DETECTED_BUT_TOO_LATE
- EGLD-EUR — BUILDING_ACCELERATION — score 5.181/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- QKC-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- WMTX-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- ARK-EUR — MEMORY_24H — score mémoire 8.892/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TIA-EUR — ACTIVE_NOW — score mémoire 8.289/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.169/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BTT-EUR — ACTIVE_NOW — score mémoire 8.082/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 7.918/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +52.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ONDO-EUR +28.65% — DETECTED_EARLY — couche NONE — action NONE
- QNT-EUR +28.49% — DETECTED_EARLY — couche NONE — action NONE
- TREAD-EUR +26.73% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- XPL-EUR +22.20% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- DYM-EUR +19.22% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEAQ-EUR +18.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DBR-EUR +16.64% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XAI-EUR +16.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LTC-EUR +16.42% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
