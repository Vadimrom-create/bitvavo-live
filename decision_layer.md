# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T20:01:12.294593+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ZIG-EUR | action ACHETE_MAINTENANT | opportunité 9.181 | entrée 7.450 | trend 8.100 | rang 8.214
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : FIL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.845 | entrée 6.000 | trend 8.400 | rang 7.518
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : IOST-EUR | action LATENT_ACCELERATOR | opportunité 8.680 | entrée 5.750 | trend 7.650 | rang 7.595
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : GMT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.473 | entrée 6.500 | trend 9.000 | rang 8.110
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ZIG-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.214
2. GMT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.110
3. BEAM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.069

## Accélération indépendante

- TREAD-EUR — CONFIRMED_ACCELERATION — score 9.110/10 — DETECTED_BUT_TOO_LATE
- ALIGN-EUR — CONFIRMED_ACCELERATION — score 7.379/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BTT-EUR — BUILDING_ACCELERATION — score 6.380/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — BUILDING_ACCELERATION — score 6.149/10 — DETECTED_BUT_TOO_LATE
- FRAX-EUR — BUILDING_ACCELERATION — score 5.736/10 — DETECTED_BUT_TOO_LATE
- SKL-EUR — BUILDING_ACCELERATION — score 5.711/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- METIS-EUR — BUILDING_ACCELERATION — score 5.474/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ENA-EUR — BUILDING_ACCELERATION — score 5.168/10 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — BUILDING_ACCELERATION — score 5.111/10 — DETECTED_BUT_TOO_LATE
- GIGA-EUR — BUILDING_ACCELERATION — score 4.918/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- FET-EUR — ACTIVE_NOW — score mémoire 7.495/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- VVV-EUR — ACTIVE_NOW — score mémoire 7.308/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- TREAD-EUR — ACTIVE_NOW — score mémoire 9.110/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- CNPY-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 8.472/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- ZIG-EUR — ACTIVE_NOW — score mémoire 8.214/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GMT-EUR — ACTIVE_NOW — score mémoire 8.110/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- TREAD-EUR +44.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XAI-EUR +39.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +34.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ONDO-EUR +24.05% — DETECTED_EARLY — couche NONE — action NONE
- NOM-EUR +23.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QNT-EUR +21.43% — DETECTED_EARLY — couche NONE — action NONE
- XPL-EUR +20.85% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PEAQ-EUR +19.47% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PLUME-EUR +19.26% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARK-EUR +17.14% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
