# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T03:47:04.430167+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : XLM-EUR | action ACHETE_MAINTENANT | opportunité 7.792 | entrée 7.450 | trend 8.200 | rang 7.577
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : BEAM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.063 | entrée 6.000 | trend 8.650 | rang 7.783
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : DEEP-EUR | action LATENT_ACCELERATOR | opportunité 7.929 | entrée 5.350 | trend 8.600 | rang 7.023
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SENT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.882 | entrée 5.700 | trend 8.150 | rang 7.898
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. SENT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.898
2. CAKE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.835
3. LTC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.805

## Accélération indépendante

- MANA-EUR — BUILDING_ACCELERATION — score 6.312/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZAMA-EUR — BUILDING_ACCELERATION — score 6.304/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — BUILDING_ACCELERATION — score 5.959/10 — DETECTED_BUT_TOO_LATE
- CAP-EUR — BUILDING_ACCELERATION — score 5.067/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NIL-EUR — BUILDING_ACCELERATION — score 5.019/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- QKC-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- UP-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- EDGE-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- HBAR-EUR — MEMORY_24H — score mémoire 7.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 7.898/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- BOB-EUR — MEMORY_24H — score mémoire 7.875/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- OGN-EUR — MEMORY_24H — score mémoire 7.854/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- QNT-EUR +29.70% — DETECTED_EARLY — couche NONE — action NONE
- TREAD-EUR +28.51% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- XPL-EUR +26.99% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ONDO-EUR +25.79% — DETECTED_EARLY — couche NONE — action NONE
- PEAQ-EUR +23.50% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +18.23% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARK-EUR +17.50% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FET-EUR +14.19% — DETECTED_EARLY — couche NONE — action NONE
- XAI-EUR +13.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SNX-EUR +12.92% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
