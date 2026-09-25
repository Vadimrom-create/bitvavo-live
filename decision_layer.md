# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T07:07:29.794503+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : JUP-EUR | action ACHETE_MAINTENANT | opportunité 8.224 | entrée 7.350 | trend 8.950 | rang 8.071
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : TIA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.290 | entrée 6.050 | trend 8.150 | rang 7.713
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : CAKE-EUR | action LATENT_ACCELERATOR | opportunité 8.253 | entrée 5.450 | trend 8.950 | rang 7.912
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AERO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.486 | entrée 6.700 | trend 8.950 | rang 7.995
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. JUP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.071
2. AERO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.995
3. TAIKO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.931

## Accélération indépendante

- MOVR-EUR — CONFIRMED_ACCELERATION — score 9.094/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — CONFIRMED_ACCELERATION — score 7.586/10 — DETECTED_BUT_TOO_LATE
- PHA-EUR — CONFIRMED_ACCELERATION — score 6.677/10 — DETECTED_BUT_TOO_LATE
- AXS-EUR — CONFIRMED_ACCELERATION — score 6.647/10 — DETECTED_BUT_TOO_LATE
- EDGE-EUR — BUILDING_ACCELERATION — score 5.945/10 — DETECTED_BUT_TOO_LATE
- CFG-EUR — BUILDING_ACCELERATION — score 5.734/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ACE-EUR — BUILDING_ACCELERATION — score 4.840/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MANTRA-EUR — BUILDING_ACCELERATION — score 4.785/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- MOVR-EUR — ACTIVE_NOW — score mémoire 9.094/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- UP-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- SAGA-EUR — MEMORY_24H — score mémoire 8.681/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- WMTX-EUR — MEMORY_24H — score mémoire 8.143/10 — sources ACCELERATION — MEMORY_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 8.071/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.995/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TAIKO-EUR — ACTIVE_NOW — score mémoire 7.931/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +43.23% — DETECTED_EARLY — couche NONE — action NONE
- TREAD-EUR +38.83% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- XPL-EUR +32.35% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ONDO-EUR +27.94% — DETECTED_EARLY — couche NONE — action NONE
- PHA-EUR +22.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +20.37% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PEAQ-EUR +18.70% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARK-EUR +16.42% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DBR-EUR +15.55% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FET-EUR +14.91% — DETECTED_EARLY — couche NONE — action NONE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
