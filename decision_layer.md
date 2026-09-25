# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T05:36:01.981813+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AERO-EUR | action ACHETE_MAINTENANT | opportunité 8.507 | entrée 7.200 | trend 8.150 | rang 7.808
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : NEAR-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.488 | entrée 6.050 | trend 8.250 | rang 7.352
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : JUP-EUR | action LATENT_ACCELERATOR | opportunité 9.304 | entrée 5.500 | trend 8.700 | rang 8.312
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : TIA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.955 | entrée 6.550 | trend 8.150 | rang 8.079
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. JUP-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 8.312
2. TIA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.079
3. EPIC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.853

## Accélération indépendante

- PHA-EUR — CONFIRMED_ACCELERATION — score 9.420/10 — DETECTED_BUT_TOO_LATE
- ZKJ-EUR — CONFIRMED_ACCELERATION — score 7.040/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ONG-EUR — BUILDING_ACCELERATION — score 5.747/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- QNT-EUR — BUILDING_ACCELERATION — score 4.957/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- QKC-EUR — MEMORY_24H — score mémoire 9.563/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 9.420/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ICX-EUR — MEMORY_24H — score mémoire 9.235/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- UP-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.742/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WMTX-EUR — MEMORY_24H — score mémoire 8.409/10 — sources ACCELERATION — MEMORY_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 8.312/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- QNT-EUR +34.10% — DETECTED_EARLY — couche NONE — action NONE
- TREAD-EUR +28.02% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- XPL-EUR +27.92% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ONDO-EUR +23.87% — DETECTED_EARLY — couche NONE — action NONE
- PEAQ-EUR +20.76% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +20.75% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARK-EUR +17.67% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DBR-EUR +16.58% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XAI-EUR +15.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TAI-EUR +14.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
