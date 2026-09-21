# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T01:02:59.123557+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : PYTH-EUR | action ACHETE_MAINTENANT | opportunité 9.318 | entrée 7.500 | trend 8.500 | rang 8.408
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AERO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.529 | entrée 6.000 | trend 8.700 | rang 7.675
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ARX-EUR | action LATENT_ACCELERATOR | opportunité 8.208 | entrée 5.400 | trend 8.900 | rang 7.868
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ZIL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.090 | entrée 6.050 | trend 8.450 | rang 8.126
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. PYTH-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.408
2. ZIL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.126
3. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.096

## Accélération indépendante

- LDO-EUR — CONFIRMED_ACCELERATION — score 9.495/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — CONFIRMED_ACCELERATION — score 8.405/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MORPHO-EUR — CONFIRMED_ACCELERATION — score 6.672/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PTB-EUR — CONFIRMED_ACCELERATION — score 6.535/10 — DETECTED_BUT_TOO_LATE
- HNT-EUR — BUILDING_ACCELERATION — score 6.076/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PUFFER-EUR — BUILDING_ACCELERATION — score 6.046/10 — DETECTED_BUT_TOO_LATE
- TRAC-EUR — BUILDING_ACCELERATION — score 5.759/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VELO-EUR — BUILDING_ACCELERATION — score 5.283/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 9.495/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ICX-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.883/10 — sources ACCELERATION — MEMORY_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.408/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- TREAD-EUR — ACTIVE_NOW — score mémoire 8.405/10 — sources ACCELERATION, V4 — WATCH_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.376/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 8.126/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- UP-EUR — MEMORY_24H — score mémoire 8.113/10 — sources ACCELERATION — MEMORY_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 8.096/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.055/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +41.48% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PTB-EUR +32.42% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FTT-EUR +29.93% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NIL-EUR +26.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +25.93% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- S-EUR +21.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CFG-EUR +20.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +19.30% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +19.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LUNA2-EUR +14.38% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
