# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T01:21:54.484517+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : PYTH-EUR | action ACHETE_MAINTENANT | opportunité 8.775 | entrée 7.800 | trend 8.500 | rang 8.167
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : PROVE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.902 | entrée 6.100 | trend 8.350 | rang 7.498
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ATH-EUR | action LATENT_ACCELERATOR | opportunité 7.513 | entrée 4.500 | trend 8.750 | rang 7.377
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : WAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.107 | entrée 6.050 | trend 9.200 | rang 7.945
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. PYTH-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.167
2. AERO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.073
3. INJ-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.011

## Accélération indépendante

- VVV-EUR — CONFIRMED_ACCELERATION — score 8.369/10 — DETECTED_BUT_TOO_LATE
- SAGA-EUR — BUILDING_ACCELERATION — score 6.390/10 — DETECTED_BUT_TOO_LATE
- CELR-EUR — BUILDING_ACCELERATION — score 5.456/10 — DETECTED_BUT_TOO_LATE
- G-EUR — BUILDING_ACCELERATION — score 5.455/10 — DETECTED_BUT_TOO_LATE
- STRK-EUR — BUILDING_ACCELERATION — score 5.127/10 — DETECTED_BUT_TOO_LATE
- AMP-EUR — BUILDING_ACCELERATION — score 4.997/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — BUILDING_ACCELERATION — score 4.990/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PENGU-EUR — BUILDING_ACCELERATION — score 4.841/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- AERO-EUR — ACTIVE_NOW — score mémoire 8.073/10 — sources DECISION_LAYER, V4 — BUYABLE_NOW
- FET-EUR — ACTIVE_NOW — score mémoire 6.865/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- XPL-EUR — ACTIVE_NOW — score mémoire 6.351/10 — sources DECISION_LAYER, V4 — BUYABLE_NOW
- ICX-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.883/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.376/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VVV-EUR — ACTIVE_NOW — score mémoire 8.369/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.167/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- UP-EUR — MEMORY_24H — score mémoire 8.113/10 — sources ACCELERATION — MEMORY_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 8.011/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +47.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PTB-EUR +34.08% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FTT-EUR +30.74% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +28.01% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +23.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CFG-EUR +20.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +19.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +19.49% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- S-EUR +19.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +18.03% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
